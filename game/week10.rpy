# ==============================================================================
# PROJECT YOUTH - WEEK 10 (FINALE & ENDINGS)
# ==============================================================================

label week10_start:
    $ current_week = "Week 10"
    if trida_route == "romance" and tridaAffection >= TRIDA_ROMANCE_THRESHOLD:
        jump week10_romance
    elif tridaAffection >= TRIDA_ROMANCE_THRESHOLD and trida_route != "friendship":
        jump week10_romance
    else:
        jump week10_friendship


# ==============================================================================
# WEEK 10: ROMANCE ROUTE (Rooftop Confession)
# ==============================================================================

label week10_romance:
    scene bg teddy_cup
    with dissolve_scene_full
    play music audio.t4 fadein 1.5 loop volume 0.7

    show trida uniform happy at center with dissolve
    p "Lucky that you've finished all of your assignments. I still need to finish up everything for my presentation…"
    trida "Don't worry, I'll be waiting here for you!"
    p "Are you really fine with that? I'm gonna be gone for a while, you know."
    trida "Don't sweat it! I was planning on staying a bit longer at school anyway. I can keep myself entertained!"
    show trida uniform smile at center, hop
    trida "Oh, good luck with that, by the way! Your character model looks great!"
    p "I have you to thank for that, you know. I don't know how your tweaks made sense, but they just did."
    trida "They make plenty of sense! I'd say my explanation was pretty detailed!"
    p "Detailed doesn't mean understandable…"
    p "Well, I'm running late. Talk to you later, Trida."
    trida "See ya, [player_name]…!"

    hide trida with dissolve
    n "Your figure retreated toward the school building, leaving Trida alone with their thoughts."
    n "Thoughts that immediately drifted to wanting to spend just a little more time with you… to feel your warmth in the quiet, mundane moments of the day, and to make you smile."

    show trida uniform embarrassed at center, dip with dissolve
    trida "Oh, you…"
    n "Trida let out a shaky sigh, their heart racing with fluttering fondness as their ears warmed beneath messy brown hair."
    n "They stared down at the iced tea in their hands, watching condensation drip along the plastic cup as their fingers fidgeted with the straw."

    show trida uniform embarrassed at center, panic
    trida "It's—agh—it's fine, I'm fine! Just… just tell them! Just tell them, and if… if they leave…"
    trida "No—no, forget that! What do I even say?! Gosh…"

    n "Trida ended their endless murmuring with a quiet whine, their anxiety spiking as they realized how completely new this territory was."
    n "Checking their phone, they saw there were still a few hours before you would finish."
    n "They needed a plan. A plan from someone who had actually done this before."

    scene bg corridor
    with dissolve_scene_full
    play music audio.t5 fadein 1.5 loop volume 0.7

    n "With a sense of terrified determination, Trida sprinted through the hallway toward the second-floor classrooms."
    n "Peeking through one of the windows, Trida spotted two familiar classmates sitting together with controllers in hand, absorbed in a video game on a shared laptop."

    show trida uniform happy at left with dissolve
    trida "Hizbul! Ilham!"

    show ilham neutral at right with dissolve
    show hizbul neutral at center with dissolve

    ilham "Jeez! I swear, I thought you were a teacher for a second!"
    show trida uniform embarrassed at left, dip
    trida "Sorry, sorry! I got a little loud."
    ilham "Pfft, a little? I think you woke up some sleepyheads in the back row."
    show hizbul smile at center
    hizbul "Well, we just started the match. Wanna join, Trida?"
    trida "Er, that'd be fun, but—"
    ilham "Come on, we haven't played a round with you in a while, Triguy! We have time to kill."
    trida "O-Okay, I get it! I'll play the next round, but that's not what I'm here for! It's…"
    show trida uniform neutral at left
    trida "I actually wanna… ask you guys about something, if that's alright."
    ilham "Oh, right. What's on your mind?"
    trida "Uhm… it's not that big of a deal, really. I just need—just a small piece of advice!"
    hizbul "Alright… Yeah, we'll try to help. What is it?"
    show trida uniform embarrassed at left, panic
    trida "Okay, yeah, but—you two need to promise me that you won't tell anyone at ALL, got it?!"
    hizbul "So it's 'not a big deal' but it's a huge secret we have to keep?"
    ilham "Also pretty hard to keep a secret when you're louder than the whole room."
    trida "Agh, it's just… I-I don't know how to say this…"
    hizbul "Take your time, Trida. Collect your thoughts a little."

    n "Trida's hands gravitated toward their pockets, fidgeting nervously with the fabric while staring down at the floor."
    trida "…You guys know [player_name], right?"
    hizbul "Yeah, you're usually around [player_name]. What about them?"
    trida "Uhm… this might be a surprise, but…"
    ilham "Gosh, just tell us already."
    hizbul "Ilham…!"
    show trida uniform blush at left, dip
    trida "I…"
    trida "…I have a huge crush on [player_name]!"
    trida "T-There, I said it!"

    n "Hizbul and Ilham exchanged an amused look, completely unsurprised."
    ilham "Oh right, act surprised—"
    show ilham smile at right
    ilham "Woah, really? I would have never guessed!"
    show hizbul smile at center
    hizbul "Ye-yeah, that's really… really shocking!"
    show trida uniform embarrassed at left, hop
    trida "Now you're just messing with me…!"
    trida "C-Come on, there's no way it was THAT obvious, was it?"
    ilham "Yeah, buddy, real subtle."
    hizbul "I mean, there were definitely signs."
    trida "It can't just be because I'm around them all the time! You two stick together constantly and nobody bats an eye!"
    ilham "Well, unlike you and [player_name], me and Hizbul aren't spending every waking breath together, are we?"
    hizbul "Hah, you'd get tired of me so quickly."
    ilham "God forbid, I don't even want to imagine it."
    show trida uniform embarrassed at left, dip
    trida "Uh—I-I guess I do follow [player_name] around pretty often… even walking home together…"
    hizbul "You also look way more relaxed around them. I don't know if you've noticed, but you tense up really easily, even around us."
    hizbul "Around them, you're more… yourself. You smile more, without worrying about keeping up appearances."
    ilham "You do look completely different around [player_name] compared to anyone else."
    show trida uniform smile at left with dissolve
    trida "I see now…"
    trida "Yeah… I-I think that's one of the things I love about [player_name] the most."
    trida "Like—I can always open up to [player_name] and speak my mind. They always seem to know what to say. It makes me feel calm."
    trida "[player_name] is just… the sweetest person I've met. Whenever they laugh or smile at a joke I make, I just want to make them even happier!"
    show trida uniform embarrassed at left, panic
    trida "And—whenever they get close, my mind just goes completely blank, and I end up acting totally lame in front of them!"
    hizbul "Yeah, I get it, Trida…"
    ilham "I didn't think someone could look like they're both deeply in love and actively having a panic attack at the exact same time."
    hizbul "Ilham…"
    trida "Ah! I was yapping again, sorry…"
    show trida uniform neutral at left
    trida "But like I said, I need some advice. I kinda thought, 'screw it, no better time than now.' I'm gonna confess to [player_name] in a few hours."
    hizbul "Wait, what? That soon?"
    trida "Yeah! They finish their work in about three hours. And you guys are in the public speaking club, right? I figured you'd know a thing or two about words!"
    ilham "Why ask us? Don't look at me, Hizbul's the only one with actual dating experience."
    show trida uniform happy at left, hop
    trida "Oh wow! You do? Tell me everything, Hizbul!"
    hizbul "Okay, don't get too excited, I've only had one partner. But look, just be genuine. Explain how you feel clearly."
    hizbul "Maybe invite them somewhere nice first so you can ease into it."
    ilham "The rooftop above the cafe has a killer view of the sunset, especially around this hour."
    show trida uniform surprised at left
    trida "Wait, there's a rooftop you can get to?!"
    ilham "Yeah, take the back stairs up to the top floor of the cafe building. It overlooks the whole campus."

    n "Ilham tore a piece of paper from his notebook and scribbled a quick map."
    ilham "Here, follow this. And write down a few bullet points of what you want to say so you don't freeze up."
    show trida uniform happy at left, hop
    $ mapAcquired = True
    trida "Thank you guys so much! You're lifesavers!"
    hizbul "Good luck, Trida! Hope it goes smoothly!"
    ilham "Let us know how it goes down, yeah?"

    hide trida
    hide hizbul
    hide ilham
    with dissolve

    scene bg rus_studio
    with dissolve_scene_full
    play music audio.t3 fadein 1.5 loop volume 0.7

    n "Back in the 3D Computer Lab, you finally leaned back into your office chair with a long, bone-deep stretch."
    n "After hours of relentless tweaking, the final render was exported and safely uploaded to the cloud folder."
    n "Your throat felt bone-dry from the air-conditioned lab, and fatigue weighed heavily on your shoulders as you packed your bag and headed toward the exit."

    scene bg gates_morning
    with dissolve_scene_full
    play music audio.t4 fadein 1.5 loop volume 0.7

    n "As soon as you pushed through the building doors, you spotted Trida jogging toward you, holding an iced tea in one hand and a chocolate chip cookie in the other."
    show trida uniform happy at to_center with dissolve
    trida "[player_name]…!!!"
    p "Hey… you're still here?"
    trida "Of course! I told you I'd wait!"
    show trida uniform smile at center
    trida "You look completely exhausted, though. Here—I brought you a drink and a cookie from the stall!"
    p "Thanks… you're a lifesaver, Trida."

    scene bg teddy_cup
    with dissolve_scene_full
    play music audio.t6 fadein 1.5 loop volume 0.7

    n "The two of you walked over to the spacious school cafe area and sank onto the cushioned sofa."
    n "You took a long, refreshing sip of the sweet iced tea, letting the cold drink revive your exhausted senses."
    show trida uniform smile at center with dissolve
    trida "Better now?"
    p "Way better. Thanks for waiting for me, really."
    show trida uniform neutral at center, sway
    trida "Uhm… if you aren't too tired… there's something really cool I want to show you in this building."
    p "Huh? What's the occasion?"
    trida "Think of it as a reward for finishing your project! I promise it'll be worth the stairs."
    p "It better be as cool as you're hyping it up to be."
    show trida uniform happy at center, hop
    trida "No doubt about it! Ready when you are!"

    scene bg corridor
    with dissolve_scene_full
    play music audio.t2 fadein 1.5 loop volume 0.7

    n "Trida led you up the flights of stairs toward the top floor of the building, checking a small handwritten map tucked in their palm."
    p "Are you sure you know where you're going?"
    show trida uniform happy at center with dissolve
    trida "I'm your pirate captain leading you to the treasure! Trust me!"
    p "I guess it really does feel like a treasure hunt…"

    scene bg residential
    with dissolve_scene_full
    play music audio.t8 fadein 1.5 loop volume 0.7

    n "Pushing past the final doorway, you stepped out onto a wide, open rooftop."
    n "The evening sky stretched endlessly before you, painted in a breathtaking gradient of amber gold, vivid rose, and soft indigo."
    n "A cool, gentle breeze swept across the open space, carrying the faint murmur of the campus below."

    show trida uniform happy at center with dissolve
    trida "Ta-da!! The super secret rooftop!"

    menu:
        "It's really nice…":
            $ tridaAffection += 1
            p "It's really nice up here… The sky looks gorgeous, and the breeze feels amazing."
            show trida uniform smile at center, sway
            trida "I know, right? I felt like you needed to see this after spending all day inside."
        "This is pretty high up…":
            $ tridaAffection += 1
            p "This is pretty high up. You can see the whole school from here."
            show trida uniform smile at center, hop
            trida "Right? Feels like you're standing on top of the world!"
        "Secret?":
            $ tridaAffection += 1
            p "So is this a place we're actually allowed to be in? Not much of a secret if we get caught."
            show trida uniform embarrassed at center, dip
            trida "Wha—no, it's totally safe! Ilham told me about it. As long as you're careful, it's fine!"
            p "…Fair enough. It really is a nice spot."

    n "You leaned against the railing, taking in the tranquil beauty of the dusk."
    n "Beside you, Trida grew unusually quiet. Their fingers nervously tapped against their pockets, breath hitching as they gathered their resolve."

    show trida uniform neutral at center with dissolve
    trida "Uhm… [player_name]?"
    p "Yeah? Everything okay?"
    show trida uniform embarrassed at center, dip
    trida "I've… I've actually been meaning to tell you something really, really important."
    trida "That's why I wanted us to come up here."
    p "What is it, Trida? You don't have to beat around the bush."

    show trida uniform blush at center with dissolve
    trida "Listen… I know we've only known each other for a few months."
    trida "But it feels like it's been forever. Like… we were destined to meet, or something like that."
    trida "You've always been there for me. Even when I'm being an anxious mess, you always know what to say. You make me feel safe."
    trida "And lately… I've started noticing all these little things."
    trida "How much I laugh when I'm around you… how my heart starts racing every time you're close… how much I wish our walks together would never end."

    n "Trida took a deep, trembling breath, their cheeks flushing crimson under the warm sunset glow."
    show trida uniform blush at center, hop
    trida "The point is… I really, really like you!!"
    trida "I have a huge crush on you, [player_name]!"
    trida "I'm sorry for keeping it inside for so long… I was just so scared of ruining what we have."
    trida "Do you… do you feel anything like that for me too?"

    menu:
        "I love you too!":
            jump week10_romance_good
        "I want to stay friends":
            jump week10_romance_friendship
        "Why would you say that?":
            jump week10_romance_bad

