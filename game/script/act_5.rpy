default act5_marry_morgan = False
default act5_minigame_timer = 20
default act5_minigame_points = 0

label act5:

    # Ferris Wheel

    #$ play_music(hospital,3)

    scene ferriswheel with dissolve

    "Passing through the gates, we entered a world of entertainment."
    "Rides that could bring screams of joy."
    "Confections that would sate the sweetest tooths."
    "Combined with the aura of fun and happiness, this was truly a magical world in one spot."
    "If this was any other night, we’d be enjoying it all. However…"

    show morg hospital default at centerstage with easeinleft:
        xpos 0.15
    #Enter Morgan
    #Morgan enters stage left
    morg happy "Wow… I can't tell how long it’s been since we’ve been here as well." # (overjoyed)

    show morg hospital happy at centerstage with ease:
        xpos 0.25
    morg playful"I would have loved to ride the rollercoaster. Probably one of the best parts of being here." # (happy)
    #Terrie enters stage right"

    show ter hospital happy at centerstage with dissolve:
        xpos 0.75
    ter "Personally, I love just riding the Ferris wheel." # (happy)
    ter playful "Best to see it all! The beauty of the city at night? Can’t be beaten." # (happy)
    morg inthought "But it’s so slow paced. I’m sure the roller coaster would be much better." # (shaking her head)
    ter melancholy "Listen Morgan. A roller coaster is fast paced for sure, but the experience is so short." # (disappointed)
    ter playful "And the lines! Who wants to wait so long in the lines?" # (smiling)
    morg default "What do you think? Is a roller coaster or a Ferris wheel better?" # (focused)

    menu:

        "Roller coasters are more exciting!":

            show morg hospital happy at centerstage:

                xpos 0.25
                ease 0.4 yoffset 50
                ease 0.2 yoffset 0
            morg "Oh I knew we’d be on the same page here." # (happy)
            ter tense "I guess no one else shares the vision I have." # (disappointed)

        "The view of the Ferris Wheel is unmatched.":

            show ter hospital happy at centerstage:

                xpos 0.75
                ease 0.4 yoffset 50
                ease 0.2 yoffset 0
            ter "Glad we are on the same page." # (happy)
            morg tense"I’m not denying it, but to put it over a roller coaster…" # (disappointed)

        "Food! It’s all about the food!":
            ter aha "I guess you always did have a sweet tooth, huh?" # (curious)
            morg happy "At least make sure to eat after the roller coaster." # (chuckling)

    #Branch Merge
    morg happy "What about you Finn? What’s your favorite thing?" # (happy)

    hide ter
    hide morg
    with dissolve
    show fin hospital default at centerstage with dissolve:

        xpos 0.25
    #Morgan fades out
    #Terrie fades out
    # Enter Finn
    #Finn enters stage left
    fin "Sitting on a bench so I can finish this online course to get ordained." # (distracted)
    fin inthought "Remember that’s what we came here for?" # (distracted)
    "The marriage. Morgan would choose one of us to marry."
    "On the list it didn’t specify who she’d marry."

    hide fin with dissolve

    show ter hospital happy at centerstage with dissolve:

                xpos 0.75
    #Finn fades out
    #Terrie enters stage right
    ter "So, who are you marrying Morgan?"
    #Terrie enters stage left

    show morg hospital happy at centerstage with dissolve:

                xpos 0.25
    morg "I’ll let you know once we reach the Ferris wheel." # (smiling)
    morg default "I do need to think about it after all." # (smiling)
    morg "I mean… marriage is a bond of love after all." # (smiling)
    morg happy "I’d want to make sure to pick the right person." # (smiling)

    show morg hospital happy at centerstage:

                xpos 0.35

    show ter hospital happy at centerstage:

                xpos 0.65

    with ease
    "Despite the debate earlier, Morgan bucket list had marriage at the top of the Ferris wheel."
    "Considering it was Morgan, we weren’t one hundred percent sure how serious this marriage would be."
    "Despite that, I found my heart beating a bit."
    "This was all to cross off something off her bucket list, yet… The moment was starting to feel… real."
    "Being married to Morgan… I could only imagine what our life would be like together."

    hide ter

    hide morg

    with dissolve
    #Morgan fades out
    #Terrie fades out
    "Eventually, we reached the base of the Ferris wheel, where Finn gave a loud audible sigh of relief."

    show fin hospital happy at centerstage with easeinleft:

                xpos 0.35
    #Finn enters stage left
    fin "You are now looking at an official priest. We are ready for this marriage." # (relieved)

    hide fin with dissolve

    show ter hospital inthought at centerstage with dissolve:

                xpos 0.35

    #Finn fades out
    #Terrie fades in
    ter "So… Who’s it going to be, Morgan?" # (curious)

    hide ter with dissolve

    show morg hospital inthough at centerstage with dissolve:

                xpos 0.35
    #Terrie fades out
    #Morgan fades in
    morg "Well…" # (thinking)

    menu:
        "Look intently at Morgan":

            if check_act3_minigame_success():
                $ act5_marry_morgan = True
            else:
                $ act5_marry_morgan = False

        "Look away when her eyes meet mine":

            $ act5_marry_morgan = False

    if act5_marry_morgan:
        jump act5_marriage_mc
    else:
        jump act5_marriage_terrie

