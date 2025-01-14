# label act3:
#     #EXT. CORRIDOR — THE SPOT
#     "The next thing on the list was a meal worth dying for. And for that, it would require a restaurant capable of producing such a meal."
#     "There was only one place that could have food that was worthy of such a title. One Morgan had listed specifically on the list due to its sheer importance to everyone."
#     "A quaint, family-run sushi restaurant called Miya’s that we visited frequently during our high school days. It might have been just another restaurant to some, but to us, this was The Spot."
#     "I can’t remember the last time I was here."
#     "Long forgotten memories come flooding back to when this place was full of life. However, time was not kind to it, like many things."
#     "Despite the wear and tear, color shines through like a flower under rubble."
#     #THE SPOT - DAY
#     #Terrie enters stage left
#     ter "And without further ado, I present to you {i}The Spot!{/i} A place we should all be familiar with!"
#     ter "Hope you’re all ready to satisfy both your body, mind, and soul with food from this joint!"
#     #Terrie fades out
#     #Morgan enters stage left
#     morg "It really has been a while, hasn’t it?"
#     morg "No time like today to make some new memories."
#     #Enter Finn
#     #Morgan fades out
#     #Finn enters stage left
#     fin "I can’t recall the last time I’ve made time to come here."
#     fin "My work made me forget just how much I missed this place, I wonder just how much has changed."
#     fin "That being said, I quite like what’s been done with the place. The art adds a nice touch."
#     "It wasn’t a surprise that the artwork was the first thing to stand out. Lining the walls in various frames, hung art pieces that stood out compared to the aging interior of The Spot."
#     #Finn fades out
#     #CG START
#     "The artwork feels familiar, you’ve seen something like this before. But where?"
#     morg "You know, I feel like we’ve seen this before."
#     fin "What do you mean?"
#     morg "Remember that one time we all almost got busted in senior year?"
#     #CG END
#     #Choice
#     menu:
#             "Ah, the infamous {i}Statue Incident.{/i} How could I forget?":
#                 jump eureka
#             "I’m sure Terr remembers!":
#                 jump memoryjog
#             "You’re gonna have to be more specific than that...":
#                 jump confusion
# label eureka:
#     #Morgan fades in
#     morg "Yes, that one! It didn’t get on the front page of our school paper for nothing."
#     jump statueop
# label memoryjog:
#     #Terrie fades in
#     ter "The statue incident... Right?"
#     #Terrie fades out
#     #Morgan fades in
#     morg "I knew you’d remember, Terr. It was kind of hard to miss with it making the school paper and all."
#     jump statueop
# label confusion:
#     morg "Surely it hasn’t been that long. Who could forget the statue incident that made the school paper?"
#     jump statueop

