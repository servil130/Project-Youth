# ==============================================================================
# PROJECT YOUTH: SWEET INSPIRATION
# ACT I - CHAPTER IV: WEEK 4
# ==============================================================================

label week4_start:
    scene bg classroom
    with fade

    # Visual: Classroom Morning
    n "The morning breeze, infused with a subtle hint of air conditioning, greeted you as you entered the classroom."
    n "You looked over the seats from the front to the back, looking for the person who had become closest to you in the last few days."
    n "Your gaze landed on Trida's vacant desk."
    n "A short pause occurred as you recognized they were probably going to be late, and a slight smile appeared on your face."

    r "Did they install a new statue in class or something?"
    n "You jolted, turning to find Radit's signature cheeky grin. Right, him."
    p "Morning, Radit."
    n "Radit eyed you for a second, then snorted, thumping your backpack so hard it drew a few stares from your classmates."
    r "Stop grinning at nothing. People are going to think you've gone off the rails already."
    p "Oh! Yeah, uh... Have you seen Trida?"

    n "You headed to your usual desks, the strap of the heavy backpack digging into your shoulder."
    n "Radit casually threw his bag onto his chair and started pulling out his books, dropping them onto his desk with practiced ease."
    r "Probably late. You know how they are. By the way, did you finish that math assignment?"

    # Trida skids in
    t "RADIT!"
    n "A rhythmic jingle of keys announced their presence before the door even clicked open."
    n "Trida skidded into the room, their chest heaving and their hair disheveled from the dash."
    n "They didn't have the breath for a full speech—just enough for a pointed glare."
    t "You... *huff*... You left me behind!"

    n "They grabbed Radit by the shoulders, shaking him frantically."
    n "Radit didn't even flinch, his expression settling into the exhausted 'done-with-this' look he reserved for Trida's morning meltdowns."
    r "Because the last time I knocked on your door, I heard nothing but your alarm wailing for the tenth time. Which means..."
    t "...I overslept."

    n "Watching their casual, lifted banter, something finally clicked in your mind."
    p "Wait, do you two live in the same boarding house?"
    n "Both of them now turn their faces to you, but the very differences in their contrasting expressions make you kind of want to laugh."
    r "Sadly, yes..."
    n "Radit let out a heavy sigh as his shoulders tensed up."
    t "Sounds fun, right?"
    r "Nah, it's a living nightmare. Imagine living across a rhythm game player who thinks the whole building needs to hear the combo sound effects at 2 AM."
    t "It's called grinding, Radit! I was trying to S-rank a track, okay?"

    n "You dropped the bag onto your chair with a heavy thud, feeling the familiar weight of exhaustion."
    n "Your hand rubbed your eyes, letting out a long, slow breath as you leaned against the desk."
    p "Of course, they were at it again..."

    t "And for your information, the lore in this new JRPG is literally life-changing. I couldn't just turn it off mid-cutscene."
    n "You saw Radit start to spin his chair around and lean back with his arm behind his head."
    n "With those half-lidded eyes moving to yours and that smirk tugging around, you knew you were going to be dragged along with this."
    r "Right. 'Life-changing...' You spent three hours dying to the same boss fight and screaming at your screen. I'm pretty sure someone beside your room is convinced you're running a fight club."

    n "Trida started slamming their hands on your desk, then leaned closer and grabbed your arms, along with those wide-looking eyes that are always there when they are over-caffeinated."
    t "It's about progression, man! Seeing yourself get better at the mechanics—it's the best feeling!"
    t "[player_name], tell him! Isn't it better to actually have a hobby you're passionate about instead of just... I don't know, staring at a wall and judging people?"

    n "You shifted in your seat, the wooden edge digging into your hips. You look over at Radit, who is lazily spinning a pen between his fingers. He doesn't even look bothered by the jab."
    r "Judging people? Nah. I'm just observing."
    r "Like how I observed you losing that same boss fight for four hours straight last night because you kept trying to brute-force the parry window."

    n "Trida froze mid-gesture, their ears flushing a bright, indignant red."
    n "You blinked, genuinely surprised by Radit's confession."
    p "So he was paying attention to Trida's game after all."

    t "Wait, what? You hear the audio cues through the wall? And how do you know it's a parry issue? You haven't touched a controller since the semester started!"
    n "Radit shrugs as he writes through his math assignment that he clearly hasn't cleared. He leans on the chair, looking completely unbothered."
    r "I don't need to play it to know you're playing it wrong. Your button-mashing is very rhythmic, Trida."
    n "Then he stopped writing, putting down his pen with a half-sneer coming at Trida, trying to pull more of a reaction out of them."
    r "If you just chilled out and timed your hits to the bass line, you'd have cleared the level days ago."

    n "Trida started looking at him like he was a ghost talking. Then they threw that look back at you, then jumped back to Radit's smug face, clearly torn between wanting to argue and wanting to know what that guy is up to."
    t "[player_name], tell him he's full of it! Tell him he's just making that up to get under my skin. He's just bluffing, right?"
    r "Go on, [player_name]. Tell them, I should show them exactly what they're doing wrong on their own console, or are you going to keep letting them suffer like this?"

    menu:
        "Agree that Radit is right":
            jump week4_agree_radit
        "Call out Radit for being rude":
            jump week4_defend_trida


