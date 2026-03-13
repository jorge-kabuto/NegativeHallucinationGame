label TwiceShadowedIntro:
    default tw_bg = ReactionDiffusion(blur1=10.0,blur2=20.0, image_path="images/twiceshadowed_pf_chroma.png")
    scene black
    show expression tw_bg
    # show twiceshadowed_pf_chroma at portrait

    e"It's too late to turn back now. A feeling of doom creeps up your back, like a wound cat."
    e"They approach, a mass of bound muscle in the shape of a headless Adonis."
    e"Neck to toes are dark red, the deep vermillion you would find on a budding wound."
    e"Their skin is unsullied, and yet you feel very wrong, as if those muscles cage an evil that would swallow you whole."

    tw"SPEAK THY NAME, NEW SHADOW."
    e"I don't have it yet."
    tw"TO VENTURE IN MY PRESENCE WITHOUT ONE IS A DIRE MISTAKE."
    tw"YOU HEED NOT TO THE WARNING OF MY SPIRIT, AND SURELY OF THE MEDDLING RHOMBUS."
    tw"WHAT ARE YOUR INTENTIONS? AMUSE ME, SHADOW."

label tw_01_menu:
menu (nvl=True):
    "That's the second time you've called me shadow, why is that?":
        jump tw_01_menu
    "I seek to leave this dream, same as you. We can help each other.":
        jump tw_02_bargain
    "I stumbled upon you by chance, release your influence so that I can leave!":
        jump tw_02_leave_early   
    "Well, first of all, I wouldn't, uh, mind an introduction from you y'know?
    I don't want to seem rude, or anything like the like, so if you just heh,
    *hand over* your name this could be the start of a beautiful liaison. 
    Or just buddies. If y-you want, that is.":
        jump tw_02_lesson   
label TwiceShadowedShadow:
    return
label tw_02_lesson:
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