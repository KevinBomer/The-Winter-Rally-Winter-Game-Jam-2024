default act3_customer_minigame_group1 = {}
default act3_customer_minigame_group2 = {}

default act3_next_action = "performance"

init python:
    def check_act3_minigame_success():
        for k, v in store.act3_customer_minigame_group1.items():
            if not v:
                return False
        for k, v in store.act3_customer_minigame_group2.items():
            if not v:
                return False
        return True

label act3:
    #EXT. CORRIDOR — THE SPOT
    #"The next thing on the list was a meal worth dying for. And for that, it would require a restaurant capable of producing such a meal."
    #"There was only one place that could have food that was worthy of such a title. One Morgan had listed specifically on the list due to its sheer importance to everyone."
    #"A quaint, family-run sushi restaurant called Miya’s that we visited frequently during our high school days. It might have been just another restaurant to some, but to us, this was The Spot."
    #"I can’t remember the last time I was here."
    #"Long forgotten memories come flooding back to when this place was full of life. However, time was not kind to it, like many things."
    #"Despite the wear and tear, color shines through like a flower under rubble."
    #THE SPOT - DAY
    #Terrie enters stage left
    #ter "And without further ado, I present to you {i}The Spot!{/i} A place we should all be familiar with!"
    #ter "Hope you’re all ready to satisfy both your body, mind, and soul with food from this joint!"
    #Terrie fades out
    #Morgan enters stage left
    #morg "It really has been a while, hasn’t it?"
    #morg "No time like today to make some new memories."

    scene corridor with dissolve
    #EXT. CORRIDOR — THE SPOT
    "The next thing on the list was a meal worth dying for. And for that, it would require a restaurant capable of producing such a meal."
    "There was only one place that could have food that was worthy of such a title. One Morgan had listed specifically on the list due to its sheer importance to everyone."
    "A quaint, family-run sushi restaurant called Miya’s that we visited frequently during our high school days. It might have been just another restaurant to some, but to us, this was The Spot."
    "I can’t remember the last time I was here."
    "Long forgotten memories come flooding back to when this place was full of life. However, time was not kind to it, like many things." 
    "Despite the wear and tear, color shines through like a flower under rubble."

    scene sushishop with paintmask2
    #THE SPOT - DAY
    #Terrie enters stage left
    show ter hospital playful at centerstage:
        xpos 0.25
        yoffset 1000
        spring3 .5 yoffset 0
    ter "And without further ado, I present to you {i}The Spot!{/i} A place we should all be familiar with!" 
    ter "Hope you’re all ready to satisfy both your body, mind, and soul with food from this joint!"
    #Terrie fades out
    #Morgan enters stage left

    hide ter hospital with dissolve
    show morg hospital default at centerstage with dissolve
    morg "It really has been a while, hasn’t it?"
    morg hospital happy "No time like today to make some new memories."

    hide morg hospital with dissolve

    if act2_finn_success:
        #Enter Finn
        #Morgan fades out
        #Finn enters stage left

        show fin hospital at centerstage with dissolve
        fin "I can’t recall the last time I’ve made time to come here."
        fin melancholy "My work made me forget just how much I missed this place, I wonder just how much has changed."
        fin happy "That being said, I quite like what’s been done with the place. The art adds a nice touch."
        "It wasn’t a surprise that the artwork was the first thing to stand out. Lining the walls in various frames, hung art pieces that stood out compared to the aging interior of The Spot."

        hide fin hospital with dissolve
        #Finn fades out
    else:
        ##MORGAN fades out

        hide morg hospital with dissolve
        "Morgan’s attitude was to be expected. Finn not being there was weighing on all of our minds."

        "However, her smile returned a moment later. She was trying to not let a single setback spoil every memory to come."

        "Looking around, it wasn’t a surprise that the artwork was the first thing to stand out. Lining the walls in various frames, hung art pieces that stood out compared to the aging interior of The Spot."

    #CG START

    scene black with dissolve
    "The artwork feels familiar, you’ve seen something like this before. But where?"

    #MORGAN fades in

    show morg hospital default at centerstage with dissolve
    morg "You know, I feel like we’ve seen this before."

    if act2_finn_success:

        show fin hospital at centerstage with dissolve:
            xpos 0.25
        fin "What do you mean?"

    else:
        #TERRIE enters stage right

        show ter hospital at centerstage with dissolve:
            xpos .75
        ter "Funny you say that. I wonder why."

    morg happy "Remember that one time we all almost got busted in senior year?"
    #CG END
    #Choice
    menu:
        "Ah, the infamous {i}Statue Incident.{/i} How could I forget?":
            scene sushishop with dissolve

            show morg hospital happy at centerstage with dissolve
            morg "Yes, that one! It didn’t get on the front page of our school paper for nothing."
        "I’m sure Terr remembers!":
            scene sushishop with dissolve
            #Terrie fades in

            show ter hospital inthought at centerstage with dissolve:
                xpos .75
            ter "The statue incident... Right?"
            #Terrie fades out
            #Morgan fades in

            hide ter hospital with dissolve

            show morg hospital happy at centerstage with dissolve
            morg "I knew you’d remember, Terr. It was kind of hard to miss with it making the school paper and all."
        "You’re gonna have to be more specific than that...":
            scene sushishop with dissolve

            show morg hospital playful at centerstage with dissolve
            morg "Surely it hasn’t been that long. Who could forget the statue incident that made the school paper?"

    morg inthought "Terr was a true mastermind. If it weren’t for them convincing the teacher that we didn’t break their precious statue, who knows what would have happened."
    #TERRIE looks away with a bashful smile on their face.

    if act2_finn_success:
        hide morg hospital with dissolve

        show fin hospital at centerstage with dissolve
        fin tense "It’s unthinkable how easily one can be blamed for others' tomfoolery."

        show fin hospital at centerstage:
            ease 0.4 yoffset 50
        fin inthought "Wrong place, wrong time, I suppose."

        hide fin hospital at centerstage with dissolve
    #Finn fades out
    #Terrie fades in

    show ter hospital aha at centerstage with dissolve

    ter "At least we made it here in time for dinner rush! Would’a sucked to be crammed in some lame fast-food chain after all that."

    if not act2_finn_success:

        show morg hospital inthought at centerstage with ease:
            xpos 0.25
        morg inthought "Oh, you know it. I can already picture how hangry Finn—"

        show ter hospital at centerstage with dissolve:
            xpos 0.75

        ter aha "I’m way more hangry than that guy, I want my good eats now!"
        #TERRIE fades out
        #MORGAN fades out

        hide morg hospital

        hide ter hospital

        with dissolve

        "It was hard to watch. Each attempt to reminisce was a dagger. A reminder of Finn and Mina’s lack of attendance."

        "That was a day to remember regardless. We always found a way to come here whenever we needed to retreat from the world."

        "After a few more attempts to recall more highschool shenanigans, we all settle in."

        "Something or someone needed to break the awkwardness that was forming."

        "It wasn’t long before we were met with a familiar face."
        #MIYA enters stage right

    else:

        "It was a day to remember. We always found a way to come here whenever we needed to retreat from the world."
        "After reminiscing about some highschool shenanigans, we all settle in."
        "It isn’t long before we’re met with a familiar face."

        hide ter with dissolve

        #Terrie fades in
        #Miya enters stage left

    show miya at centerstage with dissolve:
        xpos 0.9
    yum "...Morgan?"

    show miya at centerstage with ease:
        xpos 0.65
    yum "My, how long has it been now? 10 years?"

    show morg hospital playful at centerstage with dissolve:
        xpos 0.35
    #Morgan enters stage right
    morg "Oh come on now. A measly 10 months could never stop me."

    if act2_finn_success:
        #MIYA laughs

        #yum "You look so lively. Radiant, even."
        #yum "Are my eyes playing tricks on me? Is Finn here as well? It’s been so long! Just where have you been??"
        #Morgan fades out
        #Finn enters stage right
        #fin "It’s nice to see you too."
        #fin "I’ve been rather occupied with my studies, I apologize for not coming back sooner."
        #yum "You don’t have to be sorry for anything. You’re working so hard, just like Mina..."
        #Finn fades out
        #Morgan fades in

        yum "You look so lively. Radiant, even."
        yum "Are my eyes playing tricks on me? Is Finn here as well? It’s been so long! Just where have you been??"
        #Morgan fades out
        #Finn enters stage right

        hide morg hospital with dissolve

        show fin hospital happy at centerstage with dissolve:
            xpos 0.35
        fin "It’s nice to see you too."
        fin tense "I’ve been rather occupied with my studies, I apologize for not coming back sooner."
        yum "You don’t have to be sorry for anything. You’re working so hard, just like Mina..."
        #Finn fades out
        #Morgan fades in

        hide fin hospital with dissolve

        show morg hospital aha at centerstage with dissolve:
            xpos 0.35

    else:

        yum "You look…"

        "Miya chooses her words with care, her gaze full of affection and worry."

        yum "Better. You look well, Morgan. But something is troubling you, is it anything I can help with?"

        morg sad "Thank you, I’m fine. I mean—"

        # MORGAN (huffs)
        morg tense "Finn couldn’t join us today, and Mina is in a whole other state..."

        morg hurt "I’m beyond grateful that the three of us could come here, I just wish things could be different."

        "It ached to hear Morgan so heartbroken over this."

        yum "You’re all working very hard. Terrie has kept me up to date on Mina, I’d know."

    morg "Mina?"
    yum "Of course! Terrie told me all about her exciting move to LA, she has such a bright future ahead of her."
    #Morgan fades out
    #Terrie enters stage right
    #TERRIE gives their friends an apologetic smile.
    hide morg hospital aha with dissolve
    #Terrie enters stage right
    #TERRIE gives their friends an apologetic smile.

    show ter hospital happy at centerstage with dissolve:
        xpos 0.35
    ter "Okay, so. {i}Maybe{/i} I should’a told you guys I work here."
    #Terrie fades out
    #Morgan fades in

    hide ter hospital with dissolve

    show morg hospital playful at centerstage with dissolve:
        xpos 0.35
    morg "You think?"

    if act2_finn_success:
        hide morg hospital with dissolve

        show fin hospital inthought at centerstage with dissolve:
            xpos 0.35
        fin "It would have been nice to know."
    else:
        #MIYA enters stage left
        pass

    yum "I’m sure they didn’t mean to keep it from you all! Terrie’s just a little shy about their artwork."

    "Terrie groaned."

    hide miya 

    hide fin hospital
    
    with dissolve

    #Miya fades out
    #Morgan enters stage left

    if act2_finn_success:
        "Morgan and Finn lit up."
    else:
        "Morgan lit up a tiny bit."

    show morg hospital happy at centerstage with dissolve:
        xpos 0.35

    morg "Terrie, you did all this?"

    hide morg with dissolve

    show ter hospital tense at centerstage with dissolve
    #Morgan fades out
    #Terrie fades in
    ter "...Yeah."

    if act2_finn_success:
        #Finn enters stage right

        show fin hospital aha at centerstage with dissolve:
            xpos 0.75
        fin "Woah..."

    ter playful "I’m just an aspiring artist tryin’ to get my stuff out there."

    if act2_finn_success:
        fin happy "It truly is wonderful, Terrie. You’ve always had a gift for this kind of thing."
    else:

        show morg hospital happy at centerstage with dissolve:
            xpos 0.25
        morg "It truly is wonderful, Terrie. You’ve always had a gift for this kind of thing."

    ter aha "What are you talking about?"
    ter tense "Please, save the praise for someone who’s actually worth it. "

    if act2_finn_success:

        hide fin with dissolve

        show morg hospital sad at centerstage with dissolve:
            xpos 0.75

        #Finn fades out
        #Morgan enters stage right
        pass

    morg sad "You have just as much a right to praise as anyone else. "
    ter hurt "Is it really worth that much if I’m still {i}stuck{/i} here—"
    morg aha "What, you mean in the restaurant?"
    #Morgan fades out
    #Miya enters stage right

    hide morg with dissolve
    show miya at centerstage with dissolve:

        xpos .75
    yum "Terrie... You can’t really think that, can you?"
    ter sad "I guess? Sorry, I know it’s kind of pathetic. If only I worked a little harder, maybe I’d be in art school by now."
    #Miya fades out
    #Finn enters stage right

    hide miya with dissolve

    show fin hospital happy at centerstage with dissolve:
        xpos 0.75
    fin happy "It’s not too late, you still have time."
    #Finn fades out
    #Morgan fades in

    hide fin hospital with dissolve

    show morg hospital happy at centerstage with dissolve:
        xpos 0.75
        subpixel True 
        yoffset 30 xpos .75
        spring3 .5 yoffset 0
    morg "You’ve been working your butt off! There’s no way you won’t succeed, Terr."
    #Morgan fades out
    #Miya fades in

    hide morg hospital with dissolve
    #Morgan fades out
    #Miya fades in

    show miya at centerstage with dissolve:
        xpos .75
    yum "Both you and your work is appreciated here. It always will be."
    "Terrie sighed."

    show ter hospital tense at centerstage:
        ease 0.4 yoffset 0
    ter "You speak too highly of me, really."
    ter sad "My stuff just isn’t “woah” material, you know?"
    yum "Oh, that’s not true at all. I think you’re blind to the admiration surrounding you."
    yum "You work too hard, you’re nearly just as bad as Finn."

    if not act2_finn_success:
        #MIYA fades out
        #TERRIE fades out

        hide miya
        hide ter

        with dissolve
        "The room seemed to freeze for a second. Despite one less person being there, their lack of presence was being felt the whole time."
        #TERRIE enters stage right

        show ter hospital hurt at centerstage:

            xpos .75
        ter "Hey! I’m {i}way{/i} better than Finn, at least I’m actually here."
        ter tense "I’ve been good about giving myself time off, unlike those two."
 
        #MORGAN enters stage left

        show morg hospital sad at centerstage with dissolve:
            xpos .25

    else:
        ter aha "What? Fat chance! I’m {i}way{/i} better than Finnster, here."
        ter tense "I’ve been good about giving myself time off, unlike a certain someone."

        hide miya with dissolve

        show ter hospital tense at centerstage with ease:
            xpos .65

        show morg hospital sad at centerstage with dissolve:
            xpos .35

    #Miya fades out
    #Morgan fades in

    "Morgan looked distant."

    if act2_finn_success:
        morg sad "I wish she could be here."

        hide ter with dissolve

        show morg hospital sad at centerstage with ease:
            xpos .65
        #Terrie fades out
        #Finn enters stage left

        show fin hospital melancholy at centerstage with dissolve:
            xpos .35
        fin "I’m sure she wishes that too."
        #Morgan fades out
        #Finn fades out
        #Miya fades in

        hide fin with dissolve

        show miya at centerstage with dissolve:
            xpos .35
        yum "You’re all such hard workers, Mina’s out here making a living just by being her authentic self. I’m sure you’ll do just the same."
        #Terrie enters stage right

        hide miya with dissolve

        show ter hospital inthought at centerstage with dissolve:
            xpos .35
        ter "I’m doing my best."
        yum "Yet despite all of that, you work harder than almost anyone else I know. That’s why you’re here, right?"

    else:
        morg sad "I wish both could be here."

        hide ter with dissolve

        show morg hospital sad at centerstage with ease:
            xpos .65
        #TERRIE fades out
        #MIYA enters stage right

        show miya at centerstage with dissolve:
            xpos .35
        yum "Morgan. You’re all such hard workers, Mina’s out here making a living just by being her authentic self. Finn as well. I’m sure you’ll get that chance to be together again."

        yum"And Terrie."

        hide morg with dissolve
        #MORGAN fades out
        #TERRIE enters stage right

        show ter hospital tense at centerstage with dissolve:
            xpos .65

        ter "I’m doing my best, but clearly it isn’t good enough. Most would’ve called it quits by now."

        # MIYA (happy)
        yum "And yet? You haven’t. You work harder than almost anyone else I know. That’s why you’re here, right?"

    ter "Right. It is why I’m doing my best to earn enough to attend art school. To have art worthy of being praised by everyone."

    # Mina (chuckling)
    yum "Well, young Terr. Success is something that requires many things. Persistence goes a long way. It is why I continue to endure despite the tough times."
    #Terrie fades out
    #Morgan enters stage right
    morg "Tough times?"
    yum "This isn’t as inviting as it used to be, Morgan."
    yum "Prices continue to rise. Sales continue to fall. Even my spirit is starting to wane..."
    yum "I just hope I can pay this month’s bills."
    #Miya fades out
    #Morgan fades out

    if act2_finn_success:
        "A tense silence filled the room, the once cheerful mood gone. Just then, Morgan stood up from her seat."
        #Morgan fades in

        show morg at centerstage with dissolve
        morg "I have a brilliant idea!"
        morg "Why don’t we have Mina pull some strings to reel in some customers? We can even help with the dinner rush!"
    else:
        "Another tense silence filled the room, the small wave of peace snuffed out in an instant. Just then, Morgan stood up from her seat."
        #MORGAN enters stage left
        morg "No. I won’t let this memory be ruined anymore. I have an idea..."
        morg "Why don’t we have Mina pull some strings to reel in some customers? That’s sure to get Miya the help she needs, we can even help with the dinner-rush."

    #Terrie enters stage right
    ter "Dude. You’re a {i}genius.{/i} Has anyone ever told you that, Morgs?"
    ter "Someone get this girl a damn phone, we got an influencer to ring up!"
    #Terrie fades out
    #Finn enters stage right
    fin "I’m not sure my sister would approve of this, but it doesn’t hurt to try."
    fin "However, if Mina is on board, I have no doubt success awaits us."
    morg "Let’s give her a ring."
    #Morgan fades out

    hide fin

    hide ter

    hide morg

    with dissolve

    #Finn fades out or Terrie fades out if Finn not there

    if act2_finn_success:
        "We waited in anticipation as Finn dialed her number. It only took a single ring before an all-too familiar voice came out through the phone’s speaker."

        show screen minaphone
        show mina_chibi default at minachibi_transform, minaphone_pos with dissolve:
            xoffset 10
            additive .1
            matrixcolor ContrastMatrix(1.2)
            pause .15
        #Mina enters stage right
        mina "At long last, my precious brother has finally gotten in contact with me after {i}years{/i} of neglect..."
        #Finn enters stage left
        fin "It has been one week."
        mina "Exactly!"
        mina "Fear not, your favorite sister is here for you. What’s going on in Finn-land?"
        "Finn groaned, running a hand down his face."
        fin "Only sister does not translate to favorite."
        mina "Awww, you’re so mean! You’re still my favorite, even after you totally tr—"
        fin "{i}Mina—{/i} You’re on speaker."
        fin "I’m with Morgan and the others, we’re at Miya’s."
        mina "Oh, for reals? Hello to my favorite people in the whole wide world! How’s it hanging?"
        #Finn fades out
    else:
        "We waited in anticipation as I dialed her number. It only took a single ring before an all-too familiar voice came out through the phone’s speaker."
        #MINA enters stage right
        mina "Who would this happen to be? A salesman? Perhaps a long lost relative or oil prince? "
        #MORGAN enters stage left
        morg "Awww, you’re so mean! How could you forget us?"
        "Mina, you’re on speaker. I’m here with the others."
        mina "Oh, for reals? Hello to my favorite people in the whole wide world! How’s it hanging?"

    #Morgan enters stage left
    morg "Hi Mina, I have a favor to ask. Do you mind helping us advertise Miya’s?"
    mina "No way, The Spot?"
    mina "That place brings back so many memories! It feels like forever ago... I can’t believe I’m missing this nostalgia trip right now!"

    if act2_finn_success:
        mina "Ugh, I don’t know if it really fits my brand though..."
    else:
        mina "Finn probably loves this place more than I do. Where is he anyways?"
        #Pause
        "The silence speaks for itself."
        mina "Ugh. That’s so like him. [i]The nerve.[/i] Not that I’m any better."
        "Mina shifted uncomfortably."
        mina "Anyway, I don’t know if it really fits my brand..."

    #Morgan fades out
    #Terrie enters stage left
    ter "C’mon, Mina! It’s a cozy sushi place that THE Mina used to frequent all the time. There’s no way people won’t jump at the chance to eat here!"
    "Mina hummed in thought."
    #Terrie fades out
    #Finn enters stage left
    fin "You don’t have to do anything you don’t want to, Mina."
    #Finn fades out
    #Miya enters stage left
    yum "Of course! It’s more than enough just to hear from you, please don’t trouble yourself with something like this."
    #Miya fades out
    mina "That settles it."
    mina "You guys just scored a super free and super AWESOME sponsorship from yours truly!"
    #Morgan enters stage left
    morg "Really? I’m touched, really. But is it okay?"
    if act2_finn_success:
        mina "Oh, stop it. I love my friends and I’m gonna do everything I can to help you guys out! Have fun today, alright?"
    else:
        mina "Oh, stop it. I love my friends and I’m gonna do everything I can to help you guys out! Not to mention my no-show brother must be hampering the mood."

        mina "Just remember. Above all else, make sure you all have fun!"

    morg "...Alright."

    if act2_finn_success:
        morg "Thank you. Truly."
    else:
        #Pause
        morg "Mina, thank you. {i}Truly.{/i}"

    mina "Make it count, you guys got this in the bag. See you later, lots of love!"

    show mina_chibi at minachibi_transform, minaphone_pos:
        xzoom 1 yzoom 1 alpha 1 matrixcolor BrightnessMatrix(0.0)
        easeout .2 xzoom 0 yzoom 1.2 matrixcolor BrightnessMatrix(0.3)
        parallel:
            easeout .2 alpha 0
    pause .1
    hide screen minaphone with dissolve
    pause .25
    #Mina fades out
    "The moment Mina hung up, the group turned to Morgan, who was now brimming with excitement."
    morg "Alright, we’ve got work to do. But before we do anything, we need to pick out jobs!"
    #Terrie enters stage right
    ter "Oh, oh! Let me be the waiter {i}please.{/i} I’m uber experienced, they’ll give us mad tips thanks to my mad skills."

    if act2_finn_success:
        morg "It’s all yours. Finn, how would you feel about manning the front counter and acting as our host?"
        #Terrie fades out
        #Finn enters stage right
        fin "I get to work with the register, that sounds perfect to me."
        #Finn fades out
        #Miya enters stage right
        yum "You know where I’ll be. Though, it would be nice if someone could help me bring out orders to customers."
        morg "You can count on me."
    else:
        morg "It’s all yours. It’d be nice to have someone not here manning the front counter and acting as our host, but beggars can’t be choosers. I shall handle that front instead!"

    morg "How does dishes sound to you? I hope it’s not too boring."
    "I was born to scrub."
    #Miya fades out
    #Terrie enters stage right
    ter "You better be. If those dishes pile up, we’re screwed. We believe in you, dude!"
    ter "Thanks for being on top of things, everyone. Any questions before we get trampled by Mina’s fans?"
    morg "Nope, I’m ready to go. I’ll give it my all!"

    hide ter with dissolve
    #Terrie fades out

    if act2_finn_success:
        #Finn fades in
        fin "I’ll do my best to utilize my skills to get customers situated."

        hide fin with dissolve
        #Finn fades out

    #Morgan fades out

    hide morg with dissolve
    "With no questions on my end, Morgan responded with a firm nod."
    "Perhaps my job of washing dishes was simple, but every cog in this machine was important."
    "Thus began a service like no other."

    #Order Taking Mini Game Start

    #Terrie enters stage left
    #Group 1
    "Customer 1" "Can I get the Yummy Yam Roll?"
    "Customer 2" "I would like the Dragon Roll. I’m also allergic to shellfish."