label week4_agree_radit:
    $ radit_affection += 1
    p "He's got a point, Trida. You're overthinking the mechanics. Just listen to him for once."
    n "Radit's smirk turns into a genuine, smug grin. He points a finger at Trida with a triumphant look."
    r "See? Even [player_name] is tired of your noise pollution. Admit it, I'm right."
    n "Trida's jaw drops as they look at you with clear betrayal, their shoulders slumping as they grumble."
    t "Wow. Fine. Everyone's a critic."
    jump week4_break_grapos


label week4_defend_trida:
    $ tridaAffection += 1
    p "Stop being a jerk, Radit. Just because you're good at the game doesn't mean you have to be a total elitist about it."
    n "He stops spinning his pen as his smirk fades, replaced by an unreadable expression. He shrugs, looking unaffected."
    r "Elitist? Just being honest. But sure, keep playing wrong if it makes you feel better."
    n "Trida practically beams, their mood shifting from frustration to relief instantly. They hit their fist against the desk, pointing it at Radit."
    t "Exactly! Thank you! See, Radit? Even [player_name] thinks you're being a pain."
    jump week4_break_grapos


# ==============================================================================
# MORNING BREAK: GRAPOS
# ==============================================================================

label week4_break_grapos:
    scene bg grapos_field
    with fade

    # Visual: Lapangan Grapos
    n "After the most chaotic morning you could imagine, the three of you finally managed to get along in class."
    n "Whether it's a dull history lecture or a math session where everything seems confusing, time eventually moves on."
    n "When the bell rings, signaling break time, it feels like the end of a battle."

    n "You've just come back from the teacher's office after delivering everyone's math books when you spot a tall person in front of the studio talking with some seniors."
    n "Out of nowhere, they all turn to face you and then walk away, leaving Radit by himself."
    r "You finished?"
    p "Yeah, I already turned in everyone's books."
    r "Great job. You handle everything well, unlike someone, I guess..."

    n "Radit put both of his hands in his pockets as his face looked afar where Trida is busy talking with other students and trips on their own foot, their movements as chaotic as their morning."
    n "Radit lets out a low huff as his eyes observe Trida's movement."
    r "They've been trying to min-max that party build for, like, three days straight. They're gonna waste their whole lunch break grinding for a drop that literally doesn't exist."
    n "He looks bored, but there's a flicker of annoyance in his eyes—not at Trida, just at how hard they're making it on themself."
    r "I might have ended up hopping into their save file tonight and re-specced their main DPS. Swapped their gear for a late-game crit build and fixed their whole rotation."
    n "He lets out a dry and tired laugh, glancing at his own shoes."
    r "Whatever. Don't tell them about that, though."

    p "Wait, so you're actually helping them?"
    n "He looks at you, clearly with a sense of softness between those unusual eyes. Then he lets out a scoff that rings in your ears."
    r "I just want them to stop losing. It's getting painful to watch."

    # Sabian appears
    n "Before you can even reply, a voice cuts through the air. You look up to see Sabian looking super spirited as he moves from the studio doors."
    sab "Yo, [player_name]! Finally done?"
    p "Oh-yeah, just running a couple of errands."
    sab "Come on, skip studying for a second. We're grabbing lunch, you should come through."
    n "Sabian doesn't even wait for your words. He just gives you that very pleading look."
    n "You glance back at Radit, who is already giving his questioning look."
    r "Guess you've been recruited. Honestly, chilling with the seniors beats sitting listening to Trida complain all day."
    n "But you clearly know that tone means he hoped you would accompany him."

    menu:
        "Hang out with the seniors":
            jump week4_canteen_sabian
        "Head class with Radit":
            jump week4_classroom_radit


