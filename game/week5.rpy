label week5_start:
    $ current_week = "Week 5"
    scene bg gates_morning
    with fade

    # Visual: Kudus Town Square - Car Free Day (CFD)
    n "The morning sun feels nice and gentle as it shines through the trees on the street."
    n "It is Sunday, when you do not hear the sound of engines but instead you hear a lot of voices, the sound of bicycles, and the smell of street food."
    n "As you walk up the CFD, all the sounds and smells are too much for your senses to even keep up."
    n "The street is filled with shops in tents selling all kinds of specialties and other things."
    n "The smell of soto ayam is really good, with the smell of fresh juice and the smell of satay barbecue colliding like a music sheet."
    n "This is the weekend in weeks that you believe will be the greatest weekend ever."

    n "You walk through the crowd trying to go with the flow."
    n "You stop sometimes to look at the strange shops, watch the kids flying their balloons, and finally get caught waiting in line for iced coffee."
    p "Everything feels... peaceful."

    n "As you stand holding your drink in your palms, you scan the horizon of people from families and students milling about."
    n "Then you catch a glimpse of someone familiar standing near a clothing stall."
    n "With your courage and curiosity peeking a sense to approach, you take a step there before finally spotting Trida, who was seen leaning against a rack of shirts, looking more at ease than you've seen them all week."

    cap_boy "...I'm telling you, I spent three hours just trying to get the bridge tool to cooperate in Blender. My mesh looked like a crumpled piece of paper by the time I was done."
    braided_girl "That's because you're probably just extruding faces without thinking about your topology, dude."

    n "As Trida's gaze lands on you before anyone else, a smile tugging on their face brings a sudden contrast of warmth jolted from your stomach."
    n "Their eyes light up with a spark igniting the room before their mouth is running around again."
    trida "Oh, hey! Look who it is!"

    n "The two friends glance at each other before they turn to see what's happening."
    cap_boy "Is this the person I remember always near you at the lab all day, Trida?"
    braided_girl "Quit it, you're being a weirdo. Sorry about him—he's just a bit... much."
    cap_boy "I'm not a weirdo, I'm observant. There's a difference, thank you very much."
    braided_girl "Whatever he says."
    n "She rolls her eyes, as her attention is caught back at you with a defining smile."
    braided_girl "Anyway, back to the point—you're in our class, right?"

    menu:
        "Yeah, I am":
            p "Yeah, I am."
        "No, I am not":
            p "No, I am not."
        "Keep silent":
            n "You keep silent, watching the dynamic unfold."

    trida "Guys, please... calm down. I know we only knew each other for a couple of months, but you two should try to remember names from now on!"
    trida "This is [player_name], and yes, they are in our class."
    p "Glad to see you."

    n "The atmosphere shifts instantly as The Cap Boy stops teasing, and the Braided Girl's expression changes immediately."
    cap_boy "Ah, my bad! Didn't mean to be rude. It's just rare for me to catch names and faces, you know?"
    braided_girl "Yeah, there are so many people in RUS. It's good to meet you here, [player_name]."

    n "You exchange a few light pleasantries about the bustling weekend crowds and the morning's oppressive humidity."
    n "For a brief moment, the four of you soak in the vibrant energy of the CFD, surrounded by the sounds of distant chatter and clattering equipment."
    n "Just as you start to savor the atmosphere, the boy in a cap glances at their watch with wide eyes."

    cap_boy "How does time fly? Some food is calling my name, and I have to hurry before the stocks run out!"
    braided_girl "Oh, same. I think we still have plenty of ground to cover today anyway."
    n "The girl grins before glancing forth and back to Trida and you."
    n "You know she looks like she is picking up a hint the entire convo, before she subtly nudges the boy, who stares at her with a nod in response."

    cap_boy "Right! Totally. Catch you later, Trida! Don't spend too much on useless things!"
    n "The two friends share a knowing smirk before disappearing into the vibrant crowd."
    n "With their departure, a refreshing stillness envelops you and Trida."
    n "Trida lets out a long, exaggerated sigh of confusion and tiredness, watching both of their friends."

    trida "What's gotten into them leaving us suddenly like that?"
    trida "But they really are good people, so don't worry about that."
    n "They turn their attention fully to you, as you see their expression softening."
    trida "Also, didn't expect to run into you here..."
    trida "I thought you were the type to stay in and recharge alone on Sundays. How's your CFD been so far?"
    p "It's been nice, that's for sure."
    trida "God, I feel that. My brain feels like it's actually defragging for once."

    n "They pause, glancing at the long, winding path of the CFD stretch ahead, filled with colorful tents and the scent of grilled food."
    n "They hesitate, their fingers nervously tracing the edge of their sketchpad."
    trida "Actually... I was just going to wander a bit more. Any interest in walking together?"

    menu:
        "Accept the offer":
            jump week5_cfd_walk_trida
        "Refuse the offer":
            jump week5_cfd_walk_alone


