
transform pc_muncul:
    xalign 0.5
    yoffset 300
    alpha 0
    ease 0.6 yoffset 0 alpha 1.0

label start:
    $ current_week = "Prologue"
    stop music fadeout 1.5
    scene black
    with dissolve_scene_full

    $ player_name = renpy.input(_("Please enter your name:"), default="You", length=20).strip()
    if not player_name:
        $ player_name = "You"

    scene bg room
    with dissolve_scene_full
    # play music "audio/bgm_classroom.ogg" fadein 2.0 loop volume 0.5 # [Pending BGM asset]

    n "The dim light of a study lamp casts a shadow across the desk."
    n "The soft, amber glow bathed the room in warmth, creating a cozy cocoon against the creeping chill of the evening outside."
    n "Your heart stumbles over when your fingers brush through your open laptop."
    n "A frantic beat echoing in your chest as they skim over the cool, sleek surface."
    n "The rhythmic click of the keys punctuated the silence."
    n "As your eyes traced the content on the screen, you allowed yourself to be drawn in deeper."
    n "You hovered over the refresh button, your impatience mirrored in the slight tremor of your fingertips."
    n "With each click, anticipation hung in the air, almost electric."
    play sound "audio/phone_ding.wav"
    n "Just as you were about to refresh the website page once more, a sudden “ding!” jolted you to a halt."
    n "It echoed through the quiet room like a signal from another world."
    p "Oh its from school that i signed up for"
    show phone_foreground at pc_muncul zorder 2
    n "You open the phone as you excited..."

    show phone_background at pc_muncul zorder 1
    n "You scroll through the messages... You heartbeat quickens as you see the phone screen light up."

    n "It say you accepted to join the school, you feel a sense of accomplishment and excitement for the future."
    p "Yes! I did it! I got accepted!"
    hide phone_foreground
    hide phone_background
    with dissolve

    # Timeskip
    scene black
    with dissolve_scene_half
    n "Two months later…"

    scene bg gates_morning
    with fade

    n "The wind blows, causing your hair to move in waves."
    n "Your shoes tap against the ground as you walk with a nervous thrill towards the building of your new school."
    n "Today marks your first day as an official student at SMK Raden Umar Said."

    scene lobby_sketch
    with dissolve

    n "As you walked deeper into the school grounds, the striking red and grey buildings loomed above you, exuding a sense of modernity and excitement."
    n "The air buzzed with energy as students and parents hurried about, chatting and unloading supplies."
    n "Laughter and footsteps filled the atmosphere, reminding you that you weren't alone."
    n "Each person you saw shared the same mix of anxiety and eagerness, all ready to begin their own journey in this new school life."

    p "This felt like a dream…"

    n "You checked the board in front of the lobby, checking for any more information."
    n "More people started to hover around the board; you leaned into the crowd effortfully to read it."
    n "Upon further inspection, you could see rows of names divided into groups."
    n "After a minute of searching, you finally found your name."

    # Visual Paper on a Board
    n "[[Group 01: 1. [player_name]]"

    n "You exhaled deeply, aware of the information weighing on your mind."
    n "Determined not to forget your place, you walked deeper into the school buildings."

    # Ext. SMK RADEN UMAR SAID ASSEMBLY AREA - Visual Tenda MPLS
    jump inside_MPLS_tent


