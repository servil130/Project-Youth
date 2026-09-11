label week6_start:
    $ current_week = "Week 6"
    scene bg grapos_field
    with fade

    # Visual: Lapangan Grapos - Competition & Live Festival
    n "The atmosphere in Grapos was filled with excitement and energy."
    n "Music blasted throughout the area with a throbbing beat, vibrating in waves that sent a tremor through the ground itself."
    n "The audience churned like an excited mass, rising and falling to the music with colorful banners flying overhead."
    n "The smells of frying delicacies, sweat, and the faint metallic scent of cheap plastic ribbons from the trophy booths swirled in the air as the energy of hundreds of students built to a fever pitch."

    n "You were in your participant's zone, stretching your arms and trying to steady your beating heart."
    n "The competition was about to start, and as your gaze scanned the roaring crowd for a moment's respite, something caught your attention."
    n "Someone was jumping up and down, their movements so energetic that they seemed to propel themself without touching the ground."

    n "There was Trida, their face lit with excitement as they bounced up and down on the bench in a flash of color that made them stand out in the front row."
    n "They were practically vibrating with enthusiasm, drawing cheers from the crowd, every fiber of their being caught up in the excitement of the moment."

    trida "HEY [player_name]!"
    trida "LOOK OVER HERE!"

    menu:
        "Play along":
            jump week6_cheer_hero
        "Stay Focused":
            jump week6_cheer_subtle


label week6_cheer_hero:
    $ tridaAffection += 1
    n "You can't help but laugh. Your attention turns toward them, and you strike a ridiculously heroic pose—one hand on your hip and the other pointing to the sky like a classic anime protagonist."
    n "Trida absolutely loses it. They scream even louder, and their friends beside them start jumping and making a scene, turning into a singular roaring voice like a mosh pit."
    n "You're so caught up in the showmanship, flashing peace signs and winking at them, that you almost miss the referee clearing their throat into the microphone."
    jump week6_quiz_start


label week6_cheer_subtle:
    n "You force yourself to look straight ahead, jaw set. Your focus is on the podium, trying to tune out the sound of Trida shouting."
    trida "GO! THAT'S MY BEST FRIEND!"
    n "Trida was screaming like they were at a world championship match."
    n "Right as the countdown hits one, you can't help but look over and offer them a quick, tight-lipped smile."
    n "As you see the flash of deep red spreading across their ears when they realize you saw them, they immediately duck back, looking thoroughly shy."
    jump week6_quiz_start


# ==============================================================================
# TRIVIA COMPETITION
# ==============================================================================

label week6_quiz_start:
    n "The referee steps up to the center mic and clears his throat. The crowd goes quiet."
    moderator "Alright! Candidates, assume positions. We're going to test your general knowledge. First to three points takes the prize!"

    $ quiz_score = 0

    # Question 1
    moderator "What is the name of the longest river in the world, often debated between two major African and South American contenders?"
    menu:
        "The Amazon River":
            moderator "Incorrect!"
        "The Nile River":
            $ quiz_score += 1
            moderator "Correct!"
        "The Yangtze River":
            moderator "Incorrect!"

    # Question 2
    moderator "What process do plants use to convert light energy into chemical energy, effectively acting as the lungs of the planet?"
    menu:
        "Photosynthesis":
            $ quiz_score += 1
            moderator "Correct!"
        "Respiration":
            moderator "Incorrect!"
        "Fermentation":
            moderator "Incorrect!"

    # Question 3
    moderator "Which iconic Italian polymath painted the Mona Lisa and is often cited as the ultimate example of a Renaissance Man?"
    menu:
        "Michelangelo":
            moderator "Incorrect!"
        "Leonardo Da Vinci":
            $ quiz_score += 1
            moderator "Correct!"
        "Raphael":
            moderator "Incorrect!"

    if quiz_score >= 2:
        jump week6_quiz_win
    else:
        jump week6_quiz_lose


