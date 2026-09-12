label week3_start:
    $ current_week = "Week 3"
    scene bg classroom
    with dissolve_scene_full
    play music audio.t3 fadein 1.5 loop volume 0.7

    # Visual: 3D LAB - MORNING
    n "The dim light casts pale shadows across the room, carrying the scent of cool air and faint pine from the woods outside."
    n "The temperature is uncomfortably cold, displaying 21 degrees on the digital thermometer."
    n "Your productive teacher stands at the front of the class, with a large TV showcasing the Maya software."
    n "Some of your classmates have begun to pay attention, dragging their rolling chairs closer to join them."

    modelling_teacher "Yesterday, we created the shield model. Today, we're going to move on to modelling a game prop."

    n "The teacher sits down and navigates the computer, moving the cursor around to show us some of the 3D models we need to create over the next half hour, especially for those of us who have never worked with this software before."
    n "You watch the TV as it explains how to apply a UV texture to an organic model."
    n "The teacher's voice is low, but the class is so engaged in the lesson that some students have started yawning, lulled by the extended explanation."

    modelling_teacher "The finished product will consist of a sword, shield, barrel, wooden box, and sack."

    n "Some students begin to retreat to their own computers, not waiting to complete the task."
    n "You roll back to your desk and open Maya on your computer once again."

    modelling_teacher "Once you’re done, upload the Maya ASCII file to the server, and don’t forget to name your files correctly…"

    n "For a moment, amid the week’s assignments, you think you might be starting to understand this material a bit better."
    n "However, the most frustrating part of modelling remains UV unwrapping. Creating a seamless texture requires immense patience."

    n "Your fingers tense on the 'W', 'E', and 'R' keys, with your pinky pressing 'Alt'."
    n "Frustration builds as you click and drag the mouse aggressively, your brows knit tightly."
    n "The monitor’s glow reflects on your face, just inches away, as the UV workspace stares back at you, lingering longer than necessary."

    p "You know what? This is impossible."

    n "You find yourself stuck, staring at your screen."
    n "As you look around, you notice that some of your friends have already finished certain parts, while others are dragging one another along in search of help from someone more knowledgeable or experienced."

    classmate_a "COME ON, Trida. Can you just help me…"
    classmate_b "Yeah, you are more capable than us!"

    n "You overheard those arguments as you glance toward Trida, who is getting dragged by two of your classmates to help with their work."
    play music audio.t5 fadein 1.0 loop volume 0.7
    n "Trida groaned as they began to explain one and two to them."
    n "You start to wonder what you should do next…"

    menu:
        "Ask Trida for help":
            jump week3_ask_trida
        "Try to work it out yourself":
            jump week3_work_alone


# ==============================================================================
# BRANCH: ASK TRIDA FOR HELP
# ==============================================================================