label act5_marriage_mc:

    show mor hospital default at centerstage with ease:

                xpos 0.5

    "Morgan got onto one knee, facing me."
    morg happy "Will you marry me?" # (smiling)
    morg "Don’t worry, it’s only for a day." # (giggle)
    "Yes was all I could say."
    "I felt my heart beat the moment she selected me."
    "There was now a warm feeling building up in the coldness of the night."
    "Morgan's gentle, kind smile was all I could focus on as she looked me straight in the eyes."
    morg "So is everyone ready?" # (happy)

    hide morg with dissolve

    show ter hospital happy at centerstage with dissolve:

                xpos 0.35
    #Morgan fades out
    #Terrie fades in
    ter "I’m good to go! How about you Finn?" # (happy)
    #Terrie fades out
    #Finn fades in

    hide ter with dissolve

    show fin hospital happy at centerstage with dissolve:

                xpos 0.75

    fin "As ready as I can be." # (happy)

    hide fin with dissolve
    #Finn fades out
    "The four of us entered the line for the Ferris Wheel."
    "The three of them were chatting away about the last time we were here, yet my mind was trying to keep focus."
    "I didn’t want to mess up this moment no matter what."
    "It didn’t take too long before we were all seated in the Ferris Wheel."
    "As we began our slow ascent to the top, the beauty of the carnival and city became more and more apparent."

    show morg hospital default at centerstage with dissolve:

                xpos 0.35
    #Morgan enters stage left
    morg "You know… Looking out the window and seeing this Ferris Wheel… I always imagined getting to ride it." # (smiling)
    morg happy "Even if it wasn’t for this marriage… I did want to see the view from it at least one more time…" # (smiling)

    show ter hospital default at centerstage with dissolve:

                xpos 0.65
    #Terrie enters stage right
    ter "Yeah… it's totally something everyone should do at least once." # (happy)
    ter happy "The view can be so inspiring." # (happy)

    hide morg with dissolve

    show fin hospital default at centerstage with dissolve:

                xpos 0.35
    #Morgan fades out
    #Finn enters stage left
    fin "They say that memories are significantly easier to retain– when one is in an ideal state of mind." # (happy)
    fin happy "With little interference, these are the ideal conditions to have a matrimony that will last a lifetime." # (happy)

    hide fin 

    hide ter

    with dissolve
    #Finn fades out
    #Terrie fades out
    menu:
        "Perfect for a marriage, right?":
            show morg hospital happy at centerstage with dissolve:

                xpos 0.5

            morg "Absolutely." # (smiling)
        "This will truly be a night to remember":

            show morg hospital happy at centerstage with dissolve:

                xpos 0.5
            morg "Without question." # (smiling)
        "Remain silent":
            pass

    "Soon, we were approaching the apex of the Ferris Wheel."
    "As the Ferris Wheel slowed, my heart began to beat faster as Finn began explaining the process."

    hide mor with dissolve
    #Morgan fades out
    #Finn fades in

    show fin hospital inthought at centerstage with dissolve:

                xpos 0.35
    fin "We’ll have to skip a lot of the whole process and move on to the vows. Are you ready?"

    hide fin with dissolve

    show morg hospital happy at centerstage with dissolve:

                xpos 0.5
    #Finn fades out
    #Morgan fades in
    morg "Yes." # (smiling)
    "A gentle expression formed on Morgan as she spoke her vows first."
    morg "You are the beacon that unites us all together…" # (smile)
    morg default "… the person who gave us a memory that will never be forgotten.…" # (smile)
    morg happy "… I swear that I will make sure to cherish what you’ve done forever…" # (smile)
    morg sad "… to be someone worth remembering…" # (smile)
    morg happy "… and to continue to smile till the very end…" # (smile)
    "She meant every word."
    "I could only give a nod in response."
    "I took a deep breath before speaking my vow."

    # Vow Minigame

    "Morgan…"