# --- BRANCH: WALK WITH TRIDA ---
label week5_cfd_walk_trida:
    $ tridaAffection += 1
    p "Sure, I'd love to. It's nice to have some company."
    n "Trida's face lights up—not just a smile, but a look of genuine, unfiltered relief."
    n "They quickly tuck their phone into their pocket and adjust their bag."
    trida "Really? I was worried that I would bother you."
    trida "Alright then, I promise I'll be your great tour guide around here!"
    p "Oh, what a pleasure..."

    # Timeskip
    n "The humidity of Kudus' air is hitting hard."
    n "You and Trida have been drifting through the people walking like a sea of ants with the noise that can't be filtered."
    n "They move with their hands, sharing a bag of cireng to you and dodging people like traffic alongside."
    trida "Honestly, this was actually more fun than spending time with you in the Lab, like we're actually on hangout!"
    p "It's a Sunday thing. We are trying to clear our heads."
    trida "Clear our head, huh? That was a good thing to do besides sitting in front of the monitor and muttering I guess..."

    n "As they walk backwards, laughter spilling from their lips, they misjudge the curb and suddenly lose their footing."
    n "With a surprised expression, they crash to the ground, the impact silencing their laughter as they skid across the pavement, arms flailing before coming to a halt in a tangled heap."
    trida "OUCH!"

    p "Whoa! Are you okay?"
    n "You grab their arm, hauling them up before they hit the concrete hard."
    n "As they stand up with a face turning bright red like a boiled tomato, frantically brushing dust off their jeans."
    trida "I—I meant to do that! It was, uh... testing the ground friction. Super important for, uh, principles of animation, right?"
    p "You're a total disaster."

    n "Trida chuckled, although their cheeks remained bright red."
    trida "Shut up! My legs are just tired, okay? Just... don't tell the others!"

    n "As the laughter faded, both of you eventually found a bench far away from the hustle and bustle."
    n "Trida dropped their body onto the seat and slumped there looking as if they had just returned from war."
    trida "Sorry for the drop in energy. I think I'm just... super fried, you know?"
    p "Yeah, this event is really crowded. No wonder you felt like that."
    trida "Totally. It's making my mind feel overstimulated."

    n "They paused as their gaze drifted long into the people in that town square, who looked like they never stopped coming in."
    trida "Maybe, what I'm about to say kind of came out of nowhere, but..."
    trida "This feeling makes me remember the time I tried to join 3D Animation for the first time."
    p "I thought you were confident in there?"
    trida "No, I am not. If I look more into it, it feels—it's overwhelming. It makes me wonder if I even wanted to do it at all at the first time."

    n "They glanced up, catching your eye. Then you saw that smile that was flooded with exhaustion and a subtle confession of tiredness."
    trida "So staying in my room with those thoughts alone is making me scared sometimes for the failure of my future."
    trida "When we're here, outside of that lab. I don't feel like I'm going to fail, honestly. For a moment, it feels like I'm lifted a bit."
    n "Before they paused, their orange gaze softening as looking at you deeply."
    trida "Thank you for that."
    $ tridaAffection += 1
    jump week5_evening_dinner


# --- BRANCH: WALK ALONE ---
label week5_cfd_walk_alone:
    p "I think I'll pass for now. I'm actually craving a bit more me-time before the week starts."
    n "Trida blinks, a flicker of disappointment crossing their face before they quickly mask it with a supportive nod."
    trida "No, yeah, I totally get that. These days, it is a pressure cooker—you definitely earned some space."
    n "Trida takes a half-step back, slowly giving you a slightly lopsided grin that feels awkward."
    trida "Well, if not, what about I bought you dinner tonight? My treat."
    p "It would be fun."
    trida "It is! It was a food restaurant near school called Bazinga. You would love it. I'll text you later..."
    p "Yeah, see you, Trida."
    n "Trida gives an awkward final wave as their figure disappears into the bustling morning crowd."

    n "You get a snack, you get some cimol, and find a quiet place to watch the city."
    n "When the afternoon light starts to look like gold, your eyes catch a figure of your senior Sabian bargaining with a vendor cart."
    p "Sabian? You're out here?"
    sabian "Yo! If it isn't my favorite junior themselves! I thought you were locked in on your work!"
    p "I actually managed to escape for once."
    sabian "Good! You gotta get out, man. I ran into Trida earlier—that kid's been stressed, right? Needs to eat. You should keep an eye on them—they forget to relax when they're deep in their work."
    p "Yeah, they've been a bit overworked."
    sabian "Well, tell them not to overthink their life. Alright, let's get out of here!"
    $ sabian_affection += 1
    jump week5_evening_dinner


