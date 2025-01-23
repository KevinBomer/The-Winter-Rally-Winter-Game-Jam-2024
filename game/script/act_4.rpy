default act4_focus_minigame_success = False
default act4_focus_minigame_points = 0

label act4:

    scene icerink with dissolve

    "The ice rink sounded like a good idea on paper, we all thought."

    "A quintessentially wintry pastime where all of your friends hit the ice, then skate like a pro or look good trying."

    "And whilst some of us couldn't walk straight with blades on the soles of our feet..."

    show ter aha at centerstage:
        yoffset 1000
        spring3 .5 yoffset 0

    #$ play_music(hospital,3)

    ##Suddenly enter TERRIE from screen middle

    ter "ACK! Too frozen, too frozen!!"

    ##Enter MORGAN from screen left.

    show morg hospital default at centerstage with easeinleft:
        xpos 0.15

    morg "Give me your hand, Terr."

    morg "It's like riding a bike; the faster you move, the less you wobble."

    show morg hospital default at centerstage:
        xpos 0.5

    show ter hospital happy at centerstage:
        xpos .75

    with ease

    "...others moved like they were raised on ice."

    morg happy "Isn't this just the life, everyone? The speed, the wind, the chill all over again." # content sigh

    morg "Oh, it's just so... so freeing..."

    if act2_finn_success:

        show fin tense at centerstage:

            xpos 0.25
            yoffset 1000
            spring3 .5 yoffset 0

        ##Pop-in FINN.

        fin "I have yet to be the judge of that!" # anxious

        fin happy "Excuse me, friend, would you care to provide me with a boost off the wall?"

        menu:
            "Gently push him":

                show fin tense:

                    ease 0.2 xoffset 25
                    ease 0.2 xoffset -25
                    ease 0.2 xoffset 0
            

                fin happy "Maybe with somewhat more oomph next time— I mean, whee…"

                ter playful "Ooh, look out, attempting to break the land speed record we have FINN at a BLISTERING 2 kilometers an hour!" # like a commentator

                morg playful  "Oh, how will he and his pit crew ever hope to topple the current defending champion?" # fake gasp

                fin "When the defending champion talks like that, perhaps she should let her actions speak instead."

                jump paths

            "Link arms and pull him along":

                show fin aha:

                    ease 0.1 xoffset 50
                    ease 0.1 xoffset -50
                    ease 0.2 xoffset 0
                    ease 0.1 xoffset 50
                    ease 0.1 xoffset -50
                    ease 0.2 xoffset 0

                fin aha "YIKES! Bold today, are we?!"

                morg playful "You'll both bring yourselves down with technique like that!"

                hide fin with dissolve

                morg aha "Oop...and there it is. Do you guys need a pair of hands?"

                show fin hospital tense at centerstage with dissolve:

                    xpos 0.25

                fin tense "Like we need air to breathe." # groans

                #beat
                pause 0.5

                fin default "Thank you. Now you try zipping forward with such velocity."

                jump paths

            "You're a great friend and you'll kick ass on the ice!":

                fin happy "Enthusiasm appreciated, but wrong kind of boost. I suppose it'll suffice... and we're off."

                ter playful "Attaboy, Finn! Come join me and… Wow, never mind, Morgan's skatin' circles around us already."

                fin "Oh, really? I think she could do better."

                jump paths

        #Paths converge

        label paths:

            show morg hospital playful with dissolve:
                xpos 0.5

            "Morgan developed a keen smirk."

            ter aha "Uh, dudes, I think you just declared war."

            morg happy "They most certainly did. Hold my gloves, Terrie."

            hide morg with dissolve

            show fin hospital default:
                xpos 0.35

            show ter hospital tense:
                xpos 0.65

            with ease

            ##Exit MORGAN.

            ter tense "I don't think you realize just what you're about to witness."

            ter aha "Remember how much of a beast she was on the ice before... before the—"

            fin aha "I never forgot, don't panic."

            ter "Yeah. I'm pretty sure she spent two hours by herself here for every hour we visited as the gang!"

    else:

        show morg hospital sad at centerstage:
            xpos 0.35

        show ter hospital sad at centerstage:
            xpos .65

        with ease

        morg "Just me and you and Terrie and not—not a lot of other people to judge you or cheer you or— or..."

        ##TERRIE shares a let-down expression very briefly.

        morg happy "Hey! I have an old routine I used to practice for ages."

        morg inthought "It's an old one, but it's... it's coming back to me, I think. Care to watch?"

        ter playful "Hey, s'long as I'm not falling down and you're in your zone, I'm game!"

        morg "Right. Okay. This is it. This is really happening. Hold my gloves, Terrie."

        ##Exit MORGAN.

        ter tense "Oh, she really needs this, doesn't she?"

        ter aha "Between this whole thing and then us being down two friends, I really wouldn't blame her if we spent the rest of the night here."

        ter playful "And y'know? I wouldn't mind. Morgan's an ice queen out here!"

    ter tense "I caught the tail end of one of her routines once when I came to get my skates re-sized. It was... really somethin' else."

    if act2_finn_success:

        ter happy "So prepare for a blown mind with a side of I-told-you-so!"

        menu:
            "We're gonna eat our words, Finn.":

                fin tense "Much like the sushi we dined on prior, I fear."

                ter playful "Dinner and a show? Sounds like we had the perfect day already!"

                fin happy "Time is still on our side, now. Who knows what else we'll see today?"

            "Hey, Morgan's just happy to be here. That's a win.":

                ter playful "True that! Look at us, cheering our girl on like it's nationals day."

                fin happy "She really should consider that level of performance if things improve."

                ter sad "Yeah…" #(awkward pause)

                pause 0.5

            "What if my mind was pre-blown coming into the rink?":

                ter playful "What, by the whole fact that she can actually skate? Fair!"

                ter tense "That and, uh..."

                ter aha "You definitely saw it at the hospital, right?" #(whispering directly to player)

    else:
        ter tense "Don't forget, you're gonna cheer for her until the roof shatters. At least! She deserves it all."

    ##Enter MORGAN again, this time further away from the others.

    show ter at centerstage:
        xpos 0.35

    show fin at centerstage:
        xpos 0.10

    with ease

    show morg at centerstage with dissolve:
        xpos 0.8



    morg default "I think we're ready! Are you watching, judges?" #(far off)

    ter inthought "Huh? Hey, that's us, we're judges!"

    ter playful "Knock 'em dead, Morgan!"

    pause 0.5

    ##Pause.

    ter embarassed "I mean, uh, perform with grace and beauty an' all that!" #(flustered)

    morg happy "I can do both!" #(far off, giggling)

    if act2_finn_success:
        fin happy "Fantastic! Come on, let's give her some space."

        hide ter

        hide fin

        with dissolve

        show morg at centerstage with ease:
            xpos 0.5

        "As the three of us made our way back towards the walls and gave Morgan the thumbs up, the fire in her eyes could have melted every ice rink between here and Montreal."

    else:
        ter playful "Alright, other judge - that's you - take your places!"

        hide ter

        hide fin

        with dissolve

        show morg at centerstage with ease:
            xpos 0.5

        "As the two of us made our way back towards the walls and gave Morgan the thumbs up, there were makings of a fire in her eyes. Weak, fledgling passion, but it was there."


    "But I wondered, did she still have it in her to push this far?"

    morg tense "Three, two, one, and..." # (whispering to herself)

    "Her blades kicked ice powder into the air as she started her dance, and the rest was history."

    # MINIGAME START

    jump act4_minigame_start

