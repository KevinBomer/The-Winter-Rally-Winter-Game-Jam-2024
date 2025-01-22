label act7:

    $ mina.image = "mina" # setting Mina's image to the full sprite and not chibi

    ##SCENE HILL WITH A VIEW - NIGHT with dissolve

    #$ play_music(hospital,3)

    scene hilltop with dissolve

    # IF GOOD ENDING
    # FINN, MORGAN and TERRIE are already present - but MINA's sprite there too, blending in behind the crowd of sprites.

    # ELSE IF NEUTRAL ENDING
    # FINN, MORGAN and TERRIE are already present.

    # ELSE IF BAD ENDING
    ##MORGAN and TERRIE are already present.

    show ter hospital melancholy at centerstage:

                xpos 0.65

    show morg hospital melancholy at centerstage:

                xpos 0.35

    with dissolve

    ter happy "Aaand down we sit. Attagirl, Morgan." # (exerted sigh)

    ter tense "Last item of order comin' right up —how we feelin'?"

    if locked_in_ending != "bad":
        call act7_bad
    else:

        show fin hospital melancholy at centerstage with dissolve:

                xpos 0.75

        show morg hospital melancholy at centerstage:

                xpos 0.25

        show ter hospital melancholy at centerstage:

                xpos 0.5

        with ease
        call act7_good_neutral

    ##FADE TO BLACK

    scene black with dissolve

    ##INT./EXT. BLACK SCREEN

    "Then, it was January 8th."

    show death black cropped at centerstage with paintmask:
            subpixel True
            matrixcolor BrightnessMatrix (-1.0)
            blur 30
            xpos .6
            zoom .72
            easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65

    ##Slowly fade in DEATH.

    mortis "You know whom it is I seek."

    menu:
        "…":
            pass

        "Morgan.":
            pass

        "Be gentle, please...":
            pass

    mortis "Remain calm, little one."

    mortis "I shall take her with grace and care. It is what a spirit like hers deserves."

    if locked_in_ending == "good":

        mortis "She has left a footprint upon the sands of time which, thanks to your actions, will never weather."

        mortis "This day of hers was a gift, yet you transformed it into something greater. Even now, as we sleep, the energy she radiates is intrepid."

        mortis "You will remember this day. You all will."

        mortis "And so, in the ways that truly matter... she will persist eternally."

        mortis "If only humanity at large had such fulfilling friends, perhaps I would be feared far less."

        pause 0.5

        #After a brief pause
        "A digital alarm clock rang."

        mortis "Time has waned. We must depart now."

        mortis "Once again, I thank you. I can only hope that we do not meet again soon."

        mortis "Farewell."

        hide death black cropped with dissolve

        ##Fade out DEATH

        mortis "Good morning, Morgan." # (O.S.)

        scene white with dissolve

        ##FADE TO WHITE

    elif locked_in_ending == "neutral":

        mortis "Like the turbulent sea, the day I gifted her had its peaks and troughs. You were the winds that shaped those waves."

        mortis "I ask of you this." #  , [Player Name]

        mortis "Do you believe that if everyone were in the right place, and your control over the situation were more fruitful..."

        mortis "...that today's outcome could have been shifted?"

        mortis "Perhaps it is something upon which you should meditate. Direct the winds of change into the favor of others."

        mortis "This applies to you too." # , [PC Username]

        pause 0.5

        #After a brief pause

        "A digital alarm clock rang."

        mortis "Time has waned. We must depart now."

        mortis "Your efforts in aiding her have been appreciated."

        mortis "Farewell, until we meet again."

        

        show death black cropped at centerstage:
            subpixel True
            matrixcolor BrightnessMatrix (-1.0)
            blur 30
            xpos .6
            zoom .72
            ease 0.6 alpha 0.1 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65

        ##DEATH starts to fade out, but then the player's mobile phone begins ringing.
        ##DEATH remains semi transparent.

        "After several rings, a voicemail started playing. It was from MINA."

        mina "Heyyyy, bestie." # (O.S.)

        mina "SO, uh, I got some news for you, you're gonna flip..." # (O.S.)

        mina "I'm heading back to Vancouver for a while! Surprise!!!" # (O.S.)

        mina "Yeah, I was at a streamer party and I thought, man, this Morgan Day is giving major FOMO. So I said screw it and checked out earlier and now I'm at the airport!" # (O.S.)

        mina "I could only get there in time for the redeye flight, though, sooo… I'll call you when I touch down and need picking up, okay? Think like six, seven AM." # (O.S.)

        mina "Heck, bring Finn, and Terr and Morgan too! Agh, I'm geekin', I can't wait to see the four of you again!" # (O.S.)

        mina "Okay, TSA checkpoint coming up. Call me. And tell Morgan I— actually, don't tell her I say hi. I wanna surprise her in person!" # (O.S.)

        mina "Byeee to you~ Oh, and..." # (O.S.)

        "The voicemail clicked and ended."

        hide death black cropped with dissolve

        ##Fade-out DEATH fully.

        "Mortis and Mina" "Good morning, Morgan." # (O.S.)

        scene white with dissolve

    else:

        mortis "After all, she begged the world for a second chance, and in the end it told her no."

        mortis "Such apathy cannot be ignored, nor can it be accepted. This surely is not the experience you wanted on behalf of your dearest companion. Do you agree?" # [Player Name]

        mortis "Or perhaps you believe it matters not, as my arrival indicates."

        pause 0.5

        #Pause.

        mortis "Do you fear me too much to even try?"

        mortis "That is no way to live. The shoot that hesitates to sprout in the winter frost will never know the warmth of the springtime sun."

        mortis "Do not fall into the same trappings as your cohort. Do not hold your breath in spite of others who are so desperate for a gasp."

        mortis "Do not let what happened to Morgan happen again." # , [PC Username]

        mortis "For if we ignore all else in anticipation of my presence..."

        mortis "Nothing stops me from making myself known to everyone."

        pause 0.5

        #After a brief pause

        "A digital alarm clock rang."

        mortis "Time has waned. We must depart now."

        mortis "She will certainly be in better hands."

        mortis "However hard you think you cherish your life, cherish it tenfold."

        mortis "Farewell."

        hide death black cropped with dissolve

        ##Fade out DEATH.

        mortis "Good morning, Morgan." # (O.S.)

        jump act7_bad_epilogue

    ##FADE TO WHITE

    return



