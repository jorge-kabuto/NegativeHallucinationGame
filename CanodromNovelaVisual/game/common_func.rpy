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

    renpy.register_shader("balatro.test", variables=
    """
        uniform float u_time;
        uniform vec2 u_drawable_size;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;

        attribute vec2 a_tex_coord;

    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, -gl_Position.y * .5 + .5);
    """, fragment_300="""
        #define SPIN_ROTATION 0.5
        #define SPIN_SPEED -5.0
        #define OFFSET vec2(0.0, 0.0)
        #define COLOUR_1 vec4(0.82, 0, 0.18, 1.0)
        #define COLOUR_2 vec4(0.391, 0.017, 0.592, 1.0)
        #define COLOUR_3 vec4(0.204, 0.00, 0.349, 1.0)
        #define CONTRAST 4
        #define LIGTHING 0.6
        #define SPIN_AMOUNT 0.25
        #define PIXEL_FILTER 1920
        #define SPIN_EASE 1.1
        #define PI 3.14159265359
        #define IS_ROTATE true

        vec2 screenSize = u_drawable_size;
        vec2 outer_uv = v_coord/u_drawable_size.xy;
        vec2 screen_coords = outer_uv * u_drawable_size.xy;

        float pixel_size = length(screenSize.xy) / PIXEL_FILTER;
        vec2 uv = (floor(v_coord.xy*(1./pixel_size))*pixel_size - 0.5*screenSize.xy)/length(screenSize.xy) - OFFSET;
        float uv_len = length(uv);
        
        float speed = (SPIN_ROTATION*SPIN_EASE*0.2);
        if(IS_ROTATE){
        speed = u_time * speed;
        }
        speed += 302.2;
        float new_pixel_angle = atan(uv.y, uv.x) + speed - SPIN_EASE*20.*(1.*SPIN_AMOUNT*uv_len + (1. - 1.*SPIN_AMOUNT));
        vec2 mid = (screenSize.xy/length(screenSize.xy))/2.;
        uv = (vec2((uv_len * cos(new_pixel_angle) + mid.x), (uv_len * sin(new_pixel_angle) + mid.y)) - mid);
        
        uv *= 30.;
        speed = u_time*(SPIN_SPEED);
        vec2 uv2 = vec2(uv.x+uv.y);
        
        for(int i=0; i < 5; i++) {
            uv2 += sin(max(uv.x, uv.y)) + uv;
            uv  += 0.5*vec2(cos(5.1123314 + 0.353*uv2.y + speed*0.131121),sin(uv2.x - 0.113*speed));
            uv  -= 1.0*cos(uv.x + uv.y) - 1.0*sin(uv.x*0.711 - uv.y);
        }
        
        float contrast_mod = (0.25*CONTRAST + 0.5*SPIN_AMOUNT + 1.2);
        float paint_res = min(2., max(0.,length(uv)*(0.035)*contrast_mod));
        float c1p = max(0.,1. - contrast_mod*abs(1.-paint_res));
        float c2p = max(0.,1. - contrast_mod*abs(paint_res));
        float c3p = 1. - min(1., c1p + c2p);
        float light = (LIGTHING - 0.2)*max(c1p*5. - 4., 0.) + LIGTHING*max(c2p*5. - 4., 0.);
        gl_FragColor = (0.3/CONTRAST)*COLOUR_1 + (1. - 0.3/CONTRAST)*(COLOUR_1*c1p + COLOUR_2*c2p + vec4(c3p*COLOUR_3.rgb, c3p*COLOUR_1.a)) + light;
    """)

    renpy.register_shader("ReactionDiffusion2", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform vec2 u_drawable_size;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;

        attribute vec2 a_tex_coord;
        
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, -gl_Position.y * .5 + .5);
    """, fragment_300="""
        #extension GL_EXT_gpu_shader4 : enable
        #define PI2 6.28318530718
        #define M1 1597334677U
        #define M2 3812015801U

        //determines blob shape
        const float blurSize1 = 4.0;
        const float blurSize2 = 20.0;
        
        //coordinates
        vec2 uv = v_coord/u_drawable_size.xy;
        vec2 uvR = (v_coord - .5 * u_drawable_size.xy)/u_drawable_size.y;
        float aspect = u_drawable_size.x / u_drawable_size.y;
        
        //Fast Hash
        //noise and audio data
        vec2 q = vec2(v_coord*u_time);
        q *= vec2(M1, M2); 
        int n = (int(q.x) ^ int(q.y)) * M1;
        vec2 hash_result = float(n) * (1.0/float(0xffffffffU));
        
        vec3 noise = vec3(1.0,1.0,1.0) * hash_result;
        noise.r = clamp(noise.r, 0.0, 1.0);
        float fft = 0.0//texture(iChannel1,vec2(length(uvR), 0.25)).r;
        float wave = 0.0//texture(iChannel1, vec2(uv.x, 0.75)).r;
        
        //lookup uv
        vec2 uv2 = (uv - 0.5);
        uv2 *= 0.999 * (1.0+(length(uv2/2.0) /300.0));
        uv2 *= 1.0 - (.03 * fft) * (0.5 + 0.25 * smoothstep(length(vec2(aspect,1.0)) / 2.0, 0.0, length(uvR)));
        uv2.x += (.0001 + .002 * fft) * sin(wave + u_time + uv2.y*10.0);
        uv2.y += (.0001 + .002 * fft) * cos(wave + u_time + uv2.x*10.0);
        uv2 = uv2 + 0.5;
        
        //feedback
        vec3 prev = texture(tex0, uv2).rgb;
    
        //dymamic blur
        float vB = blurSize2 - (blurSize2 * (0.5 + 0.5 * sin(u_time)) - blurSize1 - 2.0); 
        
        //get two versions of blurred image
        sampler2D channel = tex0;
        vec2 blur_uv = uv2;
        vec2 scale = vec2(blurSize1);
        float step = blurSize1/4.0;
        float result = 0.0;
        int i=0;
        vec2 d;
        for(float y=-scale.y; y < scale.y; y+=step){
            for(float x=-scale.x; x < scale.x; x+=step){
                d = vec2(x, y);
                result += texture(channel, blur_uv + (d / u_drawable_size.xy)).r*(1.0-smoothstep(0.0, scale.y*2.0,  length(d)));
                i++;
            }
        }
        vec3 blur1 = vec3(result / float(i));

        //dymamic blur
        float vB = blurSize2 - (blurSize2 * (0.5 + 0.5 * sin(u_time)) - blurSize1 - 2.0); 
        
        //get two versions of blurred image
        sampler2D channel = tex0;
        vec2 blur_uv = uv2;
        vec2 scale = vec2(vB);
        float step = (vB)/6.0);
        float result = 0.0;
        int i=0;
        vec2 d;
        for(float y=-scale.y; y < scale.y; y+=step){
            for(float x=-scale.x; x < scale.x; x+=step){
                d = vec2(x, y);
                result += texture(channel, blur_uv + (d / u_drawable_size.xy)).r*(1.0-smoothstep(0.0, scale.y*2.0,  length(d)));
                i++;
            }
        }
        vec3 blur2 = vec3(result / float(i));
        
        //reaction diffusion
        vec3 col = prev - (blur2 - blur1*0.999);

        //seed with noise
        //col -= (0.0 + 1.0*fft)/16.0;
        col += (noise.r-0.5)/8.0;
        
        //prevent value runaway
        col = clamp(col, 0.0, 1.0);

        
        // Output to screen
        fragColor = vec4(col, 1.0);
    """)
###
#Some Shaders to look into:
#SPECTRALIZER https://www.shadertoy.com/view/wXscWN
#maze https://www.shadertoy.com/view/MldSzr
#reaction diffusion https://www.shadertoy.com/view/ctfGDl
#rythmic fluid https://www.shadertoy.com/view/XsyfDm
###