label week7_start:
    $ current_week = "Week 7"
    scene bg classroom
    with fade

    # Visual: Classroom Morning
    n "Soft morning light spilled across rows of empty seats, and the low hum of desktop fans blended with the faint tapping of keys."
    n "In the far corner, Trida sat at their usual desk with their shoulders hunched over their heavy laptop."
    n "Their eyes moved quickly over the screen, completely focused on a half-finished animation."
    n "They looked so absorbed in Maya, their world shrinking down to the glowing monitor and the quiet rhythm of their work, exactly as people imagine animation students to be."

    n "In one hand, their fingers absentmindedly turned over a slightly crumpled, half-eaten bar of chocolate."
    n "It was the same specialty snack you gave them yesterday."
    n "That day had been so tense your stomach felt like it was in knots, and your heartbeat and breath kept catching."

    n "You walked up to them, stepping quietly before leaning your weight against the edge of their desk."
    show trida uniform neutral at center with dissolve
    p "You're seriously still eating that?"

    n "You crossed your arms with a small smirk of morning greetings, with just a pinch of teasing."
    p "I bet it's been sitting in your bag since yesterday."

    show trida uniform embarrassed at center, panic
    n "Trida jerked upright in their chair, their whole body giving a startled twitch as your voice cut through their focus."
    n "Their eyes widened, and a bright red flush crept up from their neck to the tips of their ears."
    n "They fumbled with the chocolate bar, nearly dropping it, before letting out a loud, high-pitched laugh."
    n "Their fingers drummed anxiously against the desk, trying to hide their reaction behind a burst of panic."

    trida "E-eh?! What do you mean?!"
    trida "Good food has its own timeline, okay! It's called savoring, look it up!"
    n "They gestured wildly with the half-eaten chocolate bar, nearly dropping it onto their keyboard."
    trida "Besides, it's not like it went bad or anything!"

    n "You let out a soft chuckle, watching them scramble to defend their snacking habits."
    p "Sure, keep telling yourself that. Don't come crying to me if your stomach starts acting up during third period."

    show trida uniform happy with dissolve
    n "Trida grinned, the nervous tension instantly draining from their shoulders as they settled back into their chair."
    n "They reached out, giving your arm a quick, familiar nudge with their elbow—that subconscious physical touch they always did without realizing it."
    trida "Jeez, look at you, acting all worried. Who knew you cared so much about my digestive health?"

    n "They laughed dryly, but their gaze suddenly shifted, bouncing nervously toward the edge of the desk before locking back onto yours."
    n "The bright cadence in their voice faltered and was replaced by a strange hesitation."
    n "They cleared their throat, and you suddenly found their half-eaten chocolate bar very, very interesting to look at."

    trida "Um... actually..."
    n "Their voice dropped an octave, turning much quieter, stripped of its usual performative silliness."
    show trida uniform embarrassed with dissolve
    n "They rubbed the back of their neck with their free hand, their fingers fidgeting nervously against their collar."
    trida "The truth is... I was saving it on purpose."

    n "You blinked, caught off guard by the sudden shift in tone."
    p "Saving it?"
    p "Why? It's just regular chocolate."

    n "Trida's eyes darted up to meet yours, maintaining that intense, unblinking eye contact they always held when trying desperately to be sincere."
    n "Their ears were bright red now."
    trida "It's not 'just' anything when it was... you know. Given by you."

    n "They let out a dry, self-deprecating chuckle, their gaze dropping back to the desk as they tried to laugh it off."
    trida "Listen to me, ugh... I sound so cheesy right now. Ignore me."

    n "They tried to look away, but you didn't move, and they kept rushing their words as if trying to outrun their own vulnerability."
    trida "No, but seriously—I don't get stuff like that very often. Nobody really just... hands me something nice out of nowhere before."
    trida "It genuinely made my whole week better, okay?"

    n "For a second, the bustling noise of the classroom around you seemed to fade away entirely."
    n "The raw, unguarded honesty caught you completely off guard."
    trida "It made me feel like... maybe I'm not totally invisible here."

    n "You stood there, suddenly struggling to find a casual reply, feeling a hot flush creep up your own neck as you stared back at them."
    n "Trida noticed your silence, and their eyes widened in mild panic, their hands immediately flying to their pockets as if wanting to disappear into their chair."
    trida "A-anyway! Back to work, right? Before the teacher explains another thing!"
    trida "Can't have us failing, can we?"

    menu:
        "Right...":
            p "Right..."
            $ tridaAffection += 1
        "Obviously not":
            p "Obviously not."
        "Of course, we don't":
            p "Of course, we don't."
            $ tridaAffection += 1

    hide trida with dissolve
    jump week7_break_time