label week6_quiz_win:
    $ player_has_bouquet = True
    $ tridaAffection += 1
    n "The announcer throws the bouquet right into your arms."
    n "They are massive and a bit tacky with a strong smell of the florist shop."
    n "You step off the stage and spot Trida waving towards you, their face lit with the expression of someone who witnessed a miracle."

    p "Seriously now, holding these flowers feels like I have some Hollywood prop in my hands..."
    n "Your hands still tremble from pulling the trivia trigger, but the sight of flowers could not fail to inspire emotion."
    n "After all, you did not expect to get to the end of the round without making mistakes or blanking out."

    n "You thought to give the bouquet a thorough once-over, then you focused your gaze on Trida."
    n "They look genuinely delighted, as if they're about to burst into either tears or applause."
    n "A wave of tenderness washes over you as you remember that Trida has been a shoulder to lean on for the better part of recent weeks, helping you through difficult moments."

    p "Seriously now, this victory would be lesser without their aid. I think I am going to give these lovely flowers to them as a prize for being my idiotic cheerleader in the past few weeks."
    jump week6_post_competition


label week6_quiz_lose:
    $ player_has_bouquet = False
    n "The buzzer goes off, and that is it—you lost."
    n "The person who won starts holding up flowers and celebrating. You do not even want to look at them."
    n "You are staring at the ground, feeling terrible about what happened. You made a mistake on a question you knew the answer to."

    n "Suddenly, you hear a loud cheer coming from the side of the field. You look up."
    n "You see Trida standing on their toes, waving their arms in the air, and giving you a big thumbs up. Their face is bright red, looking a little silly."
    trida "It's okay!"
    n "You can tell they're trying to make you feel better from far away. They don't want you to be sad just because you lost."
    n "They look at you, stop for a second, and then start laughing warmly."
    p "Honestly, man, I owe them."
    jump week6_post_competition


# ==============================================================================
# UNDER THE BLEACHERS: SNACKS & LIVE CONCERT
# ==============================================================================

