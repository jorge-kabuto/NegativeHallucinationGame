# The game starts here.
transform gradient:
    shader "example.gradient"
    u_gradient_right (0.0, 0.0, 1.0, 1.0)
    u_gradient_left (0.0, 0.0, 0.0, 1.0)

transform balatro:
    shader "balatro.test"
    pause 1.0/60
    repeat

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene dark_waters at balatro
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
    
    jump ReflectionIntro
    jump ph_intro
    jump TwiceShadowedIntro

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

label TwiceShadowedIntro:

    e"It's too late to turn back now. A feeling of doom creeps up your back, like a wounded cat."
    e"They approach, a mass of bound muscle in the shape of a headless Adonis."
    e"Neck to toes are dark red, the deep vermillion you would find on a budding wound."
    e"Their skin is unsullied, and yet you feel very wrong, as if those muscles cage an evil that would swallow you whole."

    tw"SPEAK THY NAME, NEW SHADOW."
    e"I don't have it yet."
    tw"TO VENTURE IN MY PRESENCE WITHOUT ONE IS A DIRE MISTAKE."
    tw"YOU HEED NOT TO THE WARNING OF MY SPIRIT, AND SURELY OF THE MEDDLING RHOMBUS."
    tw"WHAT ARE YOUR INTENTIONS? AMUSE ME, SHADOW."
    
    jump TwiceShadowedMenu

label TwiceShadowedMenu:
menu (nvl=True):
    aaa"\nI should tread carefully..."

    "That's the second time you've called me shadow, why is that?":
        jump TwiceShadowedPossession
    "I seek to leave this dream, same as you. We can help each other.":
        jump TwiceShadowedPossession
    "I stumbled upon you by chance, release your influence so that I can leave!":
        jump TwiceShadowedPossession   
    "Well, first of all, I wouldn't, uh, mind an introduction from you y'know?
    I don't want to seem rude, or anything like the like, so if you just heh,
    *hand over* your name this could be the start of a beautiful liaison. 
    Or just buddies. If y-you want, that is.":
        jump TwiceShadowedPossession   

label TwiceShadowedShadow:
    return
label TwiceShadowedPossession:
    tw "YOU SEEM TO BE KIDDING. HOW GLIB OF YOU, IGNORANT AS YOU ARE IN THIS REALM WHERE *I* HAVE STOOD FOR AEONS."
    tw "I AM NOT NOT BE KIDDEN WITH, PUNY SHADOW. I SHALL... TEACH YOU A LESSON, IF NOTHING ELSE, DUE TO MY PREDISPOSITION."
    aaa "You feel a pressure rising. A kind of pounding in your vicinity."
    aaa "It's your heart. It accelerates, rising in tone like a metronome, and then a buzz, and finally a crackling until you can't seem to hear it anymore."
    whirlwind "Something feels wrong..." (func=e)
    whirlwind "THE SOUND OF THE GION SHOJA BELLS ECHOES THE IMPERMANENCE OF ALL THINGS. 
    THE COLOR OF THE SALA FLOWERS REVEALS THE TRUTH THAT THE PROSPEROUS MUST DECLINE. 
    HOWEVER, ONLY WE ARE THE EXCEPTION." (func=tw)
    whirlwind "Please.... just stop." (func=e)
    return
label TwiceShadowedBargain:
    return
