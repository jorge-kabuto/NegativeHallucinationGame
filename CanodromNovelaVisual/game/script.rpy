# The game starts here.

label start:

    $ lookedaround = False # This is an example flag. It will come in handy later
                           # in this script.

    $ health = 5 # Health bar amounts the player starts off with.
                 # Feel free to change the number.
    $ morale = 5 # Remember that in Disco Elysium, Endurance and Volition govern
                 # a player's amount of health and morale, respectively.
    $ healthmax = 5 # Max amount of health. You can change this number here or later
                    # in the story if you want to script a level up.
    $ moralemax = 5 # Max amount of morale.

    # Define different Modifiers to zero until they are unlocked by the player:
    $ modifier1 = 0
    #$ modifier2 = 0 # Unhide if you need more modifiers.
    #$ modifier3 = 0

    # Add music here:
    #play music funny_theme fadeout 1.0 fadein 1.0 # Example. Unhide and use your
                                                   # own music here.

    # Show a background here. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene "images\background.png"

    show black # places a black screen over the scene
    with fade # The fade (must be on a new line) lets you fade to black from the
              # main menu

    window show #This displayed the textbox

    #show kim happy #This shows a character sprite. A placeholder is used, but
    # you can replace it by adding a file named "kim happy.png" to the images
    # directory in declare.rpy under CHARACTERS.

# Skills, sound effects, and voice acting tutorial:

    play sound sfx_int # This plays a sound effect.
                       # See: declare.rpy to replace the audio file.
    "{color=[intel]}LOGIC{/color} — I know about cause and effect."

    play sound sfx_psy
    "{color=[psy]}VOLITION{/color} — I keep your humanity."

    play sound sfx_fys
    "{color=[fys]}ELECTROCHEMISTRY{/color} — I keep things *fun*."

    play sound sfx_mot
    "{color=[mot]}PERCEPTION (SIGHT){/color} — I take in the light around you."

    "{color=[youtext]}YOU — I'm not Harry.{/color}"

    #voice "audio/tt-001.ogg" # This lets you add a voice acting line.
    # Change the file directory to your voiced lines accordingly.
    # Hot tips: 1) .ogg files shrink audio file sizes. 2) Make a spreadsheet for
    # voiced lines so you know their file name.
    "{color=[npc]}PLACE{/color} — I'm not Harry either."

    #voice "audio/tt-002.ogg" # Another voiced line example.
    "{color=[npc]}ANCIENT REPTILIAN BRAIN{/color} — There is nothing."

    # You can also change the SFX for the sound played when pressing buttons in
    # declare.rpy at the "define click" line under "SOUND EFFECTS".

# Basic text and choices tutorial:

    menu (nvl=True):
        #Add {p} to add a new paragraph in a block of text:
        "{color=[npc]}LIMBIC SYSTEM{/color} — There is a giant ball there. And evil
        apes. And the evil apes are dukin' it out on the ball. You're one of them.
        It's basically all just evil apes dukin' it out on a giant ball.
        {p}{p}You've created a new Ren'Py game."

        "{color=[textnorm]}1. -{/color} Uh-oh.":
            "{color=[youtext]}YOU — Uh-oh.{/color}{nw}"

            "TUTORIAL AGENT — Don't worry, you're fine. By the way, this text
            only appears if you selected choice 1."

        "{color=[textnorm]}2. -{/color} Whoops. This wasn't meant to happen. I
        don't know what came over me.":
            "{color=[youtext]}YOU — Whoops. This wasn't meant to happen. I don't
            know what came over me.{/color}{nw}"

            "TUTORIAL AGENT — It's okay, it happens. This text only appears if
            you selected choice 2."

    "TUTORIAL AGENT — Once you add a story, pictures, and music, you can release
    it to the world!"

    "TUTORIAL AGENT — Hi. Thank you for trying out the Disco Framework. Check
    out the script.rpy file for #hashtags. I've tried to write helpful labels
    and notes on what things do."

    "TUTORIAL AGENT — If you find the text going off the screen, go to the
    gui.rpy file, scroll down to the \"NVL-Mode\" header (on line 364), and
    change the maximum number of NVL-mode entries Ren'Py will display. It is
    this line, {color=[youtext]}define gui.nvl_list_length = x{/color}"

    nvl clear

    "TUTORIAL AGENT — You can also use the line {color=[youtext]}nvl clear{/color}
    to clear the text on the screen, like this."

# More text info tutorial:

    "HARRY — \"If you want to include quotation marks in your text, like for
    character dialogue, you'll need to place a backslash in front
    of it. This is an example.\" Harry shuffles his feet."

    menu (nvl=True):
        "TUTORIAL AGENT — To have new text appear when a choice appears, place
        it below the {color=[youtext]}menu (nvl=True):{/color} line, followed by
        the choices, which should end with a {color=[youtext]}:{/color} at the
        end of it."

        "{color=[textnorm]}1. -{/color} (Walk to the bathroom.)":
            "{color=[youtext]}YOU — (Walk to the bathroom.){/color}{nw}"
            # {nw} automatically displays the next (below) line of text to the
            # player without them clicking.
            # Always place {nw} after a line by YOU happens.

    "TUTORIAL AGENT — {color=[youtext]}nw{/color} in square brackets automatically
    displays the next (below) line of text to the player without them clicking.
    Place \"{{nw}\" after a line by YOU happens."