label week3_ask_trida:
    play music audio.t4 fadein 1.0 loop volume 0.7
    n "You hesitate for a second, still looking at Trida and both of your classmates arguing."
    n "Trida looked like they were surrounded by two chickens poking at them to demand help."
    n "The wheels roll softly as you make your way over them, and Trida is in the middle of finally explaining with their hand moving through the mouse."

    trida "No! If you just extrude it like that, the topology—"
    n "Then Trida stops as the corner of their eye catches your presence; they shift into an annoyed expression, looking like they forgot what they were going to say."

    classmate_a "Trida, finish explaining."
    trida "Okay, okay, hold on. I'm not a miracle worker."
    n "The little breathless laughs were slipping when they rolled their focus again to the computer."
    n "They're still trying to help, even when they were pulled in two directions."

    n "After that, you stepped in closer between the three people. There is a will to interfere with that."
    n "Looking at Trida, exhausted, laughs. Your voice deliberately tries to take everyone's attention this time."
    p "Hey."

    n "Trida finally really turns their body to you, as the room finally lights up around them."
    n "The two classmates were finally turning their eyes on you."
    show trida uniform neutral at center with dissolve
    trida "Oh-hey!"
    p "Hey, could you help me for a bit?"

    n "You could feel Trida's hands instinctively grab your arms as they now faced you fully."
    n "Their expression hints at some messages; they wanted to get out of there quickly."
    show trida happy at center, hop
    trida "You need help, too? Oh yeah, yeah, I got you."
    n "They rushed their sentence, feeling the rustle of your hands as they were dragged to your seats."

    classmate_b "Hey, where are you GOING?!"
    classmate_a "BRO, not again!"

    n "Trida rolls back your chair with you sitting on it like a wheelchair."
    n "Now, both of you are facing around your computer, showing half of your UV unwrapping."
    n "Somehow, it shows a red warning code in the nodes."
    n "They leaned closer to the back of your chair without thinking, as their hands were moving through the mouse on the right side of you. There is no distance between you."

    trida "Show me where you are stuck."
    n "Slowly, you started to point at the part where you are struggling, moving your cursor towards the UV map."
    p "It just won't line up."

    n "Trida's eyes squinted through the screen as you left-clicked the mouse two or three times."
    n "Then, as your hands move, Trida finally nods in confidence."
    show trida happy at center with dissolve
    trida "Yeay, I get it. Easy fix."
    n "Trida grabs the mouse from your hands, while pausing to glance at you for a second, before continuing their explanation."

    trida "So you just cut seams along the edges where the geometry folds, unwrap it—relax the mesh here and there—"
    n "Their rapid-fire explanation, along with the massive speed of the mouse moving."
    n "You started making a loading sound in your head, so they would just continue."
    trida "—Then here you scale it based on texel density so it matches with everything else—!"

    n "Trida's ramble is like a speed of light blasting right from your ears, and stuck in the Arctic."
    n "You started doubting whether their help really makes a difference in your work."

    menu:
        "Let them cook.":
            jump week3_trida_cook_success
        "...Where is this going?":
            jump week3_trida_cook_doubt


label week3_trida_cook_success:
    $ tridaAffection += 1
    n "You sink back into the familiar chair, feeling its comforting weight cradle your body and anchor you in place."
    n "The hum of the computer fans fills the quiet room, underscoring the soft blue-white glow of the monitor that bathes your face and hands."
    n "You watch as your own shadow flickers and bends across the desk, drawn into the orbit of Trida’s restless energy."

    trida "—and then you just rotate this, and boom, it should flatten out—!"
    n "They barrel ahead, their words tripping over each other as their fingers fly across the keyboard and mouse."
    n "Just before finalising the UV map, the last click reveals a surprise—it looks surprisingly better than anticipated."
    n "While it isn’t flawless by any means, it is certainly more usable than the previous versions."

    trida "Wait,"
    n "Trida says, their gaze fixed intently on the screen."
    n "They freeze for a moment, then gradually lean in closer, studying the details with a mix of curiosity and determination."
    n "After a pause, they turn to you immediately."

    show trida happy at center, hop
    trida "WAIT—okay, that actually worked?!"
    n "Trida exclaims for a second before they open their lips again. Now they’re partially jumping from the chair."
    trida "See?! I knew it!"

    n "You glance at the screen, and then at them, taking in their sense of admiration and disbelief."
    p "…You didn’t."

    n "Trida pauses for a moment, their eyes sparkling, then bursts into loud laughter—a sound that fills the room and brings a smile to everyone around them."
    show trida happy at center, hop
    trida "Okay, yeah, I didn’t—but it counts!"
    n "Trida says, and there’s a strange charm to their enthusiasm."
    hide trida with dissolve
    jump week3_break_time


