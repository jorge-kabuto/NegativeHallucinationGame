define prev_was_menu = False
init python:
    config.keymap["dismiss"].append("K_1")
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
            renpy.exports.say(None, "{cps=0}{color=[youtext]}??? —\n" + statement + "{/color}{/cps}", interact=False)
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

    renpy.register_shader(
        "CircleFilter",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_drawable_size;
            uniform vec2 u_center_percentage;
            uniform float u_radius_percentage;
            uniform bool u_reverse;
            varying vec2 v_coord;
        """,

        fragment_functions="""
        float circle_mask(vec2 uv, vec2 center, float radius){
            float d = distance(uv, center);
            return step(d, radius);
        }
        float circle_mask_smooth(vec2 uv, vec2 center, float radius, vec2 tex_size){
            // compute aspect ratio from texture
            float aspect = tex_size.x / tex_size.y;

            // center and compensate aspect
            vec2 centered_uv = uv - center;
            centered_uv.x *= aspect;

            // distance in aspect-corrected space
            float d = length(centered_uv);

            // smooth edge
            return smoothstep(radius, radius * 0.5, d);
        }
        """,

        vertex_300="""
            v_coord = vec2(gl_Position.x * .5 + .5, gl_Position.y * .5 + .5);
        """,

        fragment_300="""
            #extension GL_EXT_gpu_shader4: enable
            vec2 uv = v_coord;
            vec2 texSize = vec2(textureSize2D(tex0, 0));

            // center and radius in pixel space
            vec2 center = u_center_percentage;
            float radius = u_radius_percentage;

            // shift UV toward center and scale
            //  vec2 centered_uv = uv - center;
            //  centered_uv /= 0.5;  // scale UVs inward
            //  vec2 scaled_uv = center + centered_uv;

            vec4 color = texture2D(tex0, uv);
            float mask_factor = circle_mask_smooth(uv, center, radius, texSize);

            if(u_reverse){
                gl_FragColor = color * (1.0-mask_factor);
            }else{
                gl_FragColor = color * mask_factor;
            }
        """
    )

    renpy.register_shader(
        "SimpleOutline",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_drawable_size;
            uniform float u_radius;
            uniform vec3 u_outline_color;
            uniform bool u_should_overlay;
            varying vec2 v_coord;
        """,
        vertex_300="""
            v_coord = vec2(gl_Position.x * .5 + .5, gl_Position.y * .5 + .5);
            //v_coord = vec2(gl_Position.xy);
        """,

        fragment_300="""
            #extension GL_EXT_gpu_shader4: enable
            const vec3 target = vec3(0.0, 1.0, 0.0); // Find green
            const float TAU = 6.28318530;
            const float steps = 32.0;
            
            // vec2 otl_uv = v_coord * vec2(2.0,1.0) + vec2(0.1,0.0);
            vec2 otl_uv = v_coord;
            
            // Correct aspect ratio
            vec2 otl_aspect = 1.0 / vec2(textureSize2D(tex0, 0));
            
            vec4 final_color = vec4(0.0,0.0,0.0,1.0);
            for (float i = 0.0; i < TAU; i += TAU / steps) {
                // Sample image in a circular pattern
                vec2 offset = vec2(sin(i), cos(i)) * otl_aspect * u_radius;
                vec4 col = texture2D(tex0, otl_uv + offset);
                
                // Mix outline with background
                float alpha = smoothstep(0.5, 0.7, distance(col.rgb, target));
                final_color = mix(final_color, vec4(u_outline_color, 1.0), alpha);
            }
            
            // Overlay original video
            if(u_should_overlay){
                vec4 mat = texture2D(tex0, otl_uv);
                float factor = smoothstep(0.5, 0.7, distance(mat.rgb, target));
                gl_FragColor = mix(final_color, mat, factor);
            }else{
                if(final_color == vec4(0.0,0.0,0.0,1.0)) discard;
                gl_FragColor = final_color;
            }
        """
    )

    

###
#Some Shaders to look into:
#SPECTRALIZER https://www.shadertoy.com/view/wXscWN
#maze https://www.shadertoy.com/view/MldSzr
#reaction diffusion https://www.shadertoy.com/view/ctfGDl
#rythmic fluid https://www.shadertoy.com/view/XsyfDm
# Satin Flow https://www.shadertoy.com/view/Mstczn
# Submerge https://www.shadertoy.com/view/NdBBzm
###