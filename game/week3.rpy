# ==============================================================================
# PROJECT YOUTH: SWEET INSPIRATION
# ACT I - CHAPTER III: WEEK 3
# ==============================================================================

label week3_start:
    scene bg classroom
    with fade

    # Visual: 3D LAB Morning
    n "The dim light casts pale shadows across the room, carrying the scent of cool air and faint pine from the woods outside."
    n "The temperature is uncomfortably cold, displaying 21 degrees on the digital thermometer."
    n "Your teacher stands at the front of the class, with a large TV showcasing the Maya software."
    n "Some of your classmates have begun to pay attention, dragging their rolling chairs closer to join him."

    mod_t "Yesterday, we created the shield model. Today, we're going to move on to modelling a game prop."
    n "The teacher sits down and navigates the computer, moving the cursor around to show us some of the 3D models we need to create over the next half hour, especially for those who have never worked with this software before."
    n "You watch the TV as it explains how to apply a UV texture to an organic model."
    n "The teacher's voice is low, but the class is so engaged in the lesson that some students have started yawning, lulled by the extended explanation."

    mod_t "The finished product will consist of a sword, shield, barrel, wooden box, and sack."
    n "Some students begin to retreat to their own computers, not waiting to complete the task."
    n "You roll back to your desk and open Maya on your computer once again."

    mod_t "Once you're done, upload the Maya ASCII file to the server, and don't forget to name your files correctly..."
    n "For a moment, amid the week's assignments, you think you might be starting to understand this material a bit better."
    n "However, the most frustrating part of modelling remains UV unwrapping. Creating a seamless texture requires immense patience."

    n "Your fingers tense on the 'W', 'E', and 'R' keys, with your pinky pressing 'Alt'."
    n "Frustration builds as you click and drag the mouse aggressively, your brows knit tightly."
    n "The monitor's glow reflects on your face, just inches away, as the UV workspace stares back at you, lingering longer than necessary."

    p "You know what? This is impossible."

    n "You find yourself stuck, staring at your screen."
    n "As you look around, you notice that some of your friends have already finished certain parts, while others are dragging one another along in search of help from someone more knowledgeable or experienced."

    lc_a "COME ON, Trida. Can you just help me..."
    lc_b "Yeah, you are more capable than us!"

    n "You overhear those arguments as you glance toward Trida, who is getting dragged by two of your classmates to help with their work."
    n "Trida groans as they begin to explain one and two to them."
    n "You start to wonder what you should do next..."

    menu:
        "Ask Trida for help":
            jump week3_ask_trida
        "Try to work it out yourself":
            jump week3_work_alone


# ==============================================================================
# BRANCH: ASK TRIDA FOR HELP
# ==============================================================================

