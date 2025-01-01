    #FADE IN
    #INT. FINN'S DORM AREA - DAY
    #NARRATOR FADE IN:
label act2:
    scene dorm with dissolve
    show fin hospital default at centerstage with dissolve

    "Believe it or not, Finn's living space was in surprisingly good shape for a struggling college student."
    $ play_music(finn_dorm,5)
    "Really nice place. Not a single cup, can or bottle in sight."
    "Well, in the common area, at least. Who knew what things were hiding on the other side of the door?"
    "All three of us were hoping we'd be able to find out. As long as Finn was all ears, of course."
    show fin inthought at centerstage with dissolve
    ter "Guys, what if he's just ignoring us?"
    morg "You simply keep knocking until he can't ignore it anymore."
    show fin tense at centerstage with dissolve
    ter "Believe me, you give that man a thick textbook and a pair of headphones and he could miss the end of the world."
    ter "Love that guy, personally, but I wouldn't put it past him."
    ter "Unless, maybe..."
    show fin aha at centerstage with dissolve
    ter "PIZZA'S HERE, DUDE!"
    show ter hospital happy at centerstage with moveinleft
    show fin default at centerstage:
        xpos .5
        ease 1 xpos .75
    fin "I did inform you I would be occupied."
    ter playful "Good to see you too, Finn!"
    ter "What are we studyin' today? A dash of Chem? Some Bio? A bit of both?"
    fin inthought "Well, you see, I {i}could{/i} be, however..."
    ter aha "Hey, don't give me that pointer finger!"
    fin default "I apologize."
    fin "I really doubt any of you could comprehend the sheer magnitude of work I’m doing right now."
    fin tense "Examinations and such, if you remember how those felt."
    ter happy "Oh, c'mon, Finn, is there anything you don't know at this point?"
    ter hurt "Just remember that the mitochondria is the powerhouse of the cell and then you're golden!"
    fin "Actually, the mitochondria produces ATP as a means of storing chemical potential—"
    ter playful "SEE?! That's exactly my point! You're good! You're done for the day!"
    show morg hospital happy at centerstage with moveinleft:
        xpos 0
        xpos .25
    morg "Terr's right. Live a little."
    #tense beat
    fin default "Morgan."
    fin "You're looking... spirited."
    morg default "Likewise."
    "Awkward silence fills the room."
    fin inthought "I truly do require maximum focus."
    fin tense "My major examination is mere days away, and I can't afford to waste even a second outside of my allotted breaks."
    morg sad "Your breaks of... what, ten minutes each, I'm guessing?"
    ter inthought "Yeah, that's gonna fry your brain no matter how ya look at it! You need some'a that crisp winter air in your lungs."
    ter "Which you definitely shoulda known, mister doctor."
    $ Failstate = 'finnlament'
    menu:
        "So, what, you don't do friends anymore?":
            jump coldshoulder
        "We’ll study with you, then.":
            jump studydate
        "If you were sick, what would you want from us?":
            jump sick

label coldshoulder:
    fin default "Not during work hours, as has been the case since high school, anyway!"
    fin upset "If you all are so desperate for my company, try waiting several hours!"
label studydate:
    fin tense "Would you {i}really?{/i} On the one day you all have the time for each other?"
    ter default "And for you, Finn. That always includes you."
label sick:
    fin inthought "But I'm not ailing currently, am I? I wouldn't take offense from you trying to get by."
    morg playful "Density is not a good look on you, Finn."


label finnlament:
    fin inthought "...Even with everything said and done, it's far from that simple, I fear."
    fin tense "Morgan. Think back to your initial diagnosis."
    fin "How rare did they tell you it was to encounter a tumor of the heart?"
    #beat
    morg sad "Unfathomably rare."
    fin "Nearly a thousandth of a percent. A {i}thousandth.{/i} It's totally not fair."
    morg "As I've come to accept these past few months, yes."
    fin upset "But {i}I{/i} can't accept it!"
    fin melancholy "If you hold on and your condition stays stable for a while longer, and I remain on track with my studies... I can aid you."
    fin inthought "And if not you, then whomever else in need!"
    morg "I've held on long enough, Finn."
    morg "Today, the best cure you can give me is a day of your time."
    fin tense "After which I shall still need to study... and you will still remain sickly."
    ter tense "Oh, for God's sake, Finn, this girl stood up for the first time in months to come say hi to us!"
    ter "You should have seen it! Or is it gonna take more to convince you, huh?"
    #MINIGAME START
    $game_player.addRelationship("Morgan")

