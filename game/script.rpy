# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player_name]")
define n = Character("")

# Core Engine Transitions
define ease = MoveTransition(0.5, enter=None, leave=None, enter_time_warp=_warper.ease, leave_time_warp=_warper.ease)

# Team Salvato / DDLC Cinematic Scene Transitions
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(0.5),
    Solid("#000"), Dissolve(1.0),
    True])
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(0.5),
    Solid("#000"), Dissolve(1.0),
    True])

image black = Solid("#000")


# ==============================================================================
# CHARACTER
# ==============================================================================

define trida = Character("Trida")
define committee = Character("Student Committee")
define radit = Character("Radit")
define chie = Character("Chie")
define shy_classmate = Character("Shy Classmate")
define sabian = Character("Sabian")
define julia = Character("Julia")
define modelling_teacher = Character("Modelling Teacher")
define civics_teacher = Character("Civics Teacher")
define teacher = Character("Teacher")
define glasses_boy = Character("Glasses Boy")
define cap_boy = Character("Cap Boy")
define braided_girl = Character("Braided Girl")
define moderator = Character("Moderator")
define classmate_a = Character("Classmate A")
define classmate_b = Character("Classmate B")


# ==============================================================================
# GAME STATE
# ==============================================================================

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

# ==============================================================================
# BACKGROUNDS
# ==============================================================================
image bg classroom = "images/mugen/pack1/School/Classroom_01_day.webp"
image bg rus_studio = "images/mugen/pack1/School/monele_arts_building.webp"
image bg grapos_field = "images/mugen/pack1/School/football_field_day.webp"
image bg gates_morning = "images/mugen/pack1/School/generic_school_gate.webp"
image bg bedroom_late_afternoon = "images/mugen/pack1/Assorted/room.webp"
image bg teddy_cup = "images/mugen/pack1/Cafe Memoria/cafe_memoria_inside_01_afternoon.webp"
image bg room = "images/mugen/pack1/Assorted/room.webp"

# ==============================================================================
# CHARACTER EXPRESSIONS (Ren'Py Tag Attributes)
# ==============================================================================
# Trida
image trida = Placeholder("boy", text="Trida")
image trida neutral = Placeholder("boy", text="Trida\n(Neutral)")
image trida smile = Placeholder("boy", text="Trida\n(Smile)")
image trida happy = Placeholder("boy", text="Trida\n(Happy)")
image trida laugh = Placeholder("boy", text="Trida\n(Laugh)")
image trida surprised = Placeholder("boy", text="Trida\n(Surprised)")
image trida sad = Placeholder("boy", text="Trida\n(Sad)")
image trida crying = Placeholder("boy", text="Trida\n(Crying)")
image trida nervous = Placeholder("boy", text="Trida\n(Nervous)")
image trida blush = Placeholder("boy", text="Trida\n(Blush)")
image trida annoyed = Placeholder("boy", text="Trida\n(Annoyed)")

# Radit
image radit = Placeholder("boy", text="Radit")
image radit neutral = Placeholder("boy", text="Radit\n(Neutral)")
image radit smile = Placeholder("boy", text="Radit\n(Smile)")
image radit happy = Placeholder("boy", text="Radit\n(Happy)")
image radit laugh = Placeholder("boy", text="Radit\n(Laugh)")
image radit surprised = Placeholder("boy", text="Radit\n(Surprised)")
image radit sad = Placeholder("boy", text="Radit\n(Sad)")
image radit frown = Placeholder("boy", text="Radit\n(Frown)")
image radit amused = Placeholder("boy", text="Radit\n(Amused)")
image radit annoyed = Placeholder("boy", text="Radit\n(Annoyed)")

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