label week3_ask_trida:
    n "You hesitate for a second, still looking at Trida and both of your classmates arguing."
    n "Trida looks like they are surrounded by two chickens poking at them to demand help."
    n "The wheels roll softly as you make your way over to them, and Trida is in the middle of explaining with their hand moving through the mouse."

    t "No! If you just extrude it like that, the topology—"
    n "Then Trida stops as the corner of their eye catches your presence; they shift into an annoyed expression, looking like they forgot what they were going to say."

    lc_a "Trida, finish explaining."
    t "Okay, okay, hold on. I'm not a miracle worker."
    n "Little breathless laughs slip as they roll their focus again to the computer. They're still trying to help, even when pulled in two directions."

    n "After that, you step in closer between the three people, a clear will to interfere."
    n "Looking at Trida's exhausted laugh, your voice deliberately tries to take everyone's attention this time."
    p "Hey."

    n "Trida finally turns their body fully to you, as if the room lights up around them."
    n "The two classmates finally turn their eyes on you."
    t "Oh—hey!"
    p "Hey, could you help me for a bit?"

    n "You could feel Trida's hands instinctively grab your arms as they now face you fully."
    n "Their expression hints at a clear message: they wanted to get out of there quickly."
    t "You need help, too? Oh yeah, yeah, I got you."
    n "They rush their sentence, the rustle of your clothes sounding as you are dragged back to your seats."

    lc_b "Hey, where are you GOING?!"
    lc_a "BRO, not again!"

    n "Trida rolls back your chair with you sitting on it like a wheelchair."
    n "Now, both of you are facing your computer, showing half of your UV unwrapping."
    n "Somehow, it shows a red warning code in the nodes."
    n "They lean closer to the back of your chair without thinking, their hand moving through the mouse on your right side. There is no distance between you."

    t "Show me where you are stuck."
    n "Slowly, you point at the part where you are struggling, moving your cursor toward the UV map."
    p "It just won't line up."

    n "Trida's eyes squint at the screen as you left-click the mouse two or three times."
    n "Then, as your hands move, Trida finally nods in confidence."
    t "Yeah, I get it. Easy fix."
    n "Trida grabs the mouse from your hands, pausing to glance at you for a second, before continuing their explanation."
    t "So you just cut seams along the edges where the geometry folds, unwrap it—relax the mesh here and there—"
    n "Their rapid-fire explanation comes with the massive speed of the mouse moving."
    t "—Then here you scale it based on texel density so it matches with everything else—!"

    menu:
        "Let them cook.":
            jump week3_trida_cook_success
        "...Where is this going?":
            jump week3_trida_cook_doubt


label week3_trida_cook_success:
    $ tridaAffection += 1
    n "You sink back into the familiar chair, feeling its comforting weight cradle your body and anchor you in place."
    n "The hum of the computer fans fills the quiet room, underscoring the soft blue-white glow of the monitor that bathes your face and hands."
    n "You watch as your own shadow flickers and bends across the desk, drawn into the orbit of Trida's restless energy."

    t "—and then you just rotate this, and boom, it should flatten out—!"
    n "They barrel ahead, words tripping over each other as their fingers fly across the keyboard and mouse."
    n "Just before finalizing the UV map, the last click reveals a surprise—it looks surprisingly better than anticipated."
    n "While it isn't flawless by any means, it is certainly more usable than the previous versions."

    t "Wait..."
    n "Trida says, their gaze fixed intently on the screen. They freeze for a moment, then gradually lean in closer, studying the details with a mix of curiosity and determination."
    n "After a pause, they turn to you immediately."
    t "WAIT—okay, that actually worked?!"
    n "Now they're partially jumping from the chair."
    t "See?! I knew it!"

    n "You glance at the screen, and then at them, taking in their sense of admiration and disbelief."
    p "...You didn't."
    n "Trida pauses for a moment, their eyes sparkling, then bursts into loud laughter—a sound that fills the room and brings a smile to everyone around them."
    t "Okay, yeah, I didn't—but it counts!"
    jump week3_break_time


label week3_trida_cook_doubt:
    p "...Where is this going?"
    n "You lean closer to the glowing screen, your eyes straining to make sense of the information flashing before you."
    n "As the frustration builds, you lean back against the chair, casting a sideways glance at Trida."
    n "They halt their rapid clicking on the mouse and turn toward you, their brow furrowed slightly in concern."
    n "A moment of uncertainty hangs in the air before they break into a wide, reassuring grin."

    t "Trust me."
    n "They say that with too much confidence; they don't even wait for your response."
    t "It looks bad now, but it'll come together. Like—like crafting builds in games, you know?"
    n "They just keep moving forward, but with more speed and chaos."
    t "—and then you just align this here—no, wait—hold on—"

    n "*Click.*"
    n "Everything breaks. The UV explodes into a distorted mess, and silence follows as they stare at it."
    n "Then they slowly lean back, before quietly adding:"
    t "...Okay."
    t "That... wasn't the plan."
    n "They rub their face as they glance at you with a sense of guilt, but try to smile."
    t "Give me one more shot?"

    menu:
        "Let them cook":
            jump week3_trida_retry_cook
        "You know what? Forget what I asked, I'll redo it.":
            jump week3_trida_retry_cancel
        "Offers to figure it out together":
            jump week3_trida_retry_together