# Character portraits and Alternate sfx tutorial:

    # The "a" before the dialogue below tells Ren'Py to display a character portrait.
    # The "drop" tells Ren'Py to add the image that I defined as "drop" in the
    # declare.rpy file. Please open that file to add your own character portraits.
    a drop "TUTORIAL AGENT — You can also add character portraits. Here is a
    placeholder image I made. If you look at this line in the script, you can
    see how I did this."

    a moon "TUTORIAL AGENT — And change it." # Gives you the "moon" defined character
                                             # portrait.

    "TUTORIAL AGENT — Or not include one." # To not include a portrait, leave it
                                           # blank like this.

    "TUTORIAL AGENT — You can change the position of the character portrait in
    {color=[youtext]}screens.rpy{/color} at line 1369."

    play sound sfx_fys
    a physique"{color=[fys]}ELECTROCHEMISTRY{/color} — This framework includes
    portrait fanart of the four attributes. The artist has given premission for
    you to use them for your fangame."

    play sound sfx_psy
    a psyche"{color=[psy]}VOLITION{/color} — Keep in mind that they are based on
    the skill portraits from Disco Elysium, which is owned by ZA/UM."

    play sound sfx_int
    a intellect"{color=[intel]}CONCEPTUALIZATION{/color} — If you want more
    different-looking portraits, you could use royalty free images and edit
    them. Or draw them. That way, they'll look *just* how you picture them. They
    will be *unique* to your game."

    play sound sfx_mot
    a motorics"{color=[mot]}SAVOIR FAIRE{/color} — Or hire an artist."

    play sound "audio/sfx_by_katy/sfx_physique.mp3"
    a physique"{color=[fys]}ELECTROCHEMISTRY{/color} — There are also alternate
    sound effects for the four attributes. Here is one for physique."

    play sound "audio/sfx_by_katy/sfx_psyche.mp3"
    a psyche"{color=[psy]}VOLITION{/color} — And psyche."

    play sound "audio/sfx_by_katy/sfx_intellect.mp3"
    a intellect"{color=[intel]}CONCEPTUALIZATION{/color} — For intellect."

    play sound "audio/sfx_by_katy/sfx_motorics.mp3"
    a motorics"{color=[mot]}SAVOIR FAIRE{/color} — And for motorics."

# Backgrounds tutorial:

    "TUTORIAL AGENT — You can hide images to reveal backgrounds underneath using
    the {color=[youtext]}hide{/color} command."

    scene image "images/bg_bathroom.png" # An example of how you would add an image
                                      # named "bg_bathroom.png" from the "game/images"
                                      # folder into this game.
    with dissolve #the transition you want to use
    # If you plan on using a background repeatedly, you can define the image with
    # a name in declare.rpy (like I did under "BACKGROUNDS" in declare.rpy).
    # Then you can just use the name you've assigned to it, like below:
    #scene bathroom

    "TUTORIAL AGENT — And you can use the scene command to add a new background.
    The difference between {color=[youtext]}scene{/color} and {color=[youtext]}show{/color}
    is that scene adds a new background to replace the currently shown images.
    And {color=[youtext]}show{/color} instead places a image overtop what images
    are already there."

    play sound sfx_int
    "{color=[intel]}CONCEPTUALIZATION{/color} {color=[check]}[[Easy: Success]{/color}
    — The artist appears to have rendered the bathroom in such a way as to
    encourage other artists to draw something else in its place."

# Character sprites tutorial:

    nvl clear

    show image "images/character_ref.png":
        pos (400, 107) # Position of the character on relation to the top-left of the screen.

    "TUTORIAL AGENT — Here is an example character. You can replace this image
    with something else."

# Wait/Hold on/Proceed text tutorial:

    nvl clear

    "TUTORIAL AGENT — Now let's have an example of a choice where one option lets
    you gather more info before proceeding. In *Disco Elysium*, usually these \"more
    info\" questions begin with \"Wait\" or \"Hold on\" in the text choice."

    menu (nvl=True):
        "TUTORIAL AGENT — Here it is. Can you see it in the script?"

        "{color=[textnorm]}1. -{/color} Wait, who are you?":

            "{color=[youtext]}YOU — Wait, who are you?{/color}{nw}"

            menu (nvl=True):
                "TUTORIAL AGENT — I'm here to help. My name is Katy. I wrote this."

                "{color=[textnorm]}1. -{/color} Let's go. (Proceed.)":

                    jump questionme # Takes you back to the choice with the same
                                    # label name.

        "{color=[textnorm]}2. -{/color} Let's go. (Proceed.)":

            label questionme:

                "{color=[youtext]}YOU — Let's go. (Proceed.){/color}{nw}"

                "TUTORIAL AGENT — Cool."

# Unlocking routes tutorial:

    "TUTORIAL AGENT — Now some more advanced stuff. Next, we'll learn about how
    to program unlockable routes that require the player to do certain actions
    before they can see them."

    label whatdo:

        nvl clear

        menu (nvl=True):
            "TUTORIAL AGENT — I've made up a scenario where you'll unlock progression
            in the game only after examining a phone. Doing anything else beforehand
            leads you back here, which you can test out."

            "{color=[textnorm]}1. -{/color} (Examine phone.)":

                if lookedaround is True:

                    play sound sfx_mot
                    "{color=[mot]}REACTION SPEED{/color} — You *already* looked at this!"

                    jump whatdo

                else:

                    "{color=[youtext]}YOU — (Examine phone.){/color}{nw}"

                    play sound sfx_mot
                    "{color=[mot]}PERCEPTION (SIGHT){/color} — It's a phone, Mullen."

                    $ lookedaround = True

                    "TUTORIAL AGENT — You've now set a flag switch named {color=[youtext]}\"lookedaround\"{/color}
                    to True. Wayyy back on {color=[youtext]}line 5{/color}, it
                    was set to {color=[youtext]}False{/color}. This means that we
                    should be able to progress in the game further."

                    jump whatdo

            "{color=[textnorm]}2. -{/color} (Call the RCM.)":

                "{color=[youtext]}YOU — (Call the RCM.){/color}{nw}"

                "TUTORIAL AGENT — No, let's not."

                jump whatdo

            "{color=[textnorm]}3. -{/color} (Proceed.)":

                "{color=[youtext]}YOU — (Proceed.){/color}{nw}"

                # If you haven't picked the other options:
                if lookedaround is False:
                    "TUTORIAL AGENT — We can't proceed yet. You need to examine
                    the phone."

                    jump whatdo

                else:
                    "TUTORIAL AGENT — Yay, we can proceed now because you examined
                    the phone earlier!"