label minigame1q1:
    $Morgan = game_player.getRelationship("Morgan")
    $ Minigame1 = True
    ###Defined at script.rpy, this is where you go if you fail to select a choice before the timer expires
    $ Failstate = 'minigame1q2'
    menu:
        "What will you be doing today that absolutely needs me to be there?"

        "No idea... BUT, nobody has an eye for putting together a plan like you, Finn.":
            $Morgan = game_player.getRelationship("Morgan")
            $game_player.increaseRelationship("Morgan",1)
            jump minigame1q2
        "I need help with my homework, like URGENTLY.":
            jump minigame1q2
        "Oh, y’know, just hanging out. Nothing special.":
            jump minigame1q2

label minigame1q2:
    $ Failstate = 'minigame1q3'
    menu:
        "Why aren’t you out having fun already?"

        "Wherever we think you’d like to go isn’t open yet.":
            jump minigame1q3
        "Because we actually care about you enough to be here! No jokes!":
            jump minigame1q3
        "What do you mean?! This is fun!! I missed back-and-forth tussles like these.":
            $Morgan = game_player.getRelationship("Morgan")
            $game_player.increaseRelationship("Morgan",1)
            jump minigame1q3

label minigame1q3:
    $ Failstate = 'minigame1q4'

    menu:
        "If I fail, how will you repay me?"

        "You’re not going to fail, you’re a genius!":
            jump minigame1q4
        "We’ll all collectively cover all of your extra credit work for a month.":
            jump minigame1q4
        "$200. Take it or leave it.":
            $Morgan = game_player.getRelationship("Morgan")
            $game_player.increaseRelationship("Morgan",1)
            jump minigame1q4

label minigame1q4:
    $ Failstate = 'minigame1q5'

    menu:
        "How are you going to scare me out of the dorm?"

        "Make him jump":
            jump minigame1q5
        "See this medical textbook? See that window? I’d hate to make the two meet.":
            jump minigame1q5
        "We’re calling Mina and telling on you.":
            $Morgan = game_player.getRelationship("Morgan")
            $game_player.increaseRelationship("Morgan",1)
            jump minigame1q5

label minigame1q5:
    $Morgan = game_player.getRelationship("Morgan")
    if Morgan <3:
        $ Failstate = 'minigame1failure'
    elif Morgan <=3:
        $ Failstate = 'minigame1success'
    menu:
        "What if I simply decide to stay in?"

        "One by one, you’re gonna find those bottles on your shelf sloooowly get emptier.":

            $Morgan = game_player.getRelationship("Morgan")

            if Morgan >= 3:
                #"DEBUG" "Success"
                $ Minigame1 = False
                jump minigame1success
            else:
                #"DEBUG" "Failure"
                $ Minigame1 = False
                jump minigame1failure
        "We’ll stay in the common area and act loud and annoying. Can’t study peacefully with the source of the problem, can you?":

            $game_player.increaseRelationship("Morgan",1)
            $Morgan = game_player.getRelationship("Morgan")

            if Morgan >= 3:
                #"DEBUG" "Success"
                $ Minigame1 = False
                jump minigame1success
            else:
                #"DEBUG" "Failure"
                $ Minigame1 = False
                jump minigame1failure

        "Let’s get the dean on the line. He’d hate to hear that a star student’s got a poor work ethic.":

            $Morgan = game_player.getRelationship("Morgan")

            if Morgan >= 3:
                #"DEBUG" "Success"
                $ Minigame1 = False
                jump minigame1success
            else:
                #"DEBUG" "Failure"
                $ Minigame1 = False
                jump minigame1failure
    #"DEBUG" "you have %(Morgan)d points."


init:
    ##FinChibi Transform
    transform finchibi_transform:
        xpos .75
        ypos .25
        xanchor .5
        yanchor .5
        zoom .25
label minigame1success:
    fin melancholy "Alright, I yield."
    #TERRIE and MORGAN sigh with relief
    fin "How opportune is this line-up of friends outside my door, indeed?"
    fin inthought "Once more, I apologize. To you especially, Morgan."
    fin happy "It's good to see you again."
    morg playful "Likewise. Don't sweat it, mister doctor."
    ter playful "D'aww, it's enough to grow my heart three sizes!"
    fin playful "So. Now that the doctor is metaphorically “in,” I suppose it's time to recount the grand agenda."
    fin inthought "Which we can find on Morgan's, uh..."
    morg happy "My bucket list! Congratulations on being the first item of order, by the way."
    fin happy "Hooray?"
    morg inthought "Of course hooray. Now, you were awfully quick to open the door at the promise of pizza."
    fin default "A lot of time has passed since my last meal. Why do you ask?"
    ter happy "Well, we all know how being hangry can—"
    "Finn's stomach audibly growls."
    fin tense "Ah."
    ter "We can do you one better than pizza, though. Remember Miya's?"
    fin melancholy "The petite little sushi establishment. Of course..."
    fin happy "That'll do. That'll do nicely."
    fin playful "The holidays have definitely imbued you with nostalgic joy, eh, Morgan?"
    "Morgan's smile turns Knowingly Melancholic."
    morg sad "What can I say, it's a time for family..."
    ter playful "Couldn't have said it better myself, guys!"
    ter "What are we waiting for, then?! Item Two: Eat a Meal Worth Dying For!"
    ter "Miya's here we come!"
    hide ter with moveoutleft
    fin inthought "By the way, Morgan, about your sudden need to come and visit..."
    #beat
    fin "Mina didn't put you up to this, did she?"

    menu:
        "I wouldn't exactly say it was Mina...":

            fin inthought 'Hm. Logically, out of everybody in the world, I cannot guess anyone important enough.'

            fin playful 'Besides your parents, that is, Morgan. Do I know this mystery person?'

            morg tense 'I’d hope not.'
            return


        "Oh, you wish.":

            fin happy "Perhaps I do. Despite her gallivanting across North America for the past few months..."

            fin melancholy "I would have welcomed an appearance from her alongside you three."

            morg happy "Who knows? The day is still young... ish."
            return

        "Mina? Who's that? Never heard of her.":

            fin playful "My sister, genius! Yea high, possesses a beguiling level of candor?"

            morg playful "A smile from Finn? That should have been on the bucket list."

            fin happy "Savor it. You too, my friend; such compliments about her are secrets you take to your grave."
            return


label minigame1failure:
    fin inthought "We're going round in circles here." 
    fin tense "You want me to engage in a day of folly, but I want to hold tight for the better part of a week to secure my entire future." 
    fin default "Are there any other observations you have yet to make clear to me yet?" 
    ter tense "How about we just care a lot and wanna see you outside your room for a change?!" 
    fin upset "You're doing it again..." 
    ter smilehurt "Alright, fine, then it's because you stink of old books and party pooping and freshening up would do miracles for you!" 
    fin inthought "Oh, don't be so puerile." 
    ter "Finn—"
    ter embarrassed "Okay. Okay." 
    morg default "If you won't listen to us then just make a decision yourself." 
    morg tense "Finn, are you coming with us or not?" 
    #Tense pause. 
    fin inthought "I want..."
    morg "Yes?"
    fin default "...for you to get back in contact with me in a few days' time." 
    "Terrie groans, and Morgan's face SINKS." 
    fin melancholy "I believe that compromise will satisfy both worlds." 
    fin inthought "Now, it's been lovely to see you all again, and I really mean that, but I don't want to imagine what a failure at this level could mean." 
    fin "I look forward to the next few days." 
    fin "Bye-bye, all." 
    scene corridor day with dissolve
    show ter c-day grief at centerstage with dissolve:
        xpos .35
    show morg c-day sad at centerstage with dissolve:
        xpos .65
    ter c-day grief "But Finn, we don't HAVE—"
    #Fade out Finn, with the door shutting again. 
    morg c-day sad "No..."
    ter c-day melancholy "Man." 
    ter "Was this guy always such a jerk, or does Med school just do that to you?" 
    ter "I swear, I'll bust down that door n' carry him out myself if it means you—" 
    morg default "Please don't." 
    morg "We can't afford to lose any friendships anymore." 
    morg "Let's just try to enjoy our day." 
    ter melancholy "Alright, I gotchu." 
    ter happy "Y'know what cures hangriness? Sushi. At Miya's. Made to order, just for you." 
    "Morgan smiles weakly." 
    show morg sad
    ter playful "Okay girl, okay! I see that smile!"
    morg "It's on the list, so... why not?"
    ter happy "Exactly! Exactly why not?! Item Two: Eating A Meal Worth... well, worth every bite." 
    ter "We'll get you double servings, okay?" 
    morg "Okay."
    morg "With extra avocado?" 
    ter default "The whole orchard, dude. C'mon." 
    hide morg with dissolve
    hide ter with dissolve
    "So it was just the three of us for the day." 
    "Finn not being there left a foul taste in my mouth, of course. I think it did for everyone." 
    "But, we hoped, we could wash down the bitter pill with a delicious, fresh banquet of sushi."
    scene black with fade
    return