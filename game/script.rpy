# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(ctc="ctc", ctc_position="fixed")
define p = Character("[player_name]", ctc="ctc", ctc_position="fixed")
define n = Character("", ctc="ctc", ctc_position="fixed")

define ease = MoveTransition(0.5, enter=None, leave=None, enter_time_warp=_warper.ease, leave_time_warp=_warper.ease)

define config.dismiss_blocking_transitions = False
default _dismiss_pause = False

define dissolve = Dissolve(0.25)
define dissolve_cg = Dissolve(0.75)
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.5),
    Solid("#000"), Dissolve(0.5),
    True, Pause(0.5),
    True])
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(0.5),
    Solid("#000"), Dissolve(0.5),
    True, Pause(0.5),
    True])

define audio.t1 = "audio/bgm/1.ogg"        
define audio.t2 = "audio/bgm/2.ogg"          
define audio.t3 = "audio/bgm/3.ogg"         
define audio.t4 = "audio/bgm/4.ogg"          
define audio.t5 = "audio/bgm/5.ogg"       
define audio.t6 = "audio/bgm/6.ogg"        
define audio.t7 = "audio/bgm/7.ogg"     
define audio.t8 = "audio/bgm/8.ogg"     
define audio.t9 = "audio/bgm/9.ogg" 
define audio.t10 = "audio/bgm/10.ogg" 
define audio.tcredits = "audio/bgm/credits.ogg" 

define trida = Character("Trida", ctc="ctc", ctc_position="fixed")
define committee = Character("Student Committee", ctc="ctc", ctc_position="fixed")
define radit = Character("Radit", ctc="ctc", ctc_position="fixed")
define chie = Character("Chie", ctc="ctc", ctc_position="fixed")
define shy_classmate = Character("Shy Classmate", ctc="ctc", ctc_position="fixed")
define sabian = Character("Sabian", ctc="ctc", ctc_position="fixed")
define julia = Character("Julia", ctc="ctc", ctc_position="fixed")
define modelling_teacher = Character("Modelling Teacher", ctc="ctc", ctc_position="fixed")
define civics_teacher = Character("Civics Teacher", ctc="ctc", ctc_position="fixed")
define teacher = Character("Teacher", ctc="ctc", ctc_position="fixed")
define glasses_boy = Character("Glasses Boy", ctc="ctc", ctc_position="fixed")
define cap_boy = Character("Cap Boy", ctc="ctc", ctc_position="fixed")
define braided_girl = Character("Braided Girl", ctc="ctc", ctc_position="fixed")
define moderator = Character("Moderator", ctc="ctc", ctc_position="fixed")
define classmate_a = Character("Classmate A", ctc="ctc", ctc_position="fixed")
define classmate_b = Character("Classmate B", ctc="ctc", ctc_position="fixed")

default player_name = "You"
default current_week = "Prologue"
default splash_art = False
default current_splash_art = False
default trida_route = None
default mapAcquired = False
default player_has_bouquet = False
default tridaAffection = 0
default radit_affection = 0
default ch_affection = 0
default sabian_affection = 0
default julia_affection = 0

image bg classroom = "images/ddlc/class.png"
image bg rus_studio = "images/ddlc/club.png"
image bg grapos_field = "images/ddlc/corridor.png"
image bg gates_morning = "images/ddlc/residential.png"
image bg bedroom_late_afternoon = "images/ddlc/bedroom.png"
image bg teddy_cup = "images/ddlc/kitchen.png"
image bg room = "images/ddlc/bedroom.png"

image bg club = "images/ddlc/club.png"
image bg corridor = "images/ddlc/corridor.png"
image bg closet = "images/ddlc/closet.png"
image bg residential = "images/ddlc/residential.png"
image bg house = "images/ddlc/house.png"
image bg kitchen = "images/ddlc/kitchen.png"
image bg sayori_bedroom = "images/ddlc/sayori_bedroom.png"
image bg space_room = "images/ddlc/space_room.png"