label week6_post_competition:
    scene bg grapos_field
    with fade

    n "They do not wait for you to come to them. They jog over, dodging through the crowd that is getting smaller."
    n "Their hair is all messy from the humidity. Their cheeks are red from cheering so much. They're full of energy."
    n "They hand you a cup of tea and grab your elbow to take you to the shade under the bleachers."

    trida "You were great. Do not worry about the score. Come on, sit down for a minute. You look like you are going to faint."
    p "Thanks..."

    n "The air under the bleachers smells like grass, and you can smell the food from the canteen nearby."
    n "You sit down on the bench. It feels good to be off your feet."
    n "Trida pulls out a paper bag from their hoodie. They open it."
    n "You see your favorite snack, but it is all smashed and messy. They see you looking at it. Their ears turn pink."

    trida "I know it is a mess. I got hungry waiting for you to finish. I am sorry. It does not look very good, does it?"

    menu:
        "What do you mean? It looks so good!":
            p "What do you mean? It looks so good!"
            $ tridaAffection += 1
        "Oh shut up, look at those goodies":
            p "Oh shut up, look at those goodies."
        "Don't mind it, it was the greatest thing ever":
            p "Don't mind it, it was the greatest thing ever."
            $ tridaAffection += 1

    n "You take a bite of the snack. It is warm and salty, and the flavor tastes good."
    n "As you eat, the noise from the field starts to fade. The crowd is still making noise, but you notice that Trida is quiet now."
    n "They're not watching the field or the other students. They're watching you with their eyes on you, so it feels different. It is not like when you are just talking at school."

    p "They say that intimacy is born in the space of the shared hour, but I felt it comes from something deeper—a feeling which only two people in the hall have learned to communicate in a shorthand language."
    p "When they first showed up, I was too busy worrying about something else, that suddenly they were becoming my closest companion—"

    n "As the school band launches into its lively performance, the sound envelops the area like an exhilarating wave."
    n "The music blares with a powerful intensity, the bass thumping so deeply that it resonates through the air and sends vibrations rippling through the ground beneath."

    p "—Now, I feel them in everything they do, from the food they bring me and them helping me in class, or even every single time they wave at me and tell me how glad they are to know me."

    n "Trida turns their head to the stage, and their eyes light up. Without thinking, they reach out and grab your wrist with a firm grip."
    trida "They already started the live music, let's go!"
    p "W-wait, Trida!"
    trida "Come on, we're gonna miss it!"

    n "You feel a shock when they touch you. It is like a spark of electricity that goes up your arm and to your chest."
    n "It is not a casual touch. It feels like they're trying to hold onto you. As they pull you up, your knees feel weak. Your heart is beating fast."
    n "You stumble forward, unsure if it is because of the music or because of the way they are touching you."

    # In the live concert crowd
    n "Trida works their way through the thick crowd of students until they find themself swallowed by the mass, where you watch from the inside."
    n "You are pressed from all sides, almost without space to breathe. The whole group sways slightly, and the pressure from the others, together with the pounding music, creates a barrier through which the world outside has been shut away."
    n "For a moment, it seems as if this is all that exists."

    n "The music erupts in a momentary pause to swell in your ears until suddenly the lead singer stands and screams something beautiful and sad into the metal grid above your heads."
    n "Your heart stops as you realize that it is most probably a love song, a confession perhaps, for it sounds as if the singer is addressing you directly as you hear the words for the first time."
    p "God, of course it's this song..."

    n "It is so embarrassingly romantic that you feel as if they're speaking it out to everybody in the school."
    n "You start thinking over all those things that have happened over the last few months—how they brought you food, waited for you, and looked at you as if you were the only one in the world."

    # Visual Splash Art: Trida looking at the stage
    $ splash_art = True
    n "Trida leans close to you, the warmth of their shoulder barely brushing against your own as they talk over the deafening music."
    trida "Man, listen to that vocalist. I mean, the way they were singing really sounded incredible... Honest, you know."

    # Visual Splash Art: Trida turning their gaze to Player
    n "They turn to you, eyes reflecting the thousand bright lights that flicker and dance overhead, glowing white-hot and flashing in all directions at once."
    n "For a moment, you are held spellbound by the sheer beauty of their gaze."
    n "It is as if they're looking right through you, and the sheer honesty of their voice makes the very words sound as if they come from them, not the singer on stage."

    menu:
        "It feels… kinda want to sound personal, doesn't it?":
            p "It feels… kinda want to sound personal, doesn't it?"
            $ tridaAffection += 1
        "Yeah. It's honest. Maybe a little too honest, don’t you think?":
            p "Yeah. It's honest. Maybe a little too honest, don't you think?"
            $ tridaAffection += 1
        "Geez. That’s—that’s really loud. Like, emotionally loud.":
            p "Geez. That's—that's really loud. Like, emotionally loud."

    n "You watch them intently, noting every flicker of emotion that passes across their face."
    n "They're still close, impossibly close, watching the stage as they hum along to the music almost absentmindedly, a lopsided smile playing across their lips."
    trida "Maybe. I don't know, but it's nice to hear something really true for once, isn't it?"

    $ splash_art = False
    n "Before you have time to react, you find yourself caught up in the surging mass of people around you."
    n "The band launches into a second number with a driving rhythm that seesaws furiously, while the lead singer joins in, his voice a rich ballad of longing."
    n "You are so unaware of the surging mass around you that you are caught completely off guard when suddenly Trida runs right into you, knocking you off balance sideways."

    trida "Oh, sorry! I'm sorry, I'm really sorry this crowd is crazy!"
    n "Their face is lit up as they apologize genuinely, flashing an expression of surprise as they turn to one side to make room and straighten up."
    trida "They sound really good, don't they? This guitarist... I mean, it's a beautiful song! Just beautiful music..."

    # Visual Splash Art: Trida is close to Player with a blushing face
    $ splash_art = True
    p "My heart is hitting my ribs so hard I'm terrified they can actually hear it over the music."
    p "It's ridiculous. It was just a bump, just an accident. God, the air in here is suddenly so unbearably hot. I don't know where to look, I don't know what to do with my hands..."

    n "Trida clears their throat as they turn back toward you, their hand hovering just above your sleeve."
    n "When the final note fades into the cheers of the crowd, the lights change abruptly from violet haze to bright white, and the magic is broken."
    n "The band begins to clear the stage as the chatter and noise of the next group drown out the music, leaving the charged tension between you and Trida to linger softly in the air."
    $ splash_art = False

    if player_has_bouquet:
        jump week6_bouquet_gifting
    else:
        jump week6_end_summary