# Passive rolls tutorial:

    nvl clear

    "TUTORIAL AGENT — Next, we'll talk about passive rolls. Those moments where
    your skills will chime in to say something."

    # \n creates a new paragraph. Using """ lets you contain several paragraphes
    # of test into one dialgoue chunk.
    """TUTORIAL AGENT — The values in Disco Elysium are roughly:
    \nTrivial: 6
    \nEasy: 8
    \nMedium: 10
    \nChallenging: 12
    \nFormidable: 13
    \nLegendary: 14
    \nHeroic: 15
    \nGodly: 16
    \nImpossible: 18"""

    "TUTORIAL AGENT — If you want to make a more linear game, you can just make
    a passive check as a visual thing. Something that doesn't do any math."

    play sound sfx_psy
    "{color=[psy]}VOLITION{/color} {color=[check]}[[Impossible: Success]{/color}
    — Like this."

    nvl clear

    "TUTORIAL AGENT — But we can also make passive checks that *do* do math.
    Let's add given you character stats, since you'll need them to do that."

    menu (nvl=True):
        "TUTORIAL AGENT — Select archetype."

        "{color=[textnorm]}1. -{/color} Thinker. | 5 INT | 2 PSY | 1 FYS | 4 MOT":
            "{color=[youtext]}YOU — Thinker. | 5 INT | 2 PSY | 1 FYS | 4 MOT{/color}{nw}"

            $ intellect = 5 # These set your abilities. # intellect has to be
                               # called "intellect" instead of "int" because we
                               # are already defining text colours using that name.
            $ psyche = 2
            $ physique = 1
            $ motorics = 4

        "{color=[textnorm]}2. -{/color} Sensitive. | 1 INT | 5 PSY | 4 FYS | 2 MOT":
            "{color=[youtext]}YOU — Sensitive. | 1 INT | 5 PSY | 4 FYS | 2 MOT{/color}{nw}"

            $ intellect = 1
            $ psyche = 5
            $ physique = 4
            $ motorics = 2

        "{color=[textnorm]}3. -{/color} Physical. | 1 INT | 2 PSY | 5 FYS | 4 MOT":
            "{color=[youtext]}YOU — Physical. | 1 INT | 2 PSY | 5 FYS | 4 MOT{/color}{nw}"

            $ intellect = 1
            $ psyche = 2
            $ physique = 5
            $ motorics = 4

        "{color=[textnorm]}4. -{/color} Average. | 3 INT | 3 PSY | 3 FYS | 3 MOT":
            "{color=[youtext]}YOU — Average. | 3 INT | 3 PSY | 3 FYS | 3 MOT{/color}{nw}"

            $ intellect = 3
            $ psyche = 3
            $ physique = 3
            $ motorics = 3

    "TUTORIAL AGENT — Great. Now I'll set your 24 skills' stats using this
    choice. I'll basically make each skills the same number as their
    corresponding attribute."

    # Defines the 24 skills:
    $ logic = intellect # "Logic is equal to the player's current Intellect."
    $ encyclopedia = intellect
    $ rhetoric = intellect
    $ drama = intellect
    $ conceptualization = intellect
    $ visual_calculus = intellect

    $ volition = psyche
    $ inland_empire = psyche
    $ empathy = psyche
    $ authority = psyche
    $ esprit_de_corps = psyche # If your character isn't a cop, this skill can be
                               # replaced with whatever their occupation/vocation is.
    $ suggestion = psyche

    $ endurance = physique
    $ pain_threshold = physique
    $ physical_instrument = physique
    $ electrochemistry = physique
    $ shivers = physique
    $ half_light = physique

    $ hand_eye_coordination = motorics
    $ perception = motorics
    $ reaction_speed = motorics
    $ savoir_faire = motorics
    $ interfacing = motorics
    $ composure = motorics

    "TUTORIAL AGENT — According to esoteric sources, passive checks are calculated
    by taking your skill's stat number, adding 7 to it (the median value of 2d6),
    and then checking to see if it is a number *the same as* or *higher than* the
    difficulty of the roll."

    "TUTORIAL AGENT — For example, someone who has 5 Logic will get a score of 12
    for passive skill-checks (5+7=12). They can succeed passive checks that are
    Challenging or lower in difficulty."

    "TUTORIAL AGENT — Remember that you can also program passive checks for
    *failing* rolls. These can be very funny."

    "TUTORIAL AGENT — We will now play out some passive checks."

    if logic+7 >9: # "If Logic+7 is greater than 9." Making the last number
                     # larger (or smaller) makes it harder (or easier) to succeed
                     # a roll. This is a Medium difficulty roll.
        play sound sfx_int
        "{color=[intel]}LOGIC{/color} {color=[check]}[[Medium: Success]{/color}
        — Yay. You succeeded a passive check and got this missable text."
    else:
        pass

    "TUTORIAL AGENT — If Logic didn't just appear, then you failed the passive
    check."

    "TUTORIAL AGENT — Let's do some more rolls."

    if volition+7 >5: # "If Volition+7 is greater than 5."
        play sound sfx_psy
        "{color=[psy]}VOLITION{/color} {color=[check]}[[Trivial: Success]{/color}
        — Welp. Looks like I get to say something here."
    else:
        play sound sfx_psy
        "{color=[psy]}VOLITION{/color} {color=[check]}[[Trivial: Failure]{/color}
        — Um. You failed the roll."

    if electrochemistry+7 >11: # "If greater than 11."
        play sound sfx_fys
        "{color=[fys]}ELECTROCHEMISTRY{/color} {color=[check]}[[Challenging: Success]{/color}
        — Yeah, you're got this!"
    else:
        play sound sfx_fys
        "{color=[fys]}ELECTROCHEMISTRY{/color} {color=[check]}[[Challenging: Failure]{/color}
        — Whoops!"

    if perception+7 >17: # "If perception+7 is greater than 17."
        play sound sfx_mot
        "{color=[mot]}PERCEPTION (SIGHT){/color} {color=[check]}[[Impossible: Success]{/color}
        — Welp. Looks like I get to say something here."
    else:
        play sound sfx_mot
        "{color=[mot]}PERCEPTION (SIGHT){/color} {color=[check]}[[Impossible: Failure]{/color}
        — UM."

    "TUTORIAL AGENT — It was literally *impossible* for the player to succeed
    that last Perception roll. The most a player can have in any stat right now
    is 12 (5+7). They can't reach 18 here. Keep that in mind when scripting rolls."

    "TUTORIAL AGENT — Okay, that's enough. Let's move on."