label week3_trida_cook_doubt:
    p "…Where is this going?"
    n "You lean closer to the glowing screen, your eyes straining to make sense of the information flashing before you."
    n "As the frustration builds, you lean back against the chair, casting a sideways glance at Trida."
    n "They halt their rapid clicking on the mouse and turn toward you, their brow furrowed slightly in concern."
    n "A moment of uncertainty hangs in the air before they break into a wide, reassuring grin, as if to say everything will be okay."

    show trida happy at center, hop
    trida "Trust me."
    n "They say that with too much confidence, they don’t even wait for your response."
    trida "It looks bad now, but it’ll come together. Like—like crafting builds in games, you know?"
    n "They just keep moving forward, but with more speed and chaos."
    show trida embarrassed at center, panic
    trida "—and then you just align this here—no, wait—hold on—"

    n "Click and everything breaks."
    n "The UV explodes into a distorted mess, and silence follows as they stare at it."
    n "Then slowly leaned back in a beat, before they quietly added."
    show trida embarrassed at center, dip
    trida "…Okay."
    trida "That… wasn’t the plan."
    n "They rub their face as they glance with a sense of guilt, but try to smile."
    trida "Give me one more shot?"

    menu:
        "Let them cook":
            jump week3_trida_retry_cook
        "You know what? Forget what I asked, I'll redo it.":
            jump week3_trida_retry_cancel
        "Offers to figure it out together":
            jump week3_trida_retry_together


label week3_trida_retry_cook:
    $ tridaAffection += 1
    n "You sigh softly, letting the air linger on your lips before nodding and shaking your head slightly."
    p "…Alright. One more shot."

    n "Upon hearing your words, Trida immediately straightens up."
    n "Their eyes widen with determination, and a big smile spreads across their face."
    show trida happy at center, hop
    n "They turn their attention back to the computer, locking in their focus completely."
    trida "Okay. Okay—this time we’ll do it properly."

    n "They slow down, thoughtfully considering their next move."
    n "There’s less chatter coming from them now, a clear sign that they are more focused than before."
    n "The mouse clicks are more deliberate, and you notice the UV improving a bit after half a minute."
    n "They attempt it again, and while it may not look perfect, it's a step forward."
    n "After making a few adjustments, the hard clicks lead to refinements, and you can already see the final result, a clean and functional UV."

    n "Trida exhales, and you can feel the heaviness of their earlier panic wash away with this small victory."
    n "They finally turn to look at you again, their eyes sparkling with pride like a bright star that could swallow you whole."
    show trida happy at center, hop
    trida "Okay, that one was real."
    n "A small grin spreads across their face, followed by a moment of sincerity."
    trida "Thanks for trusting me."
    hide trida with dissolve
    jump week3_break_time


label week3_trida_retry_cancel:
    $ tridaAffection -= 1
    n "You sigh softly, letting the air linger on your lips."
    n "Then, you slowly shake your head, causing some of your bangs to flutter."
    n "With both hands, you reach forward, taking back the keyboard and pressing CTRL + Z multiple times to reset everything."

    n "As your work returns to a clean state, you glance back, and Trida freezes in place."
    show trida sad at center, dip
    n "The mouse is still in their hand, unmoving like a symbol of guilt reflected faintly on the screen."
    n "Slowly, they let go of the mouse as a heavy, tense atmosphere fills the room."
    n "A small pause of silence hangs between you before you finally break it with a quiet voice."
    p "You know, I think I’ll just try it myself again."

    n "Trida reacts with a nod, perhaps a bit too quickly."
    n "While they contemplate how to respond, you notice a shift in their tone that seems different from usual."
    trida "Yeah, that’s fair."

    n "Their calm demeanor contrasts with the way their hands drop to their sides. You feel a pang of guilt."
    n "They appear to be worried that you might be disappointed."
    n "A small laugh escapes you, but it feels awkward and doesn’t quite land."
    n "They glance at your screen before looking away, distracted by random spots in the room."
    trida "Sorry. I, uh… made it worse."
    n "Trida pauses."
    trida "I’ll… figure it out properly first."

    hide trida with dissolve
    n "Then they trudge back to their desk, each step quiet, that brown strand of foolish hair falling from the top of their forehead like a leaf drifting in the breeze, reflecting their mood."
    n "Sitting down, they open their own project, seemingly indifferent to the fact that they’re repeating the same steps as before, only more slowly and more carefully."
    n "The smile that once adorned their face has faded, and you sense that you’ve dampened their spirits."
    n "But perhaps, right now, silence is what both of you need."
    jump week3_break_time