label act5_vow_minigame:

    show screen act5_vow_choice_snowflake()
    if persistent.longer_choice_timers:
        $ act5_minigame_timer *= 1.5

    menu(choice_timer=act5_minigame_timer, timeout_label="act5_vow_minigame_failure", special_multi_choice=True):

        "I swear to be cool as a cucumber…":
            pass
        "I swear to make every moment we have together meaningful…":
            $ act5_minigame_points += 1
        "I swear to not forget to turn off the stove before leaving home…":
            pass

    menu(choice_timer=act5_minigame_timer, timeout_label="act5_vow_minigame_failure", special_multi_choice=True):
        "… to protect our credit score…":
            pass
        "… to protect you from those aggressive car salesman…":
            pass
        "… to protect that smile of yours that you cherish…":
            $ act5_minigame_points += 1

    menu(choice_timer=act5_minigame_timer, timeout_label="act5_vow_minigame_failure", special_multi_choice=True):
        "… to do what you want…":
            pass
        "… to hold these memories we have close to my heart forever…":
            $ act5_minigame_points += 1
        "… to be the best at everything…":
            pass

    menu(choice_timer=act5_minigame_timer, timeout_label="act5_vow_minigame_failure", special_multi_choice=True):
        "… and make sure you are happy…":
            pass
        "… and make sure our cat is happy…":
            pass
        "… and make sure everyone is happy…":
            $ act5_minigame_points += 1

    menu(choice_timer=act5_minigame_timer, timeout_label="act5_vow_minigame_failure", special_multi_choice=True):
        "… so long as I live.":
            $ act5_minigame_points += 1
        "… so long as we are together.":
            pass
        "… until the heat-death of the universe.":
            pass

    #Morgan fades out
    #Finn fades in

    hide screen act5_vow_choice_snowflake

    if act5_minigame_points == 5:
        jump act5_vow_minigame_success
    else:
        jump act5_vow_minigame_failure

label act5_vow_minigame_success:

    show fin hospital happy at centerstage with dissolve:

                xpos 0.5

    fin "You may now kiss the bride." # (smiling)
    #Finn fades out
    #Morgan fades in

    show morg hospital default at centerstage with dissolve:

                xpos 0.5
    "I found myself closing my eyes, ready for the kiss."
    morg happy "Hey…"
    #Morgan fades out

    scene topofferriswheel with dissolve
    # Scene Change – Ferris Wheel Top
    #Morgan fades in

    show morg hospital happy at centerstage with dissolve:

                xpos 0.5
    "When my eyes opened, I felt it."
    "It wasn’t too long, but it was a kiss I would never forget."

    jump act5_vow_minigame_end

label act5_vow_minigame_failure:

    show fin hospital happy at centerstage with dissolve:

                xpos 0.5

    fin "You may now kiss the bride." # (smiling)

    hide fin with dissolve

    show morg hospital default at centerstage with dissolve:

                xpos 0.5
    #Finn fades out
    #Morgan fades in
    "I found myself closing my eyes, ready for the kiss."

    pause 0.5
    # Pause
    #Morgan fades out

    scene topofferriswheel with dissolve
    # Scene Change – Ferris Wheel Top
    #Morgan fades in

    show morg hospital default at centerstage with dissolve:

                xpos 0.5
    "My eyes open, with me feeling the side of my cheek."
    morg playful "It was a bit messy, but… I appreciate the effort." # (chuckling)
    "I could only smile, wishing I had gotten all those vows correct."

    jump act5_vow_minigame_end

