transform reaction_diffusion:
    shader "ReactionDiffusion2"
    pause 1.0/24
    repeat

init python:
    config.use_cpickle = False
    class ReactionDiffusion(renpy.Displayable):

        def __init__(self, child=None, blur1=20.0,blur2=80.0, **kwargs):
            super(ReactionDiffusion, self).__init__(**kwargs)
            self.buffer_a = None
            self.tex = None
            self.blur1 = blur1
            self.blur2 = blur2

        def render(self, width, height, st, at):
            
            ds = 1.0/2.0
            # eff_x = 400
            # eff_y = 400

            if self.buffer_a is None:
                self.buffer_a = renpy.Render(width*ds, height*ds)
                # self.buffer_a = renpy.Render(eff_x, eff_y)
            if self.tex is None:
                self.tex = renpy.render_to_surface(self.buffer_a, resize=False)

            self.buffer_a = renpy.Render(width*ds, height*ds)
            # self.buffer_a = renpy.Render(eff_x, eff_y)
            self.buffer_a.blit(self.tex,(0,0))
            self.buffer_a.add_shader("ReactionDiffusion2")
            self.buffer_a.add_uniform("u_blur_1", self.blur1)
            self.buffer_a.add_uniform("u_blur_2", self.blur2)

            self.tex = renpy.render_to_surface(self.buffer_a, resize=False)
            present = renpy.Render(width, height)
            self.tex=renpy.display.scale.smoothscale(self.tex, (width, height))
            present.blit(self.tex,(0,0))
            renpy.redraw(self, 0)

            return present

    renpy.register_shader("ReactionDiffusion2", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform vec2 u_drawable_size;
        uniform float u_blur_1;
        uniform float u_blur_2;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;
        varying vec2 v_position;

        attribute vec4 a_position;
        
    """, fragment_functions="""
        #extension GL_EXT_gpu_shader4 : enable
        #define M1 1597334677U
        #define M2 3812015801U
        //monochrome fast blur
        float monoBlur(sampler2D channel, vec2 uv, vec2 scale, float step){
            float result = 0.0;
            int i=0;
            vec2 d;
            for(float y=-scale.y; y < scale.y; y+=step){
            for(float x=-scale.x; x < scale.x; x+=step){
                d = vec2(x, y);
                result += texture2D(channel, uv + (d / u_drawable_size.xy)).r*(1.0-smoothstep(0.0, scale.y*2.0,  length(d)));

                i++;
            }}
            return result / float(i);
        }

        //Fast Hash
        float hash(uint q_x, uint q_y ){
            q_x *= M1;
            q_y *= M2;
            uint n = (q_x ^ q_y) * M1;
            return float(n) * (1.0/float(0xffffffffU));
        }

    """,  vertex_300="""
        v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, -gl_Position.y * .5 + .5);
        v_position = a_position.xy;
    """, fragment_300="""

        #define PI2 6.28318530718

        //coordinates
        vec2 uv = v_coord/u_drawable_size.xy;
        vec2 uvR = (v_coord - .5 * u_drawable_size.xy)/u_drawable_size.y;
        float aspect = u_drawable_size.x / u_drawable_size.y;
        
        //noise and audio data
        vec3 noise = vec3(1.0,1.0,1.0) * hash(uint(v_coord.x*u_time),uint(v_coord.y*u_time));
        noise.r = clamp(noise.r, 0.0, 1.0);
        float fft = 0.0;//texture2D(iChannel1,vec2(length(uvR), 0.25)).r;
        float wave = 0.0;//texture2D(iChannel1, vec2(uv.x, 0.75)).r;
        
        //lookup uv
        vec2 uv2 = (uv - 0.5);
        uv2 *= 0.999 * (1.0+(length(uv2/2.0) /300.0));
        uv2 *= 1.0 - (.03 * fft) * (0.5 + 0.25 * smoothstep(length(vec2(aspect,1.0)) / 2.0, 0.0, length(uvR)));
        uv2.x += (.0001 + .002 * fft) * sin(wave + u_time + uv2.y*10.0);
        uv2.y += (.0001 + .002 * fft) * cos(wave + u_time + uv2.x*10.0);
        uv2 = uv2 + 0.5;
        
        //feedback
        vec3 prev = texture2D(tex0, uv2).rgb;
    
        //dymamic blur
        float vB = u_blur_2 - (u_blur_2 * (0.5 + 0.5 * sin(u_time)) - u_blur_1 - 2.0); 
        
        //get two versions of blurred image
        vec3 blur1 = vec3(monoBlur(tex0, uv2, vec2(u_blur_1),u_blur_1/4.0));
        vec3 blur2 = vec3(monoBlur(tex0, uv2, vec2(vB),(vB)/6.0));
        
        //reaction diffusion
        vec3 col = prev - (blur2 - blur1*0.999);

        //seed with noise
        //col -= (0.0 + 1.0*fft)/16.0;
        col += (noise.r-0.5)/8.0;
        
        //prevent value runaway
        col = clamp(col, 0.0, 1.0);
        col = vec3(col.r,0.05,0.05);
        
        // Output to screen
        gl_FragColor = vec4(col, 1.0);
    """)