label week3_trida_retry_cook:
    $ tridaAffection += 1
    n "You sigh softly, letting the air linger on your lips before nodding."
    p "...Alright. One more shot."

    n "Upon hearing your words, Trida immediately straightens up. Their eyes widen with determination, and a big smile spreads across their face."
    n "They turn their attention back to the computer, locking in their focus completely."
    t "Okay. Okay—this time we'll do it properly."

    n "They slow down, thoughtfully considering their next move. There's less chatter coming from them now, a clear sign that they are more focused than before."
    n "The mouse clicks are more deliberate, and you notice the UV improving a bit after half a minute."
    n "After making a few adjustments, the hard clicks lead to refinements, and you can already see the final result: a clean and functional UV."

    n "Trida exhales, and you can feel the heaviness of their earlier panic wash away with this small victory."
    n "They finally turn to look at you again, their eyes sparkling with pride like a bright star."
    t "Okay, that one was real."
    n "A small grin spreads across their face, followed by a moment of sincerity."
    t "Thanks for trusting me."
    jump week3_break_time


label week3_trida_retry_cancel:
    $ tridaAffection -= 1
    n "You sigh softly, letting the air linger on your lips. Then, you slowly shake your head."
    n "With both hands, you reach forward, taking back the keyboard and pressing Ctrl + Z multiple times to reset everything."
    n "As your work returns to a clean state, you glance back, and Trida freezes in place."
    n "The mouse is still in their hand, unmoving like a symbol of guilt reflected faintly on the screen."
    n "Slowly, they let go of the mouse as a heavy, tense atmosphere fills the room."

    p "You know, I think I'll just try it myself again."
    n "Trida reacts with a nod, perhaps a bit too quickly. While they contemplate how to respond, you notice a shift in their tone."
    t "Yeah, that's fair."
    n "Their calm demeanor contrasts with the way their hands drop to their sides. You feel a pang of guilt."
    t "Sorry. I, uh... made it worse."
    n "Trida pauses softly."
    t "I'll... figure it out properly first."

    n "Then they trudge back to their desk, each step quiet, that strand of brown hair falling from their forehead like a leaf drifting in the breeze."
    n "Sitting down, they open their own project, repeating steps more slowly and carefully. The smile that once adorned their face has faded."
    jump week3_break_time


label week3_trida_retry_together:
    $ tridaAffection += 2
    n "Your fingers brush against Trida's on the mouse, stopping their frantic clicking mid-motion."
    n "You lean back, catching their eye over the headrest of your chair."
    p "Wait, let's figure it out together."

    n "Trida's head snaps from side to side in a quick, defensive shake. Panic surges through them."
    n "On the screen, the cursor jerks as they shove the mouse, clicking wildly in a desperate bid to fix the mess."
    n "Instead, the UV map tangles into an unrecognisable knot of vertices. Trida goes rigid, the colour draining from their face."
    t "No, no—I've got it. Just—give me a second—"
    n "Slowly, they turn to look at you, a familiar, hollow grin creeping across their lips—a mask for the embarrassment radiating off them."
    t "Okay, maybe I don't have it."
    n "They lean back, finally yielding the space you need."
    t "Team effort?"

    n "You nod, and this time, the frantic energy vanishes. You both move with deliberate and rhythmic slowness."
    n "Every action is preceded by a conversation, a shared thought, a breath."
    p "What if we cut here first?"

    n "Trida's eyes follow your gesture."
    t "Oh—wait, yeah."
    n "Trida pauses."
    t "That might actually—hold on—"

    n "They follow your lead, their movements becoming careful and precise. You adjust, test, and unwrap the model."
    n "Piece by piece, the chaotic UV begins to make sense, smoothing out into a clean, logical layout."
    n "When the final vertex snaps into place, the result is balanced and complete."
    n "The two of you sit in silence for a moment, simply staring at the screen. Then, the tension breaks."

    t "Wait—we actually did it!"
    n "They say, letting out a laugh that sounds lighter, stripped of the usual force."
    t "Okay, yeah. That felt way better."
    p "…I like this more."
    t "Working together, you mean..."
    n "Their hands lift, hovering for a heartbeat as if intending to tap your shoulder or offer a grateful touch, before gently dropping back."
    jump week3_break_time


