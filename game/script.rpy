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
default tridaAffection = 0
default mapAcquired = False


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

    n "It say you accepted to join the school, you feel a sense of accomplishment and excitement for the future."
    p "Yes! I did it! I got accepted!"
    hide phone_foreground
    hide phone_background
    n "Then you start prepare for tommorow"
    p "Better be i should sleep..."
    menu:
        "Go to sleep":
            n "You go to sleep and dream about your future in the school"
    scene lobby_sketch
    n "next day... you arrive at school excited to start your new journey"
    n "you arrive at lobby of school, so many people gather at billboard, you had to effortfully push through the crowd to get a better view of the information posted on the board."
    p "Oh i should find way to the tent!"
    n "you start to look around the school"
    jump MPLS


label getting_map:
    scene vw
    p "Oh damn, i lost... why this school so big..."
    n "you keep walking aroud till..."
    n "accidently bump to someone"
    p "Oh-"
    m "Ow-"
    p "Sorry, i didn't see you there"
    m "Its okey kid, be careful"
    n "Seem like he notice your confused look"
    m "You lost huh? this place are really big"
    p "Yeah, im new here so... can you help me?"
    m "Sure, but not now... so for now i just can help you witth this..."
    m "Give me your phone"
    p "Eh? Okay...?"
    menu:
        "Give him your phone":
            n "You give him your phone"
    n "..."
    m "Here your phone"
    menu:
        "Take it":
            n "You take your phone"
            n "Acquire map"
    $ mapAcquired = True
    p "Thanks sir!"
    m "Anytime kid, good luck!"
    n "he walk away, you decide to continue search the tent of MPLS"
    jump MPLS
    


label MPLS:
    p "Where i should go..."
    if mapAcquired:
        p "Oh right, i have the map"
        n "You open the map and see the location of MPLS tent"
        p "I should go to the tent of MPLS"
        jump inside_MPLS_tent
    else:
        p "I should ask someone for help"
        n "You look around but lost"
        menu : 
            "Walk inside":
                jump getting_map
        

label inside_MPLS_tent:
    # lanjutan cerita setelah sampai di tenda MPLS
    n "You finally arrive at the MPLS tent."
    p ""

    return