label week4_canteen_sabian:
    $ sabian_affection += 1
    p "Catch you later, Radit. I'm starving, and I don't think I can handle Trida's gaming meltdowns on an empty stomach."
    n "Radit scoffs, his lazy eyes rolling toward the ceiling."
    r "Traitor. Leaving me alone with the hurricane? Fine, go eat. Just don't let Sabian talk your ear off about his latest project."

    scene bg teddy_cup
    with fade
    # Visual Canteen
    n "You jog to catch up with Sabian, leaving the studio behind. The canteen is buzzing—a welcome escape from the tension of the workspace."
    n "As you enter, Sabian claps a hand on your shoulder."
    sab "Took you long enough! Thought you were going to spend your whole break running errands. Sit, sit."
    n "You made your orders and hopped into the seat across from him."
    n "The conversation shifts to topics worlds away from your daily grind. It's very chaotic, and for once, you don't have to think about tasks or anything to fix Trida's game stats."
    n "It's the perfect small recharge, even as the guilty part of you wonders how Radit will survive."
    jump week4_sunset_walk


label week4_classroom_radit:
    $ radit_affection += 2
    n "Radit looks at you, his smirk softening into something almost... relieved."
    n "He starts walking toward the classroom, his posture finally relaxing."
    r "Honestly? Let's go, I've got some leftover snacks in my bag if you're actually gonna die of hunger."

    scene bg classroom
    with fade
    # Visual Classroom
    n "You walk through with Radit as the chaotic noise of break time slowly fades behind you, replaced by the cool air of the empty classroom."
    n "Radit drops into his chair and tosses a bag of chips to you."
    n "He doesn't say anything for a while, just pulls out his phone to scroll through game forums."
    n "You put your head down on your desk, the cool wood feeling amazing against your face."
    n "You don't have to entertain anyone or fix anyone's problems. It's the kind of recharge that actually feels like a break."

    r "You know, you're the only person who doesn't constantly try to force me to talk."
    n "His eyes were still glued to the phone, but you knew the sentence was for you."
    r "It's appreciated."
    n "You shift your head slightly on the desk, looking over at him. Then a soft laugh escapes your mouth as you start to unpack the chips bag."

    menu:
        "Yeah, well, someone has to balance your edge. Honestly, you're way less annoying when you aren't talking.":
            p "Yeah, well, someone has to balance your edge. Honestly, you're way less annoying when you aren't talking."
        "It's nice to just chill, you know?. Plus, you're decent company when you aren't roasting people.":
            p "It's nice to just chill, you know? Plus, you're decent company when you aren't roasting people."
        "I'm literally too fried to talk. Just enjoying the silence, man. Don't take it the wrong way.":
            p "I'm literally too fried to talk. Just enjoying the silence, man. Don't take it the wrong way."

    n "Radit lets out a low, genuine laugh that you rarely catch; he looks more relaxed. He taps his screen down, then glances over at you."
    r "Don't get used to it, man. I've got a whole list of sarcastic comments ready for when the others get back."
    n "He tosses his phone onto his desk and leans back, closing his eyes for a second. The classroom is silent again; even so, it was not an awkward quietness. There is something warmer about it."
    r "Glad you ditched him. That senior was giving me a headache just by existing."
    n "A slow snort comes from your lips as you munch through the chips on your desk."
    p "I think he just wanted someone to be his pack mule."
    r "Exactly. Which is why you have top-tier taste in friends. Keep it up."
    n "He went back to his phone, but the silence shifted, and a whole lot more was earned. For these few minutes, everything feels like it can be tossed aside."
    jump week4_sunset_walk