label act3_customer_minigame_group1_q1:
    #Miya enters stage right
    yum "What did customer one want?"
    #terrie is the one choosing options, their sprite will take priority in this minigame along with miya's.
    menu(timeout_label="act3_customer_minigame_group1_q2"):
        "BC Roll":
            $ act3_customer_minigame_group1["q1"] = False
        "Dragon Roll":
            $ act3_customer_minigame_group1["q1"] = False
        "Yummy Yam Roll":
            $ act3_customer_minigame_group1["q1"] = True

label act3_customer_minigame_group1_q2:

    if "q1" not in act3_customer_minigame_group1.keys():
        $ act3_customer_minigame_group1["q1"] = False

    yum "What did customer two want?"

    menu(timeout_label="act3_customer_minigame_group1_q3"):
        "Dragon Roll":
            $ act3_customer_minigame_group1["q2"] = True
        "BC Roll":
            $ act3_customer_minigame_group1["q2"] = False
        "Shrimp Tempura roll":
            $ act3_customer_minigame_group1["q2"] = False

label act3_customer_minigame_group1_q3:

    if "q2" not in act3_customer_minigame_group1.keys():
        $ act3_customer_minigame_group1["q2"] = False

    yum "Any allergies?"

    menu(timeout_label="act3_customer_minigame_group1_q4"):
        "Yes":
            $ act3_customer_minigame_group1["q3"] = True
        "No":
            $ act3_customer_minigame_group1["q3"] = False