# Success/Fail rolls tutorial:

    nvl clear

    menu (nvl=True):
        "TUTORIAL AGENT — You can also create big success and fail rolls. I can
        show you these. However, they include a flashing light, similar to rolls
        in Disco Elysium. Do you want to see these?"

        "{color=[textnorm]}1. -{/color} Yes, I'm okay with a flashing image.":
            "{color=[youtext]}YOU — Yes, I'm okay with a flashing image.{/color}{nw}"

        "{color=[textnorm]}2. -{/color} No, let's skip seeing these. (Skip Fail/Success
        Rolls Tutorial.)":
            "{color=[youtext]}YOU — No, let's skip seeing these. (Skip Fail/Success
            Rolls Tutorial.){/color}{nw}"

            "TUTORIAL AGENT — Okay, we'll skip this bit."

            jump skipflashes

    "TUTORIAL AGENT — Okay, here we go."

    play sound dice_rolling
    show dicebg at dicespin
    pause 1.3
    play sound dice_result
    hide dicebg
    show white:
        alpha 0.5
    pause 0.1
    show success_roll
    hide white
    with dissolve
    hide success_roll with dissolve

    play sound sfx_int
    "{color=[intel]}LOGIC{/color} {color=[check]}[[Trivial: Success]{/color} — A
    successful roll!"

    "TUTORIAL AGENT — Next is a failed roll. There will be another flash."

    play sound dice_rolling
    show dicebg at dicespin
    pause 1.3
    play sound dice_result
    hide dicebg
    show white:
        alpha 0.5
    pause 0.1
    show success_roll:
        matrixcolor HueMatrix(-120) # This takes the green success roll image
                                    # and changes the hue to orange.
        # Alternatively, you can make your own custom image for fail rolls, name
        # it "fail_roll.png" and define it in declare.rpy. Just remove the hashtag
        # at the beginning of "image fail_roll" in declare.rpy
    hide white
    with dissolve
    hide success_roll with dissolve

    play sound sfx_int
    "{color=[intel]}LOGIC{/color} {color=[check]}[[Impossible: Failure]{/color}
    — A failed roll."

    "TUTORIAL AGENT — You can script these so that they just happen no matter
    what, or you can add an actual die roll. Let's learn how to do that."

    "TUTORIAL AGENT — In Disco Elysium, you roll 2d6 (2 6-sided dice), then add
    your skill value and corresponding stat value. If the result is equal or
    higher than the difficulty level, you succeeded."

    "TUTORIAL AGENT — So if, say, you want to succeed a medium roll, you'll want
    to tell the engine, \"If I get a number greater than (>) 9, *this* happens\".
    Because a Medium roll is 10."

    play sound sfx_int
    "{color=[intel]}VISUAL CALCULUS{/color} — In other words: Always go one
    number lower than the roll's value."

    nvl clear

    # You can find a cheat sheet to skill checks for quick reference in cheat_sheet.rpy

    "TUTORIAL AGENT — Unlike the standard Python random number generator, this
    object cooperates with rollback, generating the same numbers regardless of
    how many times we press the back button."

    play sound sfx_psy
    "{color=[psy]}VOLITION{/color} — In other words, it's hard for players to
    cheat."

    play sound sfx_mot
    "{color=[mot]}PERCEPTION (SIGHT){/color} — This method also means that
    there's no critical success (rolling 2 sixes) or fail (rolling snake eyes)
    rolls."

    menu (nvl=True):
        "TUTORIAL AGENT — Here's how you do it. Another flash."

        "{color=[textnorm]}1. -{/color} [[Endurance - Medium 10] Disco. Let's try
        it out.":
            "{color=[youtext]}YOU — Disco. Let's try it out.{/color}{nw}"

            # Return a random integer between 2 and 12. We use a 2 as the lowest
            # number because the lowest you can roll with a 2d6 is "snake eyes" (2).

            $ roll2d6 = renpy.random.randint(2, 12) # Rolling die...

            if roll2d6+endurance+physique >9: # "If the roll+endurance+physique
                                              # is greater than 9." Making the number
                                              # larger (or smaller) makes it harder
                                              # (or easier) to succeed a roll.
                play sound dice_rolling
                show dicebg at dicespin
                pause 1.3
                play sound dice_result
                #hide dicebg # Don't need to hide the dice if you show a result.
                show white:
                    alpha 0.5
                pause 0.1
                show screen notice(_("CHECK SUCCESS"), ())
                show success_roll behind dicebg # Keeps dice art as the top layer.
                show dicebg # This shows us the dice.
                show screen text_dicenumber() # This shows us the dice number.
                hide white
                with dissolve
                hide success_roll with dissolve
                pause 0.1
                hide dicebg
                hide screen text_dicenumber
                hide screen notice
                with dissolve

                play sound sfx_fys
                "{color=[fys]}ENDURANCE{/color} {color=[check]}[[Medium: Success]{/color}
                — You succeeded the check with a roll of [roll2d6], plus
                [endurance] Endurance."
            else:
                play sound dice_rolling
                show dicebg at dicespin
                pause 1.3
                play sound dice_result
                #hide dicebg # Don't need to hide the dice if you show a result.
                show white:
                    alpha 0.5
                pause 0.1
                show screen notice(_("CHECK FAILURE"), ())
                show success_roll behind dicebg: # Keeps dice art as the top layer.
                    matrixcolor HueMatrix(-120) # Changes the hue to orange.
                show dicebg
                show screen text_dicenumber()
                hide white
                with dissolve
                hide success_roll with dissolve
                pause 0.1
                hide dicebg
                hide screen text_dicenumber
                hide screen notice
                with dissolve

                play sound sfx_fys
                "{color=[fys]}ENDURANCE{/color} {color=[check]}[[Medium: Failure]{/color}
                — You failed the roll with a roll of [roll2d6], plus
                [endurance] Endurance."

    "TUTORIAL AGENT — The images folder also contains png images of a 6 sided
    die if you need it..."