# ==============================================================================
# BRANCH: WORK ALONE
# ==============================================================================

label week3_work_alone:
    n "You hesitate, the momentum of the room pulling at you."
    n "Your eyes flick toward Trida; they are still an island in a sea of students, hands gesturing at someone else's monitor, their voice a steady anchor for everyone but you."
    n "You look back at your own screen. The blue light reflects in your pupils, a cold reminder of the work left undone."
    n "A small, tired sigh leaves you as your fingers settle back onto the mechanical keys."

    p "I'll figure it out myself."
    n "You lean in until the pixels are sharp and the outside world begins to blur."
    n "The UV map stares back at you—a mangled, uncooperative bird's-eye view of digital skin. It is a puzzle of jagged edges and overlapping shells."
    n "You pause, your breath hitching, staring at the digital seams until they feel etched into your retinas."
    n "Then, you try something different. A surgical cut along the back edge. The mesh blooms open across the workspace."
    n "It isn't perfect, but the tension in the map suddenly gives way. Step by step, the digital chaos begins to settle into a logical, flattened grid."
    n "It isn't clean, and it certainly isn't elegant, but it is finally workable."
    n "You exhale quietly, your shoulders loosening just a fraction."
    jump week3_break_time


# ==============================================================================
# BREAK TIME: ROUTES SELECTION
# ==============================================================================

label week3_break_time:
    scene bg classroom
    with fade

    n "The moment lingered, thick and heavy, until it was gradually swallowed by the low, omnipresent hum of the computer fans."
    n "Around the room, the spell began to break. Chairs creaked against the floor, someone offered a bone-deep stretch, and the clock ticked forward—it was break time."
    p "Where should I go during this break time?"

    menu:
        "Go to RUS Animation Studio":
            jump week3_studio_sabian
        "Go to Photography Lounge":
            jump week3_lounge_julia
        "Stay in The 3D Lab":
            jump week3_lab_trida


# --- OPTION 1: SABIAN ROUTES (RUS Animation Studio) ---
label week3_studio_sabian:
    scene bg rus_studio
    with fade

    n "You decided to walk to the main studio of RUS Animation, heading toward the large room that smelled like a library and hummed with the sound of computers."
    n "The room buzzes with an unexpected energy, far louder than you initially anticipated."
    n "A kaleidoscope of voices bounces off the walls, mingling with bursts of laughter and the upbeat strains of music emanating from someone's phone."
    n "Above, a library is perched on the second floor, its collection of books just a glimpse of knowledge waiting to be explored."

    n "Nestled in the centre of the room, one individual stands out, their voice booming over the din."
    sab "BRO—if you burn it again, I'm banning you from the kitchen forever—"
    n "You step in before that guy notices you, while some of his friends beside him shift their attention toward you."
    sab "AYO—new face!"

    n "He gestures wildly, beckoning you to move closer. You pause briefly, feeling confused, before making your way towards them."
    sab "You're the 10th grader, right? Yeah."
    n "He leans in slightly, grinning."
    sab "Name's Sabian. Sophomore year and currently an intern here."
    n "He shakes your hand confidently, offering a firm grip. Sabian's face breaks into a surprisingly friendly smile."
    p "I'm [player_name], nice to know you-uh, Sabian."

    sab "Anyways, what have you been working on? Wait. Lemme guess—"
    n "He gestures with his palms, pausing for you to answer him, before humming and clicking his fingers with a very confident smile."
    sab "Basic 3D modelling, maybe around making a garden?"

    menu:
        "Yeah, you got it.":
            p "Yeah, you got it."
        "…Wow. That was actually spot on.":
            p "…Wow. That was actually spot on."
        "That’s right.":
            p "That's right."

    $ sabian_affection += 1
    n "Sabian hesitates for half a second before suddenly brightening with excitement."
    sab "HA! I knew it!"
    n "He bursts into laughter, giving your shoulder a playful slap that leaves a bit of a sting."
    sab "Bro, I've seen that assignment a million times. They never change it."
    n "Before you have a chance to shift, his arm wraps around your neck, comfortably firm, drawing you into his proximity."
    sab "C'mon, you're on break. You don't look like you've eaten either."
    sab "We're grabbing snacks."
    n "He pauses."
    sab "You're coming by the way. No arguments."
    jump week3_second_break