# ------------------------------------------------------------------------------
# Romance Branch A: Good Ending (Mutual Love)
# ------------------------------------------------------------------------------
label week10_romance_good:
    $ tridaAffection += 5
    play music audio.t8 fadein 1.5 loop volume 0.7

    p "I never thought you'd say it first… but to be honest, Trida… I love you too."
    show trida uniform surprised at center with dissolve
    trida "Wait—really…?"
    p "Of course I do! I've had feelings for you for a while now."
    p "Your smile lights up every room you walk into, and your energy is completely contagious."
    p "I admire your passion, your resilience, and how much you care about everyone around you."
    p "When my heart started skipping beats every time you leaned in… that's when I knew I wanted to be more than just friends."

    n "Trida stood frozen, tears glistening in their orange eyes even as a radiant, tearful smile broke across their face."
    show trida uniform happy at center, hop with dissolve
    trida "I'm… I'm so happy. I really didn't think you'd feel the same way…"
    p "I do. Entirely."
    trida "Does that mean… we're together now?"
    p "I certainly hope so."

    n "Under the brilliant glow of the evening sky, you pulled Trida into a warm embrace."
    n "Trida buried their face against your shoulder, laughing through happy tears as their arms wrapped tightly around you."
    trida "I love you, [player_name]… so much."

    hide trida with dissolve
    scene black with dissolve_scene_full
    play music audio.tcredits fadein 2.0 loop volume 0.7

    n "As the sun set over SMK Raden Umar Said, a brand new chapter began."
    n "Not just as classmates, but as two hearts moving forward together."
    n "{b}— ROMANCE ROUTE: TRUE ENDING —{/b}"

    $ debug_auto_skip = False
    $ config.skipping = None
    return

