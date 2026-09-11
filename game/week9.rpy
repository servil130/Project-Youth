label week9_start:
    $ current_week = "Week 9"

    # ==============================================================================
    # ACT III - CHAPTER I: ROUTINE, APOLOGIES, AND HONEST CONFIDENCES
    # ==============================================================================

    scene bg classroom
    with fade
    play sound "audio/school_bell.ogg"
    play music "audio/bgm_classroom.ogg" fadein 2.0 loop volume 0.5

    n "The sound of the school bell's ring fills the room in a familiar rhythm, signaling the usual 12 PM break."
    n "After the events of Saturday night, the return to routine feels welcome and reassuring, a breath of fresh air for your mind."
    n "You stretch in your seat to the warmth of the afternoon sun after the long lesson period, and as you do, catch a glimpse of Trida's figure approaching with a beaming grin and phone in hand."
    n "Although it feels as though you can feel their animated presence before you even see them."

    show trida happy at center with dissolve
    trida "[player_name]!!!"
    n "Trida's urgent booming voice was only amplified by how close their face was to yours, their eyes wide open in delight and breaths labored as visible sweat dripped down their neck."
    n "You wondered what Trida could've been possibly doing during class to inflict such a reaction."

    trida "Check it out—I—I finally got my first full combo on a level 25!"
    n "You're given no time to respond before Trida shoves their phone in your face."
    n "You quickly grab Trida's arm and back the screen away before you go blind from the bright neon game they're trying to show you."
    n "You squint at the game text and read the aforementioned words 'FULL COMBO' pop up. You see that Trida was playing their favorite rhythm game, 'Splashy!Scene' on an Expert difficulty."

    trida "Huge improvement, am I right?! I still can't believe I pulled off those ladder notes, I was basically holding my breath the entire time…!"

    menu:
        "Woah, you actually did it?!":
            $ tridaAffection += 1
            show trida laugh
            n "Trida chuckled in gratification, a giddy smirk showing through the corners of their lips; you could see a twinkle in their eyes."
            n "Trida's tone was humorous, but you could sense they were genuinely psyched by the new achievement."
            trida "You bet I did! Heh, crazy, right?"
        "So THAT'S what got you fired up, huh?":
            $ tridaAffection += 1
            show trida annoyed
            trida "Hey! What's that supposed to mean?!"
            n "Trida's lips scrunch into a childish pout as they whined out each word."
            n "Despite Trida's typical reaction when teased, you couldn't help but find this expression of theirs more endearing than usual."
            n "You let out a quiet, amused chuckle."
            p "Just wasn't expecting the strong reaction is all."
            show trida happy
            trida "Well I'd say my reaction was very reasonable, if I do say so myself!"

    show trida smile at center
    n "Trida let out a small proud huff, redirecting their gaze back to the phone screen with a radiant grin as their fingers fervently screenshotted the feat repeatedly as though it would disappear at a moment's notice."
    n "The sudden switch from the vulnerable Trida in your room was evident in every little jittery mannerism."
    n "As Trida's eyebrows perked up in delight, you found yourself paying extra attention to Trida's every move once more."
    n "How their feet shuffle on the floor from side to side, how their thumbs frantically hover over the phone screen, how their cheeks tremble with how intensely they tense their smile…"

    show trida blush at center
    trida "Uh—[player_name]? Do I look funny or something?"
    n "Your thoughts get interrupted by Trida's face leaning in so close you could see the warm flush of fluster taking form on their ears, a confused smile and furrowed brows playing on their features as you realize that you had been staring at them for what probably felt oddly long."

    menu:
        "Sorry, I was spaced out":
            p "Sorry, I was spaced out."
        "It's nothing":
            p "It's nothing."
        "Just… thinking":
            p "Just… thinking."

    n "You croak out your quick excuse, however unconvincing it was judging by Trida's quiet chuckles."
    show trida smile
    trida "I mean, you looked pretty focused on me just now…"
    n "Despite the joking words, Trida's tender voice would suggest otherwise."
    n "Their eyes darted away for a moment, lips pressed together as if physically holding back the words as they fiddled with their phone buttons."

    n "The unspoken question hung in the air, about how Trida was feeling being in class again."
    n "Trida started to redirect their attention back to their game. They rested their elbows on the rough wood surface of your desk and bent down to comfortably play, closing the proximity."
    n "You could feel the tension in your throat, as if itching to get the words out, but with how increasingly content Trida became in your presence, the opportunity kept slipping at the risk of ruining the mood."

    trida "Hm... Let me try this level 27 one..."

    n "As Trida eased back into the game, your eyes instinctively scanned through the classroom out of curiosity for what your previous groupmate was doing."
    n "After checking out the rest of your classmates chatting up a storm, your eyes catch your teammate quickly looking down at his fidgeting hands with a flat expression as he gets up from his seat."
    n "Your gaze flickered in quick glances between Trida and your teammate. You could spot him seemingly making his way closer to your desk. You…"

    menu:
        "Look away and pretend you weren't watching":
            n "You promptly turned your head back to Trida."
            n "You see they've already started playing a new song in front of you without having noticed, the frantic rhythmic taps of their fingertips matching to the beat of the aggressively cheery song playing a little too loudly from their phone."
            n "You lean forward to catch a glimpse of the chart Trida was trying to complete, as well as Trida's focused eyes and a small peek of their tongue being bitten to the side."
            n "Despite the hastiness of Trida's play style, you could see improvement show through, however small."
        "Call out to the boy":
            p "Oh hey there!"
            show trida neutral at left with ease
            show glasses_boy neutral at right with dissolve
            glasses_boy "Ah—[player_name]…"
            n "You peek from behind Trida's focused stance, hoping to catch the boy's attention, and soon enough he was looking right at you with a small frown and furrowed brows."
            n "His narrowed eyes looked away as he kept walking towards you two, as if taken aback by your sudden call."
            n "Trida didn't seem to notice a single word you shouted out, though, still obliviously giving their all into the chart with laser-focused eyes and rapid, clumsy taps on the bright phone screen."
            hide glasses_boy with dissolve
            show trida neutral at center with ease
        "Watch him get closer":
            n "You quietly observe the boy approaching from afar."
            n "The rapid rhythmic taps of Trida's gameplay catch the attention of the boy; he glanced in your direction and his gaze landed on you keenly monitoring him."
            n "It seemed to confuse the boy a little, as his narrowed eyes did quick glances between you and the rest of the class, his movements becoming slower and more hesitant."

    show glasses_boy neutral at right with dissolve
    show trida neutral at left with ease
    n "It wasn't long until the boy in glasses was awkwardly hovering around the two of you, clearly wanting to talk, but seeing how focused Trida was on beating the level 27 chart, he hesitated on interjecting."
    n "You sighed and tapped on the table to get Trida's attention."

    p "Trida, get off of Splashy for a moment, you—"
    trida "Hold up, hold up!! I'm so close to finishing this, please…!"
    n "Trida slurred out excitedly in a plea, eyes glued to the screen and finger swipes getting more and more vigorous as the song crested into a crescendo."
    n "You would've thought they were playing some kind of RPG beating a final boss, but as it seemed when you looked at the health bar of Trida's game, it was one wrong tap away from dying instantly."
    n "You shared a skeptical look with the boy as he fixed his glasses."

    p "Trida, please—"
    n "As you were about to try to interrupt a second time, Trida straightened their back without warning and placed their phone down on your desk, exhaling deeply as the song came to an end."
    show trida happy at left
    trida "Ahh, finally…"

    n "As though re-orienting with reality, Trida finally blinked a few times and looked around, where the boy in glasses was staring right back with a small grin, stifling a giggle at the ridiculousness of the situation."

    show trida surprised at left
    trida "AH! What the—!"
    n "Trida flinched back at the sudden appearance, letting out a loud yelp."
    p "Yeah, I've been trying to tell you…"
    show trida nervous at left
    trida "O-oh, it's you… Sorry…"

    n "Trida diverted their gaze to the boy, trying to keep a small smile despite the obvious guilt showing through their shakier voice and fidgeting hands."
    n "The boy's gaze softened at the sight of Trida's squirmy gestures; he halted before speaking in a quiet voice."

    glasses_boy "Oh, it's totally alright, don't even worry about it. It's just…"
    n "The boy gruffly cleared his throat, looking down at his hands."
    glasses_boy "I—I just wanted to… you know, about the last group project…"
    n "He dragged out his words with a lightly strained voice. Trida held their breath, waiting for him to finish."
    glasses_boy "…I wanted to apologize, Trida… for last time, during our discussions."

    trida "…!"
    glasses_boy "I just… let my confusion turn to anger and went off the deep end, when I really should've just… tried to be cool about it."

    show trida smile at left
    n "Trida's tensed face loosened at the boy's candid apology, their eyes on him as they swallowed their breath."
    trida "It's… it's all good. I mean, I shouldn't have dragged the team down as much as I did, I understand…"

    glasses_boy "Hey, don't beat yourself up over it too much. It was only a small assignment, wasn't it?"
    n "The boy cracked a small, awkward smile, his voice low and light-hearted—a grin that suited the usually stone-faced boy a little better."
    n "Trida seemed just as pleasantly surprised as you were."
    trida "…Yeah, thanks anyway."

    glasses_boy "No, I—I should be thanking you… honestly, it made me realize how insensitive I can be. I probably wouldn't have known otherwise…"
    n "You notice the boy's demeanor relaxing the more he talks to Trida, the grin naturally remaining on his face as he eases into the conversation."
    show trida happy at left
    trida "Really…? Well… I didn't really do anything special, but… I'm glad it helped you… somehow!"

    n "Trida's happy disbelief made the atmosphere feel breathable. The boy nodded briefly before looking back at you."
    glasses_boy "Oh, and… thank you for keeping us in check."
    p "It's nothing, I'm glad you two could talk it out."
    trida "Yeah, I feel much better…"

    glasses_boy "Uhm, if you don't mind, I'm getting a little… hungry, I'll see you two later."
    hide glasses_boy with dissolve
    n "The boy hurriedly excused himself, reminding both of you that it was still break period. Trida perked up at the mention of hunger, and you realize that your stomach has been grumbling as well."

    trida "See ya…!"
    p "Now that he mentioned it… let's get some food."
    trida "My thoughts exactly! Come on, I'm starving!"

    hide trida with dissolve
    n "You stood up from your seat, knowing Trida would immediately drag you away from class."
    n "They reach for your wrist and run out into the hallway with you, their eyes still glued to their phone as they lead you out with little caution."
    p "Couldn't you afford to look at the road a little…"
    trida "Wait, this new Splashy banner…!"

    # ==============================================================================
    # CANTEEN SCENE
    # ==============================================================================
    scene bg teddy_cup
    with fade

    n "Trida leads you to the lively canteen. Although not without bumping into at least one other student, they swiftly pocketed their phone and approached the noodle stall."
    show trida happy at center with dissolve
    trida "I'll have one of the Aceh fried noodles with an egg on the side!"
    n "All it took was one look at Trida's enthusiastic ordering before the lady running the stall was already up and ready to cook."
    n "You sit down on a nearby bench and lean back as Trida shifts back and forth in anticipation."

    p "Do you have that order on speed-dial or something? The lady barely looked at you."
    show trida smile at center
    trida "Hah, what can I say? If this was a Teddy Cups stall, I would have so many loyalty cards filled to the brim by now!"
    p "Right…"

    show trida surprised at center
    n "Before you could settle on your lunch order, you notice Trida's hands confusedly rummaging through their tight pockets with a perplexed look."
    trida "Crap! I think I forgot—no, I definitely forgot my wallet!"
    p "How shocking…"
    trida "Don't go anywhere, alright?"

    hide trida with dissolve
    n "Hushed like a secret, Trida proceeded to sprint out of the crowd like a leaf through wind, until they had left your sight toward the hallways."
    n "You're left to sit with yourself as you wait for Trida's noodle order on their behalf."

    show julia smile at center with dissolve
    julia "Oh, hey [player_name]! It's been a while!"
    n "Julia greeted you with a little more excitement than what you would've expected from someone as initially reserved as her."
    n "She made her way to the empty space beside you and sat down."
    julia "Uhm, how are you doing these days…? You know, with all the new school life?"

    menu:
        "It's been a bit much…":
            julia "Yeah, I get that… So much to get used to, right…?"
        "I've been having fun!":
            julia "Ah, that's good to hear…! Everyone is so nice here, aren't they?"
        "I'm doing just alright":
            julia "I see, better than terrible I suppose…!"

    julia "Well, me personally, I'm looking forward to next month, you know, with Inktober and all of that… I see you've been getting close with Trida as well…"
    n "Julia trails off with her words about Trida as a thoughtful silence follows, her gaze set on her shoes."

    p "Yeah, what about me and Trida?"
    julia "Oh, it's just… to be frank, I've been noticing you and Trida becoming closer for quite a while now."
    julia "You guys seem to make a great pair. Seeing you two have fun always brings up the mood, and I can't imagine the two of you ever separating, so I was just wondering…"

    n "Julia suddenly turns toward you and holds eye contact, an uncharacteristic but sincere, determined look on her face."
    julia "Perhaps this is a bit too direct, but if you don't mind being honest with me for a second…"
    julia "…Who is Trida to you, [player_name]?"

    menu:
        "Someone… I want to be more than friends with":
            $ tridaAffection += 2
            n "You stutter out your honest feelings, thinking back to how many times the small moments with Trida have made your heart race."
            n "Everything from the funny moments, the tender moments, the emotional Saturday night in your room… all culminating into a first admission of your feelings for Trida to Julia."
            julia "I see…"
            n "Julia smiles to herself upon hearing your confession, sighing quietly in relief."
            p "…What? Don't go around telling people."
            julia "Oh, of course not! You see… I had a feeling you'd say that. From what I've observed, the way you look at Trida is simply unmistakable…!"
            julia "If I may admit something too, I've had a few romantic escapades with my own friends in the past, so I understand you must be feeling very conflicted."
            p "Oh! Well… yeah, but I wouldn't have expected that from you."
            julia "Ah, yes, it's a long story, but—that's beside the point. If you'll let me, I want to throw in my two cents. Some advice, if you will."
            julia "Because… I truly think you and Trida can become something special."
            p "Yeah, I'd appreciate that…"
            julia "This is just a bit of speculation, but I think Trida is most comfortable when they're around you."
            julia "They're always smiling around everyone, sure, but it simply comes naturally with you."
            julia "I think Trida appreciates how patient and understanding you are; they feel like an equal instead of someone to constantly appeal to."
            julia "As long as you remain that safe space for Trida, I don't think it's out of the realm of possibility that…"
            julia "…Trida feels the same way about you."
            p "You… really think so?"
            julia "Well, that's just how I see it. I'd be very surprised if Trida felt any other way, especially with the way they look at you."
            julia "Besides, you'd make an amazing partner for Trida anyway."

        "A close friend I trust a lot":
            $ tridaAffection += 1
            julia "I see… I can really see that Trida is important to you."
            julia "Maybe this is an odd thing to say about someone else's friendship, but I have a feeling you two will always have each other's backs until the end."
            n "Julia's thoughtful words felt unexpected from someone like her, but you couldn't deny her pleased expression and tone of voice."
            p "Yeah? How could you tell…?"
            julia "I'd say you two bring out the best in each other; you seem the most comfortable at school when together."
            julia "I mean, Trida is always the social butterfly, but they seem to mellow out when talking with you. It's when their true personality really shines."
            julia "Dare I say your personalities complement each other perfectly."
            julia "I suppose what I'm saying is… don't ever let go of Trida, alright?"
            p "Thank you, Julia… I'm glad you think so."
            julia "It's nothing, just looking out for you two!"

    n "It was then you heard loud pants and footsteps approaching from behind."
    show julia smile at left with ease
    show trida happy at right with dissolve
    trida "I'm back!!"
    n "Trida's announcement pierced through the ambiance of the crowd as they came running towards you, flailing the acquired wallet in their hand like a gold medal."
    n "Within barely a second, Trida speeded past you and Julia, bent over gasping for air as they counted the bills in their hand."

    p "Speak of the devil…"
    julia "I reckon you'd like to keep our discussions a secret, yes?"
    n "Julia chuckled with a glint in her eyes, her knowing grin playfully teasing your embarrassment."

    n "Trida soon arrived at your bench with a styrofoam box abundant with fried noodles and a sizable sunny-side-up egg."
    show trida smile at right
    trida "Sorry for the wait, guys! I swear I did {i}not{/i} recall my wallet being under my table of all places—"
    trida "Eh, Julia? Hey, Julia! Didn't realize you were here too!"
    julia "Ah, hey, Trida…! It's been a while since we talked, right?"
    trida "Oh, totally!"

    n "You could already see the gears revving up in Trida's head upon talking to a fellow nerd, their smile widening with energy."
    trida "You know, I watched that Nimecart series you told me about! Ah, what was it called—the Sanity one?"
    julia "Oh! You actually watched it? What did you think of it?"
    trida "It's SO fun! The storytelling is so cool, and all of the members are really good improvisers—I'm really curious how it's gonna go for future episodes!"
    julia "Right? The world-building is subtle, but still so effective. Oh, I could go on, but—wait, who's your favorite, Trida?"
    trida "Oh man, they all have really interesting storylines…"

    n "You continue to quietly observe Trida and Julia's excited yapping that goes on for longer than expected."
    n "This was the most natural you've seen Julia be, and you once again admire Trida's bright energy that effortlessly puts people at ease."
    n "You enjoy the laughs and opinions exchanged, soaking in the positive vibes."

    trida "Oh—actually, reminds me… What were you and [player_name] talking about earlier anyway?"

    menu:
        "Nothing important":
            p "We were just chatting about nothing in particular."
            trida "And why do I find that hard to believe, hm? You two seem a little less awkward now."
            julia "Heh…"
            trida "And that laugh isn't convincing either!"
        "About Nimecart":
            p "Julia was just talking to me about Nimecart."
            trida "Huh, wouldn't have thought of you as a Nimecart type of person."
            trida "Tell me something about the series then!"
            p "Uhm… the, uh… Insanity series is—"
            trida "Pfft, you couldn't even get the name of it right!"
            julia "Heheh…"
        "About how slow you were":
            p "Ah, we were just agonizingly waiting for you to come back with your wallet."
            show trida annoyed at right
            trida "HEY! Didn't you see how fast I was sprinting?!"
            p "No amount of sprinting could save how slow your eyes are."
            trida "I REALLY couldn't tell where it was for the life of me!"
            julia "Ehehe…"

    show trida smile at right
    n "The three of you laugh together around the warm smell of noodles and canteen chatter."
    n "As the lunch bell approaches, you look at Trida—happier, lighter, and closer to you than ever before."

    # End of Week 9
    return