init -1 python:
    TRIDA_ZOOM = 1.30
    TRIDA_YOFFSET = 240

    def trida_sprite(outfit, expr):
        path = f"images/trida/trida_{outfit}_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=TRIDA_ZOOM, yoffset=TRIDA_YOFFSET)
        return Placeholder("boy", text=f"Trida\n[{outfit.capitalize()}]\n{expr.capitalize()}")

    RADIT_ZOOM = 1.30
    RADIT_YOFFSET = 240

    def radit_sprite(expr="neutral", outfit="uniform"):
        specific_path = f"images/radit/radit_{outfit}_{expr}.png"
        fallback_path = "images/radit/radit.png"
        if renpy.loadable(specific_path):
            return Transform(specific_path, zoom=RADIT_ZOOM, yoffset=RADIT_YOFFSET)
        elif renpy.loadable(fallback_path):
            return Transform(fallback_path, zoom=RADIT_ZOOM, yoffset=RADIT_YOFFSET)
        return Placeholder("boy", text=f"Radit\n({expr.capitalize()})")

image trida = trida_sprite("uniform", "neutral")

image trida uniform neutral = trida_sprite("uniform", "neutral")
image trida uniform happy = trida_sprite("uniform", "happy")
image trida uniform sad = trida_sprite("uniform", "sad")
image trida uniform embarrassed = trida_sprite("uniform", "embarrassed")

image trida casual neutral = trida_sprite("casual", "neutral")
image trida casual happy = trida_sprite("casual", "happy")
image trida casual sad = trida_sprite("casual", "sad")
image trida casual embarrassed = trida_sprite("casual", "embarrassed")

image trida neutral = "trida uniform neutral"
image trida happy = "trida uniform happy"
image trida sad = "trida uniform sad"
image trida embarrassed = "trida uniform embarrassed"
image trida blush = "trida uniform embarrassed"

image trida smile = "trida uniform happy"
image trida laugh = "trida uniform happy"
image trida surprised = "trida uniform happy"
image trida nervous = "trida uniform embarrassed"
image trida crying = "trida uniform sad"
image trida annoyed = "trida uniform sad"

image trida casual blush = "trida casual embarrassed"
image trida casual smile = "trida casual happy"
image trida casual laugh = "trida casual happy"
image trida casual surprised = "trida casual happy"
image trida casual nervous = "trida casual embarrassed"
image trida casual crying = "trida casual sad"
image trida casual annoyed = "trida casual sad"

# Radit
image radit = radit_sprite()
image radit neutral = radit_sprite("neutral")
image radit smile = radit_sprite("smile")
image radit happy = radit_sprite("happy")
image radit laugh = radit_sprite("laugh")
image radit surprised = radit_sprite("surprised")
image radit sad = radit_sprite("sad")
image radit frown = radit_sprite("frown")
image radit amused = radit_sprite("amused")
image radit annoyed = radit_sprite("annoyed")

image radit uniform neutral = radit_sprite("neutral", "uniform")
image radit uniform smile = radit_sprite("smile", "uniform")
image radit uniform happy = radit_sprite("happy", "uniform")
image radit uniform laugh = radit_sprite("laugh", "uniform")
image radit uniform surprised = radit_sprite("surprised", "uniform")
image radit uniform sad = radit_sprite("sad", "uniform")
image radit uniform frown = radit_sprite("frown", "uniform")
image radit uniform amused = radit_sprite("amused", "uniform")
image radit uniform annoyed = radit_sprite("annoyed", "uniform")

image radit casual neutral = radit_sprite("neutral", "casual")
image radit casual smile = radit_sprite("smile", "casual")
image radit casual happy = radit_sprite("happy", "casual")
image radit casual laugh = radit_sprite("laugh", "casual")
image radit casual surprised = radit_sprite("surprised", "casual")
image radit casual sad = radit_sprite("sad", "casual")
image radit casual frown = radit_sprite("frown", "casual")
image radit casual amused = radit_sprite("amused", "casual")
image radit casual annoyed = radit_sprite("annoyed", "casual")

# Chie
image chie = Placeholder("girl", text="Chie")
image chie neutral = Placeholder("girl", text="Chie\n(Neutral)")
image chie smile = Placeholder("girl", text="Chie\n(Smile)")
image chie happy = Placeholder("girl", text="Chie\n(Happy)")
image chie laugh = Placeholder("girl", text="Chie\n(Laugh)")
image chie surprised = Placeholder("girl", text="Chie\n(Surprised)")
image chie sad = Placeholder("girl", text="Chie\n(Sad)")
image chie pout = Placeholder("girl", text="Chie\n(Pout)")

# Sabian
image sabian = Placeholder("boy", text="Sabian")
image sabian neutral = Placeholder("boy", text="Sabian\n(Neutral)")
image sabian smile = Placeholder("boy", text="Sabian\n(Smile)")
image sabian laugh = Placeholder("boy", text="Sabian\n(Laugh)")
image sabian surprised = Placeholder("boy", text="Sabian\n(Surprised)")
image sabian confident = Placeholder("boy", text="Sabian\n(Confident)")

# Julia
image julia = Placeholder("girl", text="Julia")
image julia neutral = Placeholder("girl", text="Julia\n(Neutral)")
image julia smile = Placeholder("girl", text="Julia\n(Smile)")
image julia shy = Placeholder("girl", text="Julia\n(Shy)")
image julia nervous = Placeholder("girl", text="Julia\n(Nervous)")
image julia blush = Placeholder("girl", text="Julia\n(Blush)")

# Supporting Characters
image mas_it = Placeholder("boy", text="Mas It")
image mas_it neutral = Placeholder("boy", text="Mas It\n(Neutral)")
image mas_it smile = Placeholder("boy", text="Mas It\n(Smile)")

image committee = Placeholder("boy", text="Committee")
image committee neutral = Placeholder("boy", text="Committee\n(Neutral)")
image committee speaking = Placeholder("boy", text="Committee\n(Speaking)")

image mod_t = Placeholder("boy", text="Modelling Teacher")
image modelling_teacher = Placeholder("boy", text="Modelling Teacher")
image lc_a = Placeholder("boy", text="Classmate A")
image classmate_a = Placeholder("boy", text="Classmate A")
image lc_b = Placeholder("boy", text="Classmate B")
image classmate_b = Placeholder("boy", text="Classmate B")
image civ_t = Placeholder("boy", text="Civics Teacher")
image civics_teacher = Placeholder("boy", text="Civics Teacher")
image glasses = Placeholder("boy", text="Glasses Boy")
image glasses_boy = Placeholder("boy", text="Glasses Boy")
image cap_b = Placeholder("boy", text="Cap Boy")
image cap_boy = Placeholder("boy", text="Cap Boy")
image braid_g = Placeholder("girl", text="Braided Girl")
image braided_girl = Placeholder("girl", text="Braided Girl")
image mod_announcer = Placeholder("boy", text="Moderator")
image moderator = Placeholder("boy", text="Moderator")
image shy = Placeholder("girl", text="Shy Classmate")
image shy_classmate = Placeholder("girl", text="Shy Classmate")

image teacher = Placeholder("boy", text="Teacher")
image teacher neutral = Placeholder("boy", text="Teacher\n(Neutral)")
image teacher smile = Placeholder("boy", text="Teacher\n(Smile)")

image white = Solid("#ffffff")
image logo = "images/logo.png"
image judul_game = "images/judul-game.png"

transform splash_logo:
    truecenter
    zoom 0.3

transform splash_judul:
    truecenter
    zoom 0.175

label splashscreen:
    scene white
    with Pause(0.5)
    
    show logo at splash_logo with dissolve
    with Pause(1.5)
    hide logo with dissolve

    show judul_game at splash_judul with dissolve
    with Pause(1.5)
    hide judul_game with dissolve
    
    with Pause(0.5)
    
    return

