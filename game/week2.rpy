label week2_start:
    $ current_week = "Week 2"
    scene bg classroom
    with dissolve_scene_full
    play music audio.t3 fadein 1.5 loop volume 0.7

    # Visual: Classroom Afternoon
    n "The humming sound of the air conditioner fills the room as a gentle breeze blows through the warming space."
    n "You yawn softly, watching the minutes crawl by like a snail in a race."
    n "Your fingers gently rub your eyelids, trying to fight off the heavy midday drowsiness."
    n "Then, the sharp chime of the school bell rings through the hall."
    n "The teacher at the front gathers their notes and steps out, letting the room burst into chatter once more."

    # Trida approaches
    n "You shift your gaze as a familiar figure approaches your desk."
    show trida uniform neutral at center with dissolve
    n "Trida holds a worn textbook against their chest, their posture a mix of hesitation and nervous energy."

    if player_name:
        trida "[player_name], can I ask you something real quick?"
    else:
        trida "Hey, can I ask you something real quick?"

    n "You look up, meeting those vibrant sunset-orange eyes."
    trida "You do remember that English assignment from last week, right...?"

    n "You think back to the first week's lesson."
    n "The teacher had assigned a profile essay about a new classmate—a classic icebreaker to get students talking."
    p "Ah, the 'get to know your friend' essay?"

    n "Trida nods eagerly, shifting the book between their hands."
    n "Their eyes dart toward the window as if gathering courage before returning to you."
    trida "Have you got a partner yet, for that assignment?"

    n "You pause, observing the way their fingers fidget restlessly against the cover."
    p "I don't think I've got one yet... why?"

    trida "Because I'm calling dibs on you as my partner!"
    show trida happy at center, hop
    play music audio.t4 fadein 1.0 loop volume 0.7
    n "The quick, playful declaration catches you off guard."
    n "Even though you've only known each other for a couple of weeks, it's flattering to know they wanted to work with you."

    menu:
        "That can be arranged.":
            p "That can be arranged."
            trida "Sweet! I knew I could count on you!"
            $ tridaAffection += 1
        "Sure! Honestly, that sounds kinda great.":
            p "Sure! Honestly, that sounds kinda great."
            show trida happy at center, hop
            trida "Really?! Awesome! This is gonna be a breeze!"
            $ tridaAffection += 2
        "Well, it was a pretty good idea.":
            p "Well, it was a pretty good idea."
            trida "Right? Great minds think alike!"
            $ tridaAffection += 1

    n "Trida grins broadly, the earlier hesitation melting away completely."

    # NPC Shy Classmate approaches
    shy_classmate "Um... sorry for disturbing..."
    n "A hesitant, quiet voice breaks into your conversation."
    n "You and Trida look over to see a soft-spoken girl standing a few paces away, clutching her notebook tightly."

    shy_classmate "May I... join you two?"
    show trida happy at to_left
    n "You and Trida exchange a brief glance before Trida speaks up with natural warmth."
    trida "Yeah, of course! The more the merrier, right?"

    shy_classmate "R-Really? Thank you..."
    n "A look of profound relief washes over her face, her knuckles unclenching slightly."
    show shy_classmate at slide_right, dip with dissolve
    n "She steps closer to your desks as a brief, awkward quiet settles among the three of you."
    n "Someone needs to break the ice..."

    menu:
        "So, how about we split the work now?":
            p "So, how about we split the work now?"
        "Maybe we can divide the work first.":
            p "Maybe we can divide the work first."

    shy_classmate "I can do anything, really. I mean, I'm okay with writing, or infographics—"
    n "Before she can finish her rushed, trembling sentence, Trida cuts in."
    trida "No, no, hey! You don't have to take on everything by yourself."

    n "Trida scratches the back of their neck, offering a reassuring, lopsided smile."
    show trida neutral at tleft with dissolve
    trida "We're a team now, so we'll divide it fairly."

    n "The girl blinks, staring at Trida with quiet surprise before giving a gentle nod."
    shy_classmate "Okay... yeah, that sounds really nice."

    n "You can practically hear the slow exhale from Trida, clearly relieved to have put her at ease."
    p "Guess this works out pretty well."

    hide shy_classmate
    hide trida
    with dissolve
    jump week2_project_afternoon


# ==============================================================================
# AFTERNOON STUDY SESSION
# ==============================================================================