# ==============================================================================
# BREAK TIME
# ==============================================================================

label week7_break_time:
    scene bg classroom
    with fade

    n "You can't focus the whole time in class, the voice of the teacher passing by like a buzzing sound through your head."
    n "You kept stealing glances at Trida's desk, where that chocolate belongs."
    n "Before you realized, the speaker was already announcing break time, snapping you out of your thoughts."
    p "I probably need to just forget this. I need to enjoy the break time..."
    p "Where should I go now?"

    menu:
        "Go To Grapos":
            jump week7_grapos_radit
        "Stay in The Class":
            jump week7_stay_trida


# --- OPTION 1: RADIT ROUTE (Grapos) ---
label week7_grapos_radit:
    scene bg grapos_field
    with fade

    n "The Grapos field outside hummed with life, a vibrant tapestry of students stretching their limbs and leaning against the weathered concrete pillars, savoring the brief yet precious respite from their hectic schedules."
    n "Clusters of them flocked to the canteen, drawn in like moths to a flickering flame, their laughter and chatter creating a symphony of youthful exuberance."
    n "The warm midday air enveloped you, infused with the faint aroma of food and the distant murmur of vocational students animatedly discussing render queues and impending project deadlines."
    n "You found yourself leaning against the cool concrete railing, relishing the quiet reprieve, the bustle around you fading into a soft background hum."

    n "Suddenly, you noticed footsteps padding softly against the pavement nearby."
    show radit neutral at center with dissolve
    n "Radit appeared, his easy-going demeanor evident as he sauntered over, hands tucked deep into the pockets of his jacket."
    n "With a gentle shake of his head, he cast off the last remnants of moisture from his hurried trip to the washroom."

    radit "Man... sometimes I think about dropping out to become a professional sleeper."
    n "Radit spoke softly, his words drawn out as he slipped into his signature easygoing rhythm."
    n "After a moment of deep contemplation, he let the silence linger before continuing, his tone languid and unhurried, as if savoring each syllable."
    radit "My bed's calling me from across town, I swear."

    n "You let out a soft huff of laughter, glancing sideways at him."
    p "Your bed is a mattress on the floor in a cramped boarding room, Radit. It's not calling you, it's begging for mercy."

    radit "True. But at least my mattress doesn't crash when I'm halfway through saving a file."
    show radit smile with dissolve
    n "Radit gave a leisurely grin as his shoulders dropped with a laugh."
    radit "Speaking of terrible life choices..."
    n "He hesitated, transferring his weight to the opposite foot, his gaze wandering toward the horizon before returning to you with a wry sparkle in his eye."
    radit "I found this absolute trash-tier garage band from Shimokitazawa yesterday. Their entire aesthetic is just four guys standing in a dark basement playing out-of-tune guitars."

    p "And?"
    radit "And honestly? It's speaking to my soul."

    n "You raised an eyebrow and then crossed your arms with a knowing smile."
    p "Let me guess. Another band with double-digit monthly listeners on Spotify, and you're about to spend half your allowance on an import vinyl that'll take three months to clear customs?"

    show radit amused with dissolve
    n "Radit just stared at you for a beat, with an amused twitch at the corner of his mouth."
    radit "First of all, it's a cassette tape, not a vinyl. Get your indie hipster formats right."
    radit "Second is... wow, okay! Look at you, tracking my purchasing habits like an auditor."
    n "He tilted his head, his hands staying firmly planted in his pockets as he leaned a shoulder against the railing next to you."
    radit "Should I be flattered that you remember what kind of garbage I waste my money on, or worried that you're turning into a stalker?"

    p "I don't need to stalk you when your room practically smells like shrink-wrapped album art and regret."
    n "You retorted, nudging your elbow into Radit, who smirked with sincere warmth shining through his typical stoic demeanor, though he quickly masked it again with another casual jest."
    $ radit_affection += 1

    radit "Hey, someone's gotta keep the local underground scene alive..."
    n "He glanced back toward the doorway of the classroom, catching a brief glimpse of the frantic energy still humming inside."
    radit "Anyways, we should probably head back before the teacher locks us out and assumes we ran away to join an indie band ourselves."
    radit "Though, honestly? Not the worst backup plan."

    n "With an eased shrug, Radit pushed away from the railing, withdrawing one hand from his pocket briefly to point toward the door."
    n "With an unhurried pace, the two of you turned and floated back into the classroom together."
    hide radit with dissolve
    jump week7_civics_assignment