label act4_minigame_start:

    menu(timeout_label="act4_minigame_both_q2"):
        "Take a deep breath.":
            $ act4_focus_minigame_points += 1
        "Am I doing this now of all times?":
            pass
        "Are they watching?":
            pass

label act4_minigame_both_q2:

    menu(timeout_label="act4_minigame_both_q3"):
        "When was the last time I did this?":
            pass
        "Let muscle memory take over.":
            $ act4_focus_minigame_points += 1
        "Notice your heart rate is picking up.":
            pass

label act4_minigame_both_q3:

    menu(timeout_label="act4_minigame_both_q4"):
        "It's like I never left the ice.":
            $ act4_focus_minigame_points += 1
        "It’s been so long…":
            pass
        "Is my form alright?":
            pass

label act4_minigame_both_q4:

    menu(timeout_label="act4_minigame_both_q5"):
        "Are they watching?":
            pass
        "Wait, is it getting quiet?":
            pass
        "My body is moving on its own…":
            $ act4_focus_minigame_points += 1

label act4_minigame_both_q5:

    menu(timeout_label="act4_minigame_both_q6"):
        "Hold on, are we going for it??":
            pass
        "I think I’m getting sick.":
            pass
        "Bend your knees.":
            $ act4_focus_minigame_points += 1

