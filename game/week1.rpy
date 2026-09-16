label week1_start:
    $ current_week = "Week 1"
    play music audio.t2 fadein 1.5 loop volume 0.7

    # ==============================================================================
    # ACT I - CHAPTER I: FIRST DAY OF CLASS & ENCOUNTERS
    # ==============================================================================

    scene bg gates_morning
    with dissolve_scene_full

    # Ext. SMK RADEN UMAR SAID GATES - MORNING
    n "Your body comes back to those buildings. It was a breath of fresh air after a week of the MPLS event had finally ended."
    n "People are already chattering and talking about the class arrangements after it came out."
    n "Your heart thumps as you finally reach your class."

    scene bg classroom
    with dissolve_scene_full
    play music audio.t3 fadein 1.5 loop volume 0.7

    # Int. CLASSROOM - MORNING
    n "The loud hum of the air conditioner fills the room, making the walls feel chill and stiff as your eyes wander around."
    n "The atmosphere in the classroom is uneasy, with everyone looking tense and lost in their own thoughts."
    n "You step into the room, inhaling an unfamiliar scent. After examining a few desks, you finally choose to sit down."

    menu:
        "Sit at the front of the class":
            n "You take a seat in the front row, right under the view of the blackboard."
        "Sit in the middle of the class":
            n "You settle into a desk in the middle row, surrounded by the chatter of your peers."
        "Sit at the back of the class":
            n "You choose a desk near the back corner, where you can observe the whole room."

    n "A voice catches your attention, its familiar tone ringing in your ears."
    n "You turn to see the same brown hair that you noticed during the MPLS event. Those sunset-orange eyes are already etched in your memory."

    show trida uniform happy at center with dissolve
    trida "Hey!"
    trida "Sooo… we're in the same class, huh?"
    show trida happy at center, hop
    n "They smile, revealing a grin and teeth you've never seen before."
    n "Your memory of them being all awkward has changed to someone who is maybe more confident and bright."
    trida "Wow, what a coincidence!"

    n "You were about to respond when the sound of footsteps made you pause."
    n "The figure you recognised as your homeroom teacher entered the classroom."
    show teacher at slide_right
    teacher "Sit down, everyone."
    n "The sound of scraping chairs and the clattering of desks shattered the lingering quiet, creating an echo that bounced off the walls."
    n "A few seats were occupied, their occupants shifting restlessly as they settled in. You glanced over at Trida, who remained poised beside your table."

    show trida neutral at to_left
    trida "That was the teacher, wasn't it!"
    n "They shot a glance your way, their eyes wide with urgency and a hint of panic."
    trida "Mind if I sit next to you?"

    menu:
        "Let them sit beside you":
            $ tridaAffection += 1
            p "Yeah, sure!"
            show trida happy at tleft, hop
            trida "Really? Thank you!"
            n "You nodded eagerly as Trida hurried to take a seat at the desk next to you."
            n "They looked at you with a wide, cheerful smile, just like a kid who's just been given a delicious piece of candy!"
            trida "Thank you so much, I owe you one."
            n "Their words rushed out with a compassionate tone. You smiled back just as the teacher cleared his throat."
            n "You sneak another look at Trida, and your eyes meet for a fleeting moment."
            n "A spark of recognition passes between you, igniting a warm, tingling sensation that travels all the way from your toes to the top of your head."
            n "It's as if tiny fireworks are bursting in your mind, each one illuminating the thrill of the moment."

        "Ask them to sit anywhere else":
            $ tridaAffection -= 1
            p "Uh, I don't know… Sorry, I think someone's already sitting there."
            show trida sad at tleft, dip
            n "You bit your lip, a nervous habit that betrayed your anxious thoughts."
            n "Trida's eyes dimmed, a poignant reflection of their sadness, as they tried to play it cool and looked for other remaining seats."
            n "But the teacher had already cleared his throat, making them panic as they still sat down at the desk next to you."
            trida "I didn't have time, I'm sorry…"
            n "They said with a wry smile, disappointment evident on their face."

    teacher "Is everyone here today?"
    n "A noticeable silence fell over the room as the students refrained from answering."
    teacher "I'll check your attendance first, okay?"

    n "He then called out each student's name one by one, asking for their nickname."
    n "When it was your turn, you stood up to explain your nickname and where you were from."
    n "After attendance was taken, he outlined the classroom rules, teaching philosophy, and the importance of interactive learning."

    teacher "It's all from me, you can take a break now. Gather here again later, as I will provide a subtle overview of our curriculum and materials."
    hide teacher with dissolve
    show trida happy at to_center
    n "Your homeroom teacher takes a walk out of the class, leaving you sitting there with exhaled breath."

    p "Where should I go now?"

    menu:
        "Go to Grapos":
            jump week1_grapos
        "Go to RUS Animation Studio":
            jump week1_rus
        "Stay at the Class":
            jump week1_stay