label act5_marriage_terrie:

    #Terrie enters stage right

    show morg hospital happy at centerstage:

                xpos 0.35

    show ter hospital default at centerstage with dissolve:

                xpos 0.65
    "Morgan got onto one knee, facing Terr."
    morg "Will you marry me Terr?" # (smiling)
    morg "Just for the day though." # (giggle)
    ter happy "Ah…I… I won’t let you down Morgan." # (smiling)
    morg "You got this Terr." # (smiling)

    hide morg

    hide ter

    with dissolve
    #Morgan fades out
    #Terrie fades out
    #Finn fades in

    show fin hospital happy at centerstage:

                xpos 0.5

    fin "Shall we get going?" # (smiling)

    hide fin with dissolve
    #Finn fades out
    "The four of us entered the line for the Ferris Wheel."
    "The four of us were chatting away, talking about the last time we were all here together."
    "I could remember us riding the roller coaster and Terr getting sick right after."
    "It was probably one of the reasons Terr started to prefer the Ferris Wheel."
    "It didn’t take too long before we were all seated in the Ferris Wheel."
    "As we began our slow ascent to the top, the beauty of the carnival and city became more and more apparent."

    show morg hospital default at centerstage with dissolve:

                xpos 0.35
    #Morgan enters stage left
    morg default "You know… Looking out the window and seeing this Ferris Wheel… I always imagined getting to ride it." # (smiling)
    morg happy "Even if it wasn’t for this marriage… I did want to see the view from it at least one more time…" # (smiling)
    #Terrie enters stage right

    show ter hospital default at centerstage with dissolve:

                xpos 0.65
    ter default "Yeah… it's totally something everyone should do at least once." # (happy)
    ter happy "The view can be so inspiring." # (happy)
    #Terrie fades out
    #Morgan fades out
    #Finn fades in

    hide morg 

    hide ter

    with dissolve

    show fin hospital inthought at centerstage with dissolve:

                xpos 0.35
    fin inthought "They say that memories are significantly easier to retain when one is in an ideal state of mind." # (happy)
    fin happy "With little interference, these are the ideal conditions to have a matrimony that will last a lifetime." # (happy)

    hide fin with dissolve
    #Finn fades out

    menu:
        "Perfect for a marriage, right?":
            #Morgan fades in

            show morg hospital happy at centerstage with dissolve:

                xpos 0.5
            morg "Absolutely." # (smiling)

            hide morg with dissolve
            #Morgan fades out
        "This will truly be a night to remember":
            #Morgan fades in

            show morg hospital happy at centerstage with dissolve:

                xpos 0.5
            morg "Without question." # (smiling)

            hide morg with dissolve
            #Morgan fades out
        "Remain silent":
            pass

    "Soon, we were approaching the apex of the Ferris Wheel."
    #Morgan enters stage left
    #Terrie enters stage right

    show morg hospital default at centerstage with dissolve:

                xpos 0.35

    show ter hospital tense at centerstage with dissolve:

                xpos 0.65
    "Looking at the two of them, I could tell both were mentally preparing themselves for the marriage."
    "Terr, who was usually all smiles, seemed to be in deep concentration."
    "On the flip side, Morgan seemed to be looking intently at Terr."
    "I had no idea what she was thinking, but all I knew was she was treating this seriously."
    "As the Ferris Wheel slowed, the four of us got ready to perform the ceremony."

    hide ter 

    hide morg 

    with dissolve

    show fin hospital inthought at centerstage with dissolve:

                xpos 0.5
    #Terrie fades out
    #Morgan fades out
    #Finn fades in
    fin "We’ll have to skip a lot of the whole process and move on to the vows. Are you ready?"

    hide fin with dissolve
    #Finn fades out
    #Morgan enters stage left

    show morg hospital happy at centerstage with easeinleft:

                xpos 0.35
    morg "Yes." # (smiling)
    #Finn fades out
    #Terrie enters stage right

    show ter hospital happy at centerstage with easeinright:

                xpos 0.75
    ter "You know it!"
    "A gentle expression formed on Morgan as she spoke her vows first."
    morg default "You are the artistic soul that protects our memories…" # (smile)
    morg happy "… the person who has done so much for me.…" # (smile)
    morg "… I swear that I will make sure to cherish what you’ve done forever…" # (smile)
    morg sad"… to be someone worth remembering…" # (smile)
    morg happy "… and to continue to smile till the very end…" # (smile)
    "She meant every word."
    "Terrie must have realized it as well, as their expression changed as well."
    "I found myself smiling as I listened to Terr give the vows."
    ter inthought "Morgan…  You're the inspiration that inspires me to keep drawing…" # (gaze on Morgan)
    "The emotion I could feel from Terr’s voice told me all I needed to know."
    ter tense "… the one I aspire to protect no matter what …" # (staring)
    "They were giving it their all and Morgan was no different."
    ter happy "… I will love and cherish you till the very end…" # (staring)
    "Their focus was only on each other, with both me and Finn shut out."
    ter "… and hold the memories we have together forever close to my heart." #
    "And finally…"
    #Morgan fades out
    #Terrie fades out

    hide ter

    hide morg

    with dissolve

    show fin hospital happy at centerstage with dissolve:

                xpos 0.5
    #Finn fades in
    fin "By the power vested in me, you may now kiss the bride."

    hide fin with dissolve
    #Finn fades out

    #Scene Change – Ferris Wheel Top

    scene topofferriswheel with dissolve
    #Morgan enters stage left
    #Terrie enters stage right

    show morg hospital happy at centerstage:

                xpos 0.40

    show ter hospital happy at centerstage:

                xpos 0.60

    with dissolve

    "My heart fluttered seeing the two kiss."
    "It didn’t last long, but it seemed both of them were happy with the kiss."
    "Both had a smile on their face as they looked at each other lovingly."
    "I began wondering how it would have been if I gave the vows… but that wasn’t important."
    "Morgan was happy, and that was all that mattered."