label inside_MPLS_tent:
    # ===== PROLOGUE: Tenda MPLS (kelanjutan setelah sampai/ketemu tenda) =====
    scene bg grapos_field
    with fade
    n "Following the instructions, you headed toward the chairs arranged in the school field."
    n "Amidst the bustling voices announcing the start of the ceremonies, you hurried to find your designated spot."
    n "You take a seat with your group."
    n "As you finally settle at your desk, a deep sigh of relief escapes your lips."
    n "It releases the tension that had been building up since you arrived at the school building."
    n "Your shoulders droop slightly as you begin to relax."
    n "The air around you is filled with a symphony of chatter."
    n "The warmth of the crowded tent makes beads of sweat trickle down your back."
    n "With a slow, deliberate glance, you notice someone your age sitting next to you."
    # Visual Splash Art: Trida Sitting Next To Players
    $ splash_art = True
    n "Their eyes twinkle with excitement as they dart around the tent, drinking in the vibrant atmosphere."
    n "The rich orange of their irises sparkles like the sunset, drawing your attention."
    n "Their brown hair bounces rhythmically as they fidget with enthusiasm."
    n "An animated presence that contrasts with your stillness."

    n "Just as you're about to look at them for a second too long, a clear voice breaks through the chatter."
    n "It commands the room's focus."
    $ splash_art = False
    committee "Good morning, everyone!"
    committee "Has everyone taken a breakfast yet?"
    committee "It seems like you guys haven't charged up energy yet."
    n "It's one of the seniors, their tone authoritative yet welcoming, cutting through the noise like a knife through butter."
    committee "Oh well then..."
    committee "Welcome, new students to SMK Raden Umar Said!"
    n "The excited applause fills the space, a chorus of clapping hands that washes over you like a wave, urging you to join in."
    n "You can't help but feel the pulse of the crowd as you begin to move."
    n "Swept along with your peers as the ceremonies officially commence."

    # --- CUT: opening ceremonies berjalan ---
    n "For the next few hours, the opening ceremonies unfold gracefully."
    n "Each moment designed to immerse the new students in the spirit of the school."
    n "Colourful banners flap gently overhead."
    n "Cheerful presentations from various clubs and societies fill the air with lively chitchat."
    n "Yet amidst the lively atmosphere, your mind drifts into introspection, only half-listening as the day rolls on."
    play sound "audio/school_bell.ogg"
    committee "It's break time! We repeat, it's break time!"
    committee "If anyone has brought lunch, feel free to enjoy it now."
    committee "But, if you prefer the school canteen, TeddyCup stall, or RB Mart, they are open for food too!"
    with dissolve
    n "Excitement ripples through the crowd as students spring to their feet."
    n "Eager for a moment of freedom and the chance to explore the tantalising options awaiting them."
    n "You start to feel your stomach rumbling as everyone starts to disperse and take out their lunch boxes."
    n "Your mind wanders for a moment before you finally decide to..."

    # --- ROUTES OPTION (3 rute: Trida / Radit / Chie) ---
    menu:
        "I'll just eat my lunch box":
            jump trida_lunch
        "Maybe we can check out the TeddyCup stall?":
            jump radit_teddy
        "I'm not that hungry, but I might go to the bathroom":
            jump chie_bathroom


# ===== ROUTE 01: TRIDA =====
label trida_lunch:
    n "You sat there, slowly opening your blue container box with a bunny drawing that you had doodled when you were younger."
    n "The smell of the fresh savoury sandwich hits your nose."
    n "Before you could pick it up, you could feel eyes glancing towards you."
    show trida uniform neutral at center with dissolve
    n "You blinked as you saw that the person earlier looked like they were mesmerised by your food."
    n "Before then, they noticed and flicked their attention fully towards you."
    menu:
        "Do you want some?":
            jump trida_lunch_nice
        "Silently ignore them":
            jump trida_lunch_bad


