transform submerge_default:
    shader ['submerge']
    u_res_scale 4.0
    u_tint (1.0, 1.0, 2.5)
    # matrixcolor SaturationMatrix(0.1)
    # matrixcolor TintMatrix("#f00")
    pause 1.0/30 #Divide by desired framerate
    repeat

transform submerge_main_menu:
    shader ['submerge']
    mesh True
    u_res_scale 6.0
    u_uv_min(0.218,0.0)
    u_uv_max(1.0,1.0)
    u_tint (1.0, 1.0, 2.5)
    # matrixcolor SaturationMatrix(0.1)
    # matrixcolor TintMatrix("#f00")
    pause 1.0/30 #Divide by desired framerate
    repeat

transform submerge_pf:
    shader ['submerge']
    u_res_scale 4.0
    u_uv_min(0.0,0.0)
    u_uv_max(0.55,1.0)
    # u_tint (1.0, 1.0, 2.5)
    u_tint (0.0, 0.0, 0.3)
    # matrixcolor SaturationMatrix(0.1)
    # matrixcolor TintMatrix("#f00")
    pause 1.0/30 #Divide by desired framerate
    repeat

init python:
    from renpy.python import NoRollback

    submerge_def = {
        "u_res_scale": 1.0,
        "u_tint": (0.0, 0.0, 0.0),
        "u_uv_min": (0.0,0.0),
        "u_uv_max": (1.0,1.0),
    }

    submerge_presets = {
        "main_menu": {
                "u_res_scale": 6.0,
                "u_uv_min": (0.218,0.0),
                "u_uv_max": (1.0,1.0),
                "u_tint": (1.0, 1.0, 2.5),
        },
        "pf_start": {
                "u_uv_min": (0.0,0.0),
                "u_uv_max": (0.55,1.0),
                "u_tint": (0.0, 0.0, 0.3),
        },
        "pf_emerging": {
                "u_uv_min": (0.0,0.0),
                "u_uv_max": (0.55,1.0),
                "u_tint": (1.0, 1.0, 2.5),
        },
    }

    def submerge_build_target(preset_dict):
        target=dict(submerge_def)
        if preset_dict: target.update(preset_dict)
        return target

    class SubmergeState(NoRollback):
        def __init__(self):
            self.tex = None
            self.bg = None
            self.submerge = UniformTween(submerge_build_target(submerge_def.get("pf_start")))
    store.bg_states["SubmergeState"] = SubmergeState()

    def submerge_set_preset(name="pf_start", duration=0.5, use_smoothstep=True):
        preset = submerge_presets.get(name, None)
        if preset is None:
            preset = submerge_presets["pf_start"]

        # Snapshot current as the presetition start.
        target = submerge_build_target(preset)
        ch = store.bg_states["SubmergeState"].submerge
        ch.start(target, getattr(ch, "_last_st", 0.0), duration=duration, use_smoothstep=use_smoothstep)

    def submerge_get_uniforms(st):
        return store.bg_states["SubmergeState"].submerge.advance(st)

    class SubmergeBackground(renpy.Displayable):

        def __init__(self, child=None, image_path="", **kwargs):
            super(SubmergeBackground, self).__init__(**kwargs)
            self.image_path = image_path

        def render(self, width, height, st, at):
            
            ds = 1.0/2.0
            if store.bg_states["SubmergeState"].bg is None:
                store.bg_states["SubmergeState"].bg = renpy.load_image(self.image_path)

            buffer_a = renpy.Render(width*ds, height*ds)
            buffer_a.blit(store.bg_states["SubmergeState"].bg, (0,0))
            buffer_a.add_shader("submerge")

            u = submerge_get_uniforms(st)
            for key, value in u.items():
                buffer_a.add_uniform(key, value)

            store.bg_states["SubmergeState"].tex = renpy.render_to_surface(buffer_a, resize=True)
            
            present = renpy.Render(width, height)
            present.add_shader("CircleFilter")
            present.add_uniform("u_tex0_size", (width, height))
            present.add_uniform("u_center_percentage", (0.30, 0.5))
            present.add_uniform("u_radius_percentage", 0.5)
            present.add_uniform("u_reverse", False)

            scaled_tex_a = renpy.display.scale.smoothscale(store.bg_states["SubmergeState"].tex, (width, height))
            present.blit(scaled_tex_a,(0,0))
            renpy.redraw(self, 0)

            return present

    # Created by Xor at https://www.shadertoy.com/view/NdBBzm
    renpy.register_shader("submerge", variables=
    """
        uniform float u_time;
        uniform vec2 u_drawable_size;
        uniform float u_res_scale;
        uniform vec3 u_tint;

        uniform vec2 u_uv_min;
        uniform vec2 u_uv_max;

        varying vec2 v_tex_coord;
        varying vec2 v_coord;

        attribute vec2 a_tex_coord;

    """, fragment_functions="""
        //Blur functions
        #define SAMPLES 64.0

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

            vec2 submg_uv = v_coord / u_drawable_size.xy;
            if (submg_uv.x < u_uv_min.x || submg_uv.y < (1.0-u_uv_max.y) ||
                submg_uv.x > u_uv_max.x || submg_uv.y > (1.0-u_uv_min.y))
            {
                discard;
            }

            vec2 low_res_coord = floor(v_coord / u_res_scale) * u_res_scale;

            vec3 ray = normalize(vec3(low_res_coord*2.0 - u_drawable_size.xy, u_drawable_size.x));
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

            gl_FragColor = vec4(u_tint * vec4(sqrt(spec) * fog).rgb, 1.0);
    """)