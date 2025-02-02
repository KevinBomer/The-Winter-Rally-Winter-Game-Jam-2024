init:
    transform centerstage:
        xanchor .5 yanchor 1.0
        xpos .5 ypos 1.5
    transform minachibi_transform:
        subpixel True 
        pos (0.35, 0.66) yzoom 1.0 zoom 0.4

    #####Set the automatic dissolve between expressions to dissolve
    define config.say_attribute_transition = dissolve

    $ Minigame1 = False
    $ Failstate = 'minigame1failure'


label start:
    scene black
    scene nightsky with slowerdissolve
    play music introduction fadein 3.0 volume .4
    "We always loved going to see the fireworks."
    "It was the one tradition we could always count on."
    "Just the five of us, watching time march on and the sky burst with colour... I could always count on them to join me."
    show ter sky default at centerstage with dissolve
    "Practical, plucky, passionate Terrie..."
    hide ter with dissolve
    show mina hill default at centerstage with dissolve:    
        subpixel True 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(-25.0) 

    "Silver-tongued, savvy, sociable Mina..."

    #Enter FINN. 
    hide mina with dissolve
    show fin sky default at centerstage with dissolve
    "Wise, wild workaholic Finn..." 
    hide fin with dissolve
    show morg sky happy at centerstage with dissolve
    "And, of course, Morgan."

    "The five of us as a group ran like a clock, but life, as always..."
    show fadetoblack behind morg with slowerdissolve
    pause .5
    show morg at centerstage:
        alpha 1
        ease 2 alpha 0
    hide morg with dissolve
    "It mutated beyond our control and spread all of us thin." 
    "Mina made it big online and flew out to LA for all the brand deals you could dream of." 
    "Finn got swallowed whole by the mire of academia, studying for a degree with all the energy he could possibly muster." 
    "And Morgan?"
    stop music fadeout 3.0
    scene corridor with paintmask2:
        zoom .52
        easein_cubic 1 zoom .5
    "They all said it was the most aggressive case they'd ever seen in their years of practicing medicine."
    "It was so deep in her system they couldn't even pin down what kind of cancer it was to start with." 
    "Being bound to a bed with two of her friends basically vanishing off the radar, I thought she'd never smile again..." 
    "But I'd make sure it would happen. I promised myself." 
    "So, on a chilly January 7th, I went to Nigh Hill Medical Clinic once more for Morgan." 
    "Well, not before inviting the only constant presence in our lives, too..." 
    "Nobody quite like good ol'..." 
    show ter at centerstage:
        yoffset 1000
        spring3 .5 yoffset 0
    ter c-day playful "You made it! Good, I wouldn't miss this for the world."
    ter c-day tense "How long's it been since Morgan last gave us a call... like, what, two, three weeks? God." 
    ter "Treatment must be rough for a gap of silence that wide." 
    ter "Hmmm..."
    ter c-day smile "No time like the present though, right? She's waitin'!"
    ter "C'mon, Nigh Hill's just that way."
    $ play_music(hospital,3)
    hide ter with easeoutright
    scene purgatory with dissolve
    "As far as we knew, Morgan rarely got visitors aside from me and Terrie."
    "So imagine seeing that, on today of all days, somebody else had beaten us to the punch." 
    ###SCRIPT show death]
    camera:
        easein 1 matrixcolor SaturationMatrix(0.5)

    show image "death black cropped.png" at centerstage with paintmask:
        subpixel True
        matrixcolor BrightnessMatrix (-1.0)
        blur 30
        xpos .6
        zoom .72
        easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (0.0) zoom .75 blur 0 xpos .65
    mortis "You... you have a gift." 
    mortis "A gift seldom experienced to the fullest, and even more seldom stripped away so prematurely." 
    #Pop-in TERRIE. 
    ter "Crap, did we double book our visiting slot?" 
    mortis "For you... this will not do." 
    mortis  "I shall visit here again tomorrow, at dawn's break." 
    mortis "You are to recount to me all that you got up to this coming day. Promise to me that you will return promptly." 
    mortis "...yes, and what of your constitution, indeed?" 
    mortis "You will find that much of what you miss will come to you in very due time." 
    mortis "I leave you to your devices now. To your good health, Morgan. Do not be late." 
    #Beat.
    show ter hospital inthought at centerstage with dissolve:
        xpos .15
    ter "...are you getting any of that? I sure ca— "
    ter "...huh?" 
    #SCRIPT Enter from screen left DEATH. Long beat. 
    mortis "Your friend awaits you." 
    mortis "Hurry along, now. Live a little." 
    #Exit Death from screen right. 
    show image "death black cropped.png" at centerstage with paintmask:
        subpixel True
        matrixcolor BrightnessMatrix (0.0)
        blur 0
        xpos .65
        zoom .75
        easein_cubic 1 alpha 1.0 matrixcolor BrightnessMatrix (-1.0) zoom .75 blur 30 xpos 2.0
    camera:
        easeout 1 matrixcolor SaturationMatrix(1.0)
    ter "I..." 
    ter hospital tense "I'm going in. You're coming with, yeah?" 
    ter hospital happy "Heyyy, Morgan? It's Terrie. It's us. How're you holding up?" 
    #Fade-in MORGAN. 
    "She breathes heavily with a noticeable wheeze and coughs." 
    "As she breathes more, the wheezing fades... and then disappears altogether." 
    show morg hospital inthought at centerstage:
        subpixel True
        zoom .97 alpha 0
        easein 1 zoom 1 alpha 1

        
    morg hospital inthought "Never better?" 
    #FADE TO BLACK 
    #INT. HOSPITAL ROOM - DAY
    ter hospital aha "Morgan, oh my {i}God{/i}, you're glowing!"
    morg hospital playful "Not literally, I hope." 
    show morg hospital default with dissolve
    ter "It's just— wh— how— what kinda treatment are they giving you guys in here?!" 
    ter "It's like a miracle!" 
    morg playful "Who knows? Maybe they hooked me up to the Elixir of Life by accident." 
    ter hospital default "D'you feel like you could... y'know... again?"
    morg hospital sad "What, this?"
    "The moment that Morgan stood up again, it was like she'd never fallen ill."
    "It was like the future we wished for as teenagers could finally come to pass." 
    ter hospital hurt "Dude... pinch me right now."

    morg hospital playful "Okay, then." 
    
    show ter hospital aha at centerstage:
        subpixel True 
        yoffset 10 xpos .15
        spring3 .5 yoffset 0
    ter hospital aha "Ow— hey! You KNOW that's a figure of speech, you!"
    morg "Oh, I'm sorry, I've been cut off from the outside world for the past ten months."
    morg "Who knows how people speak now?"
    ter hospital happy "Well, since you're up and walkin', we could probably go out and see for ourselves." 
    morg default "We could..."
    #Beat.
    morg "...Hm. Terrie, see that wastepaper over there in the trash?"
    morg "There's something written on it that I want to show you guys."
    "The wad of paper that Morgan threw away who knows how long ago was actually a to-do list." 
    "Packed with fun activities to pass the  time with alongside friends across Vancouver." 
    "It was filled top to bottom. And Morgan, although she almost gave up on it, now..."
    morg hospital happy "All of it."
    ter hospital inthought "All of it? Today?"
    morg "{i}All{/i} of it. Today."
    morg "With as many people as we can find. Heck, invite the neighbour's dog if you have to."
    morg hospital default "Hey, how are Mina and Finn getting on?"
    ter hospital playful "Oh, y'know, still giving their careers everything!"
    ter default "I dunno if we could reach them... to tell the truth, it's been a while. Like, with a capital W." 
    morg hospital aha "All the more reason to get them on board."
    morg sad "Terrie, this is something we won't have- we haven't had - for ages."
    ter "Well..."
    ter happy "I’m sure someone can make the time if we ask nicely!"
    morg default "Oh, we'll ask, alright." 
    morg "You call Finn, I'll get in touch with Mina." 
    morg playful "And, hey, if he's slow to pick up, introduce yourself as the pizza guy." 
    morg "You know how he is." 
    ter inthought "Girl, he has our contacts saved. Be for real."
    ter default "Oh well, here we go, then! Gimme one sec while I just..."
    hide ter with dissolve
    #Exit Terrie. 
    morg default "Right, now, my phone. Where oh where oh where is—"
    morg sad "Ah. Right. Only 1%% left."
    morg default "You won't mind if I use yours? Thanks."
    play sound "audio/sfx/cell_ring.mp3"
    "A dial-tone can be heard. Silence while the phone rings."
    morg "...Hey, what's with that look?"
    #Further beat.
    morg tense "You saw it too, didn't you?" 
    "After some feedback and mic bumping on the other side of the phone, Mina picks up."
    #Pop-in chibi MINA.
    show screen minaphone
    show mina chibi default at minachibi_transform, minaphone_pos with dissolve:
        xoffset 10
        additive .1
        matrixcolor ContrastMatrix(1.2)
        pause .15
    mina "—llo? Hello? You there?" 
    morg happy "Mina. It's me, Morgan. I'm here with the others." 
    morg inthought "Well, just Terrie and—" 
    show morg default
    mina overjoyed "Get outta town, MORGAN?! Girly it's been forever! How are things?!" 
    mina pained "Uh, I mean, outside of the... hospital stuff." 
    show mina default
    morg playful "That's why I'm calling." 
    morg "I've got a day outside to myself, and I was thinking of crossing a few items off of my to-do list." 
    morg default "In the company of whoever I wished." 
    mina overjoyed "And you thought of me? D'aww."
    mina default "What notice period am I lookin' at?" 
    morg playful "None. Obviously."
    #Beat.
    mina happy "Man, it really has been a million years." 
    mina nervous "Ugh, how do I put this? for the last few months, streaming's gone so well that I, uh..."
    mina "LA called, and I went. Like, for good."
    mina pained "Morgan, I really wanna be there, like, really really, but with the timings and all I don't think I can—" 
    morg sad "It’s fine."
    mina nervous "...You sure?"
    morg happy "Yes, really, Mina."
    mina default "I can try making changes or something—"
    morg sad "i promise."
    morg "Hearing from you's good enough for me."
    morg "Next time we all want to be in the same place together, you'll know first."
    morg happy "And congratulations on the streaming blow-up. You really deserved it."
    mina "Morgan..."
    mina nervous "You better tell me how things went after today, 'kay?"
    morg default "You got it."
    mina default "Mhm... listen, uh, I had a stream to set up for like, five minutes ago, so I gotta bounce."
    morg playful "No worries! Go to work!"
    morg "Everyone will be cheering you on. We'll talk soon. Lots of love from us all."
    mina overjoyed "Okay thank you guys miss you talk later byeeeeeee~! Sorry again bye gang. Buh-bye."
    "Awkward second of Mina's clothes rustling against her phone's microphone before she hangs up."
    show mina at minachibi_transform, minaphone_pos:
        xzoom 1 yzoom 1 alpha 1 matrixcolor BrightnessMatrix(0.0)
        easeout .2 xzoom 0 yzoom 1.2 matrixcolor BrightnessMatrix(0.3)
        parallel:
            easeout .2 alpha 0
    pause .1
    hide screen minaphone with dissolve
    pause .25
    morg sad "Bye."
    play sound "audio/sfx/cell_hangup.mp3"
    #Emphasis on sudden gloom from Morgan. Enter Terrie from the right.
    show ter hospital default at centerstage with dissolve:
        xpos .15
    ter inthought "Oh, that guy!"
    morg "No luck?"
    ter default "Nada. How about Mina?"
    morg "..."
    ter sad "Oh, yeah, the career..."
    ter playful "Well, uh, I'm sure we can make today work with just the four of us!"
    morg default "We can. But we won't."
    morg "A little break from his hardships would do wonders for Finn. I would know."
    morg playful "That's why we have to tell him {i}in person." 
    morg "Guys, get out something to write with. I'm amending our master plan."
    morg default "New order, phase one: Make Finn Smile Again."
    ter happy "I mean, if you can manage a grin, no excuses for him."
    #Morgan smiles again.
    show morg hospital happy at centerstage with dissolve
    ter "EXACTLY! Just like that!"
    ter default "Now, if we're kickin' this mission Off..."
    stop music fadeout 10.0
    ter "We gotta go back to school."
    jump act2