# --- OPTION 2: JULIA ROUTES (Photography Lounge) ---
label week3_lounge_julia:
    scene bg grapos_field
    with fade

    n "A soft breeze drifts lazily through the open space, wrapping around you like a gentle embrace and carrying with it a profound sense of quiet stillness."
    n "In stark contrast to the bustling crowds below, this elevated spot feels almost deserted, as if time has slowed down just for you."
    n "From this vantage point, you can take in the vibrant scene of the cafeteria filled with laughter and chatter, while distant trees sway under the vast sky."
    n "However, your moment of solitude is interrupted when your gaze catches sight of someone seated at a nearby table."
    n "There, all alone, sits a girl whose expression is inscrutable. Hanging loosely around her neck is a camera, suggesting a hidden passion."

    jul "You're from my class, right?"
    n "Her voice is quiet, perhaps a little unsure. She still isn't fully facing you—more angled to the side."
    jul "I think I've seen you in the lab."
    n "Her fingers fidget lightly with the camera strap. She finally glances at you for just a second."
    jul "Um... are you on break from modelling?"

    menu:
        "Yeah. Needed a break before I lose my mind.":
            p "Yeah. Needed a break before I lose my mind."
        "Kind of. Escaped while I still could.":
            p "Kind of. Escaped while I still could."
        "Something like that":
            p "Something like that."

    n "You gesture toward the camera hanging from her strap."
    p "Are you into photography?"

    n "Julia stills. For a moment, she looks like she's going to give a polite, one-word answer, but then her expression softens."
    jul "…Yeah. I mean—yeah. A little."
    n "She shifts her weight, angling her body toward yours."
    jul "I just like capturing... the quiet stuff. The small things that people usually walk right past without seeing."
    n "She holds your gaze for a beat longer than usual, then suddenly blinks, her eyes dropping back to the floor."
    jul "…Sorry. Was that a bit too much? I'm probably rambling."

    p "No. It's fine."
    n "Julia stills for a moment, checking to see if you're sincere. When she realizes you are, the rigid line of her shoulders drops."
    jul "Do you want to see one?"

    n "She lifts the camera, tilting the small, glowing LCD screen toward you."
    n "On the display, the image is sharp and honest—a shot of students on the lawn below, mid-laugh. It feels alive."
    jul "I just... like moments like this. When people forget they're being watched, that's when they are actually themselves."

    menu:
        "That’s… really nice.":
            p "That's... really nice."
            $ julia_affection += 1
        "You notice a lot, huh?":
            p "You notice a lot, huh?"
            $ julia_affection += 1

    n "Julia lowers the camera with a slow, deliberate motion. The faint smile on her face is still there—fragile and small, yet genuine."
    n "Then, the distant toll of the campus bell cuts through the air, snapping the connection to the peaceful moment."
    jul "We should probably head back."
    n "She hesitates, her gaze flickering to yours one last time before turning toward the metal door."
    jump week3_second_break


