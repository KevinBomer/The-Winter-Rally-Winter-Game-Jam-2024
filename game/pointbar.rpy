### Styles


## Healthbar and expbar screens ###############################################################
##
## This screen is used to display and animate the healthbar and expbar
##
## EXAMPLE 1, show screen healthbar(name, from_health, to_health, duration_to_stay_on_screen):
## show screen healthbar("Kanna", 0, 1, 2.5)
##
## EXAMPLE 2, show screen healthbar_multiple(list_of_healthbar_values, duration_to_stay_on_screen):
## show screen healthbar_multiple([
##         ("Kanna", 0, 1),
##         ("Maya", 5, 4),
##         ("Charlotte", 2, 4),
##     ], 2.5
## )
##
## EXAMPLE 3, show screen expbar(name, from_exp, to_exp, duration_to_stay_on_screen):
## show screen expbar("Kanna", 0.1, 1.4, 2.5)
## show screen expbar2("Maya", 0.1, 1.4, 2.5)
## show screen expbar3("Charlotte", 0.1, 1.4, 2.5)
##
## EXAMPLE 4, $ show_expbar_multiple(list_of_healthbar_values, duration_to_linger_on_screen)
## $ show_expbar_multiple((
##         ("Kanna", 0.0, 1.4),
##         ("Maya", 5.0, 3.6),
##         ("Charlotte", 2.1, 4.9),
##     ), 2.5
## )
##
default healthbar_max = 5

init python:
    import math
    def show_expbar_multiple(name_exp, duration=2.5):
        pointmapping = {
            "Love Interest" :       [0.24, 1.41, 2.32, 3.52, 4.42, 5.62, 6.43, 7.72, 8.53, 9.44]
        }
        durations = []
        for i in range(len(name_exp)):
            name, from_exp, to_exp = name_exp[i]
            if i == 1:
                s_name = "expbar2"
            elif i == 2:
                s_name = "expbar3"
            else:
                s_name = "expbar"
            if name in pointmapping:
                points = pointmapping[name]
                from_exp = points[from_exp % 10] + int(from_exp / 10) * 10
                to_exp = points[to_exp % 10] + int(to_exp / 10) * 10
            else:
                from_exp += 0.5
                to_exp += 0.5
            durations.append(abs(to_exp - from_exp))
            renpy.show_screen(s_name, name, from_exp, to_exp, duration=None)
        total_duration = 0.6 + max(durations) + duration
        if duration is not None and duration is not 0:
            renpy.pause(delay=0.6 + max(durations), hard=True)
            renpy.pause(delay=duration)
            hide_all_expbar()
            renpy.pause(delay=0.6)

    def hide_all_expbar():
        renpy.hide_screen("expbar")
        renpy.hide_screen("expbar2")
        renpy.hide_screen("expbar3")

transform healthbar_transform(align=(0.95, 0.03), yoffset=-100, duration=0.6):
    on show:
        alpha 0
        align align yoffset yoffset
        easein duration yoffset 0 alpha 1
    on hide:
        easeout 0.6 yoffset yoffset alpha 0

transform healthbar_inner_transform(from_val, to_val, startdelay=0.6, duration=1.0):
    xsize from_val
    startdelay
    linear duration xsize to_val

transform expbar_inner_transform(from_val, to_val, startdelay=0.6, duration=1.0):
    crop (0, 0, from_val, 41)
    startdelay
    linear duration crop (0, 0, to_val, 41)

transform expbar_levelup_transform():
    align (0.5, 0.5)
    easeout 0.1 zoom 1.3 offset (-10, -10)
    easein 0.6 zoom 1.0 offset (0, 0)

transform expbar_levelup_particles_transform():
    align (0.5, 0.5) zoom 1.0 alpha 1
    parallel:
        linear 0.3 zoom 3.0
    parallel:
        0.1
        linear 0.2 alpha 0

transform expbar_leveldown_transform():
    ease 0.1 xoffset 5
    ease 0.1 xoffset -5
    ease 0.1 xoffset 5
    ease 0.1 xoffset -5
    ease 0.1 xoffset 0

screen healthbar(name, from_health, to_health, duration=2.5, align=(0.95, 0.03), yoffset=-100):
    fixed:
        at healthbar_transform(align=(0.95, 0.03), yoffset=-100)
        xsize 600
        ysize 50
        hbox:
            spacing 20
            fixed:
                xsize 180
                text name:
                    size 40
                    text_align 1.0
                    xalign 1.0
                    outlines [ (2, "#000") ]
            fixed:
                xsize 400
                ysize 50
                frame:
                    background Frame('gui/healthbar/healthbar_frame.png', 6, 6, 6, 6)
                    xalign 0.0
                    xsize 400
                    ysize 50
                frame:
                    background Frame('gui/healthbar/healthbar_fill.png', 6, 6, 6, 6)
                    at healthbar_inner_transform(int(1.0 * from_health / healthbar_max * 400), int(1.0 * to_health / healthbar_max * 400))
                    xalign 0.0
                    ysize 50
                frame:
                    background Tile('gui/healthbar/healthbar_overlay.png')
                    margin (6, 6)
                    xalign 0.0
                    xsize 400
                    ysize 50
    if duration is not None:
        timer duration action Hide("healthbar")

screen healthbar_multiple(name_health, duration=2.5):
    for i in range(len(name_health)):
        $ name, from_health, to_health = name_health[i]
        fixed:
            at healthbar_transform(align=(0.2, 0.3+0.08*i), yoffset=-100-100*i)
            xsize 600
            ysize 200
            xalign 0.95
            use healthbar(name, from_health, to_health, None)
    if duration is not None:
        timer duration action Hide("healthbar_multiple")



screen expbar(name, from_exp, to_exp, duration=2.5, showduration=0.6, align=(0.2, 0.3), yoffset=-100, levelup=0):
    $ from_level = int(math.floor(from_exp))
    $ to_level = int(math.floor(to_exp))
    $ start_fraction = from_exp % 1.0
    if to_level > from_level:
        $ exp_to_next_level = 1.0 - start_fraction
        $ end_fraction = 1.0
    elif from_level > to_level:
        $ exp_to_next_level = start_fraction
        $ end_fraction = 0.0
    else:
        $ exp_to_next_level = abs(to_exp - from_exp)
        $ end_fraction = to_exp % 1.0

    fixed:
        at healthbar_transform(align=(0.2, 0.3), yoffset=-100, duration=showduration)
        xsize 680
        ysize 50
        hbox:
            spacing 15
            fixed:
                xsize 180
                yoffset 2
                text name:
                    size 32
                    text_align 1.0
                    xalign 1.0
                    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
                    bold True
            fixed:
                xsize 400
                ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_frame.png', 0, 0, 0, 0)
                    xalign 0.0
                    xsize 394
                    ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_fill.png', 0, 0, 0, 0)
                    at expbar_inner_transform(int(1.0 * start_fraction * 385), int(1.0 * end_fraction * 385), startdelay=showduration, duration=exp_to_next_level)
                    xalign 0.0
                    xysize (385, 41)
                    offset (2.5, 2.5)
            fixed:
                yoffset 2
                if levelup > 0:
                    at expbar_levelup_transform
                elif levelup < 0:
                    at expbar_leveldown_transform
                fixed:
                    add 'gui/healthbar/expbar_level.png'
                    xysize (50, 50)
                    offset (-10, -10)
                fixed:
                    xysize (50, 50)
                    text str(from_level):
                        color '#fff'
                        align (0.5, 0.5)
                        text_align 0.5
                        size 40
                        outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
                        bold True
                        offset (-4, -4)
                if levelup > 0:
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
    if to_level > from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar"),
                                                    Show("expbar", None, name, from_level+1, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=1)]
    elif to_level < from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar"),
                                                    Show("expbar", None, name, from_level-0.01, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=-1)]
    elif duration is not None:
        timer (showduration+exp_to_next_level+duration) action Hide("expbar")

screen expbar2(name, from_exp, to_exp, duration=2.5, showduration=0.6, align=(0.95, 0.03), yoffset=-100, levelup=0):
    $ from_level = int(math.floor(from_exp))
    $ to_level = int(math.floor(to_exp))
    $ start_fraction = from_exp % 1.0
    if to_level > from_level:
        $ exp_to_next_level = 1.0 - start_fraction
        $ end_fraction = 1.0
    elif from_level > to_level:
        $ exp_to_next_level = start_fraction
        $ end_fraction = 0.0
    else:
        $ exp_to_next_level = abs(to_exp - from_exp)
        $ end_fraction = to_exp % 1.0

    fixed:
        at healthbar_transform(align=(0.95, 0.11), yoffset=-200, duration=showduration)
        xsize 680
        ysize 50
        hbox:
            spacing 15
            fixed:
                xsize 180
                yoffset 2
                text name:
                    size 32
                    text_align 1.0
                    xalign 1.0
                    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
                    bold True
            fixed:
                xsize 400
                ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_frame.png', 0, 0, 0, 0)
                    xalign 0.0
                    xsize 394
                    ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_fill.png', 0, 0, 0, 0)
                    at expbar_inner_transform(int(1.0 * start_fraction * 385), int(1.0 * end_fraction * 385), startdelay=showduration, duration=exp_to_next_level)
                    xalign 0.0
                    xysize (385, 41)
                    offset (2.5, 2.5)
            fixed:
                yoffset 2
                if levelup > 0:
                    at expbar_levelup_transform
                elif levelup < 0:
                    at expbar_leveldown_transform
                fixed:
                    add 'gui/healthbar/expbar_level.png'
                    xysize (50, 50)
                    offset (-10, -10)
                fixed:
                    xysize (50, 50)
                    text str(from_level):
                        color '#fff'
                        align (0.5, 0.5)
                        text_align 0.5
                        size 40
                        outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
                        bold True
                        offset (-4, -4)
                if levelup > 0:
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
    if to_level > from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar2"),
                                                    Show("expbar2", None, name, from_level+1, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=1)]
    elif to_level < from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar2"),
                                                    Show("expbar2", None, name, from_level-0.01, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=-1)]
    elif duration is not None:
        timer (showduration+exp_to_next_level+duration) action Hide("expbar2")

screen expbar3(name, from_exp, to_exp, duration=2.5, showduration=0.6, align=(0.95, 0.03), yoffset=-100, levelup=0):
    $ from_level = int(math.floor(from_exp))
    $ to_level = int(math.floor(to_exp))
    $ start_fraction = from_exp % 1.0
    if to_level > from_level:
        $ exp_to_next_level = 1.0 - start_fraction
        $ end_fraction = 1.0
    elif from_level > to_level:
        $ exp_to_next_level = start_fraction
        $ end_fraction = 0.0
    else:
        $ exp_to_next_level = abs(to_exp - from_exp)
        $ end_fraction = to_exp % 1.0

    fixed:
        at healthbar_transform(align=(0.95, 0.19), yoffset=-300, duration=showduration)
        xsize 680
        ysize 50
        hbox:
            spacing 15
            fixed:
                xsize 180
                yoffset 2
                text name:
                    size 32
                    text_align 1.0
                    xalign 1.0
                    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
                    bold True
            fixed:
                xsize 400
                ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_frame.png', 0, 0, 0, 0)
                    xalign 0.0
                    xsize 394
                    ysize 50
                frame:
                    background Frame('gui/healthbar/expbar_fill.png', 0, 0, 0, 0)
                    at expbar_inner_transform(int(1.0 * start_fraction * 385), int(1.0 * end_fraction * 385), startdelay=showduration, duration=exp_to_next_level)
                    xalign 0.0
                    xysize (385, 41)
                    offset (2.5, 2.5)
            fixed:
                yoffset 2
                if levelup > 0:
                    at expbar_levelup_transform
                elif levelup < 0:
                    at expbar_leveldown_transform
                fixed:
                    add 'gui/healthbar/expbar_level.png'
                    xysize (50, 50)
                    offset (-10, -10)
                fixed:
                    xysize (50, 50)
                    text str(from_level):
                        color '#fff'
                        align (0.5, 0.5)
                        text_align 0.5
                        size 40
                        outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
                        bold True
                        offset (-4, -4)
                if levelup > 0:
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
                    fixed:
                        add 'gui/healthbar/expbar_particles.png'
                        at expbar_levelup_particles_transform
    if to_level > from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar3"),
                                                    Show("expbar3", None, name, from_level+1, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=1)]
    elif to_level < from_level:
        timer (showduration+exp_to_next_level) action [Hide("expbar3"),
                                                    Show("expbar3", None, name, from_level-0.01, to_exp, duration=duration,
                                                    showduration=0.0, align=align, yoffset=yoffset, levelup=-1)]
    elif duration is not None:
        timer (showduration+exp_to_next_level+duration) action Hide("expbar3")