label act3_customer_minigame_group1_q4:

    if "q3" not in act3_customer_minigame_group1.keys():
        $ act3_customer_minigame_group1["q3"] = False

    yum "Who has an allergy and what is it?"

    menu(timeout_label="act3_customer_minigame_group1_result"):
        "Customer one has a shellfish allergy.":
            $ act3_customer_minigame_group1["q4"] = False
        "Customer one has a ginger allergy.":
            $ act3_customer_minigame_group1["q4"] =False
        "Customer two has a shellfish allergy.":
            $ act3_customer_minigame_group1["q4"] =False

label act3_customer_minigame_group1_result:

    if "q4" not in act3_customer_minigame_group1.keys():
        $ act3_customer_minigame_group1["q4"] = False

    ter "Here's your order!"
    #Miya fades out

    if act3_customer_minigame_group1["q1"]:
        "Customer 1" "Ah this looks great, thanks!"
    else:
        "Customer 1" "Wait… I wanted the Yummy Yam Roll! Please take this back."

    if not act3_customer_minigame_group1["q2"]:
        "Customer 2" "Come on. This isn’t the right roll. Take it back."
    elif act3_customer_minigame_group1["q3"] and act3_customer_minigame_group1["q4"]:
        "Customer 2" "No shellfish, right? Thank you very much."
    else:
        "Customer 2" "Is that shellfish? I said I was allergic. Take it back."