# Roll Modifiers tutorial:

    nvl clear

    "TUTORIAL AGENT — You can also add {color=[youtext]}modifiers{/color} that
    the player can hover over to read."

    $ modifier1 = 1 # Modifier: Plus 2, minus 1, equals 1.
    "TUTORIAL AGENT — As an example, I'm going to say... you're feeling nervous
    and excited. That's what you've unlocked as a roll modifier."

    menu (nvl=True):
        "TUTORIAL AGENT — You should be able to read the modifiers as a popup by
        mousing over the number, or clicking it."

        #"[[1]" brings up a modifier
        "{color=[textnorm]}1. -{/color} [[COMPOSURE - Medium 10 [[1]] Disco.
        Let's try it out.":
            "{color=[youtext]}YOU — Disco. Let's try it out.{/color}{nw}"

            $ roll2d6 = renpy.random.randint(2, 12) #Rolling die...

            $ roll2d6 += modifier1 # Add "modifier1"'s numbers, which is -1 and +2,
                                   # which equals 1.

            if roll2d6+composure+motorics >9: # "If the roll+composure+motorics
                                              # is greater than 9."
                play sound dice_rolling
                show dicebg at dicespin
                pause 1.3
                play sound dice_result
                #hide dicebg
                show white:
                    alpha 0.5
                pause 0.1
                show screen notice(_("CHECK SUCCESS"), ())
                show success_roll behind dicebg
                show dicebg
                show screen text_dicenumber()
                hide white
                with dissolve
                hide success_roll with dissolve
                pause 0.1
                hide dicebg
                hide screen text_dicenumber
                hide screen notice
                with dissolve

                play sound sfx_mot
                "{color=[mot]}COMPOSURE{/color} {color=[check]}[[Medium: Success]{/color}
                — You succeeded the roll with a [roll2d6], plus [composure] Composure."
            else:
                play sound dice_rolling
                show dicebg at dicespin
                pause 1.3
                play sound dice_result
                #hide dicebg
                show white:
                    alpha 0.5
                pause 0.1
                show screen notice(_("CHECK FAILURE"), ())
                show success_roll behind dicebg:
                    matrixcolor HueMatrix(-120) # Changes the hue to orange.
                show dicebg
                show screen text_dicenumber()
                hide white
                with dissolve
                hide success_roll with dissolve
                pause 0.1
                hide dicebg
                hide screen text_dicenumber
                hide screen notice
                with dissolve

                play sound sfx_mot
                "{color=[mot]}COMPOSURE{/color} {color=[check]}[[Medium: Failure]{/color}
                — You failed the roll with a [roll2d6], plus [composure] Composure."

    "TUTORIAL AGENT — You can edit modifiers in the {color=[youtext]}lexicon.rpy{/color}
    file."

    "TUTORIAL AGENT — Moving on..."

label skipflashes: # A "label" is where a "jump" can bounce go.
    pass # "pass" allows you to leave something blank.

# Health/morale damage and partner portrait tutorial:

    nvl clear

    $ has_partner = False # Define whether or not players can see your partner's
                          # character portait before showing the vitality_screen,
                          # otherwise you'll get an error.

    show screen vitality_screen # Makes the health bars appear. Add this line to
                                # the start of the game if you always want it there.

    "TUTORIAL AGENT — Here is the health screen."

    $ has_partner = True # Shows your partner's character portrait.

    "TUTORIAL AGENT — You can also have a character portrait for your partner, if
    you're lucky enough to *have* one in solving crimes."

    "TUTORIAL AGENT — You can customise the character portraits in
    {color=[youtext]}vitality.rpy{/color}."

    $ health -= 1 # removes 1 health point. Remove this if you just want the
                  # effect to be visual.

    show expression AlphaMask("images/red_gradient.png", At("images/character_ref.png", pulse_anim)) as mask with dissolve:
        pos (400, 107) # Use same position as the character sprite.

    #TODO: play sound health_damage
    show effects:
        alpha 0.3
    show notification_damage_health
    show screen notice(_("DAMAGED HEALTH"), _("-1"))
    with dissolve
    pause 1.5
    hide mask
    hide effects
    hide notification_damage_health
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Here is an example of the character taking health damage."

    "TUTORIAL AGENT — Now it looks like you've taken health damage. You can take
    health away through programming, or just let it be a visual thing."

    "TUTORIAL AGENT — And this is how you remove it in the script."

    "TUTORIAL AGENT — Here is an example of morale damage."

    $ morale -= 1 # Removes 1 morale point.

    #TODO: play sound morale_damage
    show expression AlphaMask("images/red_gradient.png", At("images/character_ref.png", pulse_anim)) as mask with dissolve:
        pos (400, 107) # Use same position as the character sprite.
        matrixcolor HueMatrix(-80) # Purple
    show effects:
        alpha 0.3
        matrixcolor HueMatrix(-80) # Purple
    show notification_damage_morale
    show screen notice(_("DAMAGED MORALE"), _("-1"))
    with dissolve
    pause 1.5
    hide mask
    hide effects
    hide notification_damage_morale
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — You took morale damage."

