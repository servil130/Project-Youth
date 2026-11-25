# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(ctc="ctc", ctc_position="fixed")
define p = Character("[player_name]", ctc="ctc", ctc_position="fixed")
define n = Character("", ctc="ctc", ctc_position="fixed")
default player_job = None
default player_money = 0
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
define audio.door_open = "audio/sfx/door_open.ogg"
define audio.door_close = "audio/sfx/door_close.ogg"
define audio.paper_flip = "audio/sfx/paper_flip.ogg"
define audio.book_open = "audio/sfx/book_open.ogg"
define audio.footstep_1 = "audio/sfx/footstep_1.ogg"
define audio.footstep_2 = "audio/sfx/footstep_2.ogg"
define audio.keyboard_typing = "audio/sfx/keyboard_typing.mp3"
define audio.ui_hover = "audio/sfx/ui_hover.wav"
define audio.ui_click = "audio/sfx/ui_click.wav"
define audio.ui_choice = "audio/sfx/ui_choice.wav"
define audio.ui_back = "audio/sfx/ui_back.wav"

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
define hizbul = Character("Hizbul", ctc="ctc", ctc_position="fixed")
define ilham = Character("Ilham", ctc="ctc", ctc_position="fixed")

default player_name = "You"
default current_week = "Prologue"
default splash_art = False
default current_splash_art = False
default trida_route = None
default mapAcquired = False
default player_has_bouquet = False
default tridaAffection = 0
define TRIDA_ROMANCE_THRESHOLD = 15
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

    JULIA_ZOOM = 1.30
    JULIA_YOFFSET = 240

    def julia_sprite(expr="neutral"):
        path = f"images/julia/julia_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=JULIA_ZOOM, yoffset=JULIA_YOFFSET)
        return Placeholder("girl", text=f"Julia\n({expr.capitalize()})")

    SABIAN_ZOOM = 1.30
    SABIAN_YOFFSET = 240

    def sabian_sprite(expr="neutral"):
        path = f"images/sabian/sabian_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=SABIAN_ZOOM, yoffset=SABIAN_YOFFSET)
        return Placeholder("boy", text=f"Sabian\n({expr.capitalize()})")

    CHIE_ZOOM = 1.30
    CHIE_YOFFSET = 240

    def chie_sprite(expr="neutral"):
        path = f"images/chie/chie_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=CHIE_ZOOM, yoffset=CHIE_YOFFSET)
        return Placeholder("girl", text=f"Chie\n({expr.capitalize()})")

    def hizbul_sprite(expr="neutral"):
        path = f"images/hizbul/hizbul_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("boy", text=f"Hizbul\n({expr.capitalize()})")

    def ilham_sprite(expr="neutral"):
        path = f"images/ilham/ilham_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("boy", text=f"Ilham\n({expr.capitalize()})")

    def teacher_sprite(expr="neutral"):
        path = f"images/teacher/teacher_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("boy", text=f"Teacher\n({expr.capitalize()})")

    GLASSES_BOY_ZOOM = 0.90
    GLASSES_BOY_YOFFSET = 280

    def glasses_boy_sprite(expr="neutral"):
        path = f"images/glasses_boy/glasses_boy_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=GLASSES_BOY_ZOOM, yoffset=GLASSES_BOY_YOFFSET)
        return Placeholder("boy", text=f"Glasses Boy\n({expr.capitalize()})")

    def braided_girl_sprite(expr="neutral"):
        path = f"images/braided_girl/braided_girl_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("girl", text=f"Braided Girl\n({expr.capitalize()})")

    def shy_classmate_sprite(expr="neutral"):
        path = f"images/shy_classmate/shy_classmate_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("girl", text=f"Shy Classmate\n({expr.capitalize()})")

    def cap_boy_sprite(expr="neutral"):
        path = f"images/cap_boy/cap_boy_{expr}.png"
        if renpy.loadable(path):
            return Transform(path, zoom=1.30, yoffset=240)
        return Placeholder("boy", text=f"Cap Boy\n({expr.capitalize()})")

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

image trida uniform smile = "trida uniform happy"
image trida uniform laugh = "trida uniform happy"
image trida uniform surprised = "trida uniform happy"
image trida uniform blush = "trida uniform embarrassed"
image trida uniform nervous = "trida uniform embarrassed"
image trida uniform crying = "trida uniform sad"
image trida uniform annoyed = "trida uniform sad"

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
image chie = chie_sprite("neutral")
image chie neutral = chie_sprite("neutral")
image chie smile = chie_sprite("happy")
image chie happy = chie_sprite("happy")
image chie laugh = chie_sprite("happy")
image chie surprised = chie_sprite("embarrassed")
image chie sad = chie_sprite("sad")
image chie pout = chie_sprite("sad")
image chie embarrassed = chie_sprite("embarrassed")