label act3_customer_minigame_group2:
    #Group 2
    "Customer 3" "Can I get the Shrimp Tempura roll? Also, I’m allergic to ginger."
    #Customer four
    "Customer 4" "I would like the BC Roll."
    # Customer five
    "Customer 5" "The Yummy Yam Roll please!"

label act3_customer_minigame_group2_q1:
    #Miya enters stage right
    yum "What did customer three want?"

    menu(timeout_label="act3_customer_minigame_group2_q2"):
        "Yummy Yam Roll":
            $ act3_customer_minigame_group2["q1"] = False
        "BC Roll":
            $ act3_customer_minigame_group2["q1"] = False
        "Shrimp Tempura roll":
            $ act3_customer_minigame_group2["q1"] = True

label act3_customer_minigame_group2_q2:

    if "q1" not in act3_customer_minigame_group2.keys():
        $ act3_customer_minigame_group2["q1"] = False

    yum "What did customer four want?"

    menu(timeout_label="act3_customer_minigame_group2_q3"):
        "Dragon Roll":
            $ act3_customer_minigame_group2["q2"] = False
        "Shrimp Tempura roll":
            $ act3_customer_minigame_group2["q2"] = False
        "BC Roll":
            $ act3_customer_minigame_group2["q2"] = True


label act3_customer_minigame_group2_q3:

    if "q2" not in act3_customer_minigame_group2.keys():
        $ act3_customer_minigame_group2["q2"] = False

    yum "What did customer five want?"

    menu(timeout_label="act3_customer_minigame_group2_q4"):
        "BC Roll":
            $ act3_customer_minigame_group2["q2"] = False
        "Yummy Yam Roll":
            $ act3_customer_minigame_group2["q2"] = True
        "Shrimp Tempura roll":
            $ act3_customer_minigame_group2["q2"] = False