# #Options converge here
# label statueop:
#     morg "Terr was a true mastermind. If it weren’t for them convincing the teacher that we didn’t break their precious statue, who knows what would have happened."
#     #Morgan fades out
#     #Finn fades in
#     fin "It’s unthinkable how easily one can be blamed for others' tomfoolery."
#     fin "Wrong place, wrong time, I suppose."
#     #Finn fades out
#     #Terrie fades in
#     ter "At least we made it here in time for dinner rush! Would’a sucked to be crammed in some lame fast-food chain after all that."
#     "It was a day to remember. We always found a way to come here whenever we needed to retreat from the world."
#     "After reminiscing about some highschool shenanigans, we all settle in."
#     "It isn’t long before we’re met with a familiar face."
#     #Terrie fades in
#     #Miya enters stage left
#     yum "...Morgan?"
#     yum "My, how long has it been now? 10 years?"
#     #Morgan enters stage right
#     morg "Oh come on now. A measly 10 months could never stop me."
#     yum "You look so lively. Radiant, even."
#     yum "Are my eyes playing tricks on me? Is Finn here as well? It’s been so long! Just where have you been??"
#     #Morgan fades out
#     #Finn enters stage right
#     fin "It’s nice to see you too."
#     fin "I’ve been rather occupied with my studies, I apologize for not coming back sooner."
#     yum "You don’t have to be sorry for anything. You’re working so hard, just like Mina..."
#     #Finn fades out
#     #Morgan fades in
#     morg "Mina?"
#     yum "Of course! Terrie told me all about her exciting move to LA, she has such a bright future ahead of her."
#     #Morgan fades out
#     #Terrie enters stage right
#     #TERRIE gives their friends an apologetic smile.
#     ter "Okay, so. {i}Maybe{/i} I should’a told you guys I work here."
#     #Terrie fades out
#     #Morgan fades in
#     morg "You think?"
#     #Morgan fades out
#     #Fin fades in
#     fin "It would have been nice to know."
#     yum "I’m sure they didn’t mean to keep it from you all! Terrie’s just a little shy about their artwork."
#     "Terrie groaned."
#     #Miya fades out
#     #Morgan enters stage left
#     #MORGAN and FINN light up.
#     morg "Terrie, you did all this?"
#     #Morgan fades out
#     #Terrie fades in
#     ter "...Yeah."
#     #Finn enters stage right
#     fin "Woah..."
#     ter "I’m just an aspiring artist tryin’ to get my stuff out there."
#     fin "It truly is wonderful, Terrie. You’ve always had a gift for this kind of thing."
#     ter "What are you talking about?"
#     ter "Please, save the praise for someone who’s actually worth it. "
#     #Finn fades out
#     #Morgan enters stage right
#     morg "You have just as much a right to praise as anyone else. "
#     ter "Is it really worth that much if I’m still {i}stuck{/i} here—"
#     morg "What, you mean in the restaurant?"
#     #Morgan fades out
#     #Miya enters stage right
#     yum "Terrie... You can’t really think that, can you?"
#     ter "I guess? Sorry, I know it’s kind of pathetic. If only I worked a little harder, maybe I’d be in art school by now."
#     #Miya fades out
#     #Finn enters stage right
#     fin "It’s not too late, you still have time."
#     #Finn fades out
#     #Morgan fades in
#     morg "You’ve been working your butt off! There’s no way you won’t succeed, Terr."
#     #Morgan fades out
#     #Miya fades in
#     yum "Both you and your work is appreciated here. It always will be."
#     "Terrie sighed."
#     ter "You speak too highly of me, really."
#     ter "My stuff just isn’t “woah” material, you know?"
#     yum "Oh, that’s not true at all. I think you’re blind to the admiration surrounding you."
#     yum "You work too hard, you’re nearly just as bad as Finn."
#     ter "What? Fat chance! I’m {i}way{/i} better than Finnster, here."
#     ter "I’ve been good about giving myself time off, unlike a certain someone."
#     #Miya fades out
#     #Morgan fades in
#     "Morgan looked distant."
#     morg "I wish she could be here."
#     #Terrie fades out
#     #Finn enters stage left
#     fin "I’m sure she wishes that too."
#     #Morgan fades out
#     #Finn fades out
#     #Miya fades in
#     yum "You’re all such hard workers, Mina’s out here making a living just by being her authentic self. I’m sure you’ll do just the same."
#     #Terrie enters stage right
#     ter "I’m doing my best."
#     yum "Yet despite all of that, you work harder than almost anyone else I know. That’s why you’re here, right?"
#     ter "Right. It is why I’m doing my best to earn enough to attend art school. To have art worthy of being praised by everyone."
#     yum "Well, young Terr. Success is something that requires many things. Persistence goes a long way. It is why I continue to endure despite the tough times."
#     #Terrie fades out
#     #Morgan enters stage right
#     morg "Tough times?"
#     yum "This isn’t as inviting as it used to be, Morgan."
#     yum "Prices continue to rise. Sales continue to fall. Even my spirit is starting to wane..."
#     yum "I just hope I can pay this month’s bills."
#     #Miya fades out
#     #Morgan fades out
#     "A tense silence filled the room, the once cheerful mood gone. Just then, Morgan stood up from her seat."
#     #Morgan fades in
#     morg "I have a brilliant idea!"
#     morg "Why don’t we have Mina pull some strings to reel in some customers? We can even help with the dinner rush!"
#     #Terrie enters stage right
#     ter "Dude. You’re a {i}genius.{/i} Has anyone ever told you that, Morgs?"
#     ter "Someone get this girl a damn phone, we got an influencer to ring up!"
#     #Terrie fades out
#     #Finn enters stage right
#     fin "I’m not sure my sister would approve of this, but it doesn’t hurt to try."
#     fin "However, if Mina is on board, I have no doubt success awaits us."
#     morg "Let’s give her a ring."
#     #Morgan fades out
#     #Finn fades out
#     "We waited in anticipation as Finn dialed her number. It only took a single ring before an all-too familiar voice came out through the phone’s speaker."
#     #Mina enters stage right
#     mina "At long last, my precious brother has finally gotten in contact with me after {i}years{/i} of neglect..."
#     #Finn enters stage left
#     fin "It has been one week."
#     mina "Exactly!"
#     mina "Fear not, your favorite sister is here for you. What’s going on in Finn-land?"
#     "Finn groaned, running a hand down his face."
#     fin "Only sister does not translate to favorite."
#     mina "Awww, you’re so mean! You’re still my favorite, even after you totally tr—"
#     fin "{i}Mina—{/i} You’re on speaker."
#     fin "I’m with Morgan and the others, we’re at Miya’s."
#     mina "Oh, for reals? Hello to my favorite people in the whole wide world! How’s it hanging?"
#     #Finn fades out
#     #Morgan enters stage left
#     morg "Hi Mina, I have a favor to ask. Do you mind helping us advertise Miya’s?"
#     mina "No way, The Spot?"
#     mina "That place brings back so many memories! It feels like forever ago... I can’t believe I’m missing this nostalgia trip right now!"
#     mina "Ugh, I don’t know if it really fits my brand though..."
#     #Morgan fades out
#     #Terrie enters stage left
#     ter "C’mon, Mina! It’s a cozy sushi place that THE Mina used to frequent all the time. There’s no way people won’t jump at the chance to eat here!"
#     "Mina hummed in thought."
#     #Terrie fades out
#     #Finn enters stage left
#     fin "You don’t have to do anything you don’t want to, Mina."
#     #Finn fades out
#     #Miya enters stage left
#     yum "Of course! It’s more than enough just to hear from you, please don’t trouble yourself with something like this."
#     #Miya fades out
#     mina "That settles it."
#     mina "You guys just scored a super free and super AWESOME sponsorship from yours truly!"
#     #Morgan enters stage left
#     morg "Really? I’m touched, really. But is it okay?"
#     mina "Oh, stop it. I love my friends and I’m gonna do everything I can to help you guys out! Have fun today, alright?"
#     morg "...Alright."
#     morg "Thank you. Truly."
#     mina "Make it count, you guys got this in the bag. See you later, lots of love!"
#     #Mina fades out
#     "The moment Mina hung up, the group turned to Morgan, who was now brimming with excitement."
#     morg "Alright, we’ve got work to do. But before we do anything, we need to pick out jobs!"
#     #Terrie enters stage right
#     ter "Oh, oh! Let me be the waiter {i}please.{/i} I’m uber experienced, they’ll give us mad tips thanks to my mad skills."
#     morg "It’s all yours. Finn, how would you feel about manning the front counter and acting as our host?"
#     #Terrie fades out
#     #Finn enters stage right
#     fin "I get to work with the register, that sounds perfect to me."
#     #Finn fades out
#     #Miya enters stage right
#     yum "You know where I’ll be. Though, it would be nice if someone could help me bring out orders to customers."
#     morg "You can count on me."
#     morg "How does dishes sound to you? I hope it’s not too boring."
#     mc "I was born to scrub."
#     #Miya fades out
#     #Terrie enters stage right
#     ter "You better be. If those dishes pile up, we’re screwed. We believe in you, dude!"
#     ter "Thanks for being on top of things, everyone. Any questions before we get trampled by Mina’s fans?"
#     morg "Nope, I’m ready to go. I’ll give it my all!"
#     #Terrie fades out
#     #Finn fades in
#     fin "I’ll do my best to utilize my skills to get customers situated."
#     #Finn fades out
#     #Morgan fades out
#     "With no questions on my end, Morgan responded with a firm nod."
#     "Perhaps my job of washing dishes was simple, but every cog in this machine was important."
#     "Thus began a service like no other."
#     #Order Taking Mini Game Start
#     #Terrie enters stage left
#     #Group 1
#     c1 "Can I get the Yummy Yam Roll?"
#     c2 "I would like the Dragon Roll. I’m also allergic to shellfish."
#     #Miya enters stage right
#     yum "What did customer one want?"
#     #terrie is the one choosing options, their sprite will take priority in this minigame along with miya's.
#     ter "BC Roll"
#     ter "Dragon Roll"
#     ter "Yummy Yam Roll"
#     yum "What did customer two want?"
#     ter "Dragon Roll"
#     ter "BC Roll"
#     ter "Shrimp Tempura roll"
#     yum "Any allergies?"
#     ter "Yes"
#     ter "No"
#     yum "Who has an allergy and what is it?"
#     ter "Customer one has a shellfish allergy."
#     ter "Customer one has a ginger allergy."
#     ter "Customer two has a shellfish allergy."
#     ter "Here's your order!"
#     #Miya fades out
#     #If Correct
#     c1 Ah this looks great, thanks!
#     c2 No shellfish, right? Thank you very much.
#     #If Incorrect
#     c1 Wait… I wanted the Yummy Yam Roll! Please take this back.
#     c2 Come on. This isn’t the right roll. Take it back.
#     c2 Is that shellfish? I said I was allergic. Take it back.
#     #Group 2
#     c3 Can I get the Shrimp Tempura roll? Also, I’m allergic to ginger.
#     Customer four
#     I would like the BC Roll.
#     Customer five
#     The Yummy Yam Roll please!
#     #Miya enters stage right
#     Miya
#     What did customer three want?
#     Terrie
#     Yummy Yam Roll
#     BC Roll
#     Shrimp Tempura roll
#     Miya
#     What did customer four want?
#     Terrie
#     Dragon Roll
#     Shrimp Tempura roll
#     BC Roll
#     Miya
#     What did customer five want?
#     Terrie
#     BC Roll
#     Yummy Yam Roll
#     Shrimp Tempura roll
#     Miya
#     Any allergies?
#     Terrie
#     Yes
#     No
#     Miya
#     Who has an allergy and what is it?
#     Terrie
#     Customer three and it’s a ginger allergy.
#     Customer four and it’s a ginger allergy.
#     Customer five and it’s a shellfish allergy.
#     #Miya fades out
#     If Correct
#     Terrie
#     Here’s your orders!
#     Customer three
#     Ah. That looks perfect. Thanks!
#     Customer four
#     You made sure to remove the ginger, right? Phew. Thank you.
#     Customer five
#     This looks like a ten out of ten. Amazing.
#     If Incorrect
#     Customer three
#     Eh… This is not what I asked for. Can you take it back?
#     Customer four
#     Hey! This isn’t what I ordered! Take it back.
#     Customer four
#     What are you doing? I said I have a ginger allergy and there’s ginger on the plate. Take it back. Immediately.
#     Customer five
#     Uh… I’m pretty sure I ordered the Yummy Yam Roll. Can you take it back?
#     #Mini Game End
#     #terrie fades out
#     Narration
#     With the hustle and bustle of the evening fading away, what was left was the fruits of our labor.
#     #If successful but Finn isn’t there
#     THE SPOT - DAY
#     Narration
#     All of us stood proudly together as one. The night was a clear success, and the Miya was filled with joy.
#     #Miya enters stage right
#     Miya (happy)
#     I cannot thank you enough for everything. This certainly will keep us afloat for a good while.
#     Miya (overjoyed)
#     This calls for our own feast to celebrate!
#     #Miya fades out
#     Narration
#     We soon began setting up one final table. One filled with everything we could ever want.
#     Narration (cont’d)
#     As we began absorbing the moment, Morgan spoke up, exuding an energy that didn’t fit the mood.
#     Narration (cont’d)
#     A rather negative energy.
#     #Morgan enters stage left
#     Morgan (neutral)
#     This should have been the perfect moment… A meal that we all worked hard to eat.
#     Morgan (sad)
#     We might have had a successful night, but…
#     Morgan (sad)
#     I wish Finn was here to share it with us.
#     #If unsuccessful
#     THE SPOT - CORRIDOR
#     Narration
#     And so, the service came to a close. It was hard to call it a success.
#     Narration (cont’d)
#     In fact, it felt as if the restaurant was worse off than when we started.
#     #Miya enters stage right
#     Miya (Disappointed)
#     I appreciate the effort everyone… truly.
#     Miya (Disappointed) (cont’d)
#     Perhaps this might be a minor setback, but it was great seeing you all try your best. That’s what matters.
#     #Morgan enters stage left
#     Morgan (sad)
#     I’m so sorry… I know we did our best, but… I guess it was too much for us.
#     #Morgan exits
#     Narration
#     Terr remained silent, thinking about how this was another failure he had to deal with.
#     Narration (cont’d)
#     I’d have to apologize to Mina later on.
#     #Branches merge
#     THE SPOT - DAY
#     Narration
#     As things settled down, the Miya retreated into the back and came back moments later with a full platter of food for everyone.
#     #Miya enters stage right
#     Miya (smiling)
#     All of you did your best today, thank you so much for all that you’ve done. Please enjoy.
#     #Miya fades out
#     #Morgan enters stage left
#     Morgan
#         Thank you for letting us do this.
#     #Terrie enters stage right
#     Terrie
#         No need to get all mushy on us now, Morgan. We all wanted to do this!
#     Morgan lets out a sigh of relief.
#     Morgan
#         I’m so glad.
#     #Morgan fades out
#     #Terrie fades out
#     Narration (cont’d)
#     As if on cue, my phone began to ring.
#     Narration
#     It was Mina. I gave her the news.
#     MC picks up, and is greeted by Mina letting out either a happy squeal or disappointed sigh.
#     #Mina enters stage right
#     #If Minigame is Successful
#     Mina (happy)
#     Aaah, you guys! I’m getting tagged in so many posts right now, you have no idea. Whatever magic you guys conjured up is WORKING!
#     A wave of relief washes over everyone.
#     Mina (happy)(cont’d)
#     Hopefully it isn’t too much for Miya to handle. I know Terr is there, but you can never underestimate the power from a rising star!
#     #If Minigame is Unsuccessful
#     Mina (disappointed)
#     You guys… I’m getting tagged in a lot of posts. There’s a lot of people complaining about mistakes.
#     Mina (disappointed)(cont’d)
#     Hopefully it isn’t too much for Miya to handle. I know Terr is there, but…
#     Narration
#     I could see Morgan wanting to apologize, but was surprised to hear what she said next.
#     #Branch Merge
#     #Morgan enters stage left
#     Morgan
#         What you did really made an impact Mina, thank you.
#     Mina
#         Morgan...
#     Mina pauses, carefully picking her words.
#     Mina (cont’d)
#         I’m sorry I can’t be there. I truly hope this helps make up for me not being with you guys...
#     #Choice
#     #It does. You really helped us out here, Mina.
#     Mina (happy)
#     Yay! Glad to be of service, anything for the gang. Especially you, Morgan.
#     #As long as Morgan is happy, I’m happy.
#     Mina
#     Same here! Pretty sure we’re all in the same boat about that.
#     Beat.
#     Mina (concerned)
#     Morgan?
#     #I really wish you could have been here.
#     Mina (apologetic)
#     Believe me, I would be there in a heartbeat.
#     Mina (cont’d)
#     You don’t even know the half of it...
#     #Branch Merge
#     Narration
#     Morgan closed her eyes, finding the courage to speak how she truly felt.
#     Morgan (grateful)
#     Thanks for everything Mina. Without your help, this wouldn’t have been possible.
#     Morgan (happy)
#     I know you might feel bad about being unable to be here in person, but I’m glad you got to play a part.
#     Mina
#     Morgan... You know I’d give anything to be with you all again.
#     Mina (cont’d)
#     The limelight is amazing, it’s been my biggest dream, I’ve done so much to make this possible.
#     Mina (cont’d)
#     However, it doesn’t mean that I’d give up everything for it.
#     Mina (sad) (cont’d)
#     The world of content creation is rough, everyone’s at each other’s throats. Fame and fortune is the only thing that matters to them. Most bonds you see online are just from fancy connections.
#     Morgan
#     Mina...
#     Mina
#     However, what we all share is different. All of you mean the world to me. Even if I can’t be there to share this moment of success... know this. I’m happy that the bond we all share is still just as strong as the day I took a step towards my dream.
#     Morgan
#     Thank you, Mina. I really appreciate everything.
#     Mina
#     Good luck with finishing off the list, I’ll be rooting for you from all the way out here!
#     #Mina fades out
#     With that, Mina hangs up.
#     #Terrie enters stage right
#     Terrie
#     I miss her already.
#     Terrie (cont’d)
#         ...So, now that we’ve had some fine dining, what’s next on the list?
#     Morgan
#     We still have plenty of runway.
#     Morgan (reading list)
#     Let’s see... there’s a performance of a lifetime or...
#     Narration
#     Morgan’s smile disappeared for a second before returning.
#     Morgan (smiling)
#     Let’s go with that. A performance to show the world what we got.
#     Terrie (happy)
#     Attagirl, We’ll knock everyone’s socks off with a performance they’ll never forget.
#     #Terrie fades out
#     #Morgan fades out
#     THE SPOT - CORRIDOR
#     Narration
#     Without further delay, we were off once again.
#     Narration (cont’d)
#     Time was slowly catching up to us, we were doing everything we could to finish strong.
#     Narration (cont’d)
#     It had to be the best it could be. To ensure Morgan had a performance worth remembering.
#     Narration (cont’d)
#     There was no room for error.
#     All exit