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
default tridaAffection = 0
default mapAcquired = False

