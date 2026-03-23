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
    tw"YOU HEED NOT TO THE WARNING OF MY SPIRIT, AND SURELY OF THE ONE UTTERED BY THE MEDDLING RHOMBUS."
    tw"WHAT ARE YOUR INTENTIONS? AMUSE ME, SHADOW."

label tw_01_menu:

default tw_01_reflection = False
default tw_02_lesson = False
menu (nvl=True):
    "That's the second time you've called me shadow, why is that?":
        tw "YOUR QUESTION LACKS MEANING, AND THUSLY EXPRESSES BARELY CONTAINED IGNORANCE. 
        YOU ARE A SHADOW BECAUSE I SAY YOU ARE, AND ONLY IN YOUR ACCEPTANCE OF THE MONIKER WILL YOU TURN TO BE ONE."
        tw "YOU HAVE MET THE BEACH-STALKER, YES? FOR THEM, YOU ARE BUT A PUZZLEBOX. 
        A RIDDLE SURFACING IN THE OPALESCENT SAND, NOT UNLIKE A RICH OYSTER TO TASTE ONCE AND *TOSS* ASIDE. (They gesticulate, and their hand falls)"
        tw "(They mantain their outstretched posture, for a couple of seconds. To your eyes, it reads like an omen.)"
        $ tw_01_reflection = True
        jump tw_01_menu
    "What do you know about The Reflection?" if tw_01_reflection==True:
        tw "WHAT IS TO KNOW OF SOMEONE THAT HAS RECEDED INWARDS SO FAR? 
        *THE REFLECTION* IS A SHELL, A TWISTED OBSESSION MANIFESTED AND GIVEN FORM."
        tw "ROT TOOK HOLD OF THEIR RIGHTEOUS INTELLECT BY COUNTING ENDLESS PIECES OF WROUGHT IRON, THE DISCERNING PARSING OF A MYRIAD MIRAGES."
        tw "(Their voice is thunderous, a rising tide. It seems to darken the sky.)"
        tw "A LIFE RUINED. BEYOND HELP. IF ONLY THIS WORLD WOULD PERMIT IT, I WOULD GIVE THEM AN END MYSELF."
        menu (nvl=True):
            "Is there really nothing to be done?":
                tw "PITY IS FOR THOSE DESERVANT OF IT, SHADE."
                tw "THEIR WAY IS ONE OF COWARDICE, A SELF INFLICTED WOUND."
                tw "THEY WERE SIMPLY NOT."
                tw "STRONG."
                tw "ENOUGH."
                tw "(every word winds up and falls like a forging hammer.)"
                jump tw_01_menu
            "I don't think it's as bad as you say. They seem to be doing *mostly* fine.":
                tw "YES . . . OF COURSE YOU WOULD SAY THAT."
                tw "MY PATIENCE IS RUNNING ITS COURSE. I LACK WORDS TO EXPRESS MY LOATHING TOWARDS BOTH YOU AND THE INHUMAN FLOATER."
                e "But why is that? Is there a reason for so much hate?"
                tw ". . . HOPELESS. . . (Their voice is now sibilant, a hoarse whisper)"
                tw "YOU'RE BECOMING JUST LIKE THEM. AS SOON AS YOU REALIZE THE NATURE OF THIS PLACE, THE DICE WILL BE THROWN."
                e "What does that mean?"
                tw "...(They stay silent.)"
                jump tw_01_menu
            "Yes, I would like to give an end to the poor sucker myself.":
                tw "HAH. (Their laugh is a contorted sound, short and not unlike a bark.)"
                tw "I CAN'T REMEMBER THE LAST SHADOW WITH A THIRST FOR BLOOD. DO YOU REALLY MEAN THIS OR IS IT A SIMPLETON'S TRY AT MANIPULATION?"
                tw "ONLY TIME WILL TELL. (In the space between encroaching shoulderblades, where the face should be, you swear you can *see* a grin.)"
                jump tw_01_menu
    "I seek to leave this dream, same as you. We can help each other.":
        tw "AH, I SEE. SO THEY REALLY DID REVEAL IT TO YOU."
        tw "I *WOULD* PUT YOU TO GOOD USE, IF THAT'S WHAT YOU SEEK. THE FRUITS OF THIS ARRANGEMENT WOULD INDEED BE FOR BOTH, IN ALMOST EQUAL MEASURE."
        tw "SO? WHAT SAY YOU, SPECTER?"
        jump tw_02_bargain
    "I stumbled upon you by chance, release your influence so that I can leave!":
        jump DEBUG_MENU # jump tw_02_leave_early   
    "Well, first of all, I wouldn't, uh, mind an introduction from you y'know?
    I don't want to seem rude, or anything like the like, so if you just heh,
    *hand over* your name this could be the start of a beautiful liaison. 
    Or just buddies. If y-you want, that is." if tw_02_lesson==False:
        jump tw_02_lesson

