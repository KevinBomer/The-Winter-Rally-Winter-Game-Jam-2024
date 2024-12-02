init python:
#Dynamic Sprite System-Each category represents a folder in the Images section. These will be auto-defined.
   # Automatically define the BGs, CGs, and some UI elements
   DefineImages('cgs')
   DefineImages('bgs', prepend='bg')
   DefineImages('mainmenu', prepend='mm')
   # define the composite sprites with LayeredImages, blinking eyes and flapping mouth
   DefineImages("sprites", composite=True)

   layerorder = ['hair', 'base', 'arms', 'armout','armwave','tail','mouth','eyes','brow','blush','anger','sweatdrop','nervous']
   DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'Kan':.85,'Rin':.6,'Kyou':.9, 'Maya': .9, 'Youk':.9, 'Char':.65}, sides=['Kan', 'Rin', 'Kyou','Maya','Youk','Char'])

   #Dynamic Sprite Emote Maps
   #MapEmote('war hugesmile',  'war md_hugesmile ed_bigsmile blush')
   # override some default eye blink and mouth flap behaviours
   #image war_ed_default = BlinkEyes("war_e_default", "war_ec_grin")
   # image war_md_hugesmile = FlapMouth("war_mc_smug", "war_m_bigsmile")

####Kanna Example
   MapEmote('Kan smile worried eo', 'Kan base mdo_happy ed_default brow_sad')
   
