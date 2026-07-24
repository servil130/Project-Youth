# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#058aff")
define n = Character("")


# The game starts here.

label start:
    transform pc_muncul:
        xalign 0.5
        yoffset 300
        alpha 0
        ease 0.6 yoffset 0 alpha 1.0

    scene bg room

    n "The dim light of a study lamp casts a shadow across the desk. The soft, amber glow bathed the room in warmth, creating a cozy cocoon against the creeping chill of the evening outside."
    n "Your heart stumbles over when your fingers brush through your open laptop, a frantic beat echoing in your chest as they skim over the cool, sleek surface. The rhythmic click of the keys punctuated the silence."
    n "As your eyes traced the content on the screen, you allowed yourself to be drawn in deeper. You hovered over the refresh button, your impatience mirrored in the slight tremor of your fingertips. With each click, anticipation hung in the air, almost electric."
    n "Just as you were about to refresh the website page once more, a sudden “ding!” jolted you to a halt, echoing through the quiet room like a signal from another world."
    p "Oh its from school that i signed up for"
    show phone_foreground at pc_muncul, zorder 2
    n "You open the phone as you excited..."

    show phone_background at pc_muncul, zorder 1
    n "You scroll through the messages... You heartbeat quickens as you see the phone screen light up."

    n "SMK RADEN UMAR SAID Selection Results: Based on the decisions from the plenary meeting by the principal of SMK RADEN UMAR SAID KUDUS, together with the admissions committee for new students for the 2XXX/2XXX academic year on XX/XXXX/XXXX, it has been decided that, Name: p name Has been admitted to the 3D Animation Major."
    p "WOOOHOOOOOO! I got accepted in this new school"

    n "Then you start prepare for tommorow"
    n "next day..."
    scene lobby_sketch
    n "you arrive at lobby of school"


    return