label week3_trida_retry_together:
    $ tridaAffection += 2
    n "Your fingers brushed against Trida’s on the mouse, stopping their frantic clicking mid-motion."
    n "You leaned back, catching their eye over the headrest of your chair."
    n "Then you spoke quickly, before everything spiralled out of control."
    p "Wait, let’s figure it out together."

    n "Trida’s head snapped from side to side in a quick, defensive shake. Panic surged through them."
    show trida embarrassed at center, panic
    n "On the screen, the cursor jerked as they shoved the mouse, rotating the model and clicking wildly in a desperate bid to fix the mess before it worsened."
    n "Instead, it only grew more chaotic. The UV map tangled into an unrecognisable knot of vertices."
    n "Trida went rigid, the colour draining from their face as the realisation of the disaster set in."

    trida "No, no—I’ve got it. Just—give me a second—"
    n "Slowly, they turned to look at you, a familiar, hollow grin creeping across their lips."
    n "It was a mask for the embarrassment radiating off them, and you could practically feel the helplessness in the way their posture sagged."
    show trida embarrassed at center, dip
    trida "Okay, maybe I don’t have it."
    n "They leaned back, finally yielding the space you needed."
    trida "Team effort?"

    n "You nodded, and this time, the frantic energy vanished."
    n "You both moved with deliberate and rhythmic slowness."
    n "Every action was preceded by a conversation, a shared thought, a breath."
    n "You then suggested, pointing to a seam."
    p "What if we cut here first?"

    n "Trida’s eyes followed your gesture."
    show trida neutral at center with dissolve
    trida "Oh—wait, yeah."
    n "Trida pauses."
    trida "That might actually—hold on—"

    n "They followed your lead, their movements becoming careful and precise."
    n "You adjusted, tested, and unwrapped the model."
    n "Piece by piece, the chaotic UV began to make sense, smoothing out into a clean, logical layout."

    n "When the final vertex snapped into place, the result was perfect—balanced and complete."
    n "The two of you sat in silence for a moment, simply staring at the screen."
    n "Then, the tension broke. Trida burst into a grin—a genuine one this time, fueled by a flood of relief."

    show trida happy at center, hop
    trida "Wait—we actually did it,"
    n "They said, letting out a laugh that sounded lighter, stripped of the usual force."
    n "Trida glanced at you, their expression softening."
    trida "Okay, yeah. That felt way better."
    p "…I like this more."
    show trida embarrassed at center, dip
    trida "Working together, you mean…"
    n "Their hands lifted, hovering for a heartbeat as if they intended to tap your shoulder or offer a grateful touch."
    n "They hesitated, the hand suspended in the air, before it finally dropped back to their side."
    hide trida with dissolve
    jump week3_break_time


# ==============================================================================
# BRANCH: WORK ALONE
# ==============================================================================

label week3_work_alone:
    n "You hesitate, the momentum of the room pulling at you."
    n "Your eyes flick toward Trida; they are still an island in a sea of students, hands gesturing at someone else's monitor, their voice a steady anchor for everyone but you."
    n "You look back at your own screen. The blue light reflects in your pupils, a cold reminder of the work left undone."
    n "A small, tired sigh leaves you as your fingers settle back onto the mechanical keys."

    p "I’ll figure it out myself."

    n "You lean in until the pixels are sharp and the outside world begins to blur."
    n "The UV map stares back at you—a mangled, uncooperative bird’s-eye view of a digital skin."
    n "It is a puzzle of jagged edges and overlapping shells."
    n "You pause, your breath hitching, staring at the digital seams until they feel like they’re etched into your retinas."

    n "Then, you try something different. A surgical cut along the back edge."
    n "The mesh blooms open across the workspace."
    n "It isn't perfect, but the tension in the map suddenly gives way."
    n "You blink, leaning even closer, your movements becoming more rhythmic and deliberate."
    n "Step by step, the digital chaos begins to settle into a logical, flattened grid."
    n "It isn’t clean, and it certainly isn't elegant, but it is finally workable."

    n "You exhale quietly, a long-held breath escaping your lungs."
    n "Your shoulders, previously hiked up to your ears, loosen just a fraction."
    n "Around you, the classroom noise becomes a low-fidelity hum."
    n "The rhythmic thrum of computer fans, the distant scraping of rolling chairs, and the muffled ripple of someone laughing three rows back—it all fades into a soft-focus haze."
    jump week3_break_time


