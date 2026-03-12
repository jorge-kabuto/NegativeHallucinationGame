transform submerge_default:
    shader "submerge"
    # matrixcolor SaturationMatrix(0.1)
    # matrixcolor TintMatrix("#f00")
    pause 1.0/60 #Divide by desired framerate
    repeat

# Created by Xor at https://www.shadertoy.com/view/NdBBzm
init python:
    renpy.register_shader("submerge", variables=
    """
        uniform float u_time;
        uniform vec2 u_drawable_size;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;

        attribute vec2 a_tex_coord;

    """, fragment_functions="""
        //Blur functions
        #define SAMPLES 64.0
        //#define TINT vec3(0.6, 0.6, 2.5)
        #define TINT vec3(1.0, 1.0, 2.5)

        vec2 hash2(vec2 p)
        {
            return normalize(fract(cos(p*mat2(95,74,86,83))*3742.0)-0.5);
        }

        vec4 fibonacci_blur(sampler2D tex, vec2 uv, vec2 texel, float radius)
        {
            vec4 blur = vec4(0.0);
            float total = 0.0;
            
            float scale = radius/sqrt(SAMPLES);
            vec2 point = hash2(uv)*scale;
            
            float rad = 1.0;
            mat2 ang = mat2(-0.7373688, -0.6754904, 0.6754904,  -0.7373688);
            
            for(float i = 0.0; i<SAMPLES; i++)
            {
                point *= ang;
                rad += 1.0/rad;
                
                vec2 coord = uv + point*(rad-1.0)*texel;
                float weight = 1.0/(1.0+i);
                vec4 samp = texture2D(tex, coord);
                
                blur += samp * weight;
                total += weight;
            }
            blur /= total;
            return blur;
        }
        ///Render water

        #define MAX 100.
        #define EPS 4e-4

        //Classic pseudo-random hash
        float hash(vec2 p)
        {
            return fract(sin(p.x*75.3 + p.y*94.2)*4952.);
        }
        //Bi-cubic value noise
        float value(vec2 p)
        {
            vec2 f = floor(p);
            vec2 s = p-f;
            s *= s * (3.0 - 2.0 * s);
            vec2 o = vec2(0, 1);
            
            return mix(mix(hash(f+o.xx),hash(f+o.yx),s.x),
                    mix(hash(f+o.xy),hash(f+o.yy),s.x),s.y);
        }
        //Approximate SDF from fractal value noise
        float dist(vec3 p)
        {
            vec2 n = p.xz*0.6+1.0;
            mat2 m = mat2(0.6754904, 0.7373688, -0.7373688, 0.6754904)*2.0;
            float weight = 0.3;
            float water = 0.0;
            float speed = 0.3;
            for(int i = 0; i<10; i++)
            {
                water += smoothstep(0.1, 0.9, value(n+speed*u_time)) * weight;
                n *= m;
                speed *= 1.3;
                weight *= 0.45;
            }
            return (water+0.5-p.y);
        }
        //Compute normals from SDF derivative
        vec3 normal(vec3 p)
        {
            vec2 e = vec2(4,-4)*EPS;
            return normalize(dist(p+e.yxx)*e.yxx+dist(p+e.xyx)*e.xyx+
                            dist(p+e.xxy)*e.xxy+dist(p+e.yyy)*e.yyy);
        }
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_coord = vec2(v_tex_coord.x,1.0-v_tex_coord.y) * u_drawable_size;
    """, fragment_300="""
            vec3 ray = normalize(vec3(v_coord*2.0 - u_drawable_size.xy, u_drawable_size.x));
            ray.yz *= mat2(cos(0.5+vec4(0,11,33,0)));
            vec3 pos = vec3(u_time*0.2,0,0);
            vec4 mar = vec4(pos,0);
            
            for(int i = 0; i<50; i++)
            {
                float stp = dist(mar.xyz);
                mar += vec4(ray, 1) * stp;
                
                if (stp<EPS || mar.w>MAX) break;
            }
            vec3 nor = normal(mar.xyz);
            vec3 sun = normalize(vec3(0,-1,9));
            vec3 ref = refract(ray, nor, 1.333);
            float spec = exp(dot(ref, sun) * 9.0 - 9.0);
            float fog = max(1.0 - mar.w/MAX, 0.0);

            gl_FragColor = vec4(TINT * vec4(sqrt(spec) * fog).rgb, 0.0);
    """)