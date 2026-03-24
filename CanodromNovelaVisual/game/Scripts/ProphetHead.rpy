init python:
    from renpy.python import NoRollback

    # Global values shared by all presets unless explicitly overridden.
    PH_BALATRO_GLOBAL_DEFAULTS = {
        "u_offset": (0.0, 0.0),
        "u_is_rotate": True,
        "u_pixel_filter": 1920,
    }

    # Prepare your presets here. Any key omitted will fall back to base/global defaults.
    PH_BALATRO_PRESETS = {
        "default": {
            "u_color_1": (0.82, 0.0, 0.18, 1.0),
            "u_color_2": (0.391, 0.017, 0.592, 1.0),
            "u_color_3": (0.204, 0.0, 0.349, 1.0),
            "u_spin_rotation": 0.5,
            "u_spin_speed": -5.0,
            "u_contrast": 4,
            "u_lighting": 0.6,
            "u_spin_amount": 0.25,
            "u_spin_ease": 1.1,
        },
        "fast": {
            "u_color_1": (0.0, 0.0, 0.18, 1.0),
            "u_color_2": (0.0, 0.017, 0.592, 1.0),
            "u_color_3": (0.0, 0.0, 0.349, 1.0),
            "u_spin_rotation": 0.5,
            "u_spin_speed": -10.0,
            "u_contrast": 6,
            "u_lighting": 0.6,
            "u_spin_amount": 0.4,
            "u_spin_ease": 1.15,
        }
    }

    def ph_build_balatro_target(preset_dict):
        """
        Merge base defaults + global defaults + preset overrides (in that order).
        """
        target = dict(PH_BALATRO_GLOBAL_DEFAULTS)
        if preset_dict: target.update(preset_dict)
        return target
    
    class PhState(NoRollback):
        def __init__(self):
            self.tex = None
            self.pfp = None
            self.balatro = UniformTween(ph_build_balatro_target(PH_BALATRO_PRESETS.get("default")))
    store.bg_states["PhState"] = PhState()

    def ph_set_balatro_preset(name="default", duration=0.5, use_smoothstep=True):
        """
        Start a smooth presetition of balatro uniforms toward a named preset.
        Call from script, or via an ATL presetform (see `ph_to_preset` below).
        """
        preset = PH_BALATRO_PRESETS.get(name, None)
        if preset is None:
            preset = PH_BALATRO_PRESETS["default"]

        # Snapshot current as the presetition start.
        target = ph_build_balatro_target(preset)
        ch = store.bg_states["PhState"].balatro
        ch.start(target, getattr(ch, "_last_st", 0.0), duration=duration, use_smoothstep=use_smoothstep)

    def ph_get_uniforms(st):
        return store.bg_states["PhState"].balatro.advance(st)

    class PhBackground(renpy.Displayable):

        def __init__(self, child=None, image_path="", **kwargs):
            super(PhBackground, self).__init__(**kwargs)
            self.image_path = image_path

        def render(self, width, height, st, at):
            
            ds = 1.0/4.0
            if store.bg_states["PhState"].tex is None:
                store.bg_states["PhState"].tex = renpy.load_image("images/backgrounds/dark_waters.png")
            if store.bg_states["PhState"].pfp is None:
                store.bg_states["PhState"].pfp = Image(self.image_path)

            u = ph_get_uniforms(st)
            buffer_a = renpy.Render(width*ds, height*ds)
            buffer_b = renpy.Render(width*ds, height*ds)
            buffer_otl = renpy.Render(width*ds, height*ds)

            pfp_render = renpy.render(store.bg_states["PhState"].pfp, 1000, 1000, st, at)
            buffer_otl.blit(pfp_render,(0,0))
            buffer_otl.add_shader("SimpleOutline")
            # buffer_otl.add_uniform("u_tex0_size", (width*ds, height*ds))
            buffer_otl.add_uniform("u_radius",10)
            buffer_otl.add_uniform("u_outline_color",u["u_color_2"])
            buffer_otl.add_uniform("u_should_overlay",True)
            buffer_otl.add_uniform("u_pixel_offset",(0.5,0.125))
            buffer_otl.add_uniform("u_scale",(0.4,0.4)) 

            buffer_a.add_shader("balatro")
            buffer_a.add_uniform("u_color_1", u["u_color_1"])
            buffer_a.add_uniform("u_color_2", u["u_color_2"])
            buffer_a.add_uniform("u_color_3", u["u_color_3"])
            buffer_a.add_uniform("u_spin_rotation", u["u_spin_rotation"])
            buffer_a.add_uniform("u_spin_speed", u["u_spin_speed"])
            buffer_a.add_uniform("u_is_rotate", u["u_is_rotate"])
            buffer_a.add_uniform("u_offset", u["u_offset"])
            buffer_a.add_uniform("u_contrast", u["u_contrast"])
            buffer_a.add_uniform("u_lighting", u["u_lighting"])
            buffer_a.add_uniform("u_spin_amount", u["u_spin_amount"])
            buffer_a.add_uniform("u_pixel_filter", u["u_pixel_filter"])
            buffer_a.add_uniform("u_spin_ease", u["u_spin_ease"])
            buffer_a.blit(store.bg_states["PhState"].tex,(0,0))

            store.bg_states["PhState"].tex = renpy.render_to_surface(buffer_a, resize=False)
            # buffer_b.add_shader("Tunnel")
            # buffer_b.add_uniform("u_speed_scale",0.0)
            # buffer_b.blit(store.bg_states["PhState"].tex,(0,0))
            
            
            present = renpy.Render(width, height)

            scaled_tex_a = renpy.display.scale.smoothscale(store.bg_states["PhState"].tex, (width, height))
            scaled_tex_b = renpy.display.scale.smoothscale(renpy.render_to_surface(buffer_b, resize=False), (width, height))
            present.blit(scaled_tex_a,(0,0))
            # present.blit(scaled_tex_b,(0,0))
            present.blit(buffer_otl,(0,0))
            renpy.redraw(self, 0)

            return present