label act7_good_neutral:

    show morg hospital sad at centerstage:

                xpos 0.35

    "Morgan took a deep, calm breath."

    show morg hospital default at centerstage:

                xpos 0.35

    morg "Ready."

    fin melancholy "Me too. Being back here once again, I'd have kicked myself had I passed you up earlier today."

    morg happy "Yeah, we always loved going to see the fireworks."

    ter playful "I was actually thinking more about how you'd manage the 'screaming' part." # (chuckles)

    ter aha "There's crazy stuff on this list, but blowing your lungs out in the middle of nowhere?"

    ter "Anyone passing by's gonna hear us and think, like, bloody murder or something!"

    morg aha "Calling it now: it was Doctor Finn, with the number 2 pencil, in the open field."

    show morg hospital happy at centerstage:

                xpos 0.35

    fin happy "Relax, you." # (smirking)

    if locked_in_ending == "good":

        fin inthought "As far I know, it's just the five of us out here, okay?"

        morg happy "Like it always has been and—"

        morg aha "Wait. Five?"

        #MORGAN's expression changes to one of shock.

        fin happy "Yes, of course, five. You didn't forget anyone here, did you?" # (feigning ignorance)

        ##Suddenly MINA comes into proper focus.

        mina slysmile "Iunno, lil' bro, she looks like she's seeing ghosts."

        #TERRIE's expression becomes shocked too in a long pause.

        mina smile "Oh, yeah, hey gang."

        ter aha "WHAT THE F—"

        show morg hospital happy at centerstage:

                xpos 0.35

        "Morgan squealed extremely loudly!"

        scene black with dissolve

        pause 0.5

        scene hilltop with dissolve

        ##FADE TO BLACK

        ##SCENE HILL WITH A VIEW with dissolve

        #MOMENTS LATER

        morg aha "MINA?! HOW— WH— THE—"

        morg sad "I thought you said you were a no-show!"

        mina smile "Yeah, funny story..." # (bashful)

        mina default "D'you guys know that a flight from LAX is exactly 3 hours non-stop?"

        mina "I didn't know if I could fit it into my day, but then THIS guy."

        fin happy "That's me."

        mina smile "This GOAT of a man. He's calling me at 'round sunset all like, ooh, I am your brother and I know what's best and you can go to that streamer party next week instead." #  (imitating Finn)

        mina "And I actually could! So, big whoop!"

        fin "It was the least we could do after our stunt at Miya's."

        mina "Oh, yeah, that whole thing! Morgan, you better tell me all about what's been goin' on today."

        show morg hospital happy at centerstage:

                xpos 0.35

        "Morgan looked like she was on the verge of tears, but in a happy way."

        mina brokensmile "Crap, is she good?" # (whispering)

        morg "Yeah." # (sniffles)

        morg sad "I'm just... you came."

        mina default "Of course I did, Morgs. Told you I didn't wanna miss this."

        morg happy "Come sit down here." # (more sniffling)

        if act3_next_action == "performance":
            morg "You guys, too! Mina has to hear all about my performance first things first!" # (teary laugh)
        else:
            morg "You guys, too! Mina has to hear all about my recent marriage first things first!" # (teary laugh)

        ter playful "Oooh, yeah, that stuff was juicy! Don't 'chu dare skimp on the details!"

        ##The fireworks begin!

    elif locked_in_ending == "neutral":

        fin inthought "As far I know, it's just the four of us out here, okay?"

        ter tense "Yeah. Would'a been crazy cool if we got Mina on board for this, though." # (sighs)

        fin default "Mina's... well, she's Mina."

        fin "Cannot tie down that free spirit."

        fin happy "You'll be sure to fill her in about everything tomorrow, yes? She seemed keen to hear from you."

        morg playful "I'll make sure I'm up bright and early, then."

        pause 0.5

        #Awkward pause.

        morg default "So, about that yell."

        morg playful "We have to time it just right so that we match the start of the fireworks."

        ter playful"Aaaah, no, fireworks, I'm gonna scream and cry and throw up like I'm a dog on Halloween!" # (jokingly)

        ter "Okay, I'm in character now."

        fin inthought "I feel like a cry from me is not in the cards tonight."

        ter aha "What, lack of inspiration?"

        ter playful "It's simple; just pretend that there's a huge shadowy monster that's been stalking you all day and you finally got a good look at it!"

        fin aha "Oh, you saw that thing too?"

        show morg hospital aha at centerstage:

                xpos 0.35

        "Terrie and Morgan looked shocked. After a moment, Finn let out a surprisingly hearty laugh."

        fin happy "I kid, I kid. Oh, Terrie, your face is a picture." # (sighing)

        fin "The only monster in my life is academia. That alone is inspiration."

        show morg hospital sad at centerstage:

                xpos 0.35

        ter melancholy "Hah... so true..." # (half joking)

        #The fireworks begin!

        ter happy "Crap, that was our cue. The floor's yours, Morgan."

        morg playful "Alright, everyone, picture your monsters. Or your theses."

        mortis "On one, two, three..."

        show morg hospital happy at centerstage:

                xpos 0.35

        "Morgan took a deep breath and let out a mighty
        enthusiastic scream that echoed through the night."

    scene black with dissolve

    scene hilltop with dissolve

    ##FADE TO BLACK

    ##SCENE EXT. HILL WITH A VIEW with dissolve
    #LATER

    "The fireworks were ending, and the general mood here was more relaxed."

    show morg hospital sad at centerstage:

                xpos 0.25

    morg inthought "Hey, everyone?"

    if locked_in_ending == "good":

        mina "What's good?"

        morg tense "If you guys were... in my shoes..."

        morg sad "And you had one day where you got to do anything you wanted, what would be your plan?"

        menu:
            "I'd like a quiet day in.":

                mina smile "Y'know, that is so real of you."

                mina "Just me, my best friends, a good game, a warm fire, and all we could possibly eat."

                fin aha "What, no webcam included?"

                mina "...I guess not."

                ter happy "I've always wondered what life's like for you off- stream. That's a day I'd love to be part of, man."

                mina default "Trust, if that ever happens, I'm upgrading you all to first class to come visit."

                mina smile "N-not like I want that to happen again, obviously!"

            "Oh, I'd totally cut loose.":

                fin inthought "Consider that my decision too."

                ter aha "Whuh— you? On a series of legendary benders?! Nah."

                fin playful "Evidently, you do not understand the first thing about medical students." # (smirking)

                mina smile "Dunno if you've heard about 'break times' from this guy, but, all I'm sayin' is there's a reason he takes that time so seriously." # (mischievous)

                fin "What happens during break time stays during break time. And inside several dozen bars throughout the Vancouver area."

                fin happy "But in the event of untimely circumstances, you would also be invited."

                fin inthought "Hypothetically, bear in mind."

            "I have no idea.":

                ter aha "Right?! There's so much I wish I could do every day already!"

                ter happy "Maybe I'd just go 'bout life as normal. Except this time, be extra extra gracious to everything around me."

                fin aha "I didn't even think it possible. You're already the grandest sweetheart of us all."

                mina smile "D'aww, Finny, you're quickly becoming a close second!"

                ter playful "Agh, as long as you guys are part of that day I'd be the happiest dude in the world!"
                fin happy "Don't mention it, my friend."

                ter sad "If only we could actually have another day like this, because, y'know…"

        #Awkward silence.

        morg aha "No, no, those were good answers. Thank you for sharing."

        morg happy "I love you guys."

        ter melancholy "Morgan... God, if you knew how much we all loved you." # (bittersweet)

        "Morgan's voice began to weaken."

        morg sad "I think I already do."

        morg hurt "If it was my choice, I'd do every single one of those days back-to-back forever."

        morg default"But for now, I'm… It's getting late, and I'm feeling the cold. Is it chilly for anyone else?" # (yawn)

        fin tense "It is January, indeed." # (uncertain)

        morg happy "Maybe it's time I headed back. Give me a hand, someone?" 
        
        "Everyone else's faces begin to sink in sadness. Nobody wants to say what they already know."

        mina brokensmile "Wait. Hold on. We can take you there."

        mina smile "Heck, we can stay the night. Make a slumber party out of it!"

        mina "Nigh Hill? That's the hospital, right, Finn?"

        fin default "Good ear, that's right."

        ter playful "Yeah, yeah! There's gotta be enough chairs in there for all of us!"

        morg sad "I'd like that."

        morg happy "I'd like that very much."

        morg "Would you mind getting another headstart? Another minute, that's all I need."

        "Terrie nodded."

        ter happy "I got you."

        ter playful "Well? C'mon, what are we waitin' for?! Chop chop! Tout suite! Nigh Hill needs us!"

        mina "Hells yeah! Add it to the list! A billion more orders of action, baby!"

        ter "See? That's the spirit!"

        hide mina

        hide ter

        with dissolve

        ##Fade out MINA and TERRIE.

        fin happy "We'll reconvene soon. Take care."

        hide fin with dissolve

        ##Fade out FINN.

    elif locked_in_ending == "neutral":

        ter tense "What's good, Morgs?"

        morg default "Day's nearly finished, so, uh..."

        morg tense "How did you find it?"

        menu:

            "A day to remember, for sure.":

                ter playful "Amen, brother!"

                ter "Mark my words, once things start lookin' up, days like these are gonna become our tradition."

                ter happy "Just... maybe without the bucket list? Less absolution, more pure vibes. Right."

            "I'm thinking... really? That's it?":

                ter aha "WHOA, harsh! There's only so much you can do in one day!"

                fin happy "On the contrary, perhaps we're lamenting on how we wish the day could be longer."

                ter playful "Aww, so we can spend more time together? You guys are too cute."

            "We could have planned it better.":

                fin tense "I somewhat agree. Spontaneity can only take you so far."

                fin sad "Maybe if Mina knew in advance, or I did..."

                fin inthought "Well, perhaps we'd have had a lot less grief at the dormitories."

                ##Awkward silence.

        show morg hospital default at centerstage:

                xpos 0.35

        fin happy "Thank you for today, by the way. Regardless of how it went. My skin's never felt better."

        ter playful "And my creative juices are flowin' like crazy!"

        morg happy "Lovely. This was our day, see? Not just mine."

        ter happy "We're gonna do one of these days again soon, right, Morgan?"

        show morg hospital sad at centerstage:

                xpos 0.35

        #Pause as MORGAN begins to frown.

        ter sad "Please?"

        morg tense "We'll get there when we get there. But for now..."

        morg sad "It's getting late, and I'm feeling the cold. Is it chilly for anyone else?" # (yawn)

        fin tense "It is January, indeed." # (uncertain)

        morg "Maybe it's time to check back in, then. I'd hate to catch a cold."

        "Everyone else's faces began to sink in sadness. Nobody wanted to say what they already knew."

        morg happy "You still live close by to Nigh Hill, right? It wouldn't be fair to take Terr and Finn out of their way so late, so maybe, let's just..."

        morg playful "Let's just say our goodbyes. And you get warm, and get some rest, study, draw, all that stuff, and we'll walk back to the hospital."

        fin "Morgan."

        morg happy "We'll give you a call tomorrow! It's okay."

        fin sad "That had better be a promise."

        morg sad "Cross my heart, hope to... it's a promise."

        ter "Oh, man, that's really it? Well, uh..."

        ter "Great day we had to day. See you soon, Morgan. Can I get a hug?"

        morg playful "Only if you get Finn in on the action too." # (giggles)

        ter "Deal." # (getting sadder)

        "Terrie sighed in a big mix of emotions."

        ter "Ah, there it is. I love you guys." # (smushed)

        ter "I guess, uh... yeah. Miya's is counting on an opener, so..." # (normal)

        ter "I'll catch you all later."

        fin "Same goes for me. I look forward to hearing from you tomorrow."

        morg sad "Of course." # (weakly)

        hide fin with dissolve

        pause 1.0

        hide ter with slowerdissolve


        ##Fade out FINN and TERRIE. TERRIE exits much slower than fin

    show morg hospital happy at centerstage with ease:

                xpos 0.5

    morg happy "And then, there were two."

    morg "Didn't you want to help the others set up?"

    morg "I can't blame you for getting lost in this view, though. I'll miss it."

    #Peaceful silence.

    if locked_in_ending == "good":

        morg "Is something the matter?"

        menu:

            "What's the plan tomorrow?":

                morg inthought "Well, that's up to you."

                morg happy "I'm sure what whatever you choose to do next, it'll be something great."

                morg sad "If I could choose, I'd be cheering you on every step of the way."

                morg happy "But I would maybe suggest to just... I don't know, live little?" #  (laughs)

            "Are you in good hands?":

                morg happy "Without a doubt."

                morg "You heard everyone else. A slumber party in a hospital? They know how to lighten a mood."

                morg "Between you and Terrie, and Mina and Finn, I've always been in good hands."

                morg sad "And tomorrow, I still will be."

            "Please don't.":

                morg hurt "You all know I can't stop it." # (sighs)

                morg sad "When I realized it at first, I was terrified."

                morg happy "But then along came you and Terrie, and we had this amazing day together, and that's kind of everything I needed."

                morg "So, now... I guess I'm okay with it. We completed the list."

        "Morgan began to cry gently."

        morg hurt "I couldn't have done any of this without you."

        morg "I'm alive right now."

        morg sad "That's all you need to worry about."

        "She sobbed, caught her breath, and sniffed."

        morg "You know what I'm worried about right now?"

        morg playful "Finn clocking me with a hospital pillow. Slumber party tradition, right?" # (laughs shakily)

        morg inthought "Can't happen if we keep them waiting, though, so..."

        morg happy "Come on. Walk with me."

        morg sad "It's time to go."

    elif locked_in_ending == "neutral":

        morg sad "I don't think I can sleep alone tonight."

        morg default "Today was refreshing, of course, but, tomorrow..."

        morg hurt "What am I gonna do tomorrow?" # (starting to cry)

        morg "It's just— you've just been so kind to me."

        morg "Whenever we slipped up today, you were there ready to face the next thing, and— and when things were good we stopped and savored the moment, and..."

        morg "Whatever tomorrow throws at me, I— I think I need a hand to hold."

        morg sad "So, if you're not busy tomorrow, then..."

        morg "Please. Stay with me tonight."

        menu:
            "Of course.":
                pass

            "I'm sorry, but...":
                pass

        ##MORGAN smiles, regardless of the outcome.

        show morg hospital happy at centerstage:

                xpos 0.35

        morg "I understand."

        morg playful "Now, if we spend any more time out here, we'll be icicles. Come on."

        morg sad "I guess it's time to go."

    return