# ------------------------------------------------------------------------------
# Romance Branch B: Friendship Ending (Gentle Letdown)
# ------------------------------------------------------------------------------
label week10_romance_friendship:
    play music audio.t6 fadein 1.5 loop volume 0.7

    p "Trida… thank you for telling me. It means a lot that you trust me that much."
    p "I really care about you, but… right now, I value our friendship more than anything. I want us to stay best friends."
    show trida uniform smile at center with dissolve
    trida "Ah… don't worry, I completely get it!"
    trida "I just really needed to get it off my chest. But we're staying friends, right?"
    p "Always. You're my best friend, Trida."
    show trida uniform happy at center, hop with dissolve
    trida "That just means we'll stay the best dynamic duo in the school! Deal!"

    hide trida with dissolve
    scene black with dissolve_scene_full
    play music audio.tcredits fadein 2.0 loop volume 0.7

    n "Even without romance, the bond you built with Trida remained unshakable."
    n "A friendship forged in laughter, late-night renders, and unconditional trust."
    n "{b}— FRIENDSHIP ENDING —{/b}"

    $ debug_auto_skip = False
    $ config.skipping = None
    return

# ------------------------------------------------------------------------------
# Romance Branch C: Bad Ending (Harsh Rejection)
# ------------------------------------------------------------------------------
label week10_romance_bad:
    play music audio.t9 fadein 1.5 loop volume 0.7

    p "Why… why would you say something like that?"
    show trida uniform surprised at center, panic with dissolve
    trida "H-Huh?"
    p "We can't just stay friends like this with feelings in the way. It's better if we keep our distance."
    show trida uniform sad at center, dip with dissolve
    trida "W-What do you mean? If you don't like me back, that's fine, but why stop being friends?!"
    p "Because it'll just hurt more down the line. I'm sorry, Trida."

    n "You turned around and walked toward the stairwell, leaving Trida alone on the windy rooftop."
    n "Behind you, the quiet, broken sobs of your once-brightest friend echoed against the twilight chill."

    hide trida with dissolve
    scene black with dissolve_scene_full
    play music audio.tcredits fadein 2.0 loop volume 0.7

    n "Some words, once spoken, can never be taken back."
    n "{b}— BAD ENDING —{/b}"

    $ debug_auto_skip = False
    $ config.skipping = None
    return