label act4_minigame_both_q6:

    menu(timeout_label="act4_minigame_both_q7"):
        "I’m not ready!":
            pass
        "Hesitate.":
            pass
        "Jump!":
            $ act4_focus_minigame_points += 1

label act4_minigame_both_q7:

    menu(timeout_label="act4_minigame_with_finn_q8" if act2_finn_success else "act4_minigame_without_finn_q8"):
        "Oh god, it’s happening.":
            pass
        "Spin!":
            $ act4_focus_minigame_points += 1
        "Did someone say something?":
            pass

label act4_minigame_with_finn_q8:

    menu(timeout_label="act4_minigame_with_finn_q9"):
        "Soar!":
            $ act4_focus_minigame_points += 1
        "Notice a flash from the corner of your eye.":
            pass
        "Did someone take a picture?":
            pass

label act4_minigame_with_finn_q9:

    menu(timeout_label="act4_minigame_with_finn_q10"):
        "Time to finish strong!":
            $ act4_focus_minigame_points += 1
        "I hope they got my good side…":
            pass
        "Did I make a weird face doing that??":
            pass

label act4_minigame_with_finn_q10:

    menu(timeout_label="act4_minigame_result"):
        "Land awkwardly.":
            pass
        "Land eventually.":
            pass
        "Land with a purpose.":
            $ act4_focus_minigame_points += 1

    jump act4_minigame_result


label act4_minigame_without_finn_q8:

    menu(timeout_label="act4_minigame_without_finn_q9"):
        "Where’s Finn?":
            pass
        "Notice a flash from the corner of your eye.":
            pass
        "Did someone take a picture?":
            pass

label act4_minigame_without_finn_q9:

    menu(timeout_label="act4_minigame_without_finn_q10"):
        "Where’s Mina?":
            pass
        "I hope they got my good side…":
            pass
        "Did I make a weird face doing that??":
            pass

label act4_minigame_without_finn_q10:

    menu(timeout_label="act4_minigame_result"):
        "Land awkwardly.":
            pass
        "Land eventually.":
            pass
        "Land knowing you don’t have much time left.":
            pass

    jump act4_minigame_result

label act4_minigame_result:

    if act4_focus_minigame_points == 10:
        $ act4_focus_minigame_success = True
        jump act4_minigame_success
    else:
        $ act4_focus_minigame_success = False
        jump act4_minigame_failure