# ==============================================================================
# EVENING: DINNER CHOICES
# ==============================================================================

label week5_evening_dinner:
    scene bg bedroom_late_afternoon
    with fade

    n "The room is dim, lit only by the warm glow of your monitor."
    n "You've been staring at a half-finished UV mesh for hours, and your stomach is finally making enough noise to drown out the hum of your PC fan."
    n "You stretch, making your joints pop in the quiet, and decide it's time to head out. You need real food—not another instant noodle cup."
    p "Where should I go for dinner tonight?"

    menu:
        "KPK Cafe":
            jump week5_dinner_julia
        "Bazinga Food Restaurant":
            jump week5_dinner_trida
        "Abahciek Food Restaurant":
            jump week5_dinner_seniors


# --- OPTION 1: JULIA ROUTE (KPK Cafe) ---
label week5_dinner_julia:
    scene bg classroom
    with fade

    n "The door is creaking open, cutting through the low hum of jazz music playing over the speakers."
    n "KPK Cafe is a sanctuary of warm atmosphere with a bittersweet scent of espresso."
    n "Julia is tucked into a booth near the back. A professional-grade camera lens is resting on the table next to a stack of reference books, and her attention is fixed on a handheld console."
    n "She's wearing oversized headphones, with a furrowed expression in deep concentration."
    n "She looks up, quickly pulling one earphone back, and a smile finally blooms."
    julia "Oh. Hello. Didn't think I'd see you here tonight."
    n "She gestures to the empty seat opposite her."

    menu:
        "What are you doing here?":
            p "What are you doing here?"
        "How are you?":
            p "How are you?"

    julia "I'm just... taking a break now. Choosing somewhere not in my room kind of helps me sometimes."
    julia "I was just doing some research for a project. I found this hidden lore bit in a game, and it's honestly fascinating how they handled the environmental storytelling, and I want to look it up."
    n "She pauses, her fingers tightening slightly on the edge of the table."
    julia "Sorry. I—I didn't mean to info-dump. I just... I get lost in these things. Was that too much?"

    menu:
        "Don't apologize, just tell me. How does storytelling work? I might use it for my project.":
            p "Don't apologize, just tell me. How does storytelling work? I might use it for my project."
            $ julia_affection += 2
        "You're fine. I actually enjoy hearing what you're passionate about":
            p "You're fine. I actually enjoy hearing what you're passionate about."
            $ julia_affection += 2
        "Save the deep dive until I get food. But we're gonna get into it really":
            p "Save the deep dive until I get food. But we're gonna get into it really."
            $ julia_affection += 1

    n "Julia paused before you could see a glimpse of her eyes sparkling in the dim light of the cafe."
    julia "That was—thank you, honestly... I really appreciate that. It's the first time someone really put their attention on this stuff."
    p "We are friends, right?"
    n "Both of you were drowned in that funny tickle in your feet, because a book of friendship journey is opened there."
    jump week5_night_end


