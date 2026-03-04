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
        store.gui.nvl_anim_time = max(0.01, 0.9/store.preferences.text_cps)
        msg = ""
        for c in what[:-1]:
            msg += c
            func("{cps=0}"+msg, interact=False)
            renpy.exports.mode("say")
            renpy.ui.saybehavior()
            rv = renpy.ui.interact(mouse="pause", pause=store.gui.nvl_anim_time)
            if renpy.is_skipping() or rv != False:
                break

        store.gui.nvl_anim_time = prev_anim_time
        func("{cps=0}"+what, *args, **kwargs)
    
    # def get_default_textshader():
    #     return "typewriter"
    # config.default_textshader = "default"
    # config.textshader_callbacks["default"] = get_default_textshader

    # def menu_prev_line(name):

    #     if renpy.last_say().what is not None and store.prev_was_menu:
    #         import re
    #         statement = re.sub("{color.*color}", "", store.last_choice_label)
    #         preferences.text_cps = 0
    #         renpy.exports.say(None, "{nw}{color=[youtext]}??? —" + statement + "{/color}")
    #         preferences.text_cps = 80
    #         store.prev_was_menu = False

    #     if renpy.last_say().what is not None and "menu-nvl" in name:
    #         store.prev_was_menu = True
        
    # config.statement_callbacks.append(menu_prev_line)

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

###
#Some Shaders to look into:
#SPECTRALIZER https://www.shadertoy.com/view/wXscWN
#maze https://www.shadertoy.com/view/MldSzr
#reaction diffusion https://www.shadertoy.com/view/ctfGDl
#rythmic fluid https://www.shadertoy.com/view/XsyfDm
###