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

    renpy.register_shader("PresentFullscreen", variables="""
        uniform sampler2D tex0;
        uniform vec2 u_drawable_size;
        uniform vec2 u_size_custom;
        varying vec2 v_coord;
    """,vertex_300="""
        v_coord = u_size_custom * vec2(gl_Position.x * .5 + .5, -gl_Position.y * .5 + .5);
    """,fragment_300="""
        vec2 uv = v_coord/u_size_custom.xy;
        gl_FragColor = vec4(texture2D(tex0,uv).rgb,1.0);
    """)

    renpy.register_shader("CircleFilter", variables="""
        uniform sampler2D tex0;
        uniform vec2 u_drawable_size;
        uniform vec2 u_center_percentage;
        uniform float u_radius_percentage;
        varying vec2 v_coord;
    """,fragment_functions="""
    vec4 circle(vec2 uv, vec2 pos, float rad, vec3 color) {
        float d = length(pos - uv) - rad;
        float t = clamp(d, 0.0, 500.0);
        return vec4(color, 1.0 - t/500.0);
    }
    """,vertex_300="""
        v_coord = u_drawable_size * vec2(gl_Position.x * .5 + .5, gl_Position.y * .5 + .5);
    """,fragment_300="""
        vec2 uv = v_coord/u_drawable_size.xy;
        vec2 center = u_drawable_size.xy * u_center_percentage;
        float radius = u_radius_percentage * u_drawable_size.y;
        gl_FragColor = vec4(texture2D(tex0,uv).rgb,1.0);
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