label act7_bad:

    show morg hospital hurt at centerstage:

                xpos 0.35

    "Morgan took a deep breath... and started to sob."

    morg "...this wasn't worth the trouble."

    morg sad "Did anything we do actually go well?"

    ter aha "Well, I mean, we're togeth—"

    morg hurt "We're NOT!!"

    mortis "Finn's rotting away in his study, Mina's working on a career in another country, and I couldn't do ANYTHING right today because I'm... I'm..." # (rising hysterics)

    ter sad "No, Morgan... you're not weak, you're not \"not good enough\", you're—" # (cooing)

    morg grief "I'm fucking DYING, TERRIE!"

    "Terrie was visibly stunned into silence."

    mortis "I'm dying and I dragged you all along just to watch me bumble about all day."

    morg "What have I done?!" # (disgusted)

    ter tense "You know we're never gonna ask for anything from you to like you." # (sighs)

    ter grief "Just being here... it made me really, really… Happy..." #  (starts tearing up)

    morg sad "It could have been perfect." # (quiet)

    mortis "It could have been so, so perfect."

    morg "I miss Mina, I— miss Finn... why couldn't I get them to come?"

    # Silence

    morg hurt "I'm not ready."

    morg grief "Guys— guys, I can't do this. I can't, I can't stay here, it's cold, it's dark, it's— don't let it happen." # (panicking)

    morg "Please... please."

    ter "C'mere, Morgan. It's gonna be— We're here." # (clears throat)

    "Morgan fully burst into tears."

    morg "PLEASE!" # (screaming)

    "As she let out a haunting, anguished wail, the fireworks began."

    "She continues to cry and scream as long as the fireworks carry on."

    return

