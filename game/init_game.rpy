## Define variables that are meant to be saved with save games and rollbacks with "default"
default game_player = player()

init +1 python:

################################################################################
## System Vars
################################################################################

    config.developer = True
    renpy.start_predict_screen('main_menu')
    renpy.start_predict("gui/mainmenu*.*")
    #renpy.start_predict_screen(main_menu)