# ==============================================================================
# BREAK TIME: ROUTES SELECTION
# ==============================================================================

label week3_break_time:
    scene bg classroom
    with dissolve_scene_full

    # Visual: 3D LAB - MORNING
    n "The moment lingered, thick and heavy, until it was gradually swallowed by the low, omnipresent hum of the computer fans."
    n "It was a sterile sort of silence that settled back into the gaps where their voices had been, filling the space between them."
    n "Around the room, the spell began to break."
    n "Chairs creaked against the floor, someone nearby offered a long, bone-deep stretch, and the sharp, rhythmic click of a keyboard signalled the end of the hour."
    n "It was a subtle shift in the room's frequency, a quiet drift back toward reality, and before you could reach out to catch the tail end of it, the clock had already ticked forward—time, it was a break time."

    p "Where should I go during this break time?"

    menu:
        "Go to RUS Animation Studio":
            jump week3_studio_sabian
        "Go to Photography Lounge":
            jump week3_lounge_julia
        "Stay in The 3D Lab":
            jump week3_lab_trida


# --- OPTION 01: SABIAN ROUTES (RUS Animation Studio) ---
label week3_studio_sabian:
    scene bg rus_studio
    with dissolve_scene_full
    play music audio.t3 fadein 1.5 loop volume 0.7

    # Visual: Gedung Studio Animasi
    n "You decided to walk to the main studio of RUS Animation, heading toward the large room that smelled like a library and hummed with the sound of computers."
    n "The room buzzes with an unexpected energy, far louder than you initially anticipated."
    n "A kaleidoscope of voices bounces off the walls, creating a lively symphony that mingles with bursts of laughter and the upbeat strains of music emanating from someone's phone."
    n "The rhythmic clattering of tools adds to the cacophony, punctuating conversations with a metallic edge."

    n "It seems that break time has arrived for many, as clusters of senior students have pushed away from their desks, blending into the vibrant atmosphere."
    n "The lighting in this expansive room is notably brighter than in the lab designated for the 10th graders, highlighting the space’s high ceiling adorned with modern fixtures."
    n "Above, a library is perched on the second floor, its collection of books just a glimpse of knowledge waiting to be explored."

    n "Nestled in the centre of the room, one individual stands out, their voice booming over the din, drawing attention and laughter from those nearby."
    sabian "BRO—if you burn it again, I’m banning you from the kitchen forever—"

    n "You step in before that guy notices you, while some of their friends beside them also shift their attention towards you."
    n "They see you instantly, like radar locking on."
    show sabian at to_center
    sabian "AYO—new face!"

    n "He gestures wildly, beckoning you to move closer."
    n "You pause briefly, feeling confused, before making your way towards them."
    sabian "You’re the 10th grader, right? Yeah."

    n "He leans in slightly, grinning."
    sabian "Name’s Sabian. Sophomore year and currently an intern here."
    n "He shakes your hand confidently, offering a firm grip."
    show sabian smile at center, sway with dissolve
    n "Sabian's face breaks into a surprisingly friendly smile, reminiscent of any corporate CEO you could’ve seen on the big screen."

    p "I’m [player_name], nice to know you-uh, Sabian."

    sabian "Anyways, what have you been working on? Wait. Lemme guess-"
    n "He gestured with his palms, pausing for you to answer him, before humming and clicking his fingers with a very confident smile."
    sabian "Basic 3D modelling, maybe around making a garden?"

    menu:
        "Yeah, you got it.":
            p "Yeah, you got it."
        "…Wow. That was actually spot on.":
            p "…Wow. That was actually spot on."
        "That’s right.":
            p "That’s right."

    $ sabian_affection += 1
    n "Sabian hesitates for half a second before suddenly brightening with excitement."
    show sabian laugh at center, hop with dissolve
    sabian "HA! I knew it!"
    n "He bursts into laughter, giving your shoulder a playful slap that leaves a bit of a sting."

    sabian "Bro, I’ve seen that assignment a million times. They never change it."
    n "Before you have a chance to shift from your spot, his arm wraps around your neck, comfortably firm, drawing you into his proximity."
    sabian "C’mon, you’re on break. You don’t look like you’ve eaten either."

    n "He gestures toward the screen, directing you as they look at you, his smile growing."
    show sabian smile at center, hop with dissolve
    sabian "We’re grabbing snacks."
    n "Sabian pauses."
    sabian "You’re coming by the way. No arguments."
    hide sabian with dissolve
    jump week3_second_break