label act5_vow_minigame_end:

    if act5_marry_morgan:
        morg happy "You know… this all may seem silly considering this was just all done in such a short time, yet…" # (smiling)
        morg "It felt so meaningful. A moment that I will hold dear to my heart…" # (smiling)

    #Terrie fades out
    #Morgan fades out

    hide morg

    hide ter 

    with dissolve
    #Finn fades in

    show fin hospital happy at centerstage with dissolve:

                xpos 0.5

    fin "Now then… how’s everyone feeling?" # (smiling)

    hide fin with dissolve
    #Finn fades out
    #Morgan enters stage left

    show morg hospital default at centerstage with dissolve:

                xpos 0.35
    morg "Honestly… I’m thankful we did this." # (smiling)
    morg happy "I will never forget this moment." # (smiling)

    show ter hospital playful at centerstage with dissolve:

                xpos 0.65
    #Terrie enters stage right
    ter "I’m so ready to draw this scene of us all together." #(smiling)
    ter happy "Pictures last a lifetime and, I want this moment to last forever." # (smiling)

    if not act5_marry_morgan:
        ter "One… that will forever inspire me to keep at drawing."

    menu:
        "Let’s finish off the day strong":

            show morg hospital happy at centerstage:

                xpos 0.35

                ease 0.4 yoffset 50

                ease 0.2 yoffset 0
            morg "Oh you know it!" # (smiling)
        "I’m so ready for that rollercoaster ride":

            show morg hospital playful at centerstage:

                xpos 0.35

                ease 0.4 yoffset 50

                ease 0.2 yoffset 0
            morg "Maybe another time! We got a list to finish off!" # (laughing)
        "Remain silent":
            pass

    #Morgan fades out
    #Terrie fades out

    hide ter

    hide morg

    with dissolve

    "With that, we began our slow descent."
    "We were close to finishing off the list and nothing would stop us now."

    scene black with dissolve
    # Fade Black

    jump act6