# ==============================================================================
# BREAK TIME: RADIT ROUTE
# ==============================================================================

label week1_grapos:
    play music audio.t4 fadein 1.0 loop volume 0.7
    p "Maybe I should walk around for a bit."
    n "As you glance around the room, you realise that several students have already slipped out. With a sense of urgency, you step out into the fresh air."

    scene bg grapos_field
    with dissolve_scene_full

    # Visual Lapangan Grapos
    n "As you walk along the familiar trail, you find yourself arriving at the open field where you participated in MPLS not long ago."
    n "In the distance, the building marked 'Grapos' looms, its weathered façade a testament to the years that have passed. Tall grasses sway gently in the breeze."

    show radit smile at center with dissolve
    radit "Hi, [player_name]."
    n "You turn around when you hear your name called. A figure you're already familiar with walks toward you casually, giving your shoulder a gentle tap."
    p "…?"
    n "You raise both eyebrows while he lets out a small chuckle."
    radit "So you don't remember my name now? I know you used to trip over things, but do you also do that with your memories?"
    radit "We are classmates now, so care to get along, mate?"

    menu:
        "Only if there's a binding snack-sharing agreement involved.":
            $ radit_affection += 1
            show radit amused at center, hop with dissolve
            n "Radit looked at you with an amused expression as he let out a small scoff, placing one hand in his pocket."
            radit "Straight to negotiation, huh? Fair enough."
            show radit smile at center, sway with dissolve
            radit "Deal. But don't complain when I take the better snacks."

        "I mean… I don't fight people usually, so… that counts as getting along, right?":
            $ radit_affection += 1
            show radit neutral at center, sway with dissolve
            n "Radit tilted his head as his calm eyes glanced straight towards you."
            radit "That's… a pretty low standard."
            show radit smile at center, hop with dissolve
            n "After a pause, a small chuckle slips from his lips."
            radit "But I'll take it. Peaceful is a good start."

        "Yeah, sure. We'll be seeing each other a lot anyway, so might as well get along.":
            $ radit_affection += 1
            show radit smile at center, sway with dissolve
            n "There was a brief silence before you saw him nod lightly, placing a smirk on his lips."
            radit "Guess we're stuck with each other then."

    p "By the way, I think we should head back now."
    n "You gestured with your thumbs on the way to class. Both of you walked slowly side by side back to the room and sat in your seats."
    hide radit with dissolve
    jump week1_back_to_class


# ==============================================================================
# BREAK TIME: CHIE ROUTE
# ==============================================================================

label week1_rus:
    play music audio.t4 fadein 1.0 loop volume 0.7
    p "Maybe I should walk around for a bit."
    n "You rise from your seat and make your way toward the door, stepping out into the fresh air."

    scene bg rus_studio
    with dissolve_scene_full

    # Visual Gedung Studio Animasi
    n "The animation studio building looms impressively against the backdrop of a blazing sun, radiating heat that shimmers in the air."
    n "As you take in your surroundings, a sense of purpose washes over you."

    show chie happy at to_center
    chie "Hello there! How are you doing?"
    n "A girl with long, flowing golden hair stands just two meters away, her bright smile lighting up her face."
    n "In a burst of energy, she takes both your hands and shakes them enthusiastically."
    chie "You haven't forgotten me, have you… I'm Chie, you know, Chie!"
    chie "Don't forget me too quickly, okay? I'm always busy with my internship, so I'm a little worried people might easily forget me..."

    menu:
        "Hey, I remember you, of course. You're not that easy to forget!":
            $ ch_affection += 1
            show chie smile at center, hop with dissolve
            n "Hearing that, her shoulders visibly relaxed, the tension melting away."
            chie "Really? You do?"
            chie "Aaa, that makes me so happy! I was seriously overthinking it."
            p "You don't have to worry about that. Sounds like you've been really busy, though."
            chie "Yeah… It's been kinda hectic lately as sophomores, but it's fun too. Also, if you need help or anything, you could still ask me!"

        "Of course I remember you!":
            $ ch_affection += 1
            show chie laugh at center, hop with dissolve
            chie "Yay!! I knew it!"
            n "She lets out a delighted squeal, hopping on her heels like a playful rabbit."
            chie "See, I'm memorable, right?"
            p "Yeah, you are. So… how's the internship going anyway?"
            chie "It's been kinda hectic lately, honestly… But don't worry, if you need help, you can still ask me!"

        "Chie, right? About that internship… then you are my senior?":
            $ ch_affection += 1
            show chie smile at center, sway with dissolve
            chie "Oh! Yeah, I guess that makes me your senior, huh?"
            chie "Don't worry, I'm a nice one! If you need help, you can totally ask me!"

    p "Thank you for that, Chie. By the way, I think we should head back now."
    n "You gestured toward class, leaving her waving goodbye as you walked back and took your seat."
    hide chie with dissolve
    jump week1_back_to_class


# ==============================================================================
# BREAK TIME: NEUTRAL ROUTE
# ==============================================================================

label week1_stay:
    scene bg classroom
    with dissolve_scene_full
    p "Maybe I should just stay in here."
    n "Half of the people in the room had already left. You sat there scrolling through your phone, passing the break time."
    scene black
    with dissolve_scene_half
    jump week1_back_to_class


# ==============================================================================
# AFTERNOON: 3D ANIMATION INTRODUCTION & POP QUIZ
# ==============================================================================

label week1_back_to_class:
    scene bg classroom
    with dissolve_scene_half
    play sound "audio/school_bell.ogg"
    play music audio.t3 fadein 1.5 loop volume 0.7

    n "The lights are cast through the window, making a faint glow in the classroom."
    n "The sound of complete silence wafting through the class only reached your homeroom teacher, who was now introducing 3D Animation."

    show teacher at right with dissolve
    teacher "3D animation takes digital objects and makes them come to life by creating the illusion they're moving through a three-dimensional space."
    teacher "These computer-generated objects appear on a two-dimensional screen, but are crafted to mimic the principles of a 3D world; they appear to move, turn, and rotate like real-world objects."

    # Visual Splash Art: Trida Doodling
    $ splash_art = True
    show trida uniform happy at tleft with dissolve
    n "Trida was still doodling through their notes, making scratch sketches with their tongue sticking out—a cat and a dog intertwining their hands together."

    $ splash_art = False
    teacher "You there…"
    teacher "Are you still with us?"

    n "It was a sudden move that made everyone turn their attention to Trida."
    show trida neutral at tleft, dip
    trida "Oh-yes. Yes, sir!"
    teacher "Could you explain to me what 3D Animation does?"

    show trida embarrassed at tleft, panic
    trida "It's…"
    n "They hesitated, their eyeballs rolling through the corners of the room before both of your gazes met."
    n "Their hair antenna is bouncing, looking like they are sending a telepathic message to help them."
    trida "So, 3D Animation is…"

    menu:
        "Give them the right answer":
            $ tridaAffection += 1
            p "3D animation makes digital objects look like they're moving in real 3D space, even though you're just seeing them on a flat screen."
            n "You whispered slowly to them, making them blink repeatedly before returning an awkward smile."
            show trida happy at tleft, hop
            trida "3D animation is basically giving digital stuff a little life—like, 'go on, move around, spin a bit'."
            trida "So it looks like it's living in a real 3D world, even though it's just chilling on a flat screen."
            teacher "That was the simplest one to say."
            show teacher smile at right, hop with dissolve
            n "The teacher put on a slight smile before explaining more about the topic, leaving Trida to glance at you with a bright grin."
            # Visual Splash Art: Trida Leaning In and Smiling
            $ splash_art = True
            show trida happy at tleft with dissolve
            n "They deliberately lean in to you."
            trida "Thank you!"
            $ splash_art = False

        "Gave them the wrong answer":
            $ tridaAffection -= 1
            p "3D animation tells a story by making drawings move in a flat space, frame by frame, by hand or on a computer."
            n "You whispered slowly to them. Trida rotates their head to face the teacher."
            show trida embarrassed at tleft, dip
            trida "3D animation is like flipping through a bunch of drawings really fast, so they start moving and telling a story on a flat screen."
            teacher "That was slightly incorrect. Those were 2D animation techniques."
            show trida sad at tleft with dissolve
            n "The teacher explained more about the topic, leaving Trida to glance at you with a bitten lip and a defeated look."
            trida "It's alright, don't be bothered by it…"

    hide teacher with dissolve
    n "On that day, time seemed to race ahead. The teacher piled on lessons not far beyond what a beginner could handle."
    n "By midday, relief washed over you as the class finally drew to a close. People started packing their stuff into bags, and you did too."

    n "You feel someone come up to your desk."
    if tridaAffection > 0:
        show trida happy at to_center
    else:
        show trida embarrassed at to_center
    trida "Hey, so… thanks for earlier."

    menu:
        "It's not that much of a help tho!":
            $ tridaAffection += 1
            p "It's not that much of a help tho!"
        "That was not a big deal":
            $ tridaAffection += 1
            p "That was not a big deal."
        "Don't bother it much…":
            p "Don't bother it much…"

    trida "Well, you still helped me, whether it was correct or not, you still helped me."
    n "Trida pressed closer, their warmth enveloping you like a cosy blanket, igniting an exhilarating spark in the air."
    trida "Actually, that was kind of funny, you know… About me being all distracted… and goofy, I guess?"
    p "Yeah, that was kind of hilarious."
    n "Both of you burst into laughter, recalling the surprise pop quiz from today."
    show trida happy with dissolve

    trida "Anyways, that tension earlier makes me crave an iced tea."
    show trida embarrassed at center, dip with dissolve
    n "Trida looks at the floor fidgeting with their tie, glancing from the corner of their eye waiting for your reaction."

    menu:
        "I mean, it's kind of hot today, so…":
            $ tridaAffection += 1
            p "I mean, it's kind of hot today, so…"
        "Should we buy something to drink?":
            $ tridaAffection += 1
            p "Should we buy something to drink?"

    show trida happy at center, hop
    trida "Let's go buy it together!"
    n "For a moment, you can feel Trida's hands gripping your wrist, pulling you enthusiastically toward the Teddy Cup stall."
    hide trida with dissolve
    jump week1_teddy_cup


# ==============================================================================
# AFTER SCHOOL: TEDDY CUP STALL
# ==============================================================================

label week1_teddy_cup:
    scene bg teddy_cup
    with dissolve_scene_full
    play sound "audio/glass_chime.wav"
    play music audio.t6 fadein 1.5 loop volume 0.7

    # Visual Tenda TeddyCup
    n "The school was almost empty because most of the students had already gone home."
    n "You and Trida sat near the stall and ordered two cups of iced tea."
    n "While waiting for the drinks, both of you began chatting about today's topics and discussing what the curriculum would be like for the next three years."

    show trida uniform happy at center with dissolve
    trida "Not gonna lie, when they brought up the Final Assignment in twelfth grade? I was a little excited. I mean—how bad could it be?"

    menu:
        "It could be worse than we thought":
            p "It could be worse than we thought."
        "Maybe it was easier than we imagined?":
            p "Maybe it was easier than we imagined?"
        "I think it was still fifty-fifty for now":
            p "I think it was still fifty-fifty for now."

    # Visual Trida Looking at Players
    n "The winds rustled around them, tousling their hair in a wild dance, while the crisp sound of leaves crunching underfoot filled the air."
    n "As Trida breathed out slowly, a serene softness washed over their expression, as if they were lost in a vivid daydream."
    show trida embarrassed at center, dip
    trida "Well, however it is, I hoped we are on the same team."
    trida "I know it will be fun, with you."

    hide trida with dissolve
    jump week1_bedroom


# ==============================================================================
# EVENING: BEDROOM
# ==============================================================================

label week1_bedroom:
    scene bg bedroom_late_afternoon
    with dissolve_scene_full
    play music audio.t10 fadein 2.0 loop volume 0.6

    # Visual Player Room
    n "You just arrived in your room and let out a slow exhale."
    n "Your bags are resting on the chair while you lie back on the bed."
    n "The ceiling of your room feels emptier, but your chest is filled with joy from today's activities, mainly because you now have a friend."
    n "Then it hits you—there's something you've been wanting to do once you start high school. Maybe it will help you earn some extra pocket money."

    p "Yeah, I should get a part-time job."
    p "But what should I do?"

    menu:
        "Be an Indoapril Cashier":
            n "That sounds like easy money."
        "Work as a barista at a cafe":
            n "Maybe you'll enjoy the calm atmosphere."
        "Open a commission or a merchandise store":
            n "A creative outlet — could be fun."

    n "With a decision in mind, you close your eyes and let the exhaustion of the first week fade into sleep."

    n "Before you know it, another week at school begins..."
    jump week2_start
