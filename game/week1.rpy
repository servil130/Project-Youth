# week1.rpy — WEEK 1 (ACT I CHAPTER I)
# Reuses chars from script.rpy: p, n, t, r, ch, com
# Vars: tridaAffection (default 0), mapAcquired (default False) — already in script.rpy

label week1_start:
    scene bg gates_morning  # placeholder visual
    n "Your body returns to the school gates after the MPLS ceremony."
    n "Students chatter, the air buzzes with talk about class arrangements."
    p "Here we go, another day."

    scene bg classroom  # placeholder visual
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

    # --- TEACHER ENTERS ---
    com "Sit down, everyone."
    n "The homeroom teacher steps in. Everyone shifts to the front."

    # --- ATTENDANCE ---
    com "Is everyone here today?"
    com "I'll check your attendance first, okay?"
    n "He calls out names. When he reaches yours..."
    p "Here, sir."
    n "You stand briefly, then sit as he outlines classroom rules."
    n "Interactive learning, critical thinking, participation encouraged."

    # --- BREAK OPTIONS ---
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

# -------------------------------------------------
# OPTION A — Grapos (Radit route)
# -------------------------------------------------
label week1_grapos:
    scene bg grapos_field  # placeholder visual
    n "You walk to the Grapos field, the green grass swaying gently."
    n "Outside, students mill about or head to the canteen."
    r "Hey, you look like you need a break."
    r "Want to grab a snack? I've got some chips."

    menu:
        "Accept Radit's offer?":
            "Yes":
                $ radit_affection += 1
                n "You sit beside Radit, sharing chips and laughing about morning chaos."
            "No":
                $ radit_affection -= 1
                n "You decline politely, heading back alone."

    n "After a short chat, you head back toward the classroom."
    jump week1_back_to_class

# -------------------------------------------------
# OPTION B — RUS Animation Studio (Chie route)
# -------------------------------------------------
label week1_rus:
    scene bg rus_studio  # placeholder visual
    n "You walk to the RUS Animation Studio, the doors open to a bright space."
    n "Julia sits at a table nearby, sketching with earbuds in."
    ch "Hey! You're here too."
    ch "Want to see what I'm working on?"

    menu:
        "Browse Julia's sketch?":
            "Yes":
                $ ch_affection += 1
                n "Julia shows you a quick animation demo. You both discuss the style."
            "No":
                $ ch_affection -= 1
                n "You excuse yourself, returning to the classroom."

    n "The studio visit feels inspiring, but time runs out."
    jump week1_back_to_class

# -------------------------------------------------
# OPTION C — Stay in class (Neutral)
# -------------------------------------------------
label week1_stay:
    scene bg classroom
    n "You stay put, watching the teacher outline the week's objectives."
    n "Lessons drag, but you keep your focus."
    jump week1_back_to_class

# -------------------------------------------------
# Return to class — 3D Animation intro
# -------------------------------------------------
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

    # --- 3D ANIMATION QUIZ (Trida gets called on) ---
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

# -------------------------------------------------
# Teddy Cup stall — Trida route continues
# -------------------------------------------------
label week1_teddy_cup:
    scene bg teddy_cup  # placeholder visual
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

    # --- Bedroom scene — part-time job decision ---
    jump week1_bedroom

label week1_bedroom:
    scene bg bedroom_late_afternoon  # placeholder visual
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

    return  # → continue to week2 or wherever

default radit_affection = 0
default ch_affection = 0
default player_name = ""