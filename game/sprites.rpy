transform fin_sprite_resize:
    xsize 435 fit "contain"

layeredimage fin:

    at fin_sprite_resize

    group base auto:
        attribute hospital default

    group face variant "hospital" auto:
        if_any ["hospital"]
        attribute default default

    group face variant "c-day" auto:
        if_any ["c-day"]
        attribute default default

    group face variant "c-night" auto:
        if_any ["c-night"]
        attribute default default

    group face variant "fireworks" auto:
        if_any ["fireworks"]
        attribute default default

    group face variant "icerink" auto:
        if_any ["icerink"]
        attribute default default

    group face variant "sky" auto:
        if_any ["sky"]
        attribute default default

    group face variant "spot" auto:
        if_any ["spot"]
        attribute default default

    group glasses_state:
        attribute glasses_on default null
        attribute glasses_off null

    group glasses auto:
        if_any ["glasses_on"]
        attribute hospital default

###############

transform fin_chibi_resize:
    xsize 418 fit "contain"

layeredimage fin_chibi:

    # at fin_chibi_resize

    always:
        "fin_chibi_base"

    group face auto:
        attribute default default

    group glasses:
        attribute glasses_on default "fin_chibi_glasses"
        attribute glasses_off null


###############

transform morg_sprite_resize:
    xsize 690 fit "contain"

layeredimage morg:

    at morg_sprite_resize

    group base auto:
        attribute hospital default

    group face variant "hospital" auto:
        if_any ["hospital"]
        attribute default default

    group face variant "c-day" auto:
        if_any ["c-day"]
        attribute default default

    group face variant "c-night" auto:
        if_any ["c-night"]
        attribute default default

    group face variant "fireworks" auto:
        if_any ["fireworks"]
        attribute default default

    group face variant "icerink" auto:
        if_any ["icerink"]
        attribute default default

    group face variant "sky" auto:
        if_any ["sky"]
        attribute default default

    group face variant "spot" auto:
        if_any ["spot"]
        attribute default default


###############


transform ter_sprite_resize:
    xsize 546 fit "contain"

layeredimage ter:

    at ter_sprite_resize

    group base auto:
        attribute hospital default

    group face variant "hospital" auto:
        if_any ["hospital"]
        attribute default default

    group face variant "c-day" auto:
        if_any ["c-day"]
        attribute default default

    group face variant "c-night" auto:
        if_any ["c-night"]
        attribute default default

    group face variant "fireworks" auto:
        if_any ["fireworks"]
        attribute default default

    group face variant "icerink" auto:
        if_any ["icerink"]
        attribute default default

    group face variant "sky" auto:
        if_any ["sky"]
        attribute default default

    group face variant "spot" auto:
        if_any ["spot"]
        attribute default default


###############

transform mina_sprite_resize:
    xsize 604 fit "contain"

layeredimage mina:

    at mina_sprite_resize

    always:
        "mina_base"

    group face auto:
        attribute default default

transform mina_chibi_resize:
    xsize 418 fit "contain"

layeredimage mina_chibi:

    at mina_chibi_resize

    always:
        "mina_chibi_base"

    group face auto:
        attribute default default


###############

transform mortis_sprite_resize:
    zoom 0.5

layeredimage mortis:

    at mortis_sprite_resize

    always:
        "mortis_base"

    group face auto:
        attribute default default