# --- OPTION 02: JULIA ROUTES (Photography Lounge) ---
label week3_lounge_julia:
    scene bg grapos_field
    with dissolve_scene_full

    n "A soft breeze drifts lazily through the open space, wrapping around you like a gentle embrace and carrying with it a profound sense of quiet stillness."
    n "In stark contrast to the bustling crowds below, this elevated spot feels almost deserted, as if time has slowed down just for you."
    n "From this vantage point, you can take in the vibrant scene of the cafeteria filled with laughter and chatter, while, beyond the school walls, the distant landscape stretches out—a patchwork of green fields and trees swaying under the vast sky."

    n "For a fleeting moment, you savour the serenity that envelops you, a calming aura that seems to bring everything else to a halt."
    n "However, your moment of solitude is interrupted when your gaze catches sight of someone seated at a nearby table."
    n "There, all alone, sits a girl whose expression is inscrutable, her features soft yet distant."
    n "Hanging loosely around her neck is a camera, its presence suggesting a hidden passion or a story yet to be told."

    show julia at slide_center
    julia "You’re from my class, right?"
    n "Her voice is quiet, perhaps a little unsure. She still isn’t fully facing you—more angled to the side, as if that makes it easier."
    n "A silence follows, as if she’s second-guessing herself."
    julia "I think I’ve seen you in the lab."
    n "Her fingers fidget lightly with the camera strap. She finally glances at you for just a second, then looks away again."
    julia "Um… are you on break from modelling?"

    menu:
        "Yeah. Needed a break before I lose my mind.":
            p "Yeah. Needed a break before I lose my mind."
        "Kind of. Escaped while I still could.":
            p "Kind of. Escaped while I still could."
        "Something like that":
            p "Something like that."

    n "You gesture toward the camera hanging from her strap."
    p "Are you into photography?"

    n "Julia stills. For a moment, she looks like she’s going to give a polite, one-word answer, but then her expression softens."
    show julia smile at center, hop with dissolve
    julia "…Yeah. I mean—yeah. A little."

    n "She shifts her weight, angling her body toward yours. Her grip on the camera lens relaxes as her fingers trace the edge of the frame."
    julia "I just like capturing… the quiet stuff. The small things that people usually walk right past without seeing."
    n "She holds your gaze for a beat longer than usual, then suddenly blinks, her eyes dropping back to the floor as she realises how much she just shared."
    show julia shy at center, dip with dissolve
    julia "…Sorry. Was that a bit too much? I’m probably rambling."

    p "No. It’s fine."
    n "Julia stills for a moment, looking at you longer than necessary, as if she’s checking to see if you’re being polite."
    n "When she realises you’re sincere, her grip on the camera finally relaxes."
    n "The rigid line of her shoulders drops, and she exhales a breath she’s been holding since the conversation started."
    n "The wind sweeps between you, carrying the distant sounds of campus life, but here, it’s quiet."

    julia "Do you want to see one?"
    n "She lifts the camera, tilting the small, glowing LCD screen toward you."
    n "You step closer—close enough to catch the faint scent of her shampoo and hear the mechanical hum of the camera."
    n "On the display, the image is sharp and honest."
    n "It’s a shot of students on the lawn below. One student is mid-laugh, head thrown back, while another points at something out of frame. It’s messy, but it feels like it’s alive."

    julia "I just… like moments like this."
    n "Julia glances at you with a quick, searching look to see if you understand, then her eyes dart back to the safety of the viewfinder."
    julia "When people forget they’re being watched, that’s when they are actually themselves."

    menu:
        "That’s… really nice.":
            p "That’s… really nice."
            $ julia_affection += 1
        "You notice a lot, huh?":
            p "You notice a lot, huh?"
            $ julia_affection += 1

    n "Julia lowers the camera with a slow, deliberate motion."
    n "Her fingers linger on the casing for a moment too long, as if she’s trying to imprint the memory of the silence into the plastic."
    n "The faint smile on her face is still there—fragile and small, yet the most genuine thing you’ve seen all day."
    n "The silence that follows isn’t heavy or oppressive; it’s a shared breath."
    n "For a moment, the rest of the world becomes mere background noise."

    n "Then, the distant toll of the campus bell cuts through the air."
    n "The sound drifts up to the balcony, sharp and rhythmic, snapping the connection to the peaceful moment."
    n "Below, clusters of students that had been frozen in place break apart, flowing toward their next classes like a disturbed anthill. The stillness is gone."

    n "Julia adjusts the strap on her shoulder, the leather creaking slightly in the wind. She shifts her weight, the reality of her schedule settling back in."
    julia "We should probably head back."
    n "She hesitates, her gaze flickering to yours one last time, as if acknowledging the secret you just shared."
    hide julia with dissolve
    n "With a small, decisive nod, she turns toward the heavy metal door. You follow a step behind as the door swings open."
    jump week3_second_break