# Addiction and Heal effects tutorial:

    $ morale += 1 #adds 1 morale point.

    #TODO: play sound morale_heal
    show effects:
        alpha 0.3
        matrixcolor HueMatrix(-160) # Teal
    show notification_heal_morale
    show screen notice(_("HEALED MORALE"), _("+1"))
    with dissolve
    pause 1.5
    hide effects
    hide notification_heal_morale
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Here is an example of an addiction effect, like from
    smoking, which would raise you intellect up and tint the screen teal. It
    also looks like a heal effect."

    "TUTORIAL AGENT — And here comes a health healed animation."

    $ health += 1 # Adds 1 health point.

    #TODO: play sound health_heal
    show effects:
        alpha 0.3
        matrixcolor HueMatrix(+60) # Orange
    show notification_heal_health
    show screen notice(_("HEALED HEALTH"), _("+1"))
    with dissolve
    pause 1.5
    hide effects
    hide notification_heal_health
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — There we go. You can play around with the {color=[youtext]}HueMatrix{/color}
    number to tint the image other different colours."

# Death scenes tutorial:

    "TUTORIAL AGENT — Do you want the player character to be able to unlock death
    scenes? You can do that in this framework too!"

    play sound sfx_fys
    "{color=[fys]}HALF LIGHT{/color} {color=[check]}[[Easy: Success]{/color} — De...
    Death scenes? Sounds like *dangerous* business."

    "TUTORIAL AGENT — Here in this part of the scipt, we'll place an {color=[youtext]}if/else{/color}
    switch below. If the player has 0 or less health, they go to the death scene."

    $ health -= 5 # Removes 5 health points
    with dissolve # Adds a fade animation to the health bar draining.

    #TODO: play sound health_critical
    show effects:
        alpha 0.3
        ease 0.6 alpha 0.0 # Majes the gradient pulse in an animation.
        ease 0.6 alpha 0.3
        ease 0.6 alpha 0.0
        ease 0.6 alpha 0.3
    show notification_critical_health
    show screen notice(_("HEALTH CRITICAL!"), _("HEAL YOURSELF NOW!"))
    with dissolve
    pause 1.5
    hide effects
    hide notification_critical_health
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Okay, I'm going to remove all your health at once."

    "TUTORIAL AGENT — And now we'll have the script check to see if your health
    is all gone. You should add this check every time the character loses health
    or morale in the story."

    if health<1: # "If health less than 1."
        jump death_scene # Takes us to the death scene (game over).

    else:
        pass # "Nothing happens and we move on."

    label second_chance: # Player is given a second chance at life.
        pass

    #TODO: play sound unfreeze

    hide black with dissolve

    $ health += 5 # Adds 5 health points
    with dissolve # Adds a fade animation to the health bar filling up.

    "TUTORIAL AGENT — Any now I've brought you back to life."