# --- OPTION 3: TRIDA ROUTES (Stay in 3D Lab) ---
label week3_lab_trida:
    scene bg classroom
    with fade

    n "The 3D lab empties gradually—the low hum of rolling chairs, the rhythmic thud of the heavy exit door, and finally, a profound silence except for one corner."
    n "A single monitor casts a sharp, clinical blue glow over Trida."
    n "They are hunched forward, shoulders raised to their ears, their nose inches from the screen as if trying to merge with the pixels."

    t "No, no, that's not right... Why is it stretching? Just—stay. Stay!"
    n "*Click. Ctrl+Z. Click. Ctrl+Z.* The mechanical keyboard clacks like rapid gunfire."

    p "...You're still here?"
    n "Trida jolts, their chair screeching harshly against the floor. They whip around, blinking rapidly."
    t "Oh! Hey. You scared me for a second."
    n "They straighten up, smoothing their uniform with a shaky hand."
    t "Yeah, I just... found a tiny hiccup. One more fix and I'm out. Ten minutes, tops."
    n "Trida's eyes are bloodshot, and the scroll bar on their screen is barely a quarter of the way down. They aren't leaving anytime soon."

    menu:
        "You should eat first.":
            p "You should eat first."
        "If you keep going, you’re gonna pass out at your desk.":
            p "If you keep going, you're gonna pass out at your desk."
        "Let’s take a break. You’ve done enough.":
            p "Let's take a break. You've done enough."

    $ tridaAffection += 1
    n "Trida slams their mouse down with a decisive thud, the sound slicing through the room's silence."
    t "Yeah, break sounds good."
    n "With a swift motion, they send their bag tumbling from the edge of the table, catching the strap just in time before it hits the floor."
    n "In one seamless movement, they rise from their seat, a small, conspiratorial grin tugging at their mouth."
    t "You're coming too, right?"
    p "Of course!"
    jump week3_second_break


# ==============================================================================
# SECOND BREAK: STUDIO ANIMASI - AFTERNOON
# ==============================================================================

label week3_second_break:
    scene bg rus_studio
    with fade

    n "After the sixth period, there is a second break time for students."
    n "Some of them stick out with their groups, some go to the canteen, and others grind their work."
    n "You see that your task has already been done, and now you have to think: should you wander around and socialize?"

    menu:
        "Yes":
            jump week3_chie_encounter
        "No (Skip)":
            jump week3_bedroom_night


label week3_chie_encounter:
    scene bg gates_morning
    with fade

    n "You step out from the door when suddenly, you stumble across a very familiar figure locking her eyes on you."
    n "Bright gleaming eyes wave hands vigorously."
    ch "Hey [player_name]!"
    ch "Going back to class?"

    p "Yeah, kind of. Are you still at work?"
    n "Chie lets out a tired laugh, tucking her hair behind her ears with a restless gesture in the air."
    ch "Well, I don't wanna look like I'm whining about my work. But you know the deadlines are ruthless..."

    menu:
        "You look like you're about to collapse. Sit for a second.":
            p "You look like you're about to collapse. Sit for a second."
        "You've been pushing yourself too hard. It's okay to take a break.":
            p "You've been pushing yourself too hard. It's okay to take a break."

    $ ch_affection += 1
    ch "Ah... it's alright! It's just been rough just these past weeks."
    n "Chie's shoulders drop, the tension finally leaving her frame. She lets out a long, shaky exhale."
    ch "But, I really appreciate that! You can message me anytime too, you know, if you have any problems!"
    n "You nod as she pats your shoulder, watching her head back into the studio."
    jump week3_bedroom_night


# ==============================================================================
# BEDROOM - LATE AFTERNOON
# ==============================================================================

label week3_bedroom_night:
    scene bg bedroom_late_afternoon
    with fade

    n "Finally, after a click, the sound of your keys turning, and the smell of your room swarming through your nose."
    n "The tension and the weight in your body leave your skin entirely. Your hand reaching the bed feels warmer than ever."
    n "As your mind replays today's lecture, all your thoughts start to drift away into the place called the dream world."

    # End of Week 3 -> Continue to Week 4
    jump week4_start