# --- OPTION 03: TRIDA ROUTES (Stay in 3D Lab) ---
label week3_lab_trida:
    scene bg classroom
    with dissolve_scene_full

    n "The 3D lab empties gradually—the low hum of rolling chairs, the rhythmic thud of the heavy exit door, and finally, a profound silence except for one corner."
    n "A single monitor casts a sharp, clinical blue glow over Trida."
    n "They are hunched forward, shoulders raised to their ears, their noses inches from the screen as if trying to merge with the pixels."

    trida "No, no, that’s not right… Why is it stretching? Just—stay. Stay!"
    n "*Click. Ctrl+Z. Click. Ctrl+Z.*"
    n "The mechanical keyboard clacks like rapid gunfire. You step into the pool of blue light."

    p "...You’re still here?"

    n "Trida jolts, their chair screeching harshly against the floor. They whip around, blinking rapidly as they adjust to your presence."
    n "A practised, weary smile quickly masks their frustration."
    show trida uniform happy at center, dip with dissolve
    trida "Oh! Hey. You scared me for a second."

    n "They straighten up, smoothing their uniform with a shaky hand."
    trida "Yeah, I just… found a tiny hiccup. One more fix and I’m out. Ten minutes, tops."
    n "Trida’s eyes are bloodshot, and the scroll bar on their screen is barely a quarter of the way down. They aren't leaving anytime soon."

    menu:
        "You should eat first.":
            p "You should eat first."
        "If you keep going, you’re gonna pass out at your desk.":
            p "If you keep going, you’re gonna pass out at your desk."
        "Let’s take a break. You’ve done enough.":
            p "Let’s take a break. You’ve done enough."

    $ tridaAffection += 1
    n "Trida slams their mouse down with a decisive thud, the sound slicing through the room's silence like a sharp knife."
    n "There’s an unmistakable finality in the action, with nothing but a lingering pause, even the attempt to save any files or salvage any work didn’t occur to them—just a resolute gesture, an emphatic declaration that this chapter is thoroughly closed."

    show trida happy at center, hop
    trida "Yeah, break sounds good."
    n "With a swift and graceful motion, they send their bag tumbling from the edge of the table, the contents shifting and clattering as it falls."
    n "Just in time, they snatch the strap from the air, preventing it from landing with a thud on the floor."
    n "In one seamless movement, they rise from their seat, poised in that electrifying moment between the comfort of sitting and the urgency of sprinting."
    n "A small, conspiratorial grin tugs at their mouth as they glance back at you."

    trida "You’re coming too, right?"
    p "Of course!"
    hide trida with dissolve
    jump week3_second_break


