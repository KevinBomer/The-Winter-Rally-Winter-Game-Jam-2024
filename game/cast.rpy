# CHARACTER DEFINITIONSV
define you = Character("[povname]", color = "#ffffffff")
define morg = Character("Morgan", color = "#ffffffff")
define min = Character("Mina", color = "#ffffffff")
define fin = Character("Finn", color = "#ffffffff")
define ter = Character("Terrie", color = "#ffffffff")
define yum = Character("Owner", color = "#ffffffff")
define mortis = Character("Death", color = "#000000ff")

define slowerdissolve = Dissolve(2.0)
define slowdissolve = Dissolve(1.0)

#CHARACTER SPRITESV

#BACKGROUNDSV
image nightsky = Image("bgs/Night_Sky.png", oversample=1.8125)
image purgatory = Image("bgs/Purgatory.png", oversample=1.8125)
image hilltop = Image("bgs/Top_of_the_world.png", oversample=1.8125)
image corridor = Image("bgs/Corridor.png", oversample=1.8125)
image fadetoblack = Image("images/faded.png", oversample=1.8125)

#CGSV

#ATL transforms


#Dissolves
define paintmask = ImageDissolve("images/gui/paintmask.jpg", 1.0, ramplen=256)
define paintmask2 = ImageDissolve("images/gui/paintmask.jpg", .5, ramplen=256, reverse=False, time_warp=_warper.ease)