label week2_project_afternoon:
    scene bg classroom
    with dissolve_scene_full

    # (Timeskip: Some hours later)
    n "Some hours pass, and the classroom gradually empties as students head home."
    n "Long, golden shafts of afternoon sunlight stream through the tall windows, casting amber lines across the desks."
    n "Only the three of you remain, huddled around a shared table with notebooks and profile drafts spread out."
    show trida uniform happy at tcenter with dissolve
    n "Trida is enthusiastically rambling about their hometown, gesturing animatedly with a pen."

    n "You chuckle along, but as you glance across the desk, a faint sense of unease tugs at you."
    shy_classmate "Uhh... So the intro was... and the body part..."

    n "Her voice trails off into an unsteady whisper."
    n "Her cheeks are flushed a distressed shade of red, and her breathing sounds shallow and strained."
    n "Her slender frame trembles faintly, her eyes glistening as if fighting off tears."

    n "Gently, you reach out and place a steadying hand on her shoulder."
    n "She flinches slightly in surprise, looking at you with wide, exhausted eyes."
    n "Trida stops talking immediately, the sudden silence hanging thick in the room."

    p "Hey, are you okay?"
    n "You can feel the heat radiating through her uniform."
    shy_classmate "Ah—yeah, I'm fine. Just a little—"

    n "She tries to brush it off, but her eyebrows twitch and she sways slightly in her chair."
    show trida sad at to_center, dip
    trida "Whoa! Hey!"
    play music audio.t5 fadein 0.5 loop volume 0.7

    n "Trida shoots up so fast the wooden legs of the chair screech harshly against the linoleum floor."
    n "Their hands shoot forward to catch her, then freeze awkwardly in mid-air, unsure of where to touch."
    n "You move quickly, supporting her arm so she doesn't slip from her seat."

    trida "Wait, sit down first—no, wait, you're already sitting—um!"
    n "Panic takes over Trida's face as their eyes dart wildly across the room."
    n "Spotting their open notebook, Trida grabs it and begins fanning her with frantic, high-speed gusts."

    shy_classmate "I-I'm okay. Really—"
    show trida sad at center, panic
    trida "What do we do?!"

    n "The violent flapping sends loose worksheets fluttering across the desk, only adding to the chaos."
    p "Trida."
    n "Your firm tone cuts through the frenzy."
    p "You're making her more overwhelmed..."

    n "Trida freezes, horrified, a drop of cold sweat glistening near their hairline."
    show trida sad at center, dip
    n "They slowly lower the notebook, their chest heaving as they rein in their panic."
    p "Can you stand?"

    n "You crouch beside the girl, keeping a steady grip on her shoulder."
    shy_classmate "A little dizzy..."

    n "You glance over at Trida's thoroughly stricken expression."
    p "Could you grab some water?"

    n "Trida spins around instantly—and slams their knee right into the corner of the desk with a loud clatter."
    n "They hiss in pain, clutching their leg for half a second before willing themselves upright."
    show trida embarrassed at center, dip
    trida "-I'm okay!"
    hide trida with easeoutleft

    n "They bolt out the classroom door, footsteps echoing down the quiet corridor."
    shy_classmate "I'm sorry..."

    menu:
        "Don't be. You should've said something earlier.":
            p "Don't be. You should've said something earlier."
            n "You offer a gentle, reassuring tone so she knows she doesn't have to push past her limits."
        "Hey, it's okay. You're not feeling well, and that's what matters right now.":
            p "Hey, it's okay. You're not feeling well, and that's what matters right now."
            n "Her shoulders drop, releasing some of the agonizing tension she had been holding."

    # Trida returns with water
    n "The heavy classroom door swings open as hurried footsteps rush back in."
    show trida uniform sad at center with easeinleft
    n "Trida hurries over, carefully unscrewing a chilled water bottle before handing it to her."
    trida "Here, drink slowly..."

    n "She takes a tentative sip, the coolness helping bring faint color back to her pale cheeks."
    n "Trida hovers beside the desk, uncharacteristically still and quiet, watching her with deep concern."

    menu:
        "We should probably call it a day now.":
            p "We should probably call it a day now."
        "Let's call it a day. You should get some rest.":
            p "Let's call it a day. You should get some rest."

    shy_classmate "I'm really sorry for ruining the study session..."
    trida "Hey, you don't need to apologise at all."
    trida "Your health comes first. Group projects can always wait."

    n "A faint, grateful smile touches the girl's lips."
    n "The three of you pack up her belongings, and together you and Trida walk her down to the lobby until her parents arrive to pick her up."
    shy_classmate "I'll message you both later..."
    trida "Take care, okay? Rest up!"
    hide trida with dissolve

    jump week2_classroom_sunset


# ==============================================================================
# AFTERMATH: ALONE WITH TRIDA
# ==============================================================================

label week2_classroom_sunset:
    scene bg classroom
    with dissolve_scene_full
    play music audio.t6 fadein 2.0 loop volume 0.7

    n "The classroom door clicks shut behind you as both of you return to the empty room."
    n "The afternoon sun has dipped lower, casting long, dusty amber rays across the vacant desks."
    n "The rhythmic ticking of the wall clock seems unusually loud in the quiet room."

    n "Trida stands near your shared table, one hand rubbing the back of their neck."
    show trida uniform sad at center with dissolve
    trida "I panicked."

    n "A small, self-deprecating laugh slips from their lips."
    n "Their eyes linger on the scattered pens and notebooks on the desk, heavy with guilt and frustration."
    trida "Like, I always mess things up..."

    menu:
        "Yeah, I noticed.":
            jump week2_trida_reassure_noticed
        "Hey, it's fine. Everyone messes up sometimes.":
            jump week2_trida_reassure_fine
        "You didn't do anything wrong, you know.":
            jump week2_trida_reassure_wrong


