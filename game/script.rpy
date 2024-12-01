######################### 
# Character Declaration #
#########################
# Declare characters used by this game. The color argument colorizes the
# name of the character. Callback, Image, and Voice_tag identify a file as relating to
# this character. 

define e = Character("Eileen")
define mc = Character("MCName", callback=speaker("mc"), image="mc", voice_tag="mc")
define li = Character("LiName_Dynamic", dynamic=True, callback=speaker("li"), image="li", voice_tag="li")
#Use this to have a voiced narrator #
define nar = Character(name=None, callback=speaker("MCName"), voice_tag="mc")
#Use this to define a different name for a character before we learn their name #
default LiName_Dynamic = "???"


#########################
#Default Solids, Masks
#########################
#Define some default colors
image bg black = "#000"
image white = "#fff"

#Define some default mask shaders
#define paintmask = ImageDissolve("mask.jpg", 1.5, ramplen=256)


#########################
# Default Audio Volume Preferences
#########################
define config.default_music_volume = .5
define config.default_sfx_volume = .5
define config.default_voice_volume = .5


#########################
# Text Speed and Auto Forward Time
#########################
define config.default_text_cps = 0
default preferences.afm_time = 7


#########################
# The game starts here.
#########################
label start:
    # Enable the 3D stage and set the camera to it's defult position.
    camera:
        perspective True

    scene bg black

     # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