# --- OPTION 2: TRIDA ROUTE (Stay in Class) ---
label week7_stay_trida:
    scene bg classroom
    with fade

    n "Instead of going outside in the sweltering midday heat or grabbing something from the canteen, you chose to stay in the quiet, air-conditioned classroom."
    n "You pulled an empty wooden chair over to Trida's desk."
    show trida uniform neutral at center with dissolve
    n "They stared blankly at an open notebook filled with chaotic character sketches and rough storyboard panels, lost in their thoughts."

    p "If you keep staring at that paper, the ink is going to run away."
    n "You said, resting your chin on your hand as you leaned against the edge of their desk."

    show trida uniform embarrassed at center, panic
    n "Trida flinched, their pencil clattering onto the desk as they spun around in their chair."
    n "They let out a loud, high-pitched squawk and threw their hands up dramatically."
    trida "Oh, you're going to give me a heart attack!"
    trida "Don't sneak up on people like that when I'm trying to focus—or failing to focus!"

    n "They laughed nervously, their gaze darting around the empty room before landing on you with unblinking focus."
    trida "Besides, the ink isn't running away because it's scared of me. It's running away because my layouts are a total disaster. Look at this nonsense."
    n "They shoved the sketchbook closer to you, tapping aggressively on a messy sketch panel."
    trida "I swear, every time I try to map out the pacing for this sequence, my brain just short circuits."
    trida "Why is structuring a story so hard? I just wanted to make something cool that made you feel like you could take on the world, but here I am making garbage."

    show trida uniform sad at center, dip
    n "They slumped forward, letting their forehead thump gently against the edge of the desk next to your arm, letting out a heavy sigh."
    trida "Sometimes I wonder why I even try to aim high. Look at the other kids in our major—they're already creating amazing animation with gorgeous concepts, and here I am struggling to make a simple timeline make sense."
    trida "I kind of felt stupid, you know..."

    n "You chuckled and reached over to give their shoulder a comforting squeeze."
    p "You're too hard on yourself, Trida. You just need a break."

    show trida uniform happy at center, hop
    n "At your warm touch, Trida perked up, a bright smile replacing their moment of doubt as if those heavy thoughts had vanished."
    n "They leaned into your touch, bumping their shoulder against yours without realizing it."
    trida "See? That's why you're the best. Always showing up with the right words at the right time."
    n "They laughed, their voice speeding up when they started talking animatedly again, gesturing wildly with their hands."

    trida "It's kind of out of nowhere, you know..."
    trida "But did I tell you about the lore video I watched last night? It's this masterpiece of a classic RPG, and the plot twists just keep coming—?"

    n "They suddenly stopped, narrowing their eyes at you, though a pleased smile tugged at the corners of their mouth."
    n "They noticed how close you were sitting and that you hadn't left for break like everyone else."
    n "The tips of their ears turned a faint pink, and they quickly rubbed the back of their neck."
    trida "Hold on, I just realized that you stayed inside during break?"

    p "Yeah, well... Do you have any problems with that?"
    trida "I mean, instead of going out for actual fresh air or hanging out with anyone else like your usual?"
    n "You heard their voice lose some of its theatrical bounce and genuine warmth."
    trida "You didn't have to stay just for me, you know. I'm totally fine."

    p "I was just trying to keep you company so you don't accidentally fold your sketchpad in half out of panic."
    n "You replied with a smirk tugging as you saw Trida let out a flustered laugh affectionately."
    trida "Jeez, you're impossible. Yeah, I'm glad you're here."
    $ tridaAffection += 1
    hide trida with dissolve
    jump week7_civics_assignment


# ==============================================================================
# CIVICS GROUP ASSIGNMENT
# ==============================================================================

label week7_civics_assignment:
    scene bg classroom
    with fade

    n "The classroom is bathed in the warm, golden glow of the afternoon sunlight, which streams through the towering windows and creates a dramatic interplay of light and shadow."
    n "The tall shadows stretch languidly across the floor, juxtaposing the neat rows of bulky drawing tablets that have been momentarily set aside."
    n "In their place, vibrant notebooks and well-worn textbooks are spread out across the desks, hinting at a bustling environment where creativity intertwines with academic pursuit."

    n "The civics teacher walked in front of the class, her black shoes squeaking softly against the linoleum floor as she dropped a handful of reference handouts onto the front desk."
    show civics_teacher at right with dissolve
    civics_teacher "Quiet down, please. For today's assignment, you don't need the computers. Just open your textbook to the chapter on the 1945 Constitution."
    civics_teacher "Your task is simple: look at the group task, circle the instructions, and coordinate with your group to either answer the exercise questions, draft a short paper, or summarise the material. Get to work."

    hide civics_teacher with dissolve
    n "With a sharp click of her pen, she turned back to the whiteboard to write down the page numbers."
    n "Around the room, the sound of chairs scraping against the worn floor echoed as students pulled out sheets of loose-leaf paper and began rifling through their textbooks."
    n "Yet, at your cluster of desks, a sense of tension hung in the air, palpable and suffocating."

    n "The boy seated directly across from you—typically so inconspicuous that he practically faded into the background of the classroom—exhaled a heavy, deliberate sigh that seemed to slice through the ambient noise."
    n "With an air of practiced detachment, as if viewing group work merely as an unwelcome administrative chore rather than an opportunity for collaboration, he snapped open his hefty civics textbook with a dull thwack."
    show glasses_boy neutral at right with dissolve
    show trida uniform neutral at left with dissolve
    n "His gaze remained fixed on the pages before him, avoiding eye contact as he methodically adjusted his glasses."
    n "With a stillness that suggested he was accustomed to being overlooked, he turned straight to the assigned page without a single word escaping his lips."

    show trida uniform embarrassed at left, panic
    n "Beside him, Trida sat frozen."
    n "They stared down at their textbook, but their eyes were completely glazed over, not registering a single word of the printed text."
    n "Their fingers were locked tightly together in their lap, trembling slightly as their gaze darted anxiously around the desk, refusing to meet anyone's eyes."

    n "Without waiting for either of you to take the lead, Trida reached out a hesitant, shaking hand to flip to the correct page in their own book, completely bypassing the instruction to circle the prompt first."
    n "They rushed to grab a pencil, their hand moving too fast out of pure panic, and accidentally knocked their eraser off the desk."
    n "It bounced off your shoe with a soft thud."

    n "The boy didn't even look up from his page. His expression remained entirely flat, devoid of any emotional spike, as he delivered a deadpan critique with the casual detachment of an automated system reading a prompt."
    glasses_boy "You dropped it. And you skipped the circle instruction. It's not that complicated."

    show trida uniform sad at left, dip
    n "Trida's hand froze mid-air above the floor. The tips of their ears turned into a mortified shade of red, and they pulled their arm back in an instant, resting it limply against their knee."
    n "Trida didn't bend down to pick up the eraser. The only thing they did was stare blankly at the crease of the book, biting their lower lip until it turned white."
    n "All of their worst, deep-seated fears—the ones they always tried to mask behind loud banter or constant jokes—were completely exposed by the uninterested dismissiveness of their groupmate."
    n "Trida couldn't even force a laugh, completely unable to find words to defend themself."

    n "The boy turned the page of his textbook with a quiet rustle of paper, entirely unbothered by the sudden vacuum of air at the table."
    glasses_boy "Anyway. We have to pick between answering the questions or writing the summary. I'm just going to write the summary so we can leave early. Let me know if you guys are doing something else, or if you're just going to sit there."

    n "His voice carried no malice, which somehow made it infinitely worse."
    n "It was the absolute, crushing indifference of someone treating Trida not even as a frustrating obstacle, but as a mildly inconvenient system error to be bypassed."

    n "You sat right beside Trida, and suddenly a rush of hesitation climbed up from your throat."
    n "You had spent so long being their friend, and suddenly the absolute devastation written across Trida's usually expressive face made a heavy knot form in your chest."
    n "You had never seen Trida look completely hollowed out and defeated, reduced to silence by someone who didn't even care enough to be angry."

    n "Trida stared down at the open page, their throat working as if trying to swallow glass."
    n "The crushing weight of feeling entirely useless—of being viewed with mechanical disregard—finally forced a fractured, defensive murmur past their lips."
    trida "I... I was going to circle it..."
    n "Trida whispered with a voice cracking slightly, so quiet it was almost swallowed by the ambient noise of the classroom."
    n "They stared down at their desk, fingers clutching the edges of their textbook like a lifeline, desperately trying to excuse the panic."
    trida "I just... I was rushing. I can still do it. I'm not... I'm not trying to mess it up on purpose."

    n "The boy didn't look up from his textbook, letting out a sharp, dismissive sigh through his nose as he tapped his pen against the margin."
    glasses_boy "Well, whatever, it doesn't matter, let's just get this over with."

    n "The flatness of his tone carried a sharp edge of annoyance, dropping like another lead weight over the small cluster of desks."
    n "Instantly, any lingering sound from their corner completely vanished. The silence that followed was an absolute, suffocating awkward tension that made the air feel thin."

    n "Trida recoiled sharply as if they had received a physical blow. All of their usual chatter and restless energy seemed to vanish completely."
    n "They could only gaze downward in embarrassment, their eyes stinging and a trembling hand grasping the pencil in an attempt to continue working."
    n "They drew a haphazard circle around the instructions, but their fingers wouldn't steady, and their mind was utterly blank."
    n "The text on the page blended into a jumble of meaningless ink, and each awkward mark only served to validate the boy's assertion."
    n "They ceased their efforts, allowing their hand to fall into their lap, shoulders fully slumped."

    n "You stood frozen beside them, a tight knot of unease twisting in your chest."
    n "After all the hours you'd spent mingling with their mood swings, offering a steady presence through their emotional storms, you had never seen Trida like this."
    n "They were utterly spent, their defenses stripped away, the weight of their turmoil spilling over as they quietly crumbled next to you."

    menu:
        "Are you okay?":
            jump week7_reassure_okay
        "What did you just do?":
            jump week7_reassure_interrogate
        "Say Nothing":
            jump week7_reassure_silent


# --- OPTION 1: "ARE YOU OKAY?" ---
label week7_reassure_okay:
    $ tridaAffection += 1
    p "Are you okay?"

    n "Trida didn't look up when you spoke."
    n "For a long, agonizing second, the only movement was the faint, rapid twitch of their fingers where they were balled into tight fists in their lap."
    n "When they finally raised their head slightly, their eyes were glossy, avoiding your gaze entirely as they fixed on a scuff mark on the wooden desk."

    trida "I'm... yeah. I'm fine,"
    n "Trida whispered back with that strained voice that seemed entirely unconvincing."
    n "They managed a weak, pathetic ghost of a smile that didn't reach their eyes at all before giving a subtle shake of their head."
    trida "Just... don't worry about it right now. We need to finish this before the bell. Let's just... let's just get it done."

    n "You saw Trida's hands pick up their pencil again, their knuckles turning white from how hard they were gripping, and forced those tangerine eyes to stare back down at the blank lines of the paper."
    n "But you could see right through the fragile facade."
    n "You knew they weren't working, because Trida was just holding themself together by a thread, terrified that if they moved or spoke another word, they would completely shatter in front of everyone."
    n "Sitting right beside them, a profound wave of helplessness washed over you."
    n "You wanted to fix it, to push past their defenses and chase away the humiliation suffocating them, but watching them retreat into such a defensive shell left you wondering how you could reach them."
    jump week7_conclusion