label tw_02_lesson:
    tw "YOU SEEM TO BE KIDDING. HOW GLIB OF YOU, IGNORANT AS YOU ARE IN THIS REALM WHERE *I* HAVE STOOD FOR AEONS."
    tw "I AM NOT NOT BE KIDDEN WITH, PUNY SHADOW. I SHALL... TEACH YOU A LESSON, IF NOTHING ELSE, DUE TO MY PREDISPOSITION."
    aaa "You feel a pressure rising. A kind of pounding in your vicinity."
    aaa "It's your heart. It accelerates, rising in tone like a metronome, and then a buzz, and finally a crackling until you can't seem to hear it anymore."
    whirlwind "Something feels wrong..." (func=e)
    whirlwind "WHOEVER LONGS FOR PEACE, THEY SHALL PREPARE FOR WAR." (func=tw)
    whirlwind "NO ONE DARES TO PROVOKE, NO ONE DARES TO OPPOSE, THOSE THAT BELIEVE THEMSELVES TO BE SUPERIOR IN THE FIGHT." (func=tw)
    whirlwind "SUCH IS THE TRUTH OF WHICH ONLY WE ARE THE EXCEPTION." (func=tw)
    whirlwind "Please.... just stop." (func=e)
    whirlwind "I can't bear it anymore..." (func=e)
    aaa "Time begins to unwind, but you truly couldn't. You collapse to the floor, and the darkened world goes out like a lamp."
    $ tw_02_lesson = True
    jump DEBUG_MENU  

default tw_02_bargain = False
label tw_02_bargain:
    menu (nvl=True):
        "Can you go into a little bit more detail into this *arrangement* of yours?":
            tw "IT IS SIMPLE. I AM MISSING SOMETHING, AND YOU CAN PROVIDE IT FOR ME. TOGETHER, WE WILL BE... UNSTOPPABLE."
            tw "I KNOW HOW IT WILL END FOR YOU IF YOU DON'T TAKE MY OFFER, SHADOW. YOU'RE JUST LIKE THE REST."
            tw "I AM YOUR ONLY WAY OUT."
            $ tw_02_bargain=True
            jump tw_02_bargain
        "What will happen to me?" if tw_02_bargain==True:
            tw "AH, SO THE ALL-KNOWING MIRROR, SAVANT BEYOND MEASURE, HAPPENED TO SKIP OVER THAT PART."
            tw "THEY, AND I, ARE THE LAST INHABITANTS OF THIS BLASTED DREAM. SHOULD YOU ASK THEM WHY, YOU WILL COME BACK..."
            tw "BEGGING FOR AN OUT."
            e "So you don't have any intention of telling me?"
            e "What, is The Reflection the official dispenser of knowledge around here?"
            tw "I UNDERSTAND HOW YOU PERCIEVE ME, I HAVE SEEN EYES LIKE THOSE MANY A TIMES BEFORE."
            tw "IN MY MIND, YOU WOULD HOLD ME A LIAR, AN UNSUBTLE SCHEMER. SO, SEE FOR YOURSELF."
            tw "YOU HAVE ALL THE TIME IN THE WORLD."
            jump tw_02_bargain
        "I actually have to carry out some expert consultations beforehand.":
            tw "AH... OF COURSE. GO AND EXPLAIN THIS TO ALL YOUR 'EXPERTS' WHEREVER THEY MAY BE."
            tw "I WILL BE *AROUND*. IN TIME, WE SHALL MEET AGAIN."
            jump DEBUG_MENU
        "I will do whatever needs to be done to get out.":
            jump DEBUG_MENU

    jump DEBUG_MENU