# ==============================================================================
# BONUS ROUTE: FOR OBTAINING THE BOUQUET
# ==============================================================================

label week6_bouquet_gifting:
    scene bg gates_morning
    with fade

    n "The walk back is silent, the rustling of leaves covering the noise of the school's rabble after the performance."
    n "You find yourself by the trunk of a tree, feeling that you have found a part of the world that is solely your own."
    n "You and Trida stand in the shade of the tree, facing each other."
    n "You smooth the stems of the bouquet one last time before presenting the flowers across the small distance between you."
    n "You take a steadying breath."

    p "Hey Trida, here…"
    n "You are surprised by how quiet your voice sounds."
    p "I'm being serious. I don't really like those... so the flowers are probably better going to someone who actually wants them."

    n "Trida turns to you, regarding the flowers with an expression of utter, undiluted shock."
    n "Their eyes are wide, blinking rapidly, and for a moment, you think they'll refuse to take them."
    n "They tentatively reach forward and pull your wrist towards them before taking the stems from your grasp gently."

    trida "You... in all seriousness?"
    n "Trida asks, their voice cracking ever so slightly."
    p "Yeah, come on, take them."

    n "You encourage gently, laying the bouquet across their chest."
    n "You watch as they take the flowers with an almost reverent touch, their fingers shaking the entire time."
    n "They stare intensely at the blooms, their face all red, their fingers fidgeting with the bow in their lap."
    n "They look utterly ridiculous and breathtaking all the same, and you feel your heart hammering wildly in your chest."

    n "They look completely at a loss as to what to do with these strange flowers you have suddenly gifted them."
    n "They take a steadying breath, their shoulders hitch, and they look up at you, only to immediately turn back to the blooms in their lap."
    n "They look so surprised by your thoughtful gesture, so utterly not themself, that you think you have never seen them more beautiful in your life."

    trida "I..."
    n "Trida whimpers, saying nothing more, only brushing their lips together before giving you a small, tiny smile."
    n "You feel so overwhelmingly happy, if only because they look so utterly stunned by your gesture."
    n "A calming stillness surrounds the tree as a gentle silence falls around both of you, as if the world paused to give Trida a moment of peace."

    # Friends interrupt
    braided_girl "Trida! Hey, come here! We were looking for you!"
    n "Two of their friends round the corner from the gym, cell phones in hand, shouting excitedly."
    n "Trida jumps at the sudden intrusion, eyes widening in surprise as they cradle the small bouquet of flowers."

    trida "Oh! Uh, hey guys..."
    cap_boy "Radit has already begun his competition. Let us go and watch!"
    trida "Uhm..."
    p "It's fine, just go there. I still have to do something after this..."
    trida "Really? But..."
    p "...it's fine, Trida."

    trida "Oh god. Sorry, I... I have to go. I mean, I'll see you later."
    p "Yeah, yeah..."
    trida "Thank you so much for all of this, by the way... See you later, I mean—I hope I see you later!"

    n "They do not wait for you to respond, their boundless energy already pushing them to take off running, clutching the flowers to their chest as if they were a prize."
    n "As they turn around, a flash of guilt crosses their face before they trot off toward their friends, giving you one last parting glance, cheeks flushed with embarrassment."
    n "You see them turn around once more, showing off the bouquet of flowers to their friends, no doubt telling them an exaggerated tale."
    n "One of their friends nudges them in the side, their grin widening as they look back at you, head bent down in mock shame."

    n "As they turn around again, a wave of unexpected tenderness washes over you."
    n "This is turning out to be just another exhausting day after a competition, but you feel as if something amazing has just happened."
    n "Something that has bonded you to them in a way that will stay with you for a long time."
    n "As you trace small patterns over the rough bark of the tree with your fingers, a strange feeling of contentment washes over you."
    p "This has been a good day. It might even be the best day I have had in a long while."
    $ tridaAffection += 3
    jump week6_end_summary


label week6_end_summary:
    n "The sun dips below the horizon, painting the sky in shades of deep indigo."
    n "The memories of the music, the laughter, and the quiet moments linger warmly as you finally head home."

    # End of Week 6 -> Continue to Week 7
    jump week7_start
