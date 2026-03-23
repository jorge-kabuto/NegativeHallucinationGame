transform default_bg(framerate=60.0):
    mesh True
    pause 1.0/framerate
    repeat

define prev_was_menu = False
init -5 python:
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
    
    import hashlib
    prev_display_menu = renpy.display_menu
    def mem_menu(items, *args, **kwargs):

        hashes = []
        hashes_input = []

        for i,text_tuple in enumerate(items):
            temp_list = list(text_tuple)
            # Unpack safely
            if len(temp_list) == 2:
                text, value = temp_list
                condition = True
            else:
                text, value, condition = temp_list

            if not condition:
                continue

            filename, line = renpy.get_filename_line()
            hash_input = f"{filename}:{line}:{text}"
            line_hash = hashlib.sha1(hash_input.encode("utf-8")).hexdigest()

            # Modify text if seen before
            if line_hash in renpy.store.line_dict.keys():
                text = "{color=#3d4634}" + text + "{/color}"
                temp_list[0] = text
                items[i] = tuple(temp_list)

            hashes.append(line_hash)
            hashes_input.append(hash_input)

        menu_result = prev_display_menu(items, *args, **kwargs)

        # Safety: player may cancel menu (returns None)
        if menu_result is not None and 0 <= menu_result < len(hashes):
            renpy.store.line_dict[hashes[menu_result]] = hashes_input[menu_result]

        return menu_result
    renpy.display_menu = mem_menu

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
            uniform vec2 u_tex0_size;
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
            v_coord = vec2(gl_Position.x * .5 + .5, 1.0-(gl_Position.y * .5 + .5));
            v_coord = vec2(a_tex_coord.x, (a_tex_coord.y*1.0));
        """,

        fragment_300="""
            vec2 uv = v_coord;
            //vec2 texSize = vec2(textureSize2D(tex0, 0));
            vec2 texSize = u_tex0_size;

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
            uniform vec2 u_tex0_size;
            uniform vec2 u_drawable_size;
            uniform float u_radius;
            uniform vec3 u_outline_color;
            uniform bool u_should_overlay;
            uniform vec2 u_scale;
            uniform vec2 u_pixel_offset;
            
            varying vec2 v_coord;
            
            attribute vec2 a_tex_coord;
        """,
        vertex_300="""
            v_coord = vec2(a_tex_coord.x, (a_tex_coord.y));
        """,

        fragment_300="""
            //#extension GL_EXT_gpu_shader4: enable
            const vec3 target = vec3(0.0, 1.0, 0.0); // Find green
            const float TAU = 6.28318530;
            const float steps = 32.0;
            
            //vec2 otl_aspect = 1.0 / vec2(textureSize2D(tex0, 0));
            vec2 otl_aspect = 1.0 / vec2(1000.0,1000.0);
            //vec2 screen_scale = u_drawable_size / textureSize2D(tex0, 0);
            vec2 screen_scale = u_drawable_size / vec2(1000.0,1000.0);
            float unit_scale = max(screen_scale.x,screen_scale.y);

            vec2 center = u_pixel_offset;
            vec2 otl_uv = ((v_coord-center)/2.5)/u_scale + center;
            vec2 clamped_uv = clamp(otl_uv, 0.0, 1.0);

            if(otl_uv.x < 0.0 || otl_uv.x > 1.0) discard;
            if(otl_uv.y < 0.0 || otl_uv.y > 1.0) discard;
            
            // Correct aspect ratio
            
            vec4 final_color = vec4(0.0,0.0,0.0,1.0);
            for (float i = 0.0; i < TAU; i += TAU / steps) {
                // Sample image in a circular pattern
                vec2 offset = vec2(sin(i), cos(i)) * otl_aspect * u_radius;
                vec4 col = texture2D(tex0, clamped_uv + offset);
                float mask = step(length(otl_uv - clamped_uv), 0.00001);
                col *= mask;
                
                // Mix outline with background
                float alpha = smoothstep(0.5, 0.7, distance(col.rgb, target));
                final_color = mix(final_color, vec4(u_outline_color, 1.0), alpha);
            }
            
            // Overlay original video
            if(u_should_overlay){
                vec4 mat = texture2D(tex0, clamped_uv);
                float mask = step(length(otl_uv - clamped_uv), 0.00001);
                mat *= mask;
                float factor = smoothstep(0.5, 0.7, distance(mat.rgb, target));
                if(final_color.rgb == vec3(0.0)) discard;
                gl_FragColor = mix(final_color, mat, factor);
            }else{
                if(final_color.rgb == vec3(0.0)) discard;
                gl_FragColor = final_color;
            }
            //gl_FragColor = vec4(v_coord.x, v_coord.y, 0.0, 1.0);
        """
    )

    renpy.register_shader(
        "Tunnel",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_drawable_size;
            uniform float u_time;
            uniform float u_speed_scale;

            varying vec2 v_coord;
            
            attribute vec2 a_tex_coord;
        """,vertex_300="""
            v_coord = gl_Position.xy;
            v_coord = vec2(a_tex_coord.x-0.2, (a_tex_coord.y-0.2));
        """,fragment_300="""
            vec2 p = v_coord;
            gl_FragColor.w = length(p);
            if (gl_FragColor.w < 0.1) discard;
            vec2 tuv = vec2(atan(p.y,p.x), .2/gl_FragColor.w)+u_time*u_speed_scale ;
            tuv = vec2(mod(tuv.x/3.14,1.0),mod(tuv.y/2.0,1.0));
            gl_FragColor = texture2D(tex0, tuv) * (gl_FragColor.w*4.0);
        """,
    )

    store.bg_states = {}
    class UniformTween(object):
        """
        Tween for arbitrary dict-like uniform sets, used for shader input interpolation.
        Keys are strings; values can be numbers, tuples of numbers, or bools.
        """

        def _clamp01(self, x):
            if x <= 0.0:
                return 0.0
            if x >= 1.0:
                return 1.0
            return x

        def _smoothstep(self, t):
            # Hermite smoothstep: 3t^2 - 2t^3
            return t * t * (3.0 - 2.0 * t)

        def _lerp(self, a, b, t):
            # Supports numbers and tuples/lists of numbers. Falls back to step for bools/others.
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return a + (b - a) * t
            if isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)) and len(a) == len(b):
                return tuple(self._lerp(a[i], b[i], t) for i in range(len(a)))
            if isinstance(a, bool) and isinstance(b, bool):
                return a if t < 0.5 else b
            return a if t < 0.5 else b

        def __init__(self, initial_values):
            self.current = dict(initial_values)
            self._from = dict(initial_values)
            self._to = dict(initial_values)
            self._start_st = 0.0
            self._duration = 0.0
            self._use_smoothstep = True
            self._last_st = 0.0

        def start(self, target_values, start_st, duration, use_smoothstep):
            """
            Begin a tween toward target_values from the current state.
            """
            self._from = dict(self.current)
            self._to = dict(target_values)
            self._start_st = float(start_st or 0.0)
            self._duration = float(duration or 0.0)
            self._use_smoothstep = bool(use_smoothstep)

        def advance(self, st):
            """
            Advance this tween channel to time st and return the current values dict.
            """
            self._last_st = st

            dur = self._duration or 0.0
            if dur <= 0.0:
                self.current = dict(self._to)
                return self.current

            t = self._clamp01((st - self._start_st) / dur)
            if self._use_smoothstep:
                t = self._smoothstep(t)

            out = {}
            keys = set(self._from.keys()) | set(self._to.keys())
            for k in keys:
                a = self._from.get(k, self._to.get(k))
                b = self._to.get(k, a)
                out[k] =self._lerp(a, b, t)

            self.current = out
            return out
###
#Some Shaders to look into:
#SPECTRALIZER https://www.shadertoy.com/view/wXscWN
#maze https://www.shadertoy.com/view/MldSzr
#reaction diffusion https://www.shadertoy.com/view/ctfGDl
#rythmic fluid https://www.shadertoy.com/view/XsyfDm
# Satin Flow https://www.shadertoy.com/view/Mstczn
# Submerge https://www.shadertoy.com/view/NdBBzm -- There are more submerge versions!!
# Fluorescent https://www.shadertoy.com/view/WcGGDd
# Paradise 3 https://www.shadertoy.com/view/WcsyDM
# Light Rays https://www.shadertoy.com/view/lljGDt
# Bubbles https://www.shadertoy.com/view/4dl3zn
# Desert Sand https://www.shadertoy.com/view/WdjXRR
###