label trida_lunch_nice:
    # OPTION 01.5 - Normal Option
    $ tridaAffection += 1
    show trida happy at center, hop
    n "The fellow's eyes shimmered with excitement at the moment you posed your question."
    n "Their brilliance reminiscent of precious gems glinting in the sunlight, as if they had just unearthed a rare treasure."
    trida "Really?"
    n "You briefly turned your gaze towards them, feeling a flutter of emotions within you at the sudden enthusiasm."
    n "Then, you shifted your attention to the plate of food in front of you, its colours vibrant and enticing."
    n "Slowly, almost as if caught in a trance, you nodded your head."
    n "Your eyes flickered back to them, where you noticed the sparkly light dancing in their eyes."
    n "A mixture of curiosity and warmth that made your heart skip a beat."
    show trida happy with dissolve
    trida "Thank you...!"
    trida "You could also take mine!"
    n "They smiled, showing you their own lunchbox."
    n "The delicious-looking fried rice lay nestled among perfectly cooked eggs, making your stomach growl."
    n "Perhaps you were just hungry, but it was the most appetising fried rice you had ever seen."
    p "Oh, thanks! By the way, my name is [player_name]. Nice to meet you."
    show trida happy at center, hop
    n "The fellow grinned widely as they slowly moved closer."
    trida "You can call me Trida, [player_name]. Nice to meet you too!"
    # Visual Splash Art Trida: Eating Lunch Together
    $ splash_art = True
    n "That meeting was your first spark in this new school."
    n "Both of you continued to chat happily as the first flower of your friendship blossomed."
    $ splash_art = False
    hide trida with dissolve
    jump mpls_end


label trida_lunch_bad:
    # OPTION 01.5 - Bad Option
    $ tridaAffection -= 1
    n "You slowly shifted your gaze away and clutched your lunchbox to yourself."
    show trida sad at center, dip
    n "The person was startled for a moment, but they then returned to their own lunchbox."
    n "There is complete silence between the two of you. Perhaps you'll barely interact with the sunset fellow afterwards, if ever."
    hide trida with dissolve
    jump mpls_end


# ===== ROUTE 02: RADIT =====
label radit_teddy:
    scene bg teddy_cup
    with fade
    n "You stood up from your chair and walked out of the tents."
    n "A lot of people are walking around like an army of ants, their stomachs empty."
    n "Before you could hesitate, your foot turned toward one of the food stalls full of new students."
    n "The big names are put on top of the place: \"Teddy Cups\"."
    p "I should try this."
    n "Before you could even try to order, your body stumbled as someone bumped into your shoulders."
    show radit neutral at center with dissolve
    radit "Whoa, easy there..."
    n "Your eyes glanced to your sides as you looked at that boy."
    radit "Forgot to tie your shoes, pal?"
    p "Ah..."
    menu:
        "Yes... The ground calls for me, you see.":
            jump radit_nice
        "Did not answer and walk away":
            jump radit_bad


label radit_nice:
    # OPTION 02.5 - Normal Option
    show radit smile with dissolve
    radit "Mmm, I can see why. The ground's very down-to-earth."
    n "He said with a soft laugh that colored his tone."
    n "He appeared more approachable, a warmth radiating from his expression as he gradually moved closer."
    radit "I'm Radit, nice to meet you...?"
    n "He drew out the last syllable of his phrase, leaving a deliberate pause so you may introduce yourself."
    p "I'm [player_name]. Nice to meet you, too, Radit."
    n "You intertwine your hand with his, creating a small, unexpected handshake."
    show radit amused with dissolve
    radit "So, are you joining the queue?"
    n "He raises one eyebrow, making you realise that the line is getting longer, and you haven't stepped in line."
    p "You're right. I should hurry!"
    n "You were just about to step into line when you realised it would be rude to leave Radit alone."
    p "Don't you want to get some food too?"
    show radit smile with dissolve
    radit "I'm cool. Have fun though."
    hide radit with dissolve
    n "He softly patted your shoulder before walking away. You kept your gaze on Radit as he departed."
    n "You began to wonder if he was in the same major as you, but you quickly snapped back to reality."
    n "Some students had already returned—and you still hadn't placed your order."
    jump mpls_end


label radit_bad:
    # OPTION 02.5 - Bad Option
    show radit frown with dissolve
    n "Wordlessly, you begin to turn your back on the calm boy and search for another food stall to retreat to."
    n "For a split second out of the corner of your eye, you notice the boy's playful expression subtly sour into a small frown."
    hide radit with dissolve
    n "Despite having fled to the next stall, you could still feel the awkward air hanging around."
    jump mpls_end


# ===== ROUTE 03: CHIE =====
label chie_bathroom:
    scene bg gates_morning
    with fade
    n "You arise from your seat, following the crowd as it exits."
    n "The din of bustling crowds emphasizes your need to locate a restroom, urging you to get a move on."
    n "You pause, realising just how large the area of this school is."
    n "Your eyes scan around, glancing to the right and left as you take in your surroundings."
    n "Before you can decide where to go, you feel a light tap on your shoulder, making you jolt slightly."
    n "Your eyes are caught by a glow of dandelion petals in various shades of amber hair."
    n "You freeze as a cheerful-looking girl stands in front of you."
    show chie happy at center with dissolve
    chie "Hey! Are you lost?"
    menu:
        "Not really, I just... need the bathroom":
            jump chie_nice
        "No. Thank you":
            jump chie_bad


label chie_nice:
    # OPTION 03.5 - Normal Option
    show chie smile with dissolve
    n "With an air of amusement, she wore a smile as her eyes followed the softness of her gesture."
    chie "It's alright! Everyone has their first days, after all."
    n "She reaches for your hand, her grasp is gentle yet firm, conveying warmth and friendliness."
    chie "Here, I'll take you to the bathroom. I'm Chie, by the way!"
    n "You barely had a chance to respond before the girl pulled you along with her. The energy Chie had was truly unstoppable."
    n "You had just taken one step forward, and suddenly, both of you were standing in front of the toilet stalls."
    show chie laugh at center, hop
    chie "Here you go!"
    n "She spread her arms in a grand motion; you could almost forget that she was leading you to a toilet."
    chie "Yeah, it's not that amazing. But hey, it's better than the other toilets around here..."
    show chie smile with dissolve
    chie "Let's just say the smell is... pungent."
    n "She glanced back at you with a playful smile on her lips. She let out a soft laugh, observing your stiff posture."
    p "Thank you, uh... Chie."
    show chie happy with dissolve
    chie "No worries. Oh yeah, I didn't catch your name!"
    n "You paused. Chie was a very nice person."
    n "She might seem like a rabbit hopping around in her own words, but she is just another spirited individual."
    p "I'm [player_name]. Thanks again for your help, Chie."
    show chie smile with dissolve
    chie "Nice to meet you then, [player_name]!"
    n "Suddenly, an announcement was faintly heard in your ears."
    n "It must have been a sign that your break was ending. Chie lightly tapped your back."
    show chie happy with dissolve
    chie "I think it's also my time to head back. Good luck!"
    hide chie with dissolve
    n "You waved at her as you watched her run and disappear around the corner."
    n "You smiled, hoping that you two would meet again."
    jump mpls_end


label chie_bad:
    # OPTION 03.5 - Bad Option
    n "You gave a brief, neutral reply and turned away."
    show chie surprised with dissolve
    chie "Oh."
    show chie sad at center, dip
    n "Her expression immediately dropped, revealing a hint of disappointment."
    n "She fiddled with her hands as she shifted her gaze from her fingers to your face."
    chie "Ah, sorry 'bout that. I was just worried, you know."
    n "An uncomfortable silence hung in the air."
    chie "Well, good luck, I guess?"
    n "She plastered a strained smile on her face."
    n "The corners of her mouth twitched as if fighting against a wave of emotions."
    hide chie with dissolve
    n "You responded with a simple nod, careful to keep your expression neutral, and turned away."
    n "The significance of the moment seemed to cling to you, resembling a shadow."
    n "An embarrassment so deep, it would resonate in your memory for all time."
    jump mpls_end


# ==== Penutup prologue + sambung cerita ====
label mpls_end:
    scene black
    with fade
    n "The rest of the MPLS Day passes in a blur of introductions, games, and the warm buzz of a school finding its rhythm."
    n "By the time you head home, the first seeds of this new chapter have been planted—and a new school year is only just beginning."
    jump week1_start