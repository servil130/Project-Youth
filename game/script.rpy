# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#058aff")
define n = Character("Narrator", color="#ff0000")


# The game starts here.

label start:

    scene bg room

    n "The dim light of a study lamp casts a shadow across the desk. The soft, amber glow bathed the room in warmth, creating a cozy cocoon against the creeping chill of the evening outside."
    n "You notice your phone on the nightstand, buzzing with notifications. As you reach for it"
    p "Oh its from school that i signed up for"
    transform phone_muncul:
        xalign 0.5
        yoffset 300
        alpha 0
        ease 0.6 yoffset 0 alpha 1.0
    show phone_foreground at phone_muncul, zorder 2
    n "You open the phone as you excited..."

    show phone_background at phone_muncul, zorder 1
    n "you scroll through the messages..."
    
    p "WOOOHOOOOOO! I got accepted in this new school"


    return