# ==============================================================================
# LATE AFTERNOON: WALK HOME
# ==============================================================================

label week4_sunset_walk:
    scene bg gates_morning
    with fade

    # Visual: SMK Raden Umar Said Gates
    n "The golden hour light stretched long across the pavement, painting the world in warm, hazy tones as you and Trida drifted away from the gates of SMK Raden Umar Said."
    n "A cooling breeze carried the savory, irresistible scent of round tofu frying nearby, grounding you in the simple peace of the late afternoon."

    n "Trida moved with restless energy, clutching a greasy plastic bag of snacks in one hand and a carton of chocolate milk in the other."
    n "They seemed caught in their own internal rhythm, their excitement bubbling over with every step, and you found yourself falling into pace beside them, letting the routine of the walk settle over you like a familiar blanket."

    t "Y'know, I feel like these past four weeks have been... intense, right? Like, in a good way, but also in a 'my brain is turning into a tangled wire' kind of way."
    p "Tell me about it."
    t "It's like we're trapped in some game, except instead of leveling up stats, we're just stuck obsessing over cubes, extrusions, and topology that makes me want to pull my hair out."

    n "Trida pauses, looking up at the sky where the orange light is beginning to fade into a deep indigo."
    n "They shift the plastic bag, their fingers tapping rhythmically against the side of their chocolate milk carton—a clear sign they're bracing themself before looking over at you."

    n "Trida's steps faltered, their frantic rhythm finally tapering off. They shifted their stance to meet your gaze, the warm glow of the sky overhead bleeding into dusk to drape their features in soft, flickering amber."
    n "The morning's chaotic energy had vanished, replaced by a rare, quiet fragility that seemed to settle over them like the evening chill."

    t "Even so, I think I'm starting to trying to love it."
    t "I mean... if I didn't have the passion, I don't think I'd ever feel like I could actually see a future for myself here."
    t "...How about you? Can you picture it yet?"

    menu:
        "It's a gamble, I guess. But we're only four weeks in—maybe it's too early to decide if we're winning or losing.":
            jump week4_trida_gamble
        "I think it's worth it. Especially with you around makes it fun.":
            jump week4_trida_worth
        "Don't 'crash out' yet. We haven't even finished our first animation project, and you're already worried about the end?":
            jump week4_trida_crash


label week4_trida_gamble:
    p "It's a gamble, I guess. But we're only four weeks in—maybe it's too early to decide if we're winning or losing."
    t "Yeah... that's a good point. I'm pretty sure I'd have gone crazy by now if not for you being a good pal."
    jump week4_walk_conclusion


label week4_trida_worth:
    $ tridaAffection += 2
    p "I think it's worth it. Especially with you around makes it fun."
    t "Yeah... that's a good point. I'm pretty sure I'd have gone crazy by now if not for you being a good pal."
    jump week4_walk_conclusion


label week4_trida_crash:
    $ tridaAffection += 1
    p "Don't 'crash out' yet. We haven't even finished our first animation project, and you're already worried about the end?"
    t "Yeah... that's a good point. I'm pretty sure I'd have gone crazy by now if not for you being a good pal."
    jump week4_walk_conclusion


label week4_walk_conclusion:
    t "I'm always spiraling about whether I've got the skills for this, but then it hits me... even if I hit a 'game over,' I'm hitting it with you."
    n "Trida pauses softly."
    t "That makes the whole thing feel way less like a nightmare."

    n "They offer a lopsided, genuine smile, nudging your arm with their elbow—a faint attempt to lighten the sudden weight of the moment."
    t "Don't worry, I'm not sweating it. Not yet. We did a lot of work this year. You're stuck with me until you graduate, am I right?"
    p "Heh, I'd like to see that."

    n "Walking in the direction of the sunset, your gaze catches how the warm beams of light hit Trida's grin as if it's a sunny aura radiating from their face."
    n "Your mind starts to wander and contemplate what Trida promised."
    p "Stuck with me, huh?"

    # End of Week 4 -> Continue to Week 5
    jump week5_start