label week2_trida_reassure_noticed:
    p "Yeah, I noticed."
    n "A sharp wince crosses Trida's features, followed by a soft, breathy laugh."
    show trida embarrassed at center, dip
    trida "Wow, okay. No need to confirm it like that!"
    n "You step closer, placing a comforting hand on their shoulder."
    p "I know you just wanted to help. That's what counts."
    jump week2_trida_bond


label week2_trida_reassure_fine:
    $ tridaAffection += 1
    p "Hey, it's fine. Everyone messes up sometimes."
    n "Trida hesitates for a moment, their vibrant orange eyes settling on yours."
    n "It's a penetrating look, stripped of their usual comedic deflection."
    trida "Guess that includes me, too. Thanks."
    show trida happy at center, hop
    n "Their lips curve into a genuine, warm smile, their voice carrying a quiet relief."
    jump week2_trida_bond


label week2_trida_reassure_wrong:
    $ tridaAffection += 2
    p "You didn't do anything wrong, you know."
    n "Trida pauses, visibly caught off guard by the certainty in your voice."
    n "The words seem to sink deep beneath their defenses."
    n "Their shoulders finally slump, a long, slow breath releasing the tight knot in their chest."
    trida "Maybe, but I still wasn't helping much..."
    show trida neutral at center, dip
    trida "Still... thanks. Really."
    n "Their gaze lingers on yours, an unspoken bond of empathy and understanding tightening between you."
    jump week2_trida_bond


label week2_trida_bond:
    trida "Thanks for stepping in back there."
    n "A soft exhale reverberates in the stillness of the room."
    trida "You handled that really well."

    n "You both slowly slide back into your chairs."
    n "Even without looking directly at them, you can feel how easily readable their emotions are."
    p "Someone had to balance you out."

    trida "Hey! So I'm the chaotic one now?"
    n "A fleeting look of exaggerated bewilderment crosses their face, as if processing the accusation."
    show trida happy at center, hop
    trida "Okay, yeah. That's fair."

    n "Trida's signature cheeky grin breaks through, completely sweeping away the remaining gloom."
    p "So, guess it's just us for now..."

    n "Trida clears their throat with an awkward laugh, their fingers drumming against the draft paper."
    show trida embarrassed at center, dip
    trida "Anyway—uh, we should probably start over, right?"
    trida "...Partner."

    jump week2_partner_moment


# ==============================================================================
# TIMESKIP: THE TOUCH
# ==============================================================================

label week2_partner_moment:
    # (Timeskip: A few minutes later)
    n "A few minutes pass as you both settle into a quiet, comfortable rhythm."
    n "The soft rustle of paper and the steady scratch of pens replace the earlier noise."
    trida "Okay, so if we start with this section..."

    n "At the exact same moment, both of your hands reach toward the center of the desk for the correction tape."
    n "Your fingers graze against each other—a fleeting brush of skin."

    # (Visual Splash Art: Trida and Player Hand Touching - placeholder)
    $ splash_art = True
    n "A sudden spark of surprise courses through your fingertips."
    n "For a split second, time seems to freeze in the warm amber glow of the classroom."
    n "The air feels charged, almost electric, momentarily blurring the boundary of simple friendship."

    trida "-Ah, sorry!"
    show trida embarrassed at center, dip
    n "A bright, flustered flush blooms across Trida's cheeks."
    n "They yank their hand back too quickly, breaking the spell but leaving a lingering warmth between your hands."
    $ splash_art = False

    menu:
        "It's... fine.":
            $ tridaAffection += 1
            p "It's... fine."
            n "You feel a faint heat creeping onto your own face as you avert your eyes."
        "No problems...":
            p "No problems..."
            n "You take a steadying breath, trying to act casual despite your fluttering chest."
        "Oh-yeah. Don't mind it!":
            $ tridaAffection += 1
            p "Oh—yeah. Don't mind it!"
            n "You offer a lighthearted laugh, attempting to brush off the undeniable tension."

    n "Neither of you moves for a heartbeat."
    n "Slowly, you pick up the correction tape and hand it across the desk."
    n "Trida takes it with a slight tremble in their fingers, their eyes cautiously meeting yours."
    n "A silent, electric curiosity hangs between you."

    p "Right. About these paragraphs..."
    show trida happy at center, hop
    n "A soft, radiant smile dances across Trida's lips, warm and bright in the evening light."
    trida "...We do make a pretty good team."

    n "The quiet dusk wraps around the classroom as you both continue working side by side."
    n "And for the first time, you feel a quiet certainty that this year is going to be unforgettable."
    hide trida with dissolve
    n "With the day's work done, you gather your belongings and step out into the cool evening air."
    n "You arrive at the indoapril convenience store, where the neon lights flicker softly against the darkening sky."
    p "Time to get to work."
    jump part_time_shift
    label part_time_shift:
    if player_job == "Cashier":
    show supermarket.jpg with dissolve
        call cashier_minigame
    return
    # End of Week 2 -> Continue to Week 3
    jump week3_start
