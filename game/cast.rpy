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

#ATL transforms


#Dissolves
define paintmask = ImageDissolve("images/gui/paintmask.jpg", 1.0, ramplen=256)
define paintmask2 = ImageDissolve("images/gui/paintmask.jpg", .5, ramplen=256, reverse=False, time_warp=_warper.ease)