label ph_intro:
    default ph_bg = PhBackground(image_path="images/prophets_head_pf_chroma.png")
    scene black
    show expression ph_bg at default_bg
    $ ph_set_balatro_preset("fast", 0.0)

    nvl clear
    aaa "You drop down. You fall for a long time, the light leaves the tunnel through a pinpoint in the periapsis of your vision."
    aaa "Sinking deep, no colour comes to meet you. Not like before, through the sea."
    aaa "You fall, and in your falling, water comes to meet you. It catches you as a mother embraces their child, gentle caress for those forlorn."
    aaa "Your speed amerionates, and another layer, more solid, grounds you."
    aaa "Here, there is light, coming from above as if the scorching desert was only a few inches away."
    aaa "The walls are luminous reflection, the air rather damp."
    aaa "There, against the wall, a disembodied head. Its gaze, two trembling moons of green, indicates that they are, against all odds, alive."
    ph ".................."
    babel "You shouldn't have come." (func=ph)
    $ ph_set_balatro_preset("default", 10.0)
    babel "You couldn't have, even if you wanted to." (func=ph)
    babel "...*Cough-gh* Sorry. Long time without a talk. What is your name?" (func=ph)
label ph_1:
    menu (nvl=True):
        "Yours comes first.":
            ph "I.... Okay. I had a long time to give myself a shape. I am the Prophet."
            e "I must say, a little arrogant on your part."
            ph "I am one that seeks the light and may bring it into the world, where others failed."
            ph "Now I believe you owe me something."
            e "I don't have one. As of yet. Although after hearing yours, anything goes I guess."
            ph "One can only announce their names after being shapen by it. Most are chosen by others, mine is a rare case of isolation."
            ph "Others may have already tried to give you one, *C-Cough**Cough* or even take the potential to even own one from you."
            e "Color me impressed. I am starting to believe you are indeed a Prophet."
            ph "Mock me all you want."
            jump ph_1

        "Or what? The worst you could do is give me evil eye.":
            ph "Oh I could do much more than that. (A savage smirk is sketched on their face)"
            aaa "They mean it. You suddenly feel a little unconfortable, like the temperature around you has risen."
            e "We'll see about that..."
            jump ph_1
        "(Ignore him and explore around)":
            aaa "You move away from the head. It still beckons you, between spurious coughing."
            jump ph_1