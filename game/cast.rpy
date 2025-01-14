# CHARACTER DEFINITIONSV
define mc = Character("[povname]", image = "mc", voice_tag = "mc", color = "#ffffffff")
define morg = Character("Morgan", image = "morg", voice_tag = "morg",color = "#ffffffff")
define mina = Character("Mina", image = "mina", voice_tag = "mina",color = "#ffffffff")
define fin = Character("Finn", image = "fin", voice_tag = "fin",color = "#ffffffff")
define ter = Character("Terrie", image = "ter", voice_tag = "ter", color = "#ffffffff")
define yum = Character("Miya", image = "miya", voice_tag = "miya", color = "#ffffffff")
define mortis = Character("Mortis", voice_tag = "mortis", color = "#000000ff")

define slowerdissolve = Dissolve(2.0)
define slowdissolve = Dissolve(1.0)

#CHARACTER SPRITESV
image morgph = "sprites/morg_placeholder.png"
image finph = "sprites/fin_placeholder.png"
image terph = "sprites/ter_placeholder.png"

#BACKGROUNDSV
image nightsky = Image("bgs/Night_Sky.png", oversample=1.8125)
image purgatory = Image("bgs/Purgatory.png", oversample=1.8125)
image hilltop = Image("bgs/hilltop.png", oversample=1.8125)
image ferriswheel = Image("bgs/Ferris_wheel.png", oversample=1.8125)
image topofferriswheel = Image("bgs/topofferriswheel.png", oversample=1.8125)
image corridor day = Image("bgs/Corridor.png", oversample=1.8125)
image corridor night = Image("bgs/Corridor_night.png", oversample=1.8125)
image corridor dim = Image("bgs/Corridor_night.png", oversample=1.8125)
image dorm = Image("bgs/dorm.png", oversample=1.8125)
image sushishop = Image("bgs/sushishop.png", oversample=1.8125)
image icerink = Image("bgs/icerink.png", oversample=1.8125)
image fadetoblack = Image("images/faded.png", oversample=1.8125)

#CGSV

init python:
###Initial Audio Cues Setup
# Define every song with an alias

    menu_theme = "audio/Menu_Music_LOOP.ogg"
    introduction = "audio/Introduction_Memories.mp3"
    hospital = "audio/Hospital_Music_LOOP_2_test.ogg"
    finn_dorm = "audio/Finns_Dorm_Room_Music_LOOP.ogg"
    finn_minigame = "audio/Minigame_Music.ogg"

    # alias : "Song Title",
    music_dictionary = {
        menu_theme : "Good Morning, Morgan",
        introduction : "Voices Of The Past",
        hospital : "Purgatory",
        finn_dorm : "Finn's Study",
        finn_minigame : "Sweet Talker",








    }

    # Define every sound with an alias
    # door_close = "door closing sfx.wav"
    # alias : "Sound description."

    ### Audio Cues
    # These are used in place of "play music" and "play sound". In your script:
    # $ play_sfx(door_close)
    # will play the door close sound effect.
    # $ play_music(lamentoso,10)
    # will play "lamentoso" with a 10 second fadein.

    def play_sfx(sound_alias,fade=0):
        renpy.sound.play(sound_alias,fadein=fade)
        if persistent.audio_cues:
            renpy.notify("SFX: {i}" + sfx_dictionary[renpy.sound.get_playing('sound')] + "{/i}")

    def play_music(music_alias,fade=0):
        renpy.music.play(music_alias,fadein=fade)
        if persistent.audio_cues:
            renpy.notify("Now Playing: " + music_dictionary[renpy.music.get_playing('music')])
    ###

#Dissolves
define paintmask = ImageDissolve("images/gui/paintmask.jpg", 1.0, ramplen=256)
define paintmask2 = ImageDissolve("images/gui/paintmask.jpg", .5, ramplen=256, reverse=False, time_warp=_warper.ease)
