# init python:
# #Dynamic Sprite System-Each category represents a folder in the Images section. These will be auto-defined.
#    # Automatically define the BGs, CGs, and some UI elements
#    DefineImages('cgs')
#    DefineImages('bgs', prepend='bg')
#    DefineImages('mainmenu', prepend='mm')
#    # define the composite sprites with LayeredImages, blinking eyes and flapping mouth
#    DefineImages("sprites", composite=True)

#    layerorder = ['base', 'expression','glasses']
#    DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'morg':1.3,'mc':1.4,'mina':1.4, 'fin': 1.4, 'ter':1.4, 'yum':1.4, 'mortis':1.4}, sides=['mxxorg', 'xxter', 'xxmina','xxfin','xxyum','xxmortis'])


# ####NOTE: This script requires each character to have a file "e default" and "m default" in order to work properly. For this game, they are 25x25 blank transparent PNGs.
# #### All Components must have a base.png and at least 1 default for each layer called "layer default"
# #### All pose and lighting variations can be placed in their own directories under the character's directory. e default and m default only need to exist in 1 set of sprites.
# #### Directories must not have spaces.

#    #Dynamic Sprite Emote Maps
#    #MapEmote('war hugesmile',  'war md_hugesmile ed_bigsmile blush')
#    # override some default eye blink and mouth flap behaviours
#    #image war_ed_default = BlinkEyes("war_e_default", "war_ec_grin")
#    # image war_md_hugesmile = FlapMouth("war_mc_smug", "war_m_bigsmile")

# #### Example
#    MapEmote('morg cnight aha', 'morg corridor-night base expression_aha')
#    MapEmote('morg sky happy', 'morg night-sky base expression_happy')
#    MapEmote('morg fw neutral', 'morg fireworkferriswheel base expression_default')
#    MapEmote('morg hospital inthought', 'morg hospital-dorm base expression_inthought')
#    MapEmote('morg hospital playful', 'morg hospital-dorm base expression_playful')
#    MapEmote('morg hospital default', 'morg hospital-dorm base expression_default')
#    MapEmote('morg hospital sad', 'morg hospital-dorm base expression_sad')
#    MapEmote('morg hospital happy', 'morg hospital-dorm base expression_happy')
#    MapEmote('morg hospital aha', 'morg hospital-dorm base expression_aha')
#    MapEmote('morg hospital tense', 'morg hospital-dorm base expression_tense')

#    MapEmote('morg c-day sad', 'morg corridor-day base expression_sad')
#    MapEmote('morg c-day default', 'morg corridor-day base expression_default')

#    ###Terrie
#    MapEmote('ter sky default', 'ter sky base expression_default')
#    MapEmote('ter hospital tense', 'ter hospital-dorm base expression__hospitalanddorm_tense')
#    MapEmote('ter hospital inthought', 'ter hospital-dorm base expression__hospitalanddorm_inthought')
#    MapEmote('ter hospital happy', 'ter hospital-dorm base expression__hospitalanddorm_happy')
#    MapEmote('ter hospital aha', 'ter hospital-dorm base expression__hospitalanddorm_aha')
#    MapEmote('ter hospital default', 'ter hospital-dorm base expression_default')
#    MapEmote('ter hospital hurt', 'ter hospital-dorm base expression__hospitalanddorm_hurt')
#    MapEmote('ter hospital playful', 'ter hospital-dorm base expression__hospitalanddorm_playful')
#    MapEmote('ter hospital sad', 'ter hospital-dorm base expression__hospitalanddorm_melancholy')
#    MapEmote('ter hospital smilehurt', 'ter hospital-dorm base expression__hospitalanddorm_smilehurt')
#    MapEmote('ter hospital grief', 'ter hospital-dorm base expression_default')
#    MapEmote('ter hospital embarrassed', 'ter hospital-dorm base expression__hospitalanddorm_embarassed')

#    MapEmote('ter c-day playful', 'ter corridor-day base expression__daycorrdior_playful')
#    MapEmote('ter c-day tense', 'ter corridor-day base expression__daycorrdior_tense')
#    MapEmote('ter c-day smile', 'ter corridor-day base expression__daycorrdior_happy')
#    MapEmote('ter c-day grief', 'ter corridor-day base expression__daycorrdior_grief')
#    MapEmote('ter c-day melancholy', 'ter corridor-day base expression__daycorrdior_melancholy')
#    MapEmote('ter c-day happy', 'ter corridor-day base expression__daycorrdior_happy')
#    MapEmote('ter c-day default', 'ter corridor-day base expression_default')

#    ###Mina
#    MapEmote('mina hill default', 'mina HILL base expression_default')

#    ##Mina Chibi
#    MapEmote('mina chibi default', 'mina Chibi base expression_default')
#    MapEmote('mina chibi happy', 'mina Chibi base expression_Happy')
#    MapEmote('mina chibi nervous', 'mina Chibi base expression_Nervous')
#    MapEmote('mina chibi overjoyed', 'mina Chibi base expression_Overjoyed')
#    MapEmote('mina chibi pained', 'mina Chibi base expression_Pained')

#    ###Fin
#    MapEmote('fin sky default', 'fin sky base expression_default glasses_default')
#    MapEmote('fin hospital default', 'fin hospital-dorm base base expression_default glasses_default')
#    MapEmote('fin hospital inthought', 'fin hospital-dorm base base expression_inthought glasses_default')
#    MapEmote('fin hospital tense', 'fin hospital-dorm base expression_tense glasses_default')
#    MapEmote('fin hospital aha', 'fin hospital-dorm base expression_aha glasses_default')
#    MapEmote('fin hospital melancholy', 'fin hospital-dorm base expression_melancholy glasses_default')
#    MapEmote('fin hospital upset', 'fin hospital-dorm base expression_upset glasses_default')
#    MapEmote('fin hospital playful', 'fin hospital-dorm base expression_playful glasses_default')
#    MapEmote('fin hospital happy', 'fin hospital-dorm base expression_happy glasses_default')


#    ###Fin Chibis
#    MapEmote('fin chibi neutral', 'fin chibi base expression_default glasses_default')
#    MapEmote('fin chibi sad', 'fin chibi base expression_bad glasses_default')
#    MapEmote('fin chibi happy', 'fin chibi base expression_good glasses_default')