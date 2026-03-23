# The game starts here.
transform gradient:
    shader "example.gradient"
    u_gradient_right (0.0, 0.0, 1.0, 1.0)
    u_gradient_left (0.0, 0.0, 0.0, 1.0)

transform balatro:
    mesh True
    shader "balatro"
    u_color_1 (0.82, 0, 0.18, 1.0)
    u_color_2 (0.391, 0.017, 0.592, 1.0)
    u_color_3 (0.204, 0.00, 0.349, 1.0)
    u_spin_rotation 0.5
    u_spin_speed -5.0
    u_is_rotate True
    u_offset (0.0,0.0)
    u_contrast 4
    u_lighting 0.6
    u_spin_amount 0.25
    u_pixel_filter 1920
    u_spin_ease 1.1
    pause 1.0/60
    repeat

define slowfade = Fade(1.0, 0.0, 3.0)

# transform portrait:
    # shader "CircleFilter"
    # u_center_percentage (0.25,0.7)
    # u_radius_percentage (0.075)
    # u_reverse False
    # shader "SimpleOutline"
    # u_radius 10
    # u_outline_color (1.0,0.0,0.0)
    # rotate 360
    # zoom 0.5
    # blur 0.0
    # alpha 0.66
    # xoffset 1920*0.08

label start:
    default submerge_bg = SubmergeBackground(image_path="images/backgrounds/dark_waters.png")
    $ submerge_set_preset("pf_start", 0.0)
    # $ submerge_set_preset("pf_emerging", 0.0)
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # scene expression ReactionDiffusion()
    # scene dark_waters at reaction_diffusion
    scene black
    # show dark_waters at submerge_pf
    show expression submerge_bg
    with slowfade
    play sound beach_01
    # jump TwiceShadowedIntro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "Primordial blackness envelops you. Time itself is opaque to your senses."
    n "Provided that you still have those. Or that you ever possesed them to begin with."
    n "Reality is inky, flowing, a secret river causing downpour on a lightless cave."
    n "A few rules still seem to apply, strange and bent, like a backwards elbow, a flower closing into a golden seed."
    n "The cave, your gut tells, has a shape."
    
label intro_menu_01:
    menu(nvl=True):
        n "You have some time to reflect."
        "Let me rest. There is nothing for us out there, nothing I haven't seen already.":
            n "A self conjured mantle comes over you, white blindfold over unsharpened blades. If you had had any senses, you guard against them with all your meager might."
            n "Still, the current is strong. You feel the movement, a holistic sense of pathos. The density is different for you and your environment."
            n "A great fear cuts through your mind: there is no going back."
        "Where is this current? It feels like I'm going in circles, like the center of a whirlpool.":
            n "Prescience awakened by curiosity, you notice the current swirling. It feels faster on your right side, pulling you down and eastwards..."
            n "A shadow of a colour. A deep purple, the color of imminent dawn."
            n "You're moving towards sunrise."
        "No --nonononono. I should be somewhere, sometime... This isn't right.":
            n "The desperation claws at your mind. You flail, spasms of primal fear."
            n "The current seems to... accelerate, responding to you as a foreign body."
            n "You no longer belong here, and long to escape."

    $ submerge_set_preset("pf_emerging", 6.0)
    n "Countours are imagined and projected: a limit on the dark, something to both sustain and contain it."
    n "The deepest of azures fills you now. There's a top and a bottom, dissonance emerging."
    n "You wander upwards, buoyant despite never having drawn breath."
    n "The dark expells you, now differentiated. Lines drawn in the sand, turn to marble."
    n "There's shimmering at the surface, dancing lights at the change of mediums."
    n "And yet you know: a gnawing in the world, black maggots festering on the blanched porous stone."
    n "There's something you're forgetting."
    aaa"NEGATIVE HALLUCINATION"
    nvl clear

label DEBUG_MENU:
    menu(nvl=True):
        aaa"~DEBUG MENU~"
        "The Reflection Intro":
            jump ReflectionIntro
        "Twice Shadowed Intro":
            jump TwiceShadowedIntro
        "Prophet's Head Intro":
            jump ph_intro