label act7_bad_epilogue:

    #Years Later
    ##SCENE EXT. CORRIDOR - THE SPOT with dissolve

    scene sushishop with dissolve 
    "Entering the Spot, the emptiness of the place gave off a familiar sadness."

    "The air of the place felt stale as the place was worse than it was a few years ago."

    "It wasn’t a surprise though. After the initial boom with Mina's help, she didn’t mention this place ever since."

    "No one wanted to be associated with this place, nor did anyone want to remember it."
    ##SCENE THE SPOT - DAY with dissolve
    ##Enter Miya
    yum "Ah. It’s been awhile dear. Please follow me."

    "Miya led me to one of the empty seats."
    ##MIYA smiles
    yum "Are you here to see young Terr? Unfortunately, they have the day off today."

    menu:
        "Typical. None of us are together on the day off...":
            pass
        "Ah. I can understand why. Today is a rough day to get together.":
            pass
        "...":
            pass

    "I didn’t want to feel bitter, yet it was hard to avoid it."

    "Mina hadn’t been in contact ever since she learned of Morgan’s fate."

    "Finn had been working towards med school and finally got in. That put him even further away from all of us."

    "Terr was fully focused on getting into art school now. Enough that it felt like they wanted to stop meeting with me to hang out."

    "And me… I was lost."

    "It felt like I was the last person holding on to Morgan’s memories, but that itself was hard."

    "That day was failure after failure."

    "If no one else wanted to bear the burden of these memories, then why should I?"

    menu:
        "I should forget everything and move on.":
            pass

    ##MIYA smiles.

    yum "No one’s perfect dear."

    "I turned to Miya, noticing her gentle smile as she looked at me."

    yum "Sometimes we make mistakes."

    yum "Perhaps those mistakes lead to the worst things happening."

    yum "However, all our mistakes can be corrected."

    menu:
        "No! They cannot! Morgan is dead and it’s our fault!":
            ##MIYA surprised
            yum "Do you… really believe that you cannot fix your mistakes?"

            yum "Are you not willing to spend the time to learn what went wrong and never make those mistakes ever again?"

        "I appreciate you trying to help, but you can’t change the past.":

            ##MIYA surprised
            yum "Do you… really believe that you cannot fix your mistakes?"

            yum "Are you not willing to spend the time to learn what went wrong and never make those mistakes ever again?"

        "...":
            pass

    ##MIYA smiles
    yum "I’ll tell you this dear."

    yum "It might seem like you only get one chance to make things right, but that’s never the case."

    yum "If you are willing to do whatever it takes to correct the mistakes you’ve made, then you can obtain the ending you really want."

    yum "Perhaps it won’t result in a perfect end, but at the very least you can stand proud and tell yourself what matters the most."

    yum "You tried."

    "My phone vibrated for a second. Checking it real quick, I saw it was a message from Finn."

    fin "I’m sorry I couldn’t make it today. I’m still… beating myself up for not being there for Morgan in her final moments."

    fin "If I could have done it again, I’d have gone with you three that day."

    fin "That regret eats me up every day, which is why I’m working as hard as I can to atone."

    fin "You might hate me for never showing up, but until I can save a life, I feel like I can’t move forward."

    fin "Mina feels the same."

    fin "The memories of that day made her distance herself from those memories and us."

    fin "To make amends, she’s been working hard to use her success to help others."

    fin "Like me, she also feels like if she cannot save a life in her own way, her success means nothing."

    fin "Anyways, I hope we can all get together one day."

    fin "I’m sure you both are seeking atonement as well, so I’ll leave you two to it."

    fin "Give Terr my regards."

    "Putting my phone down, I found myself finding a resolve I never thought I’d ever have."

    "It was not too late to correct the mistakes I’ve made that day."

    yum "Good luck dear."

    "I stood up and thanked Miya for the kind words."

    scene corridor day with dissolve 

    ##SCENE EXT. CORRIDOR — THE SPOT with dissolve
    "Walking out of the Spot, I was determined to learn from every mistake I made that day."

    "I’d try as many times as I could to make things better."

    "Only after that would I be able to accept whatever outcome there was to come."

    scene black with slowerdissolve

    ##FADE TO BLACK
    #The End

    return
