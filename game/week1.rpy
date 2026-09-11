label week1_start:
    $ current_week = "Week 1"
    play music "audio/bgm_classroom.ogg" fadein 1.5 loop volume 0.5
    scene bg gates_morning
    with fade
    n "Your body returns to the school gates after the MPLS ceremony."
    n "Students chatter, the air buzzes with talk about class arrangements."
    p "Here we go, another day."

    scene bg classroom
    with fade
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
    show trida smile at center with dissolve
    trida "Hey! We're in the same class, huh?"
    show trida laugh
    n "They smile, revealing teeth you hadn't seen before."
    trida "What a coincidence!"
    n "You were about to respond when footsteps echoed in the doorway."

    hide trida with dissolve
    committee "Sit down, everyone."
    n "The homeroom teacher steps in. Everyone shifts to the front."

    committee "Is everyone here today?"
    committee "I'll check your attendance first, okay?"
    n "He calls out names. When he reaches yours..."
    p "Here, sir."
    n "You stand briefly, then sit as he outlines classroom rules."
    n "Interactive learning, critical thinking, participation encouraged."

    committee "It's all from me, you can take a break now."
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
    with fade
    n "You walk to the Grapos field, the green grass swaying gently."
    n "Outside, students mill about or head to the canteen."
    show radit smile at center with dissolve
    radit "Hey, you look like you need a break."
    radit "Want to grab a snack? I've got some chips."

    menu:
        "Accept Radit's offer":
            $ radit_affection += 1
            show radit laugh
            n "You sit beside Radit, sharing chips and laughing about morning chaos."
        "Decline Radit's offer":
            $ radit_affection -= 1
            show radit frown
            n "You decline politely, heading back alone."

    hide radit with dissolve
    n "After a short chat, you head back toward the classroom."
    jump week1_back_to_class

label week1_rus:
    scene bg rus_studio
    with fade
    n "You walk to the RUS Animation Studio, the doors open to a bright space."
    n "Julia sits at a table nearby, sketching with earbuds in."
    show chie happy at center with dissolve
    chie "Hey! You're here too."
    chie "Want to see what I'm working on?"

    menu:
        "Browse Julia's sketch":
            $ ch_affection += 1
            show chie smile
            n "Julia shows you a quick animation demo. You both discuss the style."
        "Don't browse Julia's sketch":
            $ ch_affection -= 1
            show chie pout
            n "You excuse yourself, returning to the classroom."

    hide chie with dissolve
    n "The studio visit feels inspiring, but time runs out."
    jump week1_back_to_class

label week1_stay:
    scene bg classroom
    with fade
    n "You stay put, watching the teacher outline the week's objectives."
    n "Lessons drag, but you keep your focus."
    jump week1_back_to_class

label week1_back_to_class:
    scene bg classroom
    with fade
    play sound "audio/school_bell.ogg"
    n "The bell rings, signaling the end of break."
    n "Students shuffle back to their seats."
    committee "Alright, today we begin 3D Animation basics."
    committee "Digital objects come to life on a 2D screen."
    committee "They appear to move, turn, and rotate like real objects."
    n "Trida sits beside you, doodling in their notebook."
    show trida smile at center with dissolve
    trida "This is gonna be fun, right?"
    p "Yeah. Should be interesting."

    committee "Trida, explain what 3D animation does."
    show trida surprised
    trida "Oh‑yes. Yes, sir!"
    show trida nervous
    trida "3D animation is basically giving digital stuff a little life..."
    committee "That was the simplest explanation I've heard today."
    show trida blush
    n "The class chuckles. Trida's cheeks flush slightly."
    trida "Thank you."

    n "Classes continue through the afternoon."
    n "By midday, the school day finally ends."

    n "As students pack up, you head toward the exit."
    show trida happy
    trida "Hey, thanks for helping me back there."
    menu:
        "It's not that much of a help tho!":
            show trida laugh
            n "Trida laughs softly."
            trida "That was not a big deal."
        "That was not a big deal":
            show trida smile
            n "Trida grins."
            trida "It's all good."
        "Don't bother it much...":
            show trida sad
            n "Trida's smile fades slightly."
            trida "Well, I guess..."

    show trida happy
    n "Trida suggests getting drinks at Teddy Cup stall."
    p "That sounds great."
    hide trida with dissolve
    jump week1_teddy_cup

label week1_teddy_cup:
    scene bg teddy_cup
    with fade
    play sound "audio/glass_chime.wav"
    show trida happy at center with dissolve
    n "The school is nearly empty now. You and Trida sit near the stall."
    n "Two cups of iced tea arrive. You chat about today's topics."

    trida "Not gonna lie, when they brought up the Final Assignment in 12th grade..."
    trida "I was a little excited. I mean—how bad could it be?"

    menu:
        "It could be worse than we thought":
            show trida nervous
            trida "Yeah, I know what you mean."
        "Maybe it was easier than we imagined?":
            show trida smile
            trida "Heh, maybe. I'm just overthinking."
        "I think it was still fifty-fifty for now":
            show trida happy
            trida "Fair enough. I'll take that."

    show trida smile
    trida "Well, however it is, I hoped we are on the same team."
    show trida blush
    n "Trida looks at you, their expression sincere."
    trida "I know it will be fun, with you."
    n "The wind rustles around you as the sun begins to set."
    trida "It's been a good day."
    p "Yeah. Me too."
    hide trida with dissolve

label week1_bedroom:
    scene bg bedroom_late_afternoon
    with fade
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