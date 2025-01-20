default minigame_successes = 0
default locked_in_ending = ""

label act6:

    if act2_finn_success:
        $ minigame_successes += 1
    if check_act3_minigame_success():
        $ minigame_successes += 1
    if act4_focus_minigame_success or act5_minigame_points == 5:
        $ minigame_successes += 1

    if not act2_finn_success:
        $ locked_in_ending = "bad"
    elif minigame_successes == 3:
        $ locked_in_ending = "good"
    else:
        $ locked_in_ending = "neutral"

    scene hilltop with paintmask2

    show death black cropped at centerstage with paintmask:
        subpixel True
        matrixcolor BrightnessMatrix (-1.0)
        blur 30
        xpos .6
        zoom .72
        easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65

    ##SCENE HILL WITH A VIEW - NIGHT with dissolve
    ##DEATH is already on-screen.

    "That night, when we were about to see the fireworks, we briefly lost track of Morgan."

    show morg hospital default at centerstage with dissolve:

                xpos 0.35

    #Pop-in MORGAN.

    mortis "Your time wanes." # (ominous)

    mortis "As the Sun comes to rise again, so too shall I."

    mortis "Remain mindful."

    #MORGAN's facial expression drops from happy to afraid to melancholic.

    morg sad "...Right..." # (shaky breath)

    if locked_in_ending in ["good", "neutral"]:

        mortis "Perhaps I caught your attention at an inopportune time."

        mortis "The joy I saw upon your face shone with a warmth fueled only by the wonders of life." # (softening)

        mortis "Today has treated you well, has it not?"

        morg happy "Yes... yes, like I'd never believed." # (fear easing)

        mortis "Then you shall have no problems in regaling me with your escapades." # (giggles)

        morg inthought "From the very start? Well..."

        morg happy "I gathered my friends and we set out to complete a list."

    else:
        mortis "Something has happened."

        mortis "The wills of your spirit run on fumes. You struggle with each successive step."

        mortis "You have accepted my gift, yes?"

        morg hurt "I... I tried. I promise I tried." # (despaired)

        mortis "Enlighten me. Tell me about your day."

        morg tense "I'll give you what I have."

        morg default "We started out with a list we wanted to fill."


    ##SCENE FINN'S DORM - DAY with dissolve

    scene dorm with dissolve

    if locked_in_ending == "bad":

        show morg hospital default at centerstage with dissolve:

                xpos 0.5



        morg "Our first order of action... we wanted to bring another friend with us."

        morg sad "He was busy. He told us no... so it was just us three."

        scene sushishop with dissolve

        show morg hospital tense at centerstage with dissolve:

                xpos 0.5

        morg tense "We tried to make things better with some food, but..." # (O.S.)

        morg sad "Without our other friends, the benches were noticeably empty." # (O.S.)

        morg "And when we had to help the owners out, there weren't enough of us to make a difference." # (O.S.)

        ##SCENE EXT. ICE RINK - NIGHT with dissolve

        scene icerink with dissolve

        show morg hospital default at centerstage with dissolve:

                xpos 0.35

        morg "I wanted to get back on the ice and skate like I used to, so that was next." # (O.S.)

        morg hurt "It turns out I just... don't have it in me anymore." # (O.S.)

        ##SCENE EXT. HILL WITH A VIEW - NIGHT with dissolve

        scene hilltop with dissolve

        show death black cropped at centerstage with paintmask:
            subpixel True
            matrixcolor BrightnessMatrix (-1.0)
            blur 30
            xpos .6
            zoom .72
            easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65

        show morg hospital tense at centerstage with dissolve:

                xpos 0.35

        morg "And— and that's it. I dunno what to say."

        morg sad "There's the fireworks coming up, but..."

        "Morgan coughed."

        #Then she becomes more teary.

        morg "I can't. I'm not ready, I have to try again, I have to let them all know—"

        mortis "No."

        mortis "I have already decided."

        mortis "At times, there is only so much one has the power to affect. The fates of others are, ultimately, theirs and only theirs to explore."

        mortis "You tried in earnest to the best of your abilities, but others walked a different path."

        morg hurt "No... it's not fair. I need—" # (shakily)

        mortis "Regardless of today's outcome, you would have found me here. It will not be altered."

        mortis "Acknowledge what has been, and accept what will be."

        "Morgan coughed again, harshly."

        morg sad "I can't... not yet... please..." # (weakly)

        mortis "You are graced with a matter of hours."

        mortis "The impetus is on you to set this last affair in order."

        "Morgan whimpered really depressingly."

        mortis "It will be okay, Morgan."

        mortis "No matter how overwhelmed you may feel, or how quiet the night may become."

        mortis "I will always be here for you."

        "Morgan sniffled and sobbed."

        mortis "Farewell for now. Your friends await."

    else:

        show morg hospital default at centerstage with dissolve:

                xpos 0.5

        morg "Our first order of action was to coax another of our pals, Finn, out of his shell just for the day." # (O.S.)

        morg happy "After all, if I could go so far out of my way to see Finn, then so could he for me. And he agreed." # (O.S.)

        morg "We were all pretty hungry after all that travel, so we decided to stop by somewhere familiar to eat..." # (O.S.)

        ##SCENE MIYA'S - EVENING with dissolve

        scene sushishop with dissolve

        show morg hospital happy at centerstage with dissolve:

                xpos 0.5

        morg "Oh, Miya's sushi was so good, and helping the owners out with the dinner rush made it taste all the more rewarding!" # (O.S.)

        morg inthought "And this one friend who couldn't make it today spread the word about the place enough for it to get a lot of new regulars." # (O.S.)

        if check_act3_minigame_success():
            morg happy "Plus, the atmosphere… I think they really missed us all." # (O.S.) # (sighs)
        else:
            morg sad "If only we could've handled their clientelle..."

        scene icerink with dissolve

        ##SCENE ICE RINK - NIGHT with dissolve

        show morg hospital default at centerstage with dissolve:

                xpos 0.5

        morg "Then, we all visited the ice rink. Not all of us could skate, but when I touched the ice for the first time again..." # (O.S.)

        if act4_focus_minigame_success:
            morg happy "It was like I'd never left." # (O.S.)

            morg "I just can't get across how unchaining it felt to dance and sprint and— just— wow! I get giddy thinking about it." # (O.S.)
        else:
            morg tense "I think my body betrayed me, though."

            morg sad "If I could have just known my limits, I would have NEVER embarrassed myself in front of everyone."

        ##SCENE EXT. FAIRGROUND - NIGHT with dissolve

        scene ferriswheel with dissolve

        show morg hospital happy at centerstage with dissolve:

                xpos 0.5

        morg "Oh, but then, but then!! I finally had my dream wedding." # (O.S.)

        if act5_marry_morgan:
            morg "I tied the knot with a special someone under the prettiest open sky we could imagine. A—as friends, of course!" # (O.S.)
        else:
            morg "I tied the knot with Terrie under the prettiest open sky we could imagine. A—as friends, of course!" # (O.S.)

        morg playful "But I don't like to kiss and tell, so, that's that on that. (laughs)" # (O.S.)

        ##SCENE EXT. HILL WITH A VIEW - NIGHT with dissolve

        scene hilltop with dissolve

        show death black cropped at centerstage with paintmask:
            subpixel True
            matrixcolor BrightnessMatrix (-1.0)
            blur 30
            xpos .6
            zoom .72
            easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65

        show morg hospital inthought at centerstage with dissolve:

                xpos 0.35

        if locked_in_ending == "good":
            morg happy "Now we're just going to see the fireworks, and then..."
        elif locked_in_ending == "neutral":
            morg sad "Hopefully the fireworks can bring it home."

        morg playful "And then..."

        pause 0.5

        show morg hospital tense at centerstage with dissolve:

                xpos 0.35

        #Heavy beat. Morgan's smile fades once again. She appears to be paler.

        "She coughed."

        if locked_in_ending == "good":
            morg sad "Please, just one extra day. I promise—"

            mortis "You know I will not." # (firm)

            mortis "You also, however, need not."

            pause 0.5

            #Beat.

            mortis "Child, you have lived one day of life more richly than you have for several years."

            mortis "Were it possible, I would say you have cheated me."

            mortis "Your spirit has cherished my gift in spite of your decaying vessel. For that, I possess immense pride in you."

        elif locked_in_ending == "neutral":

            morg sad "It could have gone better, really. Maybe if I had—"

            mortis "Your sentiment is universal. I watch countless souls waste away over what could have been instead of what will be."

            mortis "You encountered pleasant times, and you encountered roadblocks."

            mortis "Tree branches are often gnarled, and the path one takes towards fate is no different."

            mortis "It takes great strength to accept the unwanted alongside the dream. I trust you possess the resolve to do so."

        "Morgan coughed again."

        if locked_in_ending == "good":

            morg hurt "Is this... am I...?" # (weakly)

            mortis "Time has yet to reach you still. You shall live a little more."

            # mortis chuckles
            mortis "You may even find that what awaits you atop the hill is all you have ever hoped for."

            morg sad "Right... right. Okay." # (composing her breaths)

            morg default "I'm going. This is the fireworks ceremony, this is... this is it. I won't keep them waiting any longer."

            morg happy "Thank you. For today."

            mortis "Take care, Morgan." # (hums contently)

            mortis "We will meet again."

        elif locked_in_ending == "neutral":

            morg hurt "I hope..." # (weakly)

            mortis "Take this time to reflect deeply."

            mortis "Your friends expect you now. Their company will provide the confidence you need."

            morg default "Like they always have." # (composing her breaths)

            morg sad "So... this really is it? Okay."

            morg default "I can't keep them waiting any more."

            mortis "Savor what remains, Morgan." # (hums contently)

            mortis "I shall march on now."

    #DEATH slowly fades out.

    hide death black cropped with dissolve

    # MORGAN audibly shivers.

    ter "Morgan? Morgan?! You good, girl?" # (O.S.) # (far-away)

    morg aha "Huh—? Oh— yeah, I'm here! I'm okay!"

    show morg hospital sad at centerstage with dissolve:

                xpos 0.35

    show ter hospital playful at centerstage with dissolve:

                xpos 0.65

    ##Enter TERRIE from screen right.

    ter "Phew, you ain't sneakin' off to bed just yet, right?"

    # MORGAN labored breathing

    if locked_in_ending == "neutral":
        ter happy "Don'tchu worry. The fireworks will be just grand."

    if locked_in_ending == "bad":

        morg "Hi..." # (labored breathing)

        pause 0.5

        #Beat, as the smile on TERRIE's face falters.

        ter melancholy "It's nearly time to start. Let's go." # (soft)

        ##Exit TERRIE and MORGAN from screen right.

        hide morg

        hide ter

        with easeoutright

        "She came back up that hill, and together we watched the fireworks."

    else:
        #Beat, as the smile on TERRIE's face very briefly falters before picking back up again.

        show ter hospital melancholy at centerstage:

                xpos 0.65

        pause 0.2

        ter happy  "C'mon, just a few steps to go. I gota good feelin' about these fireworks."

        ##Exit TERRIE and MORGAN from screen right.

        hide morg

        hide ter

        with easeoutright

        if locked_in_ending == "good":

            "In hindsight, maybe Morgan taking a breather was a blessing in disguise."

            "At the end of the day, she dreamed big. And suddenly Finn and I had to prepare her for the fact that, somehow, the biggest of those dreams had come true."

            scene black with dissolve

        elif locked_in_ending == "neutral":

            "I waited at the top of the hill with Finn. It really was our spot reclaimed once again."

            "Despite the empty Mina-shaped space in between us, this would be a night to remember."

            scene black with dissolve

    jump act7






