label week1_start:
    scene bg gates_morning
    n "Your body returns to the school gates after the MPLS ceremony."
    n "Students chatter, the air buzzes with talk about class arrangements."
    p "Here we go, another day."

    scene bg classroom
    n "The classroom hums with the low whirr of the air‑conditioner."
    n "Everyone looks tense, eyes hidden behind textbooks."
    n "You step in, inhaling an unfamiliar scent."
    n "After examining a few desks, you choose to sit down."

    menu:
        "Front of the class":
            n "You sit at the front, where every eye can see you."
        "Middle of the class":
            n "You settle into a desk in the middle, watching the room."
        "Back of the class":
            n "You slide into a seat at the back, staying low."

    n "A voice catches your attention — the familiar orange‑eyed Trida."
    t "Hey! We're in the same class, huh?"
    n "They smile, revealing teeth you hadn't seen before."
    t "What a coincidence!"
    n "You were about to respond when footsteps echoed in the doorway."

    com "Sit down, everyone."
    n "The homeroom teacher steps in. Everyone shifts to the front."

    com "Is everyone here today?"
    com "I'll check your attendance first, okay?"
    n "He calls out names. When he reaches yours..."
    p "Here, sir."
    n "You stand briefly, then sit as he outlines classroom rules."
    n "Interactive learning, critical thinking, participation encouraged."

    com "It's all from me, you can take a break now."
    n "The teacher closes the attendance book and walks out."
    p "Where should I go now?"

    menu:
        "Go to Grapos":
            jump week1_grapos
        "Go to RUS Animation Studio":
            jump week1_rus
        "Stay in the class":
            jump week1_stay

label week1_grapos:
    scene bg grapos_field
    n "You walk to the Grapos field, the green grass swaying gently."
    n "Outside, students mill about or head to the canteen."
    r "Hey, you look like you need a break."
    r "Want to grab a snack? I've got some chips."

    menu:
        "Accept Radit's offer":
            $ radit_affection += 1
            n "You sit beside Radit, sharing chips and laughing about morning chaos."
        "Decline Radit's offer":
            $ radit_affection -= 1
            n "You decline politely, heading back alone."

    n "After a short chat, you head back toward the classroom."
    jump week1_back_to_class

label week1_rus:
    scene bg rus_studio
    n "You walk to the RUS Animation Studio, the doors open to a bright space."
    n "Julia sits at a table nearby, sketching with earbuds in."
    ch "Hey! You're here too."
    ch "Want to see what I'm working on?"

    menu:
        "Browse Julia's sketch":
            $ ch_affection += 1
            n "Julia shows you a quick animation demo. You both discuss the style."
        "Don't browse Julia's sketch":
            $ ch_affection -= 1
            n "You excuse yourself, returning to the classroom."

    n "The studio visit feels inspiring, but time runs out."
    jump week1_back_to_class

label week1_stay:
    scene bg classroom
    n "You stay put, watching the teacher outline the week's objectives."
    n "Lessons drag, but you keep your focus."
    jump week1_back_to_class

label week1_back_to_class:
    scene bg classroom
    n "The bell rings, signaling the end of break."
    n "Students shuffle back to their seats."
    com "Alright, today we begin 3D Animation basics."
    com "Digital objects come to life on a 2D screen."
    com "They appear to move, turn, and rotate like real objects."
    n "Trida sits beside you, doodling in their notebook."
    t "This is gonna be fun, right?"
    p "Yeah. Should be interesting."

    com "Trida, explain what 3D animation does."
    t "Oh‑yes. Yes, sir!"
    t "3D animation is basically giving digital stuff a little life..."
    com "That was the simplest explanation I've heard today."
    n "The class chuckles. Trida's cheeks flush slightly."
    t "Thank you."

    n "Classes continue through the afternoon."
    n "By midday, the school day finally ends."

    n "As students pack up, you head toward the exit."
    t "Hey, thanks for helping me back there."
    menu:
        "It's not that much of a help tho!":
            n "Trida laughs softly."
            t "That was not a big deal."
        "That was not a big deal":
            n "Trida grins."
            t "It's all good."
        "Don't bother it much...":
            n "Trida's smile fades slightly."
            t "Well, I guess..."

    n "Trida suggests getting drinks at Teddy Cup stall."
    p "That sounds great."
    jump week1_teddy_cup

label week1_teddy_cup:
    scene bg teddy_cup
    n "The school is nearly empty now. You and Trida sit near the stall."
    n "Two cups of iced tea arrive. You chat about today's topics."

    t "Not gonna lie, when they brought up the Final Assignment in 12th grade..."
    t "I was a little excited. I mean—how bad could it be?"

    menu:
        "It could be worse than we thought":
            t "Yeah, I know what you mean."
        "Maybe it was easier than we imagined?":
            t "Heh, maybe. I'm just overthinking."
        "I think it was still fifty-fifty for now":
            t "Fair enough. I'll take that."

    t "Well, however it is, I hoped we are on the same team."
    n "Trida looks at you, their expression sincere."
    t "I know it will be fun, with you."
    n "The wind rustles around you as the sun begins to set."
    t "It's been a good day."
    p "Yeah. Me too."

label week1_bedroom:
    
    scene bg bedroom_late_afternoon
    n "You arrive home and let out a slow exhale."
    n "Your bags are resting on the chair."
    n "Lying back on the bed, your thoughts drift."
    p "Yeah, I should get a part-time job."
    p "But what should I do?"

    menu:
        "Be an Indoapril Cashier":
            n "That sounds like easy money."
        "Work as a barista at a cafe":
            n "Maybe you'll enjoy the calm atmosphere."
        "Open a commission or merchandise store":
            n "A creative outlet — could be fun."
    n "With a decision in mind, you close your eyes and let the exhaustion of the first week fade into sleep."
    n "Before you know it, another week at school begins..."
    jump week2_start

default radit_affection = 0
default ch_affection = 0
default player_name = ""