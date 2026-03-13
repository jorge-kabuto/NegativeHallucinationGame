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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # scene expression ReactionDiffusion()
    # scene dark_waters at reaction_diffusion
    scene black
    show dark_waters at submerge_default
    with slowfade
    play sound beach_01
    # jump TwiceShadowedIntro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "Primordial blackness envelops you. Time itself is opaque to your senses."
    n "Provided that you still have those. Or that you ever possesed them to begin with."
    n "Reality is inky, flowing, a secret river causing downpour on a lightless cave."
    n "A few rules still seem to apply, strange and bent as they are, like a backwards elbow."
    n "The cave, your gut tells, has a shape."
    n "Countours are imagined and projected: a limit on the dark, something to sustain and contain it."
    n "The deepest of azures fills you now. There's a top and a bottom, dissonance emerging."
    n "You wander upwards, buoyant despite never having drawn breath."
    n "The dark expells you, now differentiated. Lines drawn in the sand, turn to marble."
    n "And yet you know: a gnawing in the world, black maggots festering on the blanched pourous stone."
    n "There's something you're forgetting."
    aaa"NEGATIVE HALLUCINATION"
    nvl clear
    
    menu(nvl=True):
        aaa"~DEBUG MENU~"
        "ph_intro":
            jump ph_intro
        "TwiceShadowedIntro":
            jump TwiceShadowedIntro
        "ReflectionIntro":
            jump ReflectionIntro
        "ReflectionIntro":
            jump ReflectionIntro
        "ReflectionIntro":
            jump ReflectionIntro

label ReflectionIntro:

    e"Slowly, circumspect neural pathways activate. Your body comes to be."
    e"Being is pretty rough."
    e"You caught violently, your chest jumpstarting a tingling akin to burning."
    e"Your eyes open, searing wounds in your face."
    e"An enourmous blotch of azure fills your view, although not as dark as before."
    e"Catching its shape, you see sharp edges, a perfect prism reflecting potent sunlight."

    show eileen happy

    e"It sits silently. Or rather floats, above coarse and humid sand."
    return