# ==============================================================================
# SECOND BREAK: STUDIO ANIMASI - AFTERNOON
# ==============================================================================

label week3_second_break:
    scene bg rus_studio
    with dissolve_scene_full

    # Visual: Studio Animasi
    n "After the sixth period, there will be a second breaktime for students."
    n "Some of them stick out with their groups, some of them go to the canteen, and the others probably grind their work."
    n "You see that your task has already been done, and now you have to think. Should you just wander around and try to socialize?"

    menu:
        "Yes":
            jump week3_chie_encounter
        "No (Skip)":
            jump week3_bedroom_night


label week3_chie_encounter:
    scene bg gates_morning
    with dissolve_scene_full

    n "The clock is ticking faster than a blink of an eye, after the break time your body has to drag yourself back to the studio."
    n "You step yourself moving from the door when suddenly, you stumble across a very familiar figure now locking their eyes on you."
    n "The bright gleaming eyes that waved their hands vigorously."

    show chie at to_center
    chie "Hey [player_name]!"
    chie "Going back to class?"
    n "The sound of Chie giggling waving through your ears. You stunned for a moment, before opening your lips."

    p "Yeah, kind of. Are you still at work?"
    show chie smile at center, dip with dissolve
    n "Chie looks making a sound of tired laughter hearing that. She tucked her hair to her ears."
    n "There is a nervous gesture she kind of pushes to the air. She makes a vague, restless gesture in the air."
    chie "Well, I don't wanna look like I'm whining about my work. But you know the deadlines are ruthless.."

    menu:
        "You look like you're about to collapse. Sit for a second.":
            p "You look like you're about to collapse. Sit for a second."
        "You’ve been pushing yourself too hard. It’s okay to take a break.":
            p "You’ve been pushing yourself too hard. It’s okay to take a break."

    $ ch_affection += 1
    chie "Ah.. it’s alright! It’s just been rough just these past week"
    n "Chie’s shoulders drop, the tension finally leaving her frame."
    n "She lets out a long, shaky exhale, and for the first time, her gaze meets you without that forced, bright mask."
    chie "But, I really appreciate that"
    chie "You can message me anytime too you know, if you had any problem"

    hide chie with dissolve
    n "You nod, as she patted your shoulder then moved back to the studio leaving you tracking her back moving."
    n "Hopefully you two met again, maybe during something more fun than a deadline stacking for both of you."
    jump week3_bedroom_night


# ==============================================================================
# BEDROOM - LATE AFTERNOON
# ==============================================================================

label week3_bedroom_night:
    scene bg bedroom_late_afternoon
    with dissolve_scene_full
    play music audio.t10 fadein 2.0 loop volume 0.6

    # Visual: Player’s Room
    n "Finally, after a click, the sound of your keys turning, and the smell of your room swarming through your nose."
    n "The tension and the weight in your body leave your skin entirely. Your hand reaching the bed felt warmer than ever."
    n "As your mind replayed today's lecture and all your thoughts started to drift away, in the place called the dream world."

    # End of Week 3 -> Continue to Week 4
    jump week4_start