# ==============================================================================
# WEEK 10: FRIENDSHIP ROUTE (A Close Friend I Trust A Lot)
# ==============================================================================

label week10_friendship:
    scene bg gates_morning
    with dissolve_scene_full
    play music audio.t6 fadein 1.5 loop volume 0.7

    n "Under the blazing saffron sunset, you and Trida took slow, leisurely strides side by side toward the boarding house."
    n "Plastic bags carrying dinner boxes gently swayed with your steps, accompanied by the distant rumble of evening traffic."

    show trida casual happy at center with dissolve
    trida "Hngh… Ahh, long day, eh? Man, I haven't even finished all of my assignments!"
    p "At least we got the hardest parts done. Better than nothing—we can relax a bit tonight."
    show trida casual smile at center, hop
    trida "For sure! Though I think I still have some energy left. I might just finish the whole week's work tonight!"
    p "I seriously wish I had your stamina sometimes…"
    trida "Hey, that's why I ask to walk everywhere with you! It's good to get some movement in! Helps with endurance."
    p "Helps when you're enduring slow-paced games like Goblin/Goobers, I'm sure."
    show trida casual embarrassed at center, dip
    trida "Alright, don't talk bad about GG like that! You haven't even played it!"
    p "Didn't you tell me the story was slow even for you?"
    trida "Well, you don't need endurance when the plot gets this good! Especially if you pick the Goobers' storyline!"

    n "Trida launched into an impassioned, animated explanation of the game's lore."
    n "Their words flowed with genuine enthusiasm, bringing color to the quiet sidewalk as the sunset bathed their features in honey-magenta light."

    trida "Ooh, I'm curious about something!"
    show trida casual smile at center with dissolve
    trida "[player_name], just from what I told you, which storyline would you have picked?"

    menu:
        "The Goobers":
            $ tridaAffection += 1
            p "The Goobers. The story sounds interesting, and I wouldn't mind a slower pace for an immersive narrative."
            show trida casual happy at center, hop
            trida "I see! I'm on the same boat as you! The harder the grind, the better it feels when you reach a big plot point!"
        "The Goblins":
            $ tridaAffection += 1
            p "The Goblins. Good gameplay and mechanics are what make a game truly enjoyable to play."
            show trida casual smile at center, sway
            trida "I had a feeling you'd say that! You seem like a gameplay-first type of player!"
        "Both":
            $ tridaAffection += 1
            p "I'd play both, honestly."
            show trida casual smile at center, sway
            trida "Hm… completionist, huh? Or are you just saying that because you weren't fully listening?"
            p "Well…"
            show trida casual happy at center, hop
            trida "Busted! Haha, it's alright!"

    n "Trida fell into a comfortable, quiet rhythm beside you, looking up at the scattered clouds as the dusk deepened."
    p "You know, Trida… it really doesn't feel like it's been three months since we started school, does it?"
    show trida casual surprised at center
    trida "Woah, now that you say that… July, August, September… It's already September!"
    trida "It went by so fast, but it also feels like we've known each other forever."
    p "It's been really comfortable having you around."
    show trida casual smile at center with dissolve
    trida "Exactly! I've never felt so at home at school before. I'm really glad we became friends, [player_name]."

    scene bg room
    with dissolve_scene_full
    play music audio.t10 fadein 1.5 loop volume 0.7

    n "Arriving at the boarding house, the two of you settled into the quiet lounge chairs with your warm dinner boxes."
    n "The savory scent of barbecue fried chicken and chicken katsu rice filled the cozy room."

    show trida casual happy at center with dissolve
    trida "Come on, eat up before it gets cold! Weren't you starving earlier?"
    p "Right on it."

    n "Trida took a huge bite of their rice bowl, immediately choking on the sudden mouthful."
    show trida casual embarrassed at center, panic
    trida "*COUGH* *COUGH* Ow—water—!"
    p "Here, take mine. Slow down!"
    n "You handed over your water bottle, watching Trida chug it down with frantic relief."
    show trida casual smile at center with dissolve
    trida "Phew… thanks. Paramedic of the year right there."
    p "Speaking of extracurriculars, actually, how's theatre practice treating you?"
    trida "Theatre? It's been a blast! They recommended me for the aloof comedic relief role."
    p "That sounds like a role tailored specifically for you."
    trida "Hey! I'll take that as a compliment!"
    trida "What about you? Did you do any club activities today?"

    menu:
        "I'm not in any extracurriculars":
            p "Eh, I decided not to join any clubs for now. Don't want things getting too hectic."
            show trida casual smile at center
            trida "Good point! School work is already plenty on its own."
        "Not today, but a different day":
            p "I joined filmmaking, but our meetings are on different days."
            show trida casual happy at center, hop
            trida "Woah, filmmaking! If you ever need an actor for a scene, you know who to call!"
            p "I'll keep your audition tape on file, Trida."
        "I did":
            p "I had public speaking earlier. We did debate practice."
            show trida casual smile at center, sway
            trida "Debate? Like that lawyer game you always watch me play?"
            p "Pretty much, yeah."

    n "The conversation slowed into a comfortable stillness as you finished your meals."
    n "Trida set their empty box on the coffee table, their playful expression softening into something sincere and grounded."

    show trida casual neutral at center with dissolve
    trida "[player_name]… I just wanted to say thank you."
    p "For what?"
    trida "For everything these past few weeks. When that group project fell apart and I felt like a total failure…"
    trida "You didn't judge me. You didn't get tired of my panicking. You listened to me and reminded me that I'm not useless."
    show trida casual smile at center with dissolve
    trida "I always felt like I had to be the loud, funny one so people wouldn't get bored of me. But with you, I don't have to pretend."
    trida "You're the best friend I could have ever asked for in this school."
    p "There's no need to thank me, Trida. You bring so much to the table yourself."
    p "Your…"

    menu:
        "Your positivity":
            $ tridaAffection += 1
            p "Your positivity. You make every room you walk into brighter just by being yourself."
            show trida casual happy at center, hop
            trida "You really think so? Thank you… that means the world to me."
        "Your resilience":
            $ tridaAffection += 1
            p "Your resilience. No matter how tough things get, you always pick yourself back up and keep trying."
            show trida casual smile at center, sway
            trida "I try my best! Having someone like you cheering me on makes it way easier."
        "Your passion":
            $ tridaAffection += 1
            p "Your passion. Your boundless curiosity for 3D art, games, and storytelling is genuinely contagious."
            show trida casual smile at center with dissolve
            trida "Hehe… I guess I do get a little carried away, don't I? But I'm glad you enjoy it."

    n "Trida leaned back into the armchair, a peaceful, contented smile gracing their features."
    trida "My goal… is to make games and animations that bring people the same joy and comfort that stories gave me."
    trida "And having a friend like you walking beside me… makes me feel like I can actually achieve it."
    p "I know you will, Trida. We've got plenty of time ahead of us."

    hide trida with dissolve
    scene black with dissolve_scene_full
    play music audio.tcredits fadein 2.0 loop volume 0.7

    n "Surrounded by the comforting hum of the evening, you shared a quiet laugh with your closest companion."
    n "No matter what challenges the school year would bring, you knew you would face them together."
    n "{b}— FRIENDSHIP ROUTE: TRUE ENDING —{/b}"

    $ debug_auto_skip = False
    $ config.skipping = None
    return