# Journal and money/good points/thought cabinet/inventory tutorial:

    nvl clear

    # You'll need to define money and goodbad points before players open the journal:
    $ money = 0 # Define having no money.
    $ goodbad = 0 # Define your good/bad points.

    # Declare every task that will be included in your game before the player
    # opens their journal:
    $ task_go_on_a_date = 0 # 0 means it's hidden in the journal. If you want the
                            # task to have multiple steps to complete, use numbers.
    $ task_brush_teeth = 0
    $ task_buy_hat = 0

    # Declare thoughts for the thought cabinet:
    $ thought_this_feeling = 0

    # Declare thoughts for the thought cabinet:
    $ silly_shoes = False # Since you can either have or not have this item, we'll use
                          # a True/False switch

    show screen journal_icon with dissolve # Makes the journal appear with a dissolve.

    "TUTORIAL AGENT — You also can also include a journal filled with your tasks.
    It's empty now."

    # To unlock an article, set it to True in the appropriate part of your
    # story's script:
    $ task_go_on_a_date += 1 # This unhides the task in the journal by adding a number.
    "{color=[greentext]}New task: Go on a date{/color}{nw}"

    # Add notice animation:
    #TODO: play sound task_gained
    show notification_task
    show screen notice(_("TASK GAINED:"), _("GO ON A DATE."))
    with dissolve
    pause 1.5
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Let's add a new task. It should appear in the journal now."

    # You can find a cheat sheet for different green text messages (for quick reference)
    # in cheat_sheet.rpy

    "TUTORIAL AGENT — By the way, there's more notification icons I've made that
    you can use. They are located in the {color=[youtext]}images{/color} folder
    and in {color=[youtext]}declare.rpy{/color}."

    # You can find a cheat sheet of notification messages (for quick reference)
    # in cheat_sheet.rpy

    "TUTORIAL AGENT — Notifications for things like items gained, experience
    gained, reaching critical health, and so on."

    $ task_go_on_a_date += 1 # Adds 1 to the number (which equals 2 total)
    $ task_go_on_a_date += 1 # Adds 1 to the number (which equals 3 total)

    # Add notice animation:
    #TODO: play sound task_updated
    show notification_task
    show screen notice(_("TASK UPDATED:"), _("GO ON A DATE."))
    with dissolve
    pause 1.5
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Now I'll update the task. Pretend that you completed two steps
    to finishing it. Now the completed steps are crossed out in the journal entry."

    $ task_go_on_a_date += 1 # Adds 1 to the number (which equals 4 total)

    # Add notice animation:
    #TODO: play sound task_completed
    show notification_task
    show screen notice(_("TASK COMPLETE:"), _("GO ON A DATE. +10 EXPERIENCE"))
    with dissolve
    pause 1.5
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Now the task is completed."

    $ task_brush_teeth += 1
    "{color=[greentext]}New task: Brush your teeth{/color}{nw}"

    # Add notice animation:
    #TODO: play sound task_gained
    show notification_task
    show screen notice(_("TASK GAINED:"), _("BRUSH YOUR TEETH."))
    with dissolve
    pause 1.5
    hide notification_task
    hide screen notice
    with dissolve

    $ task_buy_hat += 1
    "{color=[greentext]}New task: Buy a new hat{/color}{nw}"

    # Add notice animation:
    #TODO: play sound task_gained
    show notification_task
    show screen notice(_("TASK GAINED:"), _("BUY A NEW HAT."))
    with dissolve
    pause 1.5
    hide notification_task
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — I'll unlock the other two tasks. Again, they'll now be
    readable in your journal."

    $ thought_this_feeling += 1 # This unhides the thought in the journal by adding a number.
    # Define thought effects:
    $ logic -= 1
    $ empathy += 1
    "{color=[greentext]}Thought gained: This Feeling{/color}{nw}"

    # Add notice animation:
    #TODO: play sound thought_gained
    show notification_thought
    show screen notice(_("THOUGHT GAINED:"), _("THIS FEELING"))
    with dissolve
    pause 1.5
    hide notification_thought
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — You've also gained a thought now."

    "TUTORIAL AGENT — Imagine the player doing a lot of plot for an hour..."

    $ thought_this_feeling += 1 # Adds 1 to the number (which equals 2 total)

    # Define thought effects:
    $ suggestion += 3
    $ composure -= 1
    $ pain_threshold -= 2

    # Add notice animation:
    #TODO: play sound thought_imminent
    show notification_thought
    show screen notice(_("BREAKTHROUGH IMMINENT"), _("THIS FEELING"))
    with dissolve
    pause 1.5
    hide notification_thought
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Okay. You've now completed the thought."

    "TUTORIAL AGENT — Let's talk about money and good cop bad cop points. This
    template has those too."

    "TUTORIAL AGENT — The journal and thought cabinet can be edited in
    {color=[youtext]}journal.rpy{/color}."

    # Add notice animation:
    #TODO: play sound money_shared
    show notification_money
    show screen notice(_("MONEY GAINED:"), _("5.01 REÁL"))
    with dissolve
    pause 1.5
    hide notification_money
    hide screen notice
    with dissolve

    $ money += 5.01 # Adds 5.01 money.

    "TUTORIAL AGENT — You now have 5.01 money added to your wallet. The amount
    will appear in your journal."

    $ goodbad += 10 # Adds 10 good points.

    "TUTORIAL AGENT — Now you have gained 10 good points."

    $ goodbad -= 11

    "TUTORIAL AGENT — Now you have -1 points. This means you are bad, since you
    now have negative points."

    "TUTORIAL AGENT — Now let's do the inventory system. I'll give you a pair of
    shoes."

    $ silly_shoes = True
    "{color=[greentext]}Item gained: Silly Shoes{/color}{nw}"

    # Add item effects, if there are any:
    $ composure -= 1
    $ savoir_faire += 1

    # Add notice animation:
    #TODO: play sound item_shared
    show notification_item
    show screen notice(_("ITEM GAINED:"), _("SILLY SHOES"))
    with dissolve
    pause 1.5
    hide notification_item
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — Check them out in your inventory."

    "TUTORIAL AGENT — This framework doesn't allow you to choose what items to
    wear (if, for example, you have 2 pairs of shoes, you will end up wearing
    the effects of all of them). But you can lose items by setting the item to
    {color=[youtext]}False{/color}. Right, let's move on."

# Experience points and levelling up tutorial:

    # Define experience points and level at the beginning of your story:
    $ exp = 0
    $ level = 0

    "TUTORIAL AGENT — You can also include experience points in your game. Again,
    as either a real counter, or as a visual thing."

    $ exp += 5
    "{color=[greentext]}+5 XP: gained experience{/color}{nw}"

    # Add notice animation:
    #TODO: play sound xp_gained
    show notification_xp
    show screen notice(_("GAINED EXPERIENCE"), _("+5XP"))
    with dissolve
    pause 1.5
    hide notification_xp
    hide screen notice
    with dissolve

    "TUTORIAL AGENT — You've been a clever detective. Let's give you some free
    XP."

    "TUTORIAL AGENT — You can add a counter to your journal if you want it to
    include it."

    "TUTORIAL AGENT — And if you want the player to level up, you can add an
    {color=[youtext]}if/else switch{/color} to check if the player has reached
    100 XP (what is required to level up). You can add this switch every time they
    gain XP (or enough where they *might* have reached 100 XP)."

    $ exp += 100

    "TUTORIAL AGENT — Let's quietly give you 100 points to test that..."

    if exp >= 100: # "If exp is 100 or higher"
        $ exp -= 100 # Removes exp for next level up time
        $ level += 1 # Adds a level
        "{color=[greentext]}Level up!{/color}{nw}"

        # Add notice animation:
        #TODO: play sound skill_point
        show effects: # Levelling up tints the screen with a gradient
            alpha 0.3
            matrixcolor HueMatrix(-190) # Green
        show notification_skill
        show screen notice(_("NEW SKILL POINT!"), ())
        with dissolve
        pause 1.5
        hide effects
        hide notification_skill
        hide screen notice
        with dissolve

    else:
        pass

    nvl clear

    "TUTORIAL AGENT — Keep in mind that this framework doesn't actually have a
    skills page like in Disco Elysium, so you'll have to be more creative with
    allowing players to spend skill points."

    "TUTORIAL AGENT — A possible work around would be to, after levelling up,
    Asking the player what skill they'd like to spend the skill on, through a
    dialogue tree."

    "TUTORIAL AGENT — To prevent the clutter of giving the player 24 choices at
    once, first ask which ability the skill falls under, and then list those 6
    skills. That's when the player picks and you add a number increase to that
    skill."

