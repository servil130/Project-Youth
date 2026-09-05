# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("You", color="#058aff")
define n = Character("")
define move_transitions = {
    "fade": Fade(0.5, 0.5, 0.5, color="#000"),
    "move": MoveTransition(0.5, 0.5, 0.5, color="#000"),
}
define t = Character("Trida", color="#00ff7b")
define m = Character("Mas It", color="#ff0000")
define com = Character("Student Committee", color="#f5c542")
define r = Character("Radit", color="#4fc3f7")
define ch = Character("Chie", color="#ffb74d")
define shy = Character("Shy Classmate", color="#b39ddb")
define sab = Character("Sabian", color="#ff7043")
define jul = Character("Julia", color="#80deea")
define mod_t = Character("Modelling Teacher", color="#90a4ae")
define civ_t = Character("Civics Teacher", color="#90a4ae")
define glasses = Character("Glasses Boy", color="#78909c")
define cap_b = Character("Cap Boy", color="#a1887f")
define braid_g = Character("Braided Girl", color="#f48fb1")
define mod_announcer = Character("Moderator", color="#ffd54f")
define lc_a = Character("Classmate A", color="#b0bec5")
define lc_b = Character("Classmate B", color="#b0bec5")

default tridaAffection = 0
default mapAcquired = False
default sabian_affection = 0
default julia_affection = 0
default player_has_bouquet = False