# --- OPTION 2: "WHAT DID YOU JUST DO?" ---
label week7_reassure_interrogate:
    p "What did you just do?"

    n "Trida didn't react right away."
    n "They became completely still, the pencil awkwardly suspended above the blank page like a pendulum caught at the height of its swing."
    n "The familiar nervous chatter that usually filled the space had vanished."
    n "Instead, Trida sat with an intense tension radiating from them, their jaw clenched, and brow furrowed in a deep, conflicted frown that hinted at a storm of thoughts swirling just beneath the surface."

    n "When they finally stirred, it was not to meet your gaze."
    n "Trida's eyes flitted nervously away, avoiding yours with a desperate flicker toward the window, then darting downward to the desk as if the very surface could provide an escape from the pressure of your scrutiny."
    n "They swallowed hard, the movement of their throat betraying the struggle within, and their fingers gripped the fabric of their uniform pants so tightly that the knuckles turned white."
    n "A heavy silence enveloped you both, and the stillness stretched on, morphing into an uncomfortable tension that seeped into your own mind, amplifying the weight of unspoken words between you."

    menu:
        "Did I say the wrong thing...":
            p "Did I say the wrong thing..."
        "Was asking 'what did you just do' too aggressive?":
            p "Was asking 'what did you just do' too aggressive?"
        "Did I sound too interrogating?":
            p "Did I sound too interrogating?"

    n "Every second that stretched on without a response felt deafening."
    n "You found yourself second-guessing your own tone, wondering if you had just made an already fragile moment ten times worse."
    n "Trida kept their head down, wrapped in their own quiet misery, leaving you sitting there in overthought silence."
    jump week7_conclusion


# --- OPTION 3: SAY NOTHING ---
label week7_reassure_silent:
    n "When you chose to remain silent, an oppressive stillness enveloped the desk, settling heavily like an unwelcome blanket that stifled any remaining whispers of conversation."
    n "Trida released a shaky breath that seemed to escape their lips."
    n "As the realization of your lack of response sank in, they slowly turned their attention back to the open textbook before them, their red-rimmed eyes stubbornly fixed on the dense paper as if it held all the answers."

    n "They attempted to work once more, but each motion felt agonizingly slow and laborious."
    n "Every movement of their hand was filled with hesitance and stiffness."
    n "They would laboriously write down a solitary sentence, then stare at it, lost in thought for what felt like an eternity."
    n "After a long moment, they would erase half of it, their fingers trembling as they rewrote it, as if any imperfection could provoke yet another comment."
    n "Their shoulders remained tightly clenched, hunched inward as if trying to shield themselves from the stark scrutiny of the surrounding room."

    n "Beside them, you watched the painful, exhausting effort they put into just stringing together a few words."
    n "A part of you ached to say something, to lift the crushing weight of humiliation that pressed down upon them, but the prospect of speaking felt dangerous—like it might shatter the delicate control Trida was clinging to with everything they had."
    n "So you end up just sending support through silently, an unspoken prayer of your heart wishing to be accepted through telepathic warmth to Trida."
    jump week7_conclusion


label week7_conclusion:
    n "The painful quiet at the desk continues until the school bell finally cuts through the room."
    hide glasses_boy
    hide trida
    with dissolve
    n "Without a single word, Trida sweeps their books into their bag, keeping their eyes glued to the floor as they slip quickly out the door."
    n "You stand alone by your desk, a heavy ache lingering in your chest."
    n "You know you cannot leave things like this..."

    scene black
    with fade
    # Connect to Week 8
    jump week8_start