# In-game clock tutorial:

    $ time = 10.11 # Set the time before showing the clock icon. Avoid numbers ending
                  # in 0.

    show screen clock_icon with dissolve

    "TUTORIAL AGENT — You can also add an in-game clock. The display shown here
    can be edited in {color=[youtext]}vitality.rpy.{/color}"

    #And add time (or change it) when you need time to progress,
    $ time += 1
    #$ time = 11.11 # Does the same thing (adds 1 hour).
    #TODO: play sound clock_tick # Like in Disco Elysium, you can add a sfx.

    "TUTORIAL AGENT — You can control the time as the text progresses. I've just
    added an hour to the clock, detective."

# Point and click/map tutorial:

    nvl clear

    "TUTORIAL AGENT — Next, I'll show you how to make a screen you can interact
    with by clicking on images in the artwork. We'll pretend there's a crime
    scene to inspect."

    "TUTORIAL AGENT — Click on what you want to inspect. When you're done
    exploring, mouse over to the bottom of the screen and click on the gradient
    that appears. Okay, here comes the screen..."

    show image "images/map_ref.png" with dissolve # Show a copy of the map so it
                                                  # appears to stay up after you
                                                  # select something.

    call screen map_screen_1 # Calls the map screen.

    label done_map_1:
        hide screen map_screen_1

    "TUTORIAL AGENT — What you see here is a room with a shirt. But this same
    method could be used for a map of town. Where you select which building you
    want to enter."

    scene image "images/bg_bathroom.png" with dissolve

    "TUTORIAL AGENT — You can customise this scene in {color=[youtext]}map.rpy{/color}"

# Textbox tutorial:

    nvl clear

    "TUTORIAL AGENT — If you want to replace this textbox with something more
    stylish and custom, go to the {color=[youtext]}game/gui{/color} folder and
    replace the file named nvl.png with your own image."

    play sound sfx_mot
    "{color=[mot]}REACTION SPEED{/color} — But be sure to save an image that is
    the same dimensions and placement as the original image. Otherwise, it may
    be displayed in the game wonky."

    play sound sfx_int
    "{color=[intel]}LOGIC{/color} — Though you can play around with editing the
    gui script if that happens. But I'd only recommend that if you have some
    experience in programming, or are trying to learn programming."

    "TUTORIAL AGENT — To change the opacity of the textbox, go to {color=[youtext]}game/screens.rpy{/color}
    and change the {color=[youtext]}alpha{/color} number on line 1419."

# Main menu/in-game screen art tutorial:

    "TUTORIAL AGENT — If you want to change the main menu art, or the in-game
    menu screen art, go to the gui.rpy file, scroll down to the \"Main and Game
    Menus\" header (on line 91), and change the maximum number of NVL-mode entries
    Ren'Py will display. It is this line, {color=[youtext]}define gui.main_menu_background
    = \"gui/main_menu.png\"{/color} and {color=[youtext]}define gui.game_menu_background
    = \"gui/game_menu.png\"{/color}"

# Hyperlinks tutorial, plus where you can find more info:

    nvl clear

    play sound sfx_int
    "{color=[intel]}LOGIC{/color} — You can also add music, more sound effects,
    and voice acting. There is {a=https://www.renpy.org/doc/html/}Ren'Py
    documentation online{/a} wherein you can find more info on it."

    play sound sfx_psy
    "{color=[psy]}INLAND EMPIRE{/color} — The engine Ren'Py lets you customise
    and add in a lot of stuff, including main menu art, menu screens, splashscreens
    that you can play when the game first opens, character portrait art (called
    side images), and animated sprites."

    play sound sfx_int
    "{color=[intel]}ENCYCLOPEDIA{/color} — You can also do a lot of character
    customisation in Ren'Py. You can let the player choose the clothes that
    appear on the character sprite, choose their name, and choose the pronouns
    other characters refer to them by."

    "TUTORIAL AGENT — The {color=[youtext]}images{/color} and {color=[youtext]}gui{/color}
    folders contains other things I've made (but haven't programmed that) you can
    use, such as additional cursors for when you hover over things, thought orbs,
    and gradients for moving around a map."

# Ending the game tutorial:

    nvl clear

    "TUTORIAL AGENT — I think that's everything. If you need anything else, I
    recommend going to a Ren'Py or visual novel development space and ask the
    people there what you need help with."

    "TUTORIAL AGENT — This was a tutorial by Katy133. If you'd like to support
    my work, please take a look at my {a=https://ko-fi.com/katyartist}Ko-fi{/a},
    {a=https://www.patreon.com/Katy133}Patreon{/a}, or check out my other games
    on {a=https://katy133.itch.io/}Itch{/a}. I also write Disco Elysium fics."

    "KATY133 — Oh, and remember to rename your game to something else in the
    options.rpy file (on line 15, 39, and 156), and to add in your own credits
    in the screen.rpy file, under the \"About Screen\" header (line 541). Please
    credit me in the {color=[youtext]}Credits{/color} screen as is."

    "KATY133 — Turrah! Bye! Have fun!"

    return # This ends the game.


# Death Scene Below ################

    label death_scene:
        #TODO: play sound freeze

        show black:
            alpha 0.8
        with dissolve

        "TUTORIAL AGENT — You've now died and are in the death scene, located at
        the bottom of script so it doesn't interfere with the rest of the script."

        "TUTORIAL AGENT — Normally, this would end the game early and take you to
        the main menu, but I'm going to save you instead."

        #return # Unhide "return" if you want the player character to actuall die
                # and return to the main menu.

        jump second_chance # This saves the player, taking them back to where
                           # they were.


# Point and click scenes Below ################
    label map_1_shirt:
        "TUTORIAL AGENT — There is a brown shirt on the ground."

        call screen map_screen_1 # Brings up the map again.

    label map_1_orb_1:
        "TUTORIAL AGENT — This spot is empty."

        call screen map_screen_1

    label map_1_orb_2:
        "TUTORIAL AGENT — There is nothing to be found here."

        call screen map_screen_1
