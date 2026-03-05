transform white_drops_default:
    shader "white_drops"
    pause 1.0/60 #Divide by desired framerate
    repeat

# Original by Xor https://www.shadertoy.com/view/fdXXWH
init python:
    renpy.register_shader("white_drops", variables="""
    uniform vec2 u_drawable_size;
    uniform float u_time;

    varying vec2 v_tex_coord;
    varying vec2 v_coord;

    attribute vec2 a_tex_coord;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, gl_Position.y * .5 + .5);
    """, fragment_functions="""
        //Anti-Aliasing (SSAA). Use 1.0 on slower computers
        #define AA 2.

        //Background gradient
        vec3 background(vec3 d)
        {
            float light = dot(d,sqrt(vec3(.3,.5,.2)));
            
            return vec3(max(light*.5+.5,.0));
        }
        //Smooth minimum (based off IQ's work)
        float smin(float d1, float d2)
        {
            const float e = -6.;
            return log(exp(d1*e)+exp(d2*e))/e;
        }
        //Ripple and drop distance function
        float dist(vec3 p)
        {
            float l = pow(dot(p.xz,p.xz),.8);
            float ripple = p.y+.8+.4*sin(l*3.-u_time+.5)/(1.+l);
            
            float h1 = -sin(u_time);
            float h2 = cos(u_time+.1);
            float drop = length(p+vec3(0,1.2,0)*h1)-.4;
            drop = smin(drop,length(p+vec3(.1,.8,0)*h2)-.2);
            return smin(ripple,drop);
        }
        //Typical SDF normal function
        vec3 normal(vec3 p)
        {
            vec2 e = vec2(1,-1)*.01;
            
            return normalize(dist(p-e.yxx)*e.yxx+dist(p-e.xyx)*e.xyx+
            dist(p-e.xxy)*e.xxy+dist(p-e.y)*e.y);
        }
        //Basic raymarcher
        vec4 march(vec3 p, vec3 d)
        {
            vec4 m = vec4(p,0);
            for(int i = 0; i<99; i++)
            {
                float s = dist(m.xyz);
                m += vec4(d,1)*s;
                
                if (s<.01 || m.w>20.) break;
            }
            return m;
        }
    """, fragment_300="""
        vec2 res = u_drawable_size.xy;
        vec3 col = vec3(0.0,0.0,0.0);
        
        vec3 pos = vec3(.05*cos(u_time),.1*sin(u_time),-4);
        vec3 lig = sqrt(vec3(.3,.5,.2));
        
        //Sample
        for(float x = 0.;x<AA;x++)
        for(float y = 0.;y<AA;y++)
        {
            vec3 ray = normalize(vec3(v_coord-res/2.+vec2(x,y)/AA,res.y));
            vec4 mar = march(pos,ray);
            vec3 nor = normal(mar.xyz);
            vec3 ref = refract(ray,nor,.75);
            float r = smoothstep(.8,1.,dot(reflect(ray,nor),lig));
            float l = 1.-dot(ray,nor);
            vec3 wat = background(ref)+.3*r*l*l;
            vec3 bac = background(ray)*.5+.5;

            float fade = pow(min(mar.w/20.,1.),.3);
            col += mix(wat,bac,fade);
        }
        col /= AA*AA;
        vec3 col_inverse = vec3(1.0-col.r,1.0-col.g,1.0-col.b);
        float intensity = col_inverse.r + 0.2;
        
        vec3 desired_color = vec3(138.0/255,8.0/255,8.0/255);
        vec3 comp_color = vec3(8.0/255,136.0/255,136.0/255);
        gl_FragColor = vec4(desired_color*intensity,1);
        //gl_FragColor = vec4(desired_color*intensity + comp_color*(1.0-col_inverse.r)*0.5,1);
        //gl_FragColor = vec4(comp_color*intensity + desired_color*(1.0-col_inverse.r)*0.8,1);
    """)