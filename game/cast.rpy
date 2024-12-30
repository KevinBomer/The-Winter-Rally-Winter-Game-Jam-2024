# CHARACTER DEFINITIONSV
define mc = Character("[povname]", image = "mc", voice_tag = "mc",callback=speaker("mc"), color = "#ffffffff")
define morg = Character("Morgan", image = "morg", voice_tag = "morg",callback=speaker("morg"),color = "#ffffffff")
define mina = Character("Mina", image = "mina", voice_tag = "mina",callback=speaker("mina"), color = "#ffffffff")
define fin = Character("Finn", image = "fin", voice_tag = "fin",callback=speaker("fin"), color = "#ffffffff")
define ter = Character("Terrie", image = "ter", voice_tag = "ter",callback=speaker("ter"), color = "#ffffffff")
define yum = Character("Miya", image = "miya", voice_tag = "miya", callback=speaker("miya"), color = "#ffffffff")
define mortis = Character("Death", voice_tag = "mortis",callback=speaker("mortis"), color = "#000000ff")

define slowerdissolve = Dissolve(2.0)
define slowdissolve = Dissolve(1.0)

#CHARACTER SPRITESV
image morgph = "sprites/morg_placeholder.png"
image finph = "sprites/fin_placeholder.png"
image terph = "sprites/ter_placeholder.png"

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
