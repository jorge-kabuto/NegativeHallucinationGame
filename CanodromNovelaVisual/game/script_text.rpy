# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")
define tw = Character("The Twice-Shadowed")


# The game starts here.

label ActualGame:

    jump TwiceShadowedIntro
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dark_waters

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    e "Primordial blackness envelops you. Time itself is opaque to your senses."
    e "Provided that you still have those. Or that you ever possesed them to begin with."
    e "Reality is inky, flowing, a secret river causing downpour on a lightless cave."
    e "A few rules still seem to apply, strange and bent as they are, like a backwards elbow."
    e "The cave, your gut tells, has a shape."
    e "Countours are imagined and projected: a limit on the dark, something to sustain and contain it."
    e "The deepest of azures fills you now. There's a top and a bottom, dissonance emerging."
    e "You wander upwards, buoyant despite never having drawn breath."
    e "The dark expells you, now differentiated. Lines drawn in the sand, turn to marble."
    e "And yet you know: a gnawing in the world, black maggots festering on the blanched pourous stone."
    e "There's something you're forgetting."
    e "NEGATIVE HALLUCINATION"

    jump ReflectionIntro

label ReflectionIntro:

    e"Slowly, circunspect neural pathways activate. Your body comes to be."
    e"Being is pretty rough."
    e"You caught violently, your chest jumpstarting a tingling akin to burning."
    e"Your eyes open, searing wounds in your face."
    e"An enourmous blotch of azure fills your view, although not as dark as before."
    e"Catching its shape, you see sharp edges, a perfect prism reflecting potent sunlight."

    show eileen happy

    e"It sits silently. Or rather floats, above coarse and humid sand."
    return

label TwiceShadowedIntro:

    e"It's too late to turn back now. A feeling of doom creeps up your back, like a wounded cat."
    e"They approach, a mass of bound muscle in the shape of a headless Adonis."
    e"Neck to toes are dark red, the deep vermillion you would find on a budding wound."
    e"Their skin is unsullied, and yet you feel very wrong, as if those muscles cage an evil that would swallow you whole."

    tw"SPEAK THY NAME, NEW SHADOW."
    e"I don't have it yet."
    tw"TO VENTURE IN MY PRESENCE WITHOUT ONE IS A DIRE MISTAKE."
    tw"YOU HEED NOT TO THE WARNING OF MY SPIRIT, AND SURELY OF THE MEDDLING ROMBUS."
    tw"WHAT ARE YOUR INTENTIONTS? AMUSE ME, SHADOW."
    
    jump TwiceShadowedMenu

label TwiceShadowedMenu:
menu:
    "That's the second time you've called me shadow, why is that?":
        jump TwiceShadowedShadow
    "I seek to leave this dream, same as you. We can help each other.":
        jump TwiceShadowedPossession
    "I stumbled upon you by chance, release your influence so that I can leave!":
        jump TwiceShadowedBargain   

label TwiceShadowedShadow:
    return
label TwiceShadowedPossession:
    return
label TwiceShadowedBargain:
    return

menu:

    "As soon as she catches my eye, I decide..."

    "To ask her right away.":

        jump rightaway

    "To ask her later.":

        jump later

label rightaway:
