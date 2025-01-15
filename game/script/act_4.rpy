label act4:

    "The ice rink sounded like a good idea on paper, we all thought."

    "A quintessentially wintry pastime where all of your friends hit the ice, then skate like a pro or look good trying."

    "And whilst some of us couldn't walk straight with blades on the soles of our feet..."

    ##Suddenly enter TERRIE from screen middle

    ter "ACK! Too frozen, too frozen!!"

    ##Enter MORGAN from screen left.

    morg "Give me your hand, Terr."

    morg "It's like riding a bike; the faster you move, the less you wobble."

    "...others moved like they were raised on ice."

    morg "Isn't this just the life, everyone? The speed, the wind, the chill all over again." # content sigh

    morg "Oh, it's just so... so freeing..."

    if act2_finn_success:

        ##Pop-in FINN.

        fin "I have yet to be the judge of that!" # anxious

        fin "Excuse me, friend, would you care to provide me with a boost off the wall?"

        menu:
            "Gently push him":

                fin "Maybe with somewhat more oomph next time— I mean, whee…"

                ter "Ooh, look out, attempting to break the land speed record we have FINN at a BLISTERING 2 kilometers an hour!" # like a commentator

                morg "Oh, how will he and his pit crew ever hope to topple the current defending champion?" # fake gasp

                fin "When the defending champion talks like that, perhaps she should let her actions speak"
                instead.

        "Link arms and pull him along":

            fin "YIKES! Bold today, are we?!"

            morg "You'll both bring yourselves down with technique like that!"

            morg "Oop...and there it is. Do you guys need a pair of hands?"

            fin "Like we need air to breathe." # groans

            #beat

            "Thank you. Now you try zipping forward with such velocity."

        "You're a great friend and you'll kick ass on the ice!":

            fin "Enthusiasm appreciated, but wrong kind of boost. I suppose it'll suffice... and we're off."

            ter "Attaboy, Finn! Come join me and… Wow, never mind, Morgan's skatin' circles around us already."

            fin "Oh, really? I think she could do better."

        #Paths converge

        "Morgan developed a keen smirk."

        ter "Uh, dudes, I think you just declared war."

        morg "They most certainly did. Hold my gloves, Terrie."

        ##Exit MORGAN.

        ter "I don't think you realize just what you're about to witness."

        ter "Remember how much of a beast she was on the ice before... before the—"

        fin "I never forgot, don't panic."

        ter "Yeah. I'm pretty sure she spent two hours by herself here for every hour we visited as the gang!"

    else:

        morg "Just me and you and Terrie and not—not a lot of other people to judge you or cheer you or— or..."

        ##TERRIE shares a let-down expression very briefly.

        morg "Hey! I have an old routine I used to practice for ages."

        morg "It's an old one, but it's... it's coming back to me, I think. Care to watch?"

        ter "Hey, s'long as I'm not falling down and you're in your zone, I'm game!"

        morg "Right. Okay. This is it. This is really happening. Hold my gloves, Terrie."

        ##Exit MORGAN.

        ter "Oh, she really needs this, doesn't she?"

        ter "Between this whole thing and then us being down two friends, I really wouldn't blame her if we spent the rest of the night here."

        ter "And y'know? I wouldn't mind. Morgan's an ice queen out here!"

    ter "I caught the tail end of one of her routines once when I came to get my skates re-sized. It was... really somethin' else."

    if act2_finn_success:

        ter "So prepare for a blown mind with a side of I-told-you-so!"

        menu:
            "We're gonna eat our words, Finn.":

                fin "Much like the sushi we dined on prior, I fear."

                ter "Dinner and a show? Sounds like we had the perfect day already!"

                fin "Time is still on our side, now. Who knows what else we'll see today?"

            "Hey, Morgan's just happy to be here. That's a win.":

                ter "True that! Look at us, cheering our girl on like it's nationals day."

                fin "She really should consider that level of performance if things improve."

                ter "Yeah…" #(awkward pause)

            "What if my mind was pre-blown coming into the rink?":

                ter "What, by the whole fact that she can actually skate? Fair!"

                ter "That and, uh..."

                ter "You definitely saw it at the hospital, right?" #(whispering directly to player)

    else:
        ter "Don't forget, you're gonna cheer for her until the roof shatters. At least! She deserves it all."

    ##Enter MORGAN again, this time further away from the others.

    morg "I think we're ready! Are you watching, judges?" #(far off)

    ter "Huh? Hey, that's us, we're judges!"

    ter "Knock 'em dead, Morgan!"

    ##Pause.

    ter "I mean, uh, perform with grace and beauty an' all that!" #(flustered)

    morg "I can do both!" #(far off, giggling)

    if act2_finn_success:
        fin "Fantastic! Come on, let's give her some space."

        "As the three of us made our way back towards the walls and gave Morgan the thumbs up, the fire in her eyes could have melted every ice rink between here and Montreal."

    else:
        ter "Alright, other judge - that's you - take your places!"

        "As the two of us made our way back towards the walls and gave Morgan the thumbs up, there were makings of a fire in her eyes. Weak, fledgling passion, but it was there."


    "But I wondered, did she still have it in her to push this far?"

    morg "Three, two, one, and..." # (whispering to herself)

    "Her blades kicked ice powder into the air as she started her dance, and the rest was history."

    # MINIGAME START
    # TODO minigame...?


label act4_minigame_success:

    ## INT. ICE RINK - DAY with dissolve

    "History for the sports almanacs, that is."

    "I don't think I'd seen so many other ordinary people stop whatever they were doing and just… stare in awe."

    "All eyes were on Morgan, just as she deserved. She was like an angel, and the rink was her heaven."

    "An angel whose speed sometimes made her struggle to come to a timely Halt."

    ##Pop-in MORGAN.

    morg "Watch it watch it watch it—!!!!" # (panicky)

    "And who sometimes relied on me as a crash pad."

    morg "Oh, gosh, you. Two wipeouts in one session? Sorry, I've got you."

    menu:
        "You were glowing out there.":

            morg "Aw, you're just being nice."

            ter "Oh c'mon, be less humble; that rink was yours just now!"

        "You need to work on your finishes.":

            morg "I guess I do... you won't always be there to cushion the tough blows, will you?"


            morg "Then again, nothing's a hundred percent perfect right?" # (melancholy giggle)

        "Fancy a partner dance next time?":

            morg "Think you could keep up with me, or will you be waddling like a penguin?" #(sly giggle)

            #Beat.

            morg "Same time, next month. Save the date, and if you flake I'm snowballing your house." # (much softer)  (laughs)

    "Morgan was alive. And it seemed now that she intended to keep it that way."

    if act2_finn_success: # TODO can you ever succeed at minigame without Finn being there?

        fin "Well, there's absolutely no chance of us ever topping that. Stellar performance."

        fin "You must be exhausted now, though — I know I am."

    ter "Yeah, I'm beat, Morgs. Think you're rinked out for the day too?"

    morg "I guess I am. As for the list, let's change and see what else there is."

    jump act4_end_with_finn


label act4_minigame_failure:

    "Unfortunately, it was the kind of history you pray never repeats itself."

    "As free as she wanted things to flow, she stumbled and struggled through her routine, like she was chained and puppeteered by something we could never hope to see."

    "And as quickly as she got onto the ice..."

    "She was off her feet, and at our knees."

    morg "Ow..." # (weakly)

    if act2_finn_success:

        morg "Oh God, everyone saw that, didn't they?"

        menu:
            "It was a good effort. Well done.":

                morg "Yeah, but... what happened?"

                morg "I mean, I know what happened, but, just... to me?"

                morg "I thought I'd gotten better enough to do this again, but I guess everyone has their limits, right? Yeah."

            "Far better than any of us could do, at least!":

                morg "Thanks."

                morg "It feels like they're all staring at me. Do you think they think I'm a tryhard?"

                morg "Oh, this sucks. This sucks and my butt is frozen and I'm calling time."

        "Morgan looked like she was about to cry."

        ##Pop-in FINN and TERRIE.

        ter "Wee-oo, wee-oo, Terrie to the rescue, nothing to see here, people!" # (imitating an ambulance)

        ter "Vamoose! Don't make me call the resurfacer!"

        fin "Can you remain standing?"

        morg "Fortunately yes. Now come on, we have a list to complete."

        morg "Full time, or whatever."

        fin "For what it was worth, I loved the routine in spite of, uh..."

        "Morgan looked disappointed."

        fin "Okay, right, never mind, going with haste."

        jump act4_end_with_finn

    else:

        morg "Not again, not again...!" # (through gritted teeth)

        ##SCENE ICE RINK - DAY

        menu:
            "It was a good effort. Well done.":

                morg "You don't have to protect my feelings."

                morg "I guess I just skated too close to the sun, and then that's that!"

                morg "I guess I kind of deserve it."

            "Wordlessly help her up":

                morg "Much appreciated."

                morg "They're all staring at me now. I can feel it. Can you see it?"

            "Now at least everyone's bit the curb today, eh?":

                #MORGAN (sad sigh)

                #MORGAN (angry sigh)

                morg "Just help me up, please."

        "Morgan looked like she was about to cry."

        # Pop-in TERRIE.

        ter "Wee-oo, wee-oo, Terrie to the rescue, nothing to see here, people!" # (imitating an ambulance)"

        ter "Vamoose! Don't make me call the resurfacer!"

        ter "That should do it. You okay?" # (softens, to Morgan)

        "Morgan looked disappointed."

        ter "Don't pay any mind to the world, I thought you kicked ass."

        "The disappointment persists."

        ter "Okay. Alright. I get it. All iced out for today, huh?"

        ter "I cleared a path for us, so let's blow this popsicle stand. You too, dude."

        ##Exit MORGAN and TERRIE from screen-right.

        ##FADE TO BLACK

        ##SCENE STREET - DAY with dissolves

        ##Pop-in TERRIE and MORGAN.

        morg "The fireworks. That's what's next."

        morg "We're going to go to that pretty hill, the one with the view, and then watch the fireworks go off, and then..." # (unsure of herself)

        ter "And then...?"

        morg "I'm not sure."

        ter "One step at a time, Morgan. I mean, hey, it's OUR secret spot."

        ter "No way anyone or anything can get through into that place, right?"

        ter "Just the three of us, and that's it. We're here for you, Morgs."

        morg "Three of us. Yeah."

        morg "We just have to make sure we don't miss the starting time."

        ter "Right! What's the hold-up for, then?"

        morg "None! None at all."

        morg "...If I need help getting up the hill, I'll let you all know."

        "The day was drawing to a close faster than expected."

        "Fortunately, it would end with what we all came out for. What our hearts all held onto the most for the longest time."

        "I could only hope our grand day out would end with a bang."

        jump act6


label act4_end_with_finn:

    ##FADE TO BLACK

    ##FADE IN STREET - DAY with dissolve

    ##Pop-in TERRIE, MORGAN and FINN.

    morg "Alright, next on the agenda."

    morg "It's nearly fireworks time."

    ter "You're kidding! After all these years we're goin' back?!" # (squeals)

    morg "With a twist."

    morg "When was the last time you heard me scream?"

    ter "Huh?"

    fin "Ohhhh, I see. You aim to yell as loud as you can into the valleys and hear its echo?"

    morg "You know me so well."

    ter "Honestly, girl, I'd get it if you just screamed right now outta nowhere."

    morg "Believe me. I've wanted to. That rink nearly never heard the end of it."

    morg "That's why I thought, why not just do it in a place that matters?"

    ter "Okay, we love a bit'a showmanship!"

    ter "Let's do it, then. Let's see the pretty lights and wreck our throats for the next week."

    fin "I would prefer to preserve mine, in all honesty."

    ter "Your exam a speaking one?" # (cheeky)

    fin "No, but—"

    ter "Then we're good! C'mon!!"

    ##MORGAN laughs, and they all exit.

    jump act4_end

label act4_end:

    "The day was drawing to a close faster than expected."

    "Fortunately, it would end with what we all came out for."

    "What our hearts all held onto the most for the longest time."

    "Our grand day out would for sure end with a bang."

    ##FADE TO BLACK

    jump act6


