init python:
#Dynamic Sprite System-Each category represents a folder in the Images section. These will be auto-defined.
   # Automatically define the BGs, CGs, and some UI elements
   DefineImages('cgs')
   DefineImages('bgs', prepend='bg')
   DefineImages('mainmenu', prepend='mm')
   # define the composite sprites with LayeredImages, blinking eyes and flapping mouth
   DefineImages("sprites", composite=True)

   layerorder = ['base', 'expression','glasses']
   DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'morg':1.4,'mc':1.4,'mina':1.4, 'fin': 1.4, 'ter':1.4, 'yum':1.4, 'mortis':1.4}, sides=['Kan', 'Rin', 'Kyou','Maya','Youk','Char'])


####NOTE: This script requires each character to have a file "e default" and "m default" in order to work properly. For this game, they are 25x25 blank transparent PNGs. 
#### All Components must have a base.png and at least 1 default for each layer called "layer default"
#### All pose and lighting variations can be placed in their own directories under the character's directory. e default and m default only need to exist in 1 set of sprites. 
#### Directories must not have spaces. 

   #Dynamic Sprite Emote Maps
   #MapEmote('war hugesmile',  'war md_hugesmile ed_bigsmile blush')
   # override some default eye blink and mouth flap behaviours
   #image war_ed_default = BlinkEyes("war_e_default", "war_ec_grin")
   # image war_md_hugesmile = FlapMouth("war_mc_smug", "war_m_bigsmile")

#### Example
   MapEmote('morg cnight aha', 'morg corridor-night base expression_aha')
   MapEmote('morg sky happy', 'morg night-sky base expression_happy')
   MapEmote('morg fw neutral', 'morg fireworkferriswheel base expression_default')