# Sabian
image sabian = sabian_sprite("neutral")
image sabian neutral = sabian_sprite("neutral")
image sabian smile = sabian_sprite("happy")
image sabian happy = sabian_sprite("happy")
image sabian laugh = sabian_sprite("happy")
image sabian surprised = sabian_sprite("sad")
image sabian confident = sabian_sprite("happy")
image sabian sad = sabian_sprite("sad")
image sabian embarrassed = sabian_sprite("embarrassed")

# Julia
image julia = julia_sprite("neutral")
image julia neutral = julia_sprite("neutral")
image julia smile = julia_sprite("happy")
image julia happy = julia_sprite("happy")
image julia shy = julia_sprite("embarrassed")
image julia nervous = julia_sprite("sad")
image julia blush = julia_sprite("embarrassed")
image julia sad = julia_sprite("sad")
image julia embarrassed = julia_sprite("embarrassed")

# Supporting Characters
image mas_it = Placeholder("boy", text="Mas It")
image mas_it neutral = Placeholder("boy", text="Mas It\n(Neutral)")
image mas_it smile = Placeholder("boy", text="Mas It\n(Smile)")

image committee = Placeholder("boy", text="Committee")
image committee neutral = Placeholder("boy", text="Committee\n(Neutral)")
image committee speaking = Placeholder("boy", text="Committee\n(Speaking)")

image mod_t = teacher_sprite("neutral")
image modelling_teacher = teacher_sprite("neutral")
image lc_a = Placeholder("boy", text="Classmate A")
image classmate_a = Placeholder("boy", text="Classmate A")
image lc_b = Placeholder("boy", text="Classmate B")
image classmate_b = Placeholder("boy", text="Classmate B")
image civ_t = teacher_sprite("neutral")
image civics_teacher = teacher_sprite("neutral")
image glasses = glasses_boy_sprite("neutral")
image glasses_boy = glasses_boy_sprite("neutral")
image glasses_boy neutral = glasses_boy_sprite("neutral")
image glasses_boy smile = glasses_boy_sprite("happy")
image glasses_boy happy = glasses_boy_sprite("happy")
image glasses_boy sad = glasses_boy_sprite("sad")
image glasses_boy embarrassed = glasses_boy_sprite("embarrassed")
image cap_b = cap_boy_sprite("neutral")
image cap_boy = cap_boy_sprite("neutral")
image cap_boy neutral = cap_boy_sprite("neutral")
image cap_boy smile = cap_boy_sprite("happy")
image cap_boy happy = cap_boy_sprite("happy")
image cap_boy sad = cap_boy_sprite("sad")
image cap_boy embarrassed = cap_boy_sprite("embarrassed")
image braid_g = braided_girl_sprite("neutral")
image braided_girl = braided_girl_sprite("neutral")
image braided_girl neutral = braided_girl_sprite("neutral")
image braided_girl smile = braided_girl_sprite("happy")
image braided_girl happy = braided_girl_sprite("happy")
image braided_girl sad = braided_girl_sprite("sad")
image braided_girl embarrassed = braided_girl_sprite("embarrassed")
image mod_announcer = Placeholder("boy", text="Moderator")
image moderator = Placeholder("boy", text="Moderator")
image shy = shy_classmate_sprite("neutral")
image shy_classmate = shy_classmate_sprite("neutral")
image shy_classmate neutral = shy_classmate_sprite("neutral")
image shy_classmate smile = shy_classmate_sprite("happy")
image shy_classmate happy = shy_classmate_sprite("happy")
image shy_classmate sad = shy_classmate_sprite("sad")
image shy_classmate embarrassed = shy_classmate_sprite("embarrassed")

image teacher = teacher_sprite("neutral")
image teacher neutral = teacher_sprite("neutral")
image teacher smile = teacher_sprite("happy")
image teacher happy = teacher_sprite("happy")
image teacher sad = teacher_sprite("sad")
image teacher serious = teacher_sprite("serious")

image hizbul = hizbul_sprite("neutral")
image hizbul neutral = hizbul_sprite("neutral")
image hizbul smile = hizbul_sprite("happy")
image hizbul happy = hizbul_sprite("happy")
image hizbul sad = hizbul_sprite("sad")
image hizbul embarrassed = hizbul_sprite("embarrassed")

image ilham = ilham_sprite("neutral")
image ilham neutral = ilham_sprite("neutral")
image ilham smile = ilham_sprite("happy")
image ilham happy = ilham_sprite("happy")
image ilham sad = ilham_sprite("sad")
image ilham embarrassed = ilham_sprite("embarrassed")

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