label act4_minigame_success:

    scene icerink with dissolve

    ## INT. ICE RINK - DAY with dissolve

    "History for the sports almanacs, that is."

    "I don't think I'd seen so many other ordinary people stop whatever they were doing and just… stare in awe."

    "All eyes were on Morgan, just as she deserved. She was like an angel, and the rink was her heaven."

    "An angel whose speed sometimes made her struggle to come to a timely Halt."

    show morg aha at centerstage:
        yoffset 1000
        spring3 .5 yoffset 0

    ##Pop-in MORGAN.

    morg "Watch it watch it watch it—!!!!" # (panicky)

    show morg aha at centerstage:
        ease 0.1 xoffset 25
        ease 0.1 xoffset -25

        ease 0.1 xoffset 0
        ease 0.1 xoffset 15
        ease 0.1 xoffset -15

        ease 0.1 xoffset 0

    "And who sometimes relied on me as a crash pad."

    morg playful "Oh, gosh, you. Two wipeouts in one session? Sorry, I've got you."

    menu:
        "You were glowing out there.":

            morg happy "Aw, you're just being nice."

            show ter hospital at centerstage with dissolve:
                xpos .75

            ter "Oh c'mon, be less humble; that rink was yours just now!"

        "You need to work on your finishes.":

            morg "I guess I do... you won't always be there to cushion the tough blows, will you?"


            morg sad "Then again, nothing's a hundred percent perfect right?" # (melancholy giggle)

        "Fancy a partner dance next time?":

            morg happy "Think you could keep up with me, or will you be waddling like a penguin?" #(sly giggle)

            pause 1.0

            #Beat.

            morg default "Same time, next month. Save the date, and if you flake I'm snowballing your house." # (much softer)  (laughs)

    "Morgan was alive. And it seemed now that she intended to keep it that way."

    if act2_finn_success: # TODO can you ever succeed at minigame without Finn being there?

        show fin hospital at centerstage with dissolve:
            xpos 0.25

        fin "Well, there's absolutely no chance of us ever topping that. Stellar performance."

        fin happy "You must be exhausted now, though — I know I am."

    show ter playful at centerstage with dissolve:
        xpos .75

    ter "Yeah, I'm beat, Morgs. Think you're rinked out for the day too?"

    morg default "I guess I am. As for the list, let's change and see what else there is."

    jump act4_end_with_finn


label act4_minigame_failure:

    show morg tense at centerstage with dissolve

    "Unfortunately, it was the kind of history you pray never repeats itself."

    "As free as she wanted things to flow, she stumbled and struggled through her routine, like she was chained and puppeteered by something we could never hope to see."

    "And as quickly as she got onto the ice..."

    "She was off her feet, and at our knees."

    morg hurt "Ow..." # (weakly)

    if act2_finn_success:

        morg sad "Oh God, everyone saw that, didn't they?"

        menu:
            "It was a good effort. Well done.":

                morg tense "Yeah, but... what happened?"

                morg sad "I mean, I know what happened, but, just... to me?"

                morg "I thought I'd gotten better enough to do this again, but I guess everyone has their limits, right? Yeah."

            "Far better than any of us could do, at least!":

                morg default "Thanks."

                morg tense "It feels like they're all staring at me. Do you think they think I'm a tryhard?"

                morg sad "Oh, this sucks. This sucks and my butt is frozen and I'm calling time."

        "Morgan looked like she was about to cry."

        show ter playful at centerstage:
            xpos .75

        show fin at centerstage with dissolve:
            xpos 0.25

        with dissolve

        ##Pop-in FINN and TERRIE.

        ter "Wee-oo, wee-oo, Terrie to the rescue, nothing to see here, people!" # (imitating an ambulance)

        ter "Vamoose! Don't make me call the resurfacer!"

        fin tense "Can you remain standing?"

        morg happy "Fortunately yes. Now come on, we have a list to complete."

        morg default "Full time, or whatever."

        fin inthought"For what it was worth, I loved the routine in spite of, uh..."

        "Morgan looked disappointed."

        fin upset "Okay, right, never mind, going with haste."

        jump act4_end_with_finn

    else:

        morg tense "Not again, not again...!" # (through gritted teeth)

        ##SCENE ICE RINK - DAY

        menu:
            "It was a good effort. Well done.":

                morg "You don't have to protect my feelings."

                morg "I guess I just skated too close to the sun, and then that's that!"

                morg sad"I guess I kind of deserve it."

            "Wordlessly help her up":

                morg sad "Much appreciated."

                morg "They're all staring at me now. I can feel it. Can you see it?"

            "Now at least everyone's bit the curb today, eh?":

                #MORGAN (sad sigh)

                #MORGAN (angry sigh)

                morg tense "Just help me up, please."

        "Morgan looked like she was about to cry."

        show ter playful at centerstage:
            xpos .75

        # Pop-in TERRIE.

        ter "Wee-oo, wee-oo, Terrie to the rescue, nothing to see here, people!" # (imitating an ambulance)"

        ter "Vamoose! Don't make me call the resurfacer!"

        ter default "That should do it. You okay?" # (softens, to Morgan)

        "Morgan looked disappointed."

        ter tense "Don't pay any mind to the world, I thought you kicked ass."

        "The disappointment persists."

        ter melancholy "Okay. Alright. I get it. All iced out for today, huh?"

        ter "I cleared a path for us, so let's blow this popsicle stand. You too, dude."

        hide ter

        hide morg

        with easeoutright

        ##Exit MORGAN and TERRIE from screen-right.

        ##FADE TO BLACK

        scene black with dissolve

        scene corridor day with dissolve

        ##SCENE STREET - DAY with dissolves

        ##Pop-in TERRIE and MORGAN.

        show ter default at centerstage:
            xpos .75

        show morg default at centerstage:
            xpos 0.25

        with dissolve

        morg "The fireworks. That's what's next."

        morg sad "We're going to go to that pretty hill, the one with the view, and then watch the fireworks go off, and then..." # (unsure of herself)

        ter tense "And then...?"

        morg "I'm not sure."

        ter happy "One step at a time, Morgan. I mean, hey, it's OUR secret spot."

        ter aha "No way anyone or anything can get through into that place, right?"

        ter happy "Just the three of us, and that's it. We're here for you, Morgs."

        morg "Three of us. Yeah."

        morg default "We just have to make sure we don't miss the starting time."

        ter playful "Right! What's the hold-up for, then?"

        morg aha "None! None at all."

        morg sad "...If I need help getting up the hill, I'll let you all know."

        "The day was drawing to a close faster than expected."

        "Fortunately, it would end with what we all came out for. What our hearts all held onto the most for the longest time."

        "I could only hope our grand day out would end with a bang."

        hide morg

        hide ter 

        with dissolve

        jump act6


