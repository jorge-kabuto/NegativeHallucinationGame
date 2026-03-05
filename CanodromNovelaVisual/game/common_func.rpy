define prev_was_menu = False
init python:

    # renpy.exports.get_sdl_window_pointer()

    def color(what, color, character, *args, **kwargs):
        renpy.exports.say(None, f"{{cps=0}}{{color={color}}}{character}{{/color}} — {{/cps}}\n" + what, *args, **kwargs)
    
    def tw(what,  *args, **kwargs):
        color(what, "#a50606", "{shader=jitter:(1.5,1.5)}THE TWICE SHADOWED{/shader}", *args, **kwargs)
    def e(what,  *args, **kwargs):
        color(what, "#00bd94", "???", *args, **kwargs)
    def r(what,  *args, **kwargs):
        color(what, "#271fff", "The Reflection", *args, **kwargs)
    def ph(what,  *args, **kwargs):
        color(what, "#ae9100", "The Prophet's Head", *args, **kwargs)
    def n(what,  *args, **kwargs):
        color(what, "#3d4634", "¤¤¤¤", *args, **kwargs)
    def aaa(what,  *args, **kwargs):
        color(what, "#3d4634", "", *args, **kwargs)

    def whirlwind(what, func, *args, **kwargs):
        
        prev_anim_time = store.gui.nvl_anim_time
        store.gui.nvl_anim_time = 0.0#max(0.01, 0.9/store.preferences.text_cps)
        msg = ""
        for c in what[:-1]:
            msg += c
            func("{cps=0}"+msg, interact=False)
            renpy.exports.mode("say")
            renpy.ui.saybehavior()
            rv = renpy.ui.interact(mouse="pause", pause=0.01)
            if renpy.is_skipping() or rv != False:
                break

        store.gui.nvl_anim_time = prev_anim_time
        func("{cps=0}"+what, *args, **kwargs)
    
    # def get_default_textshader():
    #     return "typewriter"
    # config.default_textshader = "default"
    # config.textshader_callbacks["default"] = get_default_textshader

    def menu_prev_line(name):

        if renpy.last_say().what is not None and store.prev_was_menu:
            import re
            statement = re.sub("{color.*color}", "", store.last_choice_label)
            renpy.exports.say(None, "{cps=0}{nw}{color=[youtext]}??? —\n" + statement + "{/color}{/cps}")
            store.prev_was_menu = False

        if renpy.last_say().what is not None and "menu-nvl" in name:
            store.prev_was_menu = True
        
    config.statement_callbacks.append(menu_prev_line)

    renpy.register_shader("example.gradient", variables="""
        uniform vec4 u_gradient_left;
        uniform vec4 u_gradient_right;
        uniform vec2 u_model_size;
        varying float v_gradient_done;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_done= a_position.x / u_model_size.x;
    """, fragment_300="""
        float gradient_done = v_gradient_done;
        gl_FragColor *= mix(u_gradient_left, u_gradient_right, gradient_done);
    """)

    

    renpy.register_shader("ReactionDiffusion2", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform vec2 u_drawable_size;

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
        const float blurSize1 = 20.0;
        const float blurSize2 = 80.0;

        //coordinates
        vec2 uv = v_coord/u_drawable_size.xy;
        vec2 uvR = (v_coord - .5 * u_drawable_size.xy)/u_drawable_size.y;
        float aspect = u_drawable_size.x / u_drawable_size.y;
        
        //noise and audio data
        vec3 noise = vec3(1.0,1.0,1.0) * hash(uint(v_coord.x*u_time),uint(v_coord.y*u_time));
        noise.r = clamp(noise.r, 0.0, 1.0);
        float fft = 0.1;//texture2D(iChannel1,vec2(length(uvR), 0.25)).r;
        float wave = 5.0;//texture2D(iChannel1, vec2(uv.x, 0.75)).r;
        
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
        float vB = blurSize2 - (blurSize2 * (0.5 + 0.5 * sin(u_time)) - blurSize1 - 2.0); 
        
        //get two versions of blurred image
        vec3 blur1 = vec3(monoBlur(tex0, uv2, vec2(blurSize1),blurSize1/4.0));
        vec3 blur2 = vec3(monoBlur(tex0, uv2, vec2(vB),(vB)/6.0));
        
        //reaction diffusion
        vec3 col = prev - (blur2 - blur1*0.999);

        //seed with noise
        //col -= (0.0 + 1.0*fft)/16.0;
        col += (noise.r-0.5)/8.0;
        
        //prevent value runaway
        col = clamp(col, 0.0, 1.0);

        
        // Output to screen
        gl_FragColor = vec4(col, 1.0);
    """)

###
#Some Shaders to look into:
#SPECTRALIZER https://www.shadertoy.com/view/wXscWN
#maze https://www.shadertoy.com/view/MldSzr
#reaction diffusion https://www.shadertoy.com/view/ctfGDl
#rythmic fluid https://www.shadertoy.com/view/XsyfDm
# Satin Flow https://www.shadertoy.com/view/Mstczn
# Submerge https://www.shadertoy.com/view/NdBBzm
###