init 999 python:
    config.locked = False
    config.keymap['game_menu'] = []

    # And create an alternative one.
    config.keymap['phone_menu'] = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],
    config.keymap ['hide_windows'] = [ 'noshift_K_h' ],
    if _viewers.check_version(23060707):
        config.keymap["action_editor"] = ['shift_K_p']
        config.keymap["image_viewer"] =  ['shift_K_u']
        config.keymap["sound_viewer"] =  ['shift_K_s']
    else:
        config.keymap["action_editor"] = ['P']
        config.keymap["image_viewer"] =  ['U']
        config.keymap["sound_viewer"] =  ['S']
    config.locked = True
   # Su+press RenPy's "game menu" button, the cause of many woes.