# --- OPTION 2: TRIDA ROUTE (Bazinga Food Restaurant) ---
label week5_dinner_trida:
    scene bg teddy_cup
    with fade

    n "Bazinga is a total sensory overload. The air is thick with the scent of stir-fried garlic and heavy smoke."
    n "The heavy wooden chairs screech against the concrete, and the wall of chatter is loud enough to drown out the pop music blaring from a corner speaker."
    trida "YO! OVER HERE! HEY!"
    n "Trida's voice cuts through the noise like a siren. They're grinning and waving both arms like they're signaling a plane."
    n "Radit, sitting across from them, just drops his head into his hands, totally done with the drama."

    p "Hey, guys..."
    radit "I swear, one day this guy is gonna get us banned from every place in town."
    trida "Relax! You're just boring. Look, I've got a craving for fried rice tonight. You should start ordering [player_name], I'm seriously starving."

    n "You grab the greasy, laminated menu. The talk shifts to gaming."
    radit "Well, as I said, I finally cleared another run of Final Fantasy VII last night."
    trida "Yeah, the lore is actually insane. Honestly, you're right. Why am I killing myself over Maya when I could just live addicted to video games?"
    radit "You would miss touching grass."
    trida "But for real, when I'm not glued to a screen, I lowkey miss hiking. Just being out here, you know? No deadlines or anything."
    n "They catch themself, their shoulders slumping as the excitement fades into a sheepish grin."
    trida "My bad, I'm totally yapping again. I just... I needed to not be a hard-working student for five minutes, you know?"

    menu:
        "Don't sweat it, listening to you rant about games is way better than stress-talking about school.":
            p "Don't sweat it, listening to you rant about games is way better than stress-talking about school."
            $ tridaAffection += 2
        "Big mood, I'd take a rhythm game high-score over a 3D nightmare any day.":
            p "Big mood, I'd take a rhythm game high-score over a 3D nightmare any day."
            $ tridaAffection += 1
        "I thought you were kind of 'outdoorsy,' but I'll let the yapping slide just for tonight.":
            p "I thought you were kind of 'outdoorsy,' but I'll let the yapping slide just for tonight."
            $ tridaAffection += 1

    trida "See, Radit? I told you they'd get it. You're just a total buzzkill with your attitude."
    radit "Whatever, man. Just order the food before you start a three-hour essay. I'm starving."

    n "The table feels smaller, more private, despite the surrounding noise."
    n "Radit pulls out his phone to check messages, effectively giving you and Trida a pocket of space."
    trida "For real though... thanks for listening earlier. I know I'm a lot. I feel like I've been tired of myself with all this constant pressure to be perfect."
    trida "I don't really tell anyone else this, but sometimes the stress hits so hard I just sit on my floor in the dark. It's the only way I can force myself to feel something other than crushing panic."
    trida "I'm really glad you're the one I ended up sitting with tonight."
    $ tridaAffection += 1

    # Timeskip
    n "Some minutes later, the dinner crowd begins to trickle out."
    trida "Man, I think that's my limit. Hey, let's call it a night. I'm wiped."
    radit "Alright, I'm out first. I need to go to the Indoapril. Don't spend the whole walk home making a fuss about your games to [player_name], Trida. See you guys later."

    n "Radit departs on his bike, leaving the two of you standing on the edge of the dark, quiet street."
    trida "Hey... are you heading back to the boarding house now? If you don't mind... Could we walk together? I really don't want to walk back alone tonight."
    n "They sound uncharacteristically small. Trida sticks close to your side as you start walking."
    trida "I know it sounds stupid, right? Already this big but still afraid of the dark."
    p "Why would you say it like that?"
    trida "It's not about the dark... When it's just me, all the thoughts about the animation portfolio, the grades, and the pressure from home? They get so loud. They feel like they're going to swallow me whole."

    # Visual Splash Art: Trida looking at Player
    n "They glance at you, a small, sheepish smile tugging at the corners of their mouth."
    trida "Like I said, if I had company or someone to talk to... It's like the noise stops. It's actually quiet in my head for once."
    trida "You're kind of like a save point in a game, you know? The place where I can actually catch my breath before the next boss fight."
    n "They stop for a second, looking up at the sky, then back at you with an almost startling intensity."
    trida "I'm really, really glad you're the one I'm walking with. It makes the world feel... I don't know, a little less terrifying."
    n "Their hand brushes against yours as you walk, not quite holding it, but close enough that you can feel the warmth of their skin. They don't pull away."
    $ tridaAffection += 2
    jump week5_night_end


# --- OPTION 3: SENIORS ROUTE (Abahciek Food Restaurant) ---
label week5_dinner_seniors:
    scene bg teddy_cup
    with fade

    n "Abahciek skips conventional doors; the front is a spacious, open-air gathering spot with elevated wooden platforms and floor mats."
    chie "[player_name]! No way, are you serious?! Over here!"
    n "Chie is halfway out of her seated position on the floor, waving animatedly in the air. Across from her, Sabian leans casually against the wall with an amused smirk."
    p "What should I order?"

    menu:
        "Chicken Smackdown":
            p "I'll take the Chicken Smackdown."
        "Chicken Porridge":
            p "Chicken Porridge sounds good."
        "Fried Tofu":
            p "Fried Tofu for me."

    $ sabian_affection += 1
    $ ch_affection += 1
    chie "Anyways, tell me, how's your week actually going? Don't give me the boring version—I want the messy stuff!"
    n "Laughter fills the warm circle around the low table as the three of you enjoy a cheerful, lively dinner."
    jump week5_night_end


# ==============================================================================
# END OF WEEK 5
# ==============================================================================

label week5_night_end:
    scene bg bedroom_late_afternoon
    with fade

    n "Back in your room, the quiet hum of the night brings a soothing closure to a long, memorable weekend."
    n "You fall asleep with a light heart, looking forward to the school festival ahead."

    # End of Week 5 -> Continue to Week 6
    jump week6_start