label act4_end_with_finn:

    scene black with dissolve

    scene corridor with dissolve

    ##FADE TO BLACK

    ##FADE IN STREET - DAY with dissolve

    ##Pop-in TERRIE, MORGAN and FINN.

    show ter playful at centerstage:
        xpos .75

    show fin at centerstage with dissolve:
        xpos 0.25

    show morg playful at centerstage:
            xpos .75

    morg inthought "Alright, next on the agenda."

    morg happy "It's nearly fireworks time."

    ter aha "You're kidding! After all these years we're goin' back?!" # (squeals)

    morg playful "With a twist."

    morg "When was the last time you heard me scream?"

    ter default "Huh?"

    fin inthought "Ohhhh, I see. You aim to yell as loud as you can into the valleys and hear its echo?"

    morg default "You know me so well."

    ter tense "Honestly, girl, I'd get it if you just screamed right now outta nowhere."

    morg playful "Believe me. I've wanted to. That rink nearly never heard the end of it."

    morg inthought "That's why I thought, why not just do it in a place that matters?"

    ter playful "Okay, we love a bit'a showmanship!"

    ter happy "Let's do it, then. Let's see the pretty lights and wreck our throats for the next week."

    fin tense "I would prefer to preserve mine, in all honesty."

    ter playful "Your exam a speaking one?" # (cheeky)

    fin aha "No, but—"

    ter "Then we're good! C'mon!!"

    hide ter

    hide fin

    hide morg

    with dissolve

    ##MORGAN laughs, and they all exit.

    jump act4_end

label act4_end:

    "The day was drawing to a close faster than expected."

    "Fortunately, it would end with what we all came out for."

    "What our hearts all held onto the most for the longest time."

    "Our grand day out would for sure end with a bang."

    scene black with fade

    ##FADE TO BLACK

    jump act6