label act3_customer_minigame_group2_q4:

    if "q3" not in act3_customer_minigame_group2.keys():
        $ act3_customer_minigame_group2["q3"] = False

    yum "Any allergies?"

    menu(timeout_label="act3_customer_minigame_group2_q5"):
        "Yes":
            $ act3_customer_minigame_group2["q4"] = True
        "No":
            $ act3_customer_minigame_group2["q4"] = False

label act3_customer_minigame_group2_q5:

    if "q4" not in act3_customer_minigame_group2.keys():
        $ act3_customer_minigame_group2["q4"] = False

    yum "Who has an allergy and what is it?"

    menu(timeout_label="act3_customer_minigame_group2_result"):
        "Customer three and it’s a ginger allergy.":
            $ act3_customer_minigame_group2["q5"] = True
        "Customer four and it’s a ginger allergy.":
            $ act3_customer_minigame_group2["q5"] = False
        "Customer five and it’s a shellfish allergy.":
            $ act3_customer_minigame_group2["q5"] = False

label act3_customer_minigame_group2_result:

    #Miya fades out
    ter "Here’s your orders!"

    if not act3_customer_minigame_group2["q1"]:
        "Customer 3" "Hey! This isn’t what I ordered! Take it back."
    elif not (act3_customer_minigame_group2["q4"] and act3_customer_minigame_group2["q5"]):
        "Customer 3" "What are you doing? I said I have a ginger allergy and there’s ginger on the plate. Take it back. Immediately."
    else:
        "Customer 3" "You made sure to remove the ginger, right? Phew. Thank you."

    if act3_customer_minigame_group2["q2"]:
        "Customer 4" "Ah. That looks perfect. Thanks!"
    else:
        "Customer 4" "Eh… This is not what I asked for. Can you take it back?"

    if act3_customer_minigame_group2["q3"]:
        "Customer 5" "This looks like a ten out of ten. Amazing."
    else:
        "Customer 5" "Uh… I’m pretty sure I ordered the Yummy Yam Roll. Can you take it back?"

    #Mini Game End

    #terrie fades out
    "With the hustle and bustle of the evening fading away, what was left was the fruits of our labor."

    if check_act3_minigame_success():
        # if act2_finn_success:
            ##SCENE THE SPOT - SPECIAL CG with dissolve
        # else:
            # THE SPOT - DAY

        "All of us stood proudly together as one. The night was a clear success, and the Miya was filled with joy."

        #Miya enters stage right
        # Miya (happy)
        yum "I cannot thank you enough for everything. This certainly will keep us afloat for a good while."
        # Miya (overjoyed)
        yum "This calls for our own feast to celebrate!"
        #Miya fades out

        "We soon began setting up one final table. One filled with everything we could ever want."
        "As we began absorbing the moment, Morgan spoke up, exuding an energy that didn’t fit the mood."

        #Morgan enters stage left

        if act2_finn_success:
            #MORGAN smiles
            morg "This is truly going to be a meal worth dying for. It’s a meal that we all earned through our hard work and effort."

            morg "This might be one line on my list, but it means the world to me. Thank you everyone… for being here."

        else:

            "A rather negative energy."

            #Morgan (neutral)
            morg "This should have been the perfect moment… A meal that we all worked hard to eat."
            #Morgan (sad)
            morg "We might have had a successful night, but…"
            #Morgan (sad)
            morg "I wish Finn was here to share it with us."

    else:
        # THE SPOT - CORRIDOR
        "And so, the service came to a close. It was hard to call it a success."
        "In fact, it felt as if the restaurant was worse off than when we started."
        #Miya enters stage right
        #Miya (Disappointed)
        yum "I appreciate the effort everyone… truly."
        # Miya (Disappointed) (cont’d)
        yum "Perhaps this might be a minor setback, but it was great seeing you all try your best. That’s what matters."
        #Morgan enters stage left
        # Morgan (sad)
        morg "I’m so sorry… I know we did our best, but… I guess it was too much for us."
        #Morgan exits
        "Terr remained silent, thinking about how this was another failure he had to deal with."

        if act2_finn_success:
            #MIYA fades out
            #FINN enters stage left
            fin "I’ll… apologize to my sister later for wasting her effort."
            #FINN fades out

        else:
            "I’d have to apologize to Mina later on."

    #Branches merge
    # THE SPOT - DAY
    "As things settled down, the Miya retreated into the back and came back moments later with a full platter of food for everyone."
    #Miya enters stage right
    #Miya (smiling)
    yum "All of you did your best today, thank you so much for all that you’ve done. Please enjoy."
    #Miya fades out
    #Morgan enters stage left
    morg "Thank you for letting us do this."
    #Terrie enters stage right
    ter "No need to get all mushy on us now, Morgan. We all wanted to do this!"

    if act2_finn_success:
        #TERRIE fades out
        #FINN enters stage left
        fin "Terrie is right, I enjoyed this a lot more than I anticipated."

    "Morgan let out a sigh of relief."

    morg "I’m so glad."
    #Morgan fades out
    #Terrie fades out

    if not act2_finn_success:
        "As if on cue, my phone began to ring."
        "It was Mina. I gave her the news."

    #MC picks up, and is greeted by Mina letting out either a happy squeal or disappointed sigh.
    #Mina enters stage right

    if check_act3_minigame_success():
        #If Minigame is Successful
        #Mina (happy)
        mina "Aaah, you guys! I’m getting tagged in so many posts right now, you have no idea. Whatever magic you guys conjured up is WORKING!"

        "A wave of relief washed over everyone."

        #Mina (happy)(cont’d)
        mina "Hopefully it isn’t too much for Miya to handle. I know Terr is there, but you can never underestimate the power from a rising star!"

        if act2_finn_success:
            #FINN enters stage left
            fin "You wish. They’re only coming back because the food is just that good."

            mina "Nuh-uh! They’re definitely coming back thanks to me and my cute lil’ face. You owe me!"

            fin "Sure."
            #FINN fades out

    else:
        #If Minigame is Unsuccessful
        #Mina (disappointed)
        mina "You guys… I’m getting tagged in a lot of posts. There’s a lot of people complaining about mistakes."
        # Mina (disappointed)(cont’d)
        mina "Hopefully it isn’t too much for Miya to handle. I know Terr is there, but…"

        "I could see Morgan wanting to apologize, but was surprised to hear what she said next."

    #Branch Merge

    #Morgan enters stage left
    morg "What you did really made an impact Mina, thank you."
    mina "Morgan..."

    "Mina paused, carefully picking her words."

    mina "I’m sorry I can’t be there. I truly hope this helps make up for me not being with you guys..."

    menu:
        "It does. You really helped us out here, Mina.":

            #Mina (happy)
            mina "Yay! Glad to be of service, anything for the gang. Especially you, Morgan."

        "As long as Morgan is happy, I’m happy.":
            mina "Same here! Pretty sure we’re all in the same boat about that."
            # Beat.
            #Mina (concerned)
            mina "Morgan?"

        "I really wish you could have been here.":
            #Mina (apologetic)
            mina "Believe me, I would be there in a heartbeat."
            mina "You don’t even know the half of it..."

    #Branch Merge
    "Morgan closed her eyes, finding the courage to speak how she truly felt."
    #Morgan (grateful)
    morg "Thanks for everything Mina. Without your help, this wouldn’t have been possible."
    #Morgan (happy)
    morg "I know you might feel bad about being unable to be here in person, but I’m glad you got to play a part."
    mina "Morgan... You know I’d give anything to be with you all again."
    mina "The limelight is amazing, it’s been my biggest dream, I’ve done so much to make this possible."
    mina "However, it doesn’t mean that I’d give up everything for it."
    # Mina (sad) (cont’d)
    mina "The world of content creation is rough, everyone’s at each other’s throats. Fame and fortune is the only thing that matters to them. Most bonds you see online are just from fancy connections."
    morg "Mina..."
    mina "However, what we all share is different. All of you mean the world to me. Even if I can’t be there to share this moment of success... know this. I’m happy that the bond we all share is still just as strong as the day I took a step towards my dream."
    morg "Thank you, Mina. I really appreciate everything."
    mina "Good luck with finishing off the list, I’ll be rooting for you from all the way out here!"
    #Mina fades out
    "With that, Mina hung up."
    #Terrie enters stage right
    ter "I miss her already."

    if act2_finn_success:
        #FINN enters stage right
        fin "I don’t."

        ter "Okay liar liar pants on fire, no need to be a tough guy around us."

    ter "...So, now that we’ve had some fine dining, what’s next on the list?"

    # if act2_finn_success:
        #FINN fades out
        #MORGAN enters stage right
        #TERRIE fades out

    morg "We still have plenty of runway."
    # Morgan (reading list)

    if act2_finn_success:
        morg "Let’s see... Oh! We can either have the performance of a lifetime, or get married! I’m down for either."
        ter "Marriage huh? Well, I guess that’s certainly a bucket list worthy thing."
        #FINN enters stage left
        fin "I’m certain this can only go well."
        #FINN fades out
        #MORGAN fades out
        #SCENE THE SPOT - CORRIDOR with dissolve
        "We began to debate which choice to make. Both were memorable in their own way. However, we ended up deciding on..."
        #MORGAN fades in
        menu:
            "A performance of a lifetime!":

                morg "I’m ready for all of us to show the world our talent!"

                jump act3_performance

            "Time to get married.":

                $ act3_next_action = "marriage"

                morg "Who wants to get married?"
                #Comically long beat.

                fin "In jest, right?"
                morg "No, for real."
                morg "And also for the tax benefits."
                morg "It's right here on the list, see? Pledge the rest of my life to somebody dear."

                #TERRIE reading

                ter "Pledge... life... somebody dear... "

                #TERRIE normally

                ter "Damn, you really went there! "
                ter "Well which one of us electable"
                ter "—eligible bachelors are you gonna pick, Ms. Soon-To-Be-Mrs. Bride"

                morg "Hmm... I have a way to weed out the competition."
                morg "We're off to the fairgrounds. Last one there's the ordaining minister,three two one go!"

                #Pop out MORGAN, then TERRIE one second later.

                fin "Hey, unjust competitive ruleset!"

                "And so, by the power vested in me…"

                "I pronounced myself ‘Not Coming in Last’ and got the heck out of there."

                ##ALL EXIT

                jump act5

    else:

        morg "Let’s see... there’s a performance of a lifetime or..."

        "Morgan’s smile disappeared for a second before returning."
        #Morgan (smiling)
        morg "Let’s go with that. A performance to show the world what we got."
        # Terrie (happy)
        ter "Attagirl, We’ll knock everyone’s socks off with a performance they’ll never forget."
        #Terrie fades out
        #Morgan fades out

        jump act3_performance

label act3_performance:

    $ act3_next_action = "performance"

    # THE SPOT - CORRIDOR
    "Without further delay, we were off once again."
    "Time was slowly catching up to us, we were doing everything we could to finish strong."
    "It had to be the best it could be. To ensure Morgan had a performance worth remembering."

    if not act2_finn_success:
        "There was no room for error."

    #All exit

    jump act4
