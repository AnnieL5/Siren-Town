define bl = Character('Bai Liu', color="#aaffcc")
define lucy = Character('Lucy', color="#ff99cc")
define andre = Character('Andre', color="#99aaff")
define jelf = Character('Jelf', color="#ccccff")
define driver = Character("Driver", color="#0000")
define fd = Character("Front desk")
define mermaid = Character("Mermaid")
define s = Character("Siren King", color="#ffcc99")
define board = Character("Board", color="#ffcc99")


label start:
    scene bg 1 11

    "You are Bai Liu. Bai Liu woke up and found himself sitting in the back seat of a car. The interior was cramped, and the worn seatbacks reeked of cigarette smoke. Streams of water streamed down the windows, and through the glass he could vaguely see the gentle drizzle of rain outside. The sky was dim, and he couldn't tell whether it was dusk or night. A faint, unpleasant smell of salted fish lingered in his nostrils."

    "Before him floated a panel, with the words ――【Game Instructions】 written on it."

    "Bai Liu frowned."

    bl "Where is this? Why is he here? And what is this panel?"

    "The panel seemed able to sense the doubts in his heart, and answers appeared on it one by one."

    board "【You are in a deadly game, and the reason you are here is because we detected that after losing your job, you developed an overwhelming desire for money—so strong that it met the conditions for the game to begin】"

    board "【Clearing the game will earn you points, and points can be exchanged for money and anything else you desire】"

    bl "What kind of game is this? What do I have to do to clear it and get the points you mentioned?"

    board "【This is a horror survival game, filled with ghosts, serial killers, and unimaginable beings. What you must do is find their weaknesses, complete the storyline of the entire game instance, and survive their pursuit】"

    board "【Loading game instance….. Load complete】"

    board "【Game Instance Title: 《Siren Town》】\n【Level: Level One (Games with a player mortality rate below 50\% are classified as Level One)】\n【Mode: Single-player mode】\n【Overview: This is a thrilling game combining action and puzzle-solving, very popular among players, but it doesn’t seem very friendly to newcomers—the newcomer death rate is extremely high】"
     
    scene bg 1 12

    "Bai Liu was lying sideways in the last row of a van. It was cramped and narrow, and even turning over was difficult. When he moved, he noticed a necklace slipping down from his neck. His clothes, however, were exactly the same as before he entered the game—white shirt, black trousers, the typical daily attire of an office worker. The only new thing was this necklace."

    "The pendant on the necklace was a one-yuan coin with a hole punched through it. As soon as Bai Liu placed his hand on it, sure enough, the game panel popped up. The panel was the same as before, with no additional information."

    "Bai Liu poked his head out from the back seat. This was a seven-seater van. Aside from Bai Liu lying in the back row, there were four other people in front. As soon as he looked out, someone turned toward him in surprise:"

    scene bg 1 13

    lucy "Bai Liu, hey, my little sweetheart, you’re finally awake!"

    "Besides Bai Liu, the six others clearly all had foreign appearances. The one who called Bai Liu ‘sweetheart’ was a girl with long brown curly waves, red lips, and brown eyes. She wore hot pants and a camisole. The moment Bai Liu saw this person, the coin on his chest triggered the panel, and character information appeared:"

    board "【NPC Name: Lucy】\n【Character Info: Your classmate, she really likes boys of your type. Last night, you attempted a sexual encounter, but faced with Lucy—who is ten centimeters taller than you and far more passionate and bold—you were too shy, so it didn’t succeed (lol).】"

    "It seemed that in this game, the NPC panel information was only triggered when the player actually looked at the NPC—just like in online games where hovering the mouse reveals details. The player’s eyes now served as both the mouse and the game controller."

    "He pondered for a moment. It seemed that in this game, losing one’s eyesight would at least be fatal."

    lucy "Lucy winked playfully at Bai Liu: “Hey, baby, was it me who wore you out? You’ve been sleeping ever since we got in the car.”"

    bl "Quickly changing the subject, Bai Liu glanced at the increasingly desolate, cold scenery outside the window and asked: “Where exactly are we going? Why does it look so remote?”"

    andre "“Looks like the coward is thinking of bailing again.”"

    "A deep, mocking voice came from the front. A tall man in tight jeans and a sports T-shirt crossed his arms and looked at Bai Liu with contempt. His muscular build stretched his shirt to the point of nearly bursting, making him resemble an American football player."

    andre "Towering over him with arms crossed, he sneered at Bai Liu, “Too late, Bai Liu. Even if a coward like you wants to back out, we’re already on the road to Siren Town.”"

    board "【NPC Name: Andre】\n【Character Info: Your love rival. He likes Lucy but was rejected by her, and he harbors strong hostility toward you. Previously, you made a bet with him that you would protect Lucy in the most dangerous place in the world to prove your love for her. That’s why your group drove to Siren Town. But because of your cowardice, you cried bitterly before getting in the car, regretted it, and didn’t want to come. He forcibly dragged you into the car.】"

    menu:
        "“Siren Town, what kind of place is it?”":
            bl "Bai Liu had already seen the name Siren Town twice in a row. Ignoring Andre’s mockery, he asked: “Siren Town, what kind of place is it?”"
            jump siren_info
        "...":
            jump second

label siren_info: 
    scene bg siren 12

    "Andrei gave another cold snort. Just as he was about to continue mocking Bai Liu, a rambling, incessant murmur interrupted his sneer:"

    jelf "“Siren Town, the only seaside town in history where remains of sea monsters have ever been discovered. Many people throughout history claimed they saw sirens here, or heard the beautiful songs of mermaids echoing in the waves. Some even witnessed these strange-looking merfolk feasting on human corpses atop the pitch-black reefs….”"

    andre "“Jelf! Those are nothing but stories Siren Town made up to trick tourists into visiting!”"

    "Andrei impatiently cut off the other’s rapid whispering, but a flash of fear still crossed his face."

    jelf "A small boy wearing thick beer-bottle-bottom glasses hugged the book in his arms and shrank back, seeming somewhat afraid of Andrei. In a lower voice, he retorted:"

    jelf "“Then how do you explain the mysterious disappearances of those tourists who came to Siren Town? Just last month, twelve tourists came and vanished completely! The police searched everywhere, but no one ever saw them leave Siren Town….”"

    board "【NPC Name: Jelf】\n【Character Profile: An avid enthusiast of mermaids, sea monsters, and other supernatural creatures. Upon learning that Lucy’s group was going to Siren Town, he insisted on joining. He knows the legends of Siren Town very well.】"

    andre "Andrei snapped back: “Most likely they just drowned themselves. Drowning at the seaside is perfectly normal.”"

    jelf "Jelf refused to back down: “The police have been dredging the waters for a month and haven’t recovered a single body. Even if they really fell into the sea, that’s not normal..”"

    jelf "His tone grew low and eerie as he spoke, laced with a trace of excitement. “Unless their bodies were eaten by sirens. That would explain why the police couldn’t find them…”"

    andre "Andrei finally lost it. He furiously smacked Jelf hard on the head. “Shut up! Damn four-eyes! Always going on about mermaids, mermaids! You look more like a fish yourself!”"

    "Andrei struck with such force that Bai Liu could clearly see Jelf’s head slam against the edge of the seat. Dazed, he staggered and bumped into Andrei again, which further enraged him. Andrei slapped Jelf several times, hitting him so hard that one of Jelf’s teeth flew out."

    jelf "Jelf lowered his head, silently picking up his tooth. He glared at Andrei with a concealed, bitter hatred in his eyes, and mouthed something under his breath."

    jelf "No one else heard, but Bai Liu’s hearing had always been sharp. He heard Jelf whisper: 【The mermaids will tear you apart and swallow you whole, Andrei.】"

    "Bai Liu raised an eyebrow slightly but said nothing. This NPC’s relationships seemed rather complicated."

    "It appeared that Andrei’s habit of beating and cursing Jelf had been going on for quite some time. And Jelf, in turn, seemed to have already woven “mermaids” into a plan for revenge."

    jump second
    
label second:
    scene bg siren 42
    " The driver was a local from Siren Town hired with Bai Liu’s money. From Lucy’s conversation, Bai Liu realized he was indeed a rich second-generation—he had covered everyone’s food and lodging, hired the driver at a high price, and even asked him to help find a local inn. "

    driver "The car drove all the way until late at night before reaching the mysterious Siren Town. According to the driver’s description, Siren Town was a place that survived by fishing and salvaging shipwrecks. It had always been remote and rundown, until the new mayor came up with the idea of using mermaid legends to attract tourists. Only then did Siren Town flourish through tourism. "

    driver "But last month, tourists kept having accidents. These tourists weren’t just falling into the sea like Andre claimed—some hadn’t even gone to the shore before vanishing mysteriously in different corners of Siren Town. For example, one tourist checked into a hotel at night, but the next morning he was gone. The room was locked, no one saw him leave, and the bed still retained body heat, but the man himself had disappeared. "

    driver "So now, even during the peak tourist season, Siren Town is eerily desolate. Many inns and hotels have closed down due to poor business. "

    "Siren Town was indeed very dilapidated. Fences and fishing nets were strewn everywhere, the ground was covered in dried shells, seaweed, and mud. Only some inns and hotels had decent decorations. When Bai Liu’s group arrived, it was already late at night, yet there were still many people on the streets. "

    "These pedestrians had originally been walking in unison toward the sea, but once Bai Liu’s car entered, they all stopped simultaneously, tilted their heads, and stared fixedly at Bai Liu’s car. "

    bl "Bai Liu turned to ask the driver: “It’s already midnight, what are these people doing at the sea?”"

    driver "The driver shook his head: “Not many tourists come these days, the economy is bad, so they can only go back to fishing. You wouldn’t know this if you haven’t fished before, but many valuable fish are afraid of strong light. They only come out at night, so that’s why people go out to sea then.” "

    "The townsfolk stared at Bai Liu with strange gazes, their eyes glowing cat-like green in the night. Their faces wore peculiar expressions, as if smiling, but their lips never fully curved up. Instead, the corners of their mouths twitched stiffly. "

    "They held fishing nets and hooks, some carried oil lamps with hazy light. They stared unblinking at Bai Liu’s car, their eyes following it as if they might rush forward at any moment to attack the vehicle with their fishing tools. "

    driver "“You’d better be careful around these people,” the driver warned. “They’re desperate for money lately, and you’re rich.” "

    "Because of Bai Liu’s lavish spending as a rich second generation, the driver booked the group into the best hotel in town. "

    "The hotel was so luxurious that it clashed completely with the town’s style—it was a very modern and fashionable five-star type of place, with an actual fountain at the entrance. "

    "Inside the fountain was a stone statue of a mermaid. The carving was lifelike: her smooth marble skin glowed faintly like real human skin under the dim moonlight, her long hair draped over and covered her full breasts, her tail stood upright in the pool. With her eyes downcast and expression sorrowful, she held an urn in her hands. From the urn spilled fake mica pearls, and the fountain water poured from it into the pool, sounding like ocean waves crashing. "

    "The driver circled around the fountain and parked the car right at the hotel entrance. "

    scene bg 1 4

    jelf "Jelf suddenly cried out, pointing at the mermaid fountain statue at the entrance: “She just looked at me! She just moved!” "

    bl "Bai Liu followed Jelf’s gaze, but the mermaid statue still lowered her eyes, staring into the water, motionless. "

    andre "Andre was startled by Jelf’s cry and punched him hard: “Fuck! She didn’t move at all! If you keep making a fuss like this, I’ll tear out your vocal cords and let’s see if you’ll still scream then!” "

    jelf "Jelf clutched his head where he was hit, glanced fearfully at Andre, curled up into a ball, and muttered softly: “She did move, she really did…” "

    lucy "Lucy was also unsettled by Jelf, forcing a smile: “Jelf, how can you be so sure it wasn’t your eyes playing tricks on you, but that the mermaid statue actually moved? The statue doesn’t even have pupils—how could you know it was looking at you?” "

    "It was a milky-white marble mermaid statue. Though its eyes were carved, there were no black pupils—the eyes were entirely pure white, standing at the hotel entrance like some soulless, lifeless creature. "

    jelf "“Didn’t you notice?” Jelf’s voice dropped lower, trembling, “No matter where our car drove, the statue’s eyes were always staring right at us. Her eyes must be moving…” "

    lucy "“Oh… so that’s what you meant…” Lucy let out a breath of relief and finally laughed. “It’s just like that painting ‘Mona Lisa’s Smile’, right? No matter where you stand, you feel like she’s looking at you.” "

    bl "“No. That effect of a portrait’s gaze following you can only happen in two-dimensional images. It’s impossible in three dimensions, which means a statue shouldn’t be able to do that.” Bai Liu calmly refuted Lucy. “Jelf is right—the statue’s gaze has indeed been moving with us.” "

    "It was just like those townsfolk—constantly staring at them the moment they entered, as if watching prey that had stepped into their hunting grounds. "

    "This thing must be some kind of monster. "

    board "Just as this thought formed, the coin on Bai Liu’s chest suddenly trembled, and a brand-new panel popped out. The game panel transformed into a heavy, ancient book like something from the Middle Ages, slowly opening in front of Bai Liu. "

    board "【Congratulations to the player for discovering the first game monster, unlocking the Monster Book – Siren Town Special (1/4)】"
    
    scene bg 1 6

    board "【Monster Name: Mermaid Sculpture (Pupa State)】\n【Attack Value: ??? (Unknown, locked, unlocks after battle)】\n【Attack Method: ?? (Unexplored)】\n【Weakness: ?? (Unexplored)】"

    "The question marks looked like smudges of wet ink and stains, making the words unreadable. Floating behind them were glowing letters with explanations."

    board "Below the weakness was an explanatory line:\n【Note: Completing this monster book page through exploration grants corresponding point rewards and special rewards. Collecting all monster book pages from one game instance allows you to take away the most precious thing from one type of monster in that instance.】"

    "The Siren Town Monster Book had four pages, but Bai Liu couldn’t turn to the later ones—they showed as locked. They must belong to monsters from other game instances."

    "But judging from these exploration conditions, and even battles included, this was completely encouraging players to court death and provoke monsters….."

    lucy "Lucy nervously hugged Bai Liu’s hand: “…Is she really moving?!”"

    andre "“How could that be possible!” Andre seemed infected by Bai Liu’s firm words. For a moment, fear flickered across his face, but it was quickly suppressed. He sneered at Bai Liu, “Bai Liu, if you, coward, are unwilling to prove your love for Lucy, making up excuses to run away just to cling to life—then go! Once we return, you’ll automatically give up on Lucy, then kneel and lick the piss off my leather shoes!”"

    driver "The driver’s expression twitched oddly, but in the end, he pretended calm and joked: “It’s so late, you must’ve seen wrong. What moving statue? If there really was one, our town would have preserved it as a tourist attraction long ago! That’d make us a fortune. The mermaid statue is just our town’s feature, you can see them everywhere—nothing special.”"

    driver "“We’re here, get off now. Have a good night’s rest and enjoy yourselves tomorrow morning.” The driver opened the door and let them out."

    "Bai Liu glanced back at the mermaid statue in the fountain. From afar, the statue was still facing them, head meekly bowed toward the water’s surface, seemingly not watching them."

    "But Bai Liu remembered clearly: when their car had just driven in, the statue had not been facing the hotel entrance—it had been facing the gate."

    "At the hotel entrance, two more mermaid statues stood on either side, holding scepters, with strangely twisted smiles at the corners of their mouths. They seemed to be posing as attendants welcoming them, but the expressions looked as if they were forced to stand there greeting travelers."

    "When they entered the hotel, they found even more mermaid statues inside, big and small. Behind the reception desk stood a life-sized mermaid statue holding money, as if collecting payments."

    "Just as the driver said, mermaid statues seemed to be Siren Town’s specialty, visible everywhere. But this was excessive. From the mermaid-shaped floor lamps to the mermaid-carved pen holders at the front desk, this wasn’t merely ‘everywhere’—it was inseparable."

    "And all of these mermaid statues had one thing in common: Bai Liu found that no matter where he stood inside, the statues placed around always gave him the feeling of being stared at. But these statues had no eyeballs—normally, statues without pupils couldn’t make one feel watched. Yet Bai Liu felt exactly that."

    "So many densely placed marble mermaid statues staring at you was deeply unsettling. Even Andre, who had been loudly mocking Bai Liu as a coward, got goosebumps the moment he entered. He rubbed his arms. Jelf trembled behind Andre, as if too scared to even care about being beaten by him."

    lucy "Lucy clung tightly to Bai Liu’s arm like a frightened bird, her rose-like face drained pale, clearly terrified by the eerie hotel décor."

    # frontdesk

    scene bg 1 5

    bl "But Bai Liu calmly approached the front desk: “Hello, my surname is Bai, I have a reservation here.”"

    fd "The front desk clerk was a young man, his skin as pale as marble. He wore a floor-length Scottish kilt, and walked with a stiff, halting gait as if disabled. When standing still, he was indistinguishable from a statue."

    lucy "As Bai Liu’s group approached, the man suddenly moved, startling Lucy into thinking a statue had come alive. She covered her face and shrieked: “Oh my God! You’re as pale as a statue!”"

    fd "“Apologies.” The front desk clerk bowed slightly. “I have albinism. Sorry for scaring you. Mr. Bai, correct? A week ago you booked four rooms for one week. The fees are already paid. Here are your room cards. Wishing you□□ a pleasant stay.”"

    "Bai Liu accepted the room cards. Seeing four separate rooms relieved him a little."

    "He really didn’t want to share a room with Miss Lucy, who hadn’t ‘succeeded’ with him. Lucy seemed to realize this as well. Though she’d just been frightened, she quickly recovered, looking at Bai Liu with a teasing gaze as if saying: Oh! Baby! You’re just too shy! Bai Liu, face unchanged, ignored her completely."

    menu:
        "“I’d like to ask, why are there so many mermaid statues in this hotel?”":
            bl "“I’d like to ask, why are there so many mermaid statues in this hotel?”"

            fd "The receptionist answered calmly: “Sir, the mermaids gave us everything. Siren Town originally had nothing, but ever since we salvaged a mermaid’s corpse, more and more tourists have come here. We gained money, gained everything, so we’re very grateful to the mermaids. Here, every household has many mermaid statues. To us, they are like protective charms.”"

            bl "Bai Liu pointed at the mermaid statue behind the receptionist: “Your mermaid statues come in many forms, all sorts of varieties. The one behind you looks exactly like you, and its material seems different from the other statues.”"

            "It wasn’t Lucy’s fault for failing to tell the person and the statue apart. The mermaid statue behind the receptionist looked identical to them in appearance, but with an even more vivid, pained, and somewhat ferocious expression."

            "The eyes of this mermaid statue stared straight at the receptionist standing before it, never shifting no matter where the receptionist went. It was as if the statue was about to claw its way out and tear apart the receptionist—its doppelgänger—limb by limb. The sight sent chills down one’s spine. Yet the material looked thinner and more brittle, unlike the other statues that were heavy and solid, and it appeared rather worn-down."

            fd "“Yes, sir.” The receptionist raised their eyes to meet Bai Liu’s gaze. “The mermaid statue behind me is my protective charm. We carve mermaids in our own likeness. When disaster strikes, these mermaid charm statues will be mistaken for us by the devil, taking our place and bearing the danger first.”"

            "Bai Liu found this interesting. This 【protective charm statue】 was clearly something different from the other mermaid statues."

            board "【Player has gained new knowledge ― 『Siren Town Monster Book』 Mermaid Statue panel refreshed】\n【Monster Name: Mermaid Statue (Pupa State), Protective Charm Statue (Cocoon State)】"

            "Pupa and Cocoon? This monster called 【Mermaid Statue】 actually has two different states?"

            bl "Bai Liu slowly pondered. A pupa is the state before an insect breaks out of its shell. Breaking the cocoon, it becomes a butterfly. A cocoon is what’s left after the insect successfully hatches—an outer shell of protection. This aligned with what the receptionist said, a shell that shields one from harm…."

            "It’s likely that these mermaid statues also have 【Insect】 and 【Butterfly】 states. Bai Liu felt those should be more aggressive than 【Pupa】 and 【Cocoon】. For now, 【Pupa】 and 【Cocoon】 state mermaid statues didn’t seem to actively attack people, but perhaps their method of 【attack】 was something Bai Liu couldn’t perceive—like mental pollution. He already thought that having a hall full of mermaid statues staring at the players was quite mentally unsettling."

            jump third
        "Room cards distributed":
            jump third

label third:
    lucy "Bai Liu handed out the room cards. Lucy clung to him, wanting to stay in the same room as him. But Bai Liu brushed her off with the excuse: 【I haven’t yet proven my courage for you. I don’t deserve to truly have you!】. Lucy was deeply moved and went back, but before leaving, she even leaned in for a passionate kiss with Bai Liu, which was stopped by an angry Andre."

    bl "Thanks to Andre! I hope nothing happens to Andre tonight!\nBai Liu sincerely wished Andre could live a little longer, otherwise he really wouldn’t know how to deal with Lucy."

    # room

    bl "Bai Liu swiped his room card to open his room. The moment the door opened, his steps froze."

    "The NPC Bai Liu was playing had money, so he booked a better room. The furnishings inside were exquisite and refined, but everything—from the lamp design to the sculptures on the nightstand—was mermaid-themed. As soon as Bai Liu entered, the pale-eyed mermaid sculptures seemed to subtly shift their gaze toward him."

    board "【Main Quest Activated: Player Bai Liu must safely survive the night in the room, live until tomorrow, and avoid being hatched――Reward for completion: 20 points】"

    "The system gave Bai Liu his first quest, but his focus wasn’t on the quest. Instead, he stared at the words 【avoid being hatched】 and fell into thought."

    "…Hatched?\nTsk, could those sculptures hatch them?"

    "Bai Liu quietly made a note. When he turned around, he saw a life-sized mermaid statue standing opposite the bed."

    "This was the largest mermaid sculpture in the room, and also the only one that wasn’t looking directly at him."

    mermaid "The mermaid statue was stunningly beautiful, with a sorrowful expression. In its hands, it held a tall, polished mirror, its elegant arms forming the frame that supported this full-length dressing mirror."

    mermaid "It was also the only statue in the room not staring at Bai Liu. Instead, it gazed sorrowfully into the mirror. Bai Liu’s reflection appeared within it. The statue’s arms wrapped around the mirror as if embracing the Bai Liu inside it. This made Bai Liu feel a little uneasy. The mermaid statue’s eyes fixed on the mirror, its brows knit, its gaze downcast, its fish tail limp on the ground, as though weeping for the reflection. Its expression was lifelike and mournful. But when Bai Liu looked at the mirror, his 【reflection】 inside showed a chilling, statue-like smile at him."

    bl "Unmoved, Bai Liu covered the mirror with a white cloth."

    "Such horror scenes had no effect on Bai Liu. In the real world, he worked on horror games, often staying up alone until two or three in the morning designing all sorts of terrifying imagery. This cliché scene of a reflection grinning eerily back at you from a mirror barely fazed him anymore."

    "It seemed that the tourists Jelph mentioned earlier, the ones who mysteriously disappeared without a trace in the hotel and whose bodies were never found, were probably 【hatched】 by these mermaid sculptures."

    bl "Out of caution, Bai Liu covered all the mermaid statues in the room with the hotel bedsheets, including the giant mirror, to block out those eerie, omnipresent gazes. It might not be useful, but it was better than nothing. More importantly, with so many statues staring at him, Bai Liu wouldn’t be able to sleep otherwise."

    "When covering the mirror, he touched the mermaid statue’s tail. The texture wasn’t the smooth, cold feel of marble—it was sticky and slick, like the flesh of a sea fish. Bai Liu even felt the scales under his hand lightly shift and close again."

    bl "Bai Liu paused. After touching the statue, he smelled his fingers and noticed a faint fishy odor lingering there. But when he leaned closer to sniff the mermaid statue itself, all he smelled was the incense of the hotel room—no fishy smell at all."

    bl "Maybe the smell came from the bus ride…\n…Or more likely, it came from Bai Liu himself. Thinking of how the mermaid statues could 【hatch】 tourists, Bai Liu frowned, feeling uneasy."

    "What could the mermaid statues hatch? Most likely some grotesque, fish-like creatures. The word ‘hatch’ reminded Bai Liu of a film called *Mermaid in the Sewer*. He had watched it two or three times for reference, and ever since, he never again had any romantic fantasies about mermaids."

    bl "After driving through most of the night, Bai Liu was already exhausted. He washed up briefly, lay down, and quickly fell into a deep sleep. His stamina had already hit zero, and he badly needed rest to recover."

    # Midnight

    "At midnight, Bai Liu was awakened by a strange, heavy dragging sound."

    mermaid "When he opened his eyes, he saw that the white sheets covering the statues had somehow slipped off, leaving only bits still hanging on them. Some statues were only half-covered, their exposed eyes peeking out. Their expressions seemed to have subtly changed—from divine compassion to resentment and venom. They stared unblinkingly at Bai Liu, as if blaming him for covering them earlier."

    "Bai Liu also noticed that the statues seemed closer than before he fell asleep. They were slowly gathering around his bed, arms raised as though converging for a feast at the dining table."

    bl "Especially the life-sized mermaid statue with the giant mirror. When Bai Liu groggily woke up, he saw that his feet were almost touching the mirror. The enormous mirror, originally across the room, was now pressed right against his bed. When Bai Liu pulled back his legs and sat up, he saw his reflection inside the mirror."

    "The 【Bai Liu】 in the mirror had skin pale as stone, eyes without pupils, and spiderweb-like marble veins spreading from the corners. He smiled stiffly at the real Bai Liu. But in the blink of an eye, it seemed as though Bai Liu had just imagined it—his reflection appeared normal again."

    menu:
        "Sit up, and firmly tie these mermaid statues with white cloth":
            bl "Bai Liu paused for a moment. He sat up and, without a change in expression or a quickening heartbeat, firmly tied these mermaid statues with white cloth."

            bl "To prevent the mermaid statues from breaking free, Bai Liu also tied them twice tightly with rope. Then, he wrapped the smaller mermaid statues in white cloth and locked them inside the wardrobe, while he pushed the larger statues into the bathroom and locked the door behind him, his movements swift and efficient like that of a practiced kidnapper."

            mermaid "These things also seemed to be under certain movement restrictions. Before Bai Liu went to sleep, they hadn’t moved. And it appeared they needed to break free of the white cloth and see Bai Liu before they could approach him. Some of the smaller mermaid statues still wrapped in white cloth were wriggling around inside it, scattering in all directions rather than gathering by the bed."

            bl "Once he understood this, Bai Liu immediately decided to maximize this restriction."

            "Just as he finished and clapped his hands, ready to go to bed, Bai Liu heard the sound of a door opening and closing next door, followed by cautious, tiptoeing footsteps."

            "Bai Liu froze as he was just about to lie down. All the surrounding rooms had been booked by him. To his left and right were Andre and Jelf. To protect (?) himself, Bai Liu had deliberately arranged for Lucy to stay in the room farthest away from him."

            menu:
                "Get up and press against the door to look through the peephole into the hallway":
                    bl "The sound of the door came from the left. That was Jelf’s room. Bai Liu got up, pressed himself against the door, and looked through the peephole into the hallway. Jelf glanced left and right, confirmed no one was in the corridor, and then sneakily went down the hotel stairs."

                    bl "Bai Liu frowned. What was Jelf doing, sneaking out in the middle of the night instead of sleeping?"

                    "Just as he was about to open the door and follow, Bai Liu noticed the handle of Jelf’s supposedly closed room door slowly start to turn again, as if someone else was about to come out after Jelf."

                    "Each hotel room was for one person.\nJelf’s room should have only contained him. Lucy would never visit Jelf’s room in the middle of the night, and Andre didn’t get along with Jelf, so he would never go looking for him either. Bai Liu was in his own room.\nSo who—or what—was coming out of Jelf’s room?"

                    bl "Bai Liu’s heart skipped a beat. Realizing something, he slightly pulled his face away from the peephole."

                    "What came out of Jelf’s room was not a person!"

                    "With a click, Jelf’s door handle turned all the way, and the door slowly opened from the inside. Bai Liu once again heard that dull dragging sound he’d heard while half-asleep, like something being dragged along the ground while kneeling."

                    "But this time, Bai Liu knew exactly how that sound was made."

                    mermaid "A life-sized mermaid statue emerged from Jelf’s room. Its face was stiff and unmoving, with no expression at all. Its eyes were completely white without pupils, lifeless and dead. Its fishtail dragged along the ground, scraping forward inch by inch across the empty hotel corridor at night. The heavy, snow-white tail dragged across the old, sturdy red carpet, and its rigid, unmoving body kept advancing toward the stairs, reminding Bai Liu of zombies—those stiff corpses that could only hop forward."

                    "…This thing could actually leave the room on its own, and even open doors…"

                    mermaid "When the mermaid statue that had crawled out of Jelf’s room reached the staircase, it seemed to sense something. Its neck twisted stiffly a full 180 degrees, its head turning completely around on its shoulders. Suddenly, it changed direction and began walking expressionlessly toward Bai Liu’s room."

                    menu:
                        "Cry while curling up against the shaking door, clutching your ears, trembling as you hold a wooden stick":
                            bl "Every time the mermaid statue rammed the door, he cried out and screamed loudly, but no one came to save him."

                            "After shaking a couple of times, the door stopped. The mermaid statue outside seemed to have left."

                            bl "You wipe your tears away and breathe a sigh of relief like a survivor, leaning weakly against the door, your legs and arms trembling as you slowly stand up."

                            mermaid "But what he didn’t notice was that the peephole on the door was still white—a pure white stone eye staring into the room from outside."

                            "The mermaid statue hadn’t left at all. It was only pretending, testing whether someone was inside. The moment it saw you stand up, its stiff face cracked into a strange, twisted smile—like a predator finding its prey. The door suddenly banged twice more and was easily broken open. Before you could react, you screamed as you were crushed beneath the door. The mermaid statue dragged its heavy tail into the room, its smile radiating an eerie purity mixed with grotesque ferocity, spreading its arms as it slowly reached toward you beneath the door."

                            "The instant the mermaid statue touched you, it felt like something was sucking your brain dry. Your eyes rolled back, your body convulsed violently, froth spilled from the corners of your mouth, and your limbs curled up and twitched. Your legs pressed together, shaking on the ground like a fish thrashing in boiling water. Your skin stiffened and turned pale. Around your eyes appeared those gray-black marble-like veins that Bai Liu had seen in the mirror. Your pupils vanished, leaving only white eyes covered in those veins, while your stiff mouth curled upward into a grotesque grin."

                        "He quickly crouched behind his own room door and used a white cloth to cover himself, leaving only a pair of eyes exposed.":
                            bl "Bai Liu’s heart skipped a beat. He quickly crouched behind his own room door and used a white cloth to cover himself, leaving only a pair of eyes exposed."

                            "After Bai Liu made sure the door was locked from the inside, he curled up in the lower right corner of the door to see what this thing wanted to do. Bai Liu soon saw the peephole on the door turn white and keep rotating."

                            mermaid "This thing was approaching to look inside the door with its eyes. The continuously rotating object was the white eyeball of the sculpture. It was searching through the peephole for anyone inside the room."

                            "Bai Liu could hear the crisp sound of marble hitting the door, and the doorknob moved twice. Although the door was locked from the inside, under the forceful twisting of the mermaid sculpture outside, the doorknob made a fragile metallic cracking sound, as if it was about to break, and then the mermaid sculpture forcibly broke through the door. Even the door began to shake."

                            mermaid "It seemed like this thing wanted to come in. Its pale white eyes scanned Bai Liu’s room and, apparently finding no one, it seemed to leave Bai Liu’s door. The doorknob stopped moving, and the outside of the room became silent and still, as if it had gone away."

                            bl "But Bai Liu still held his breath. He remembered that this thing made a dull noise when moving. Without that sound, something was wrong. The mermaid sculpture hadn’t left; it was probably still quietly guarding his door."

                            mermaid "This thing was deceiving him, trying to lure him out. Bai Liu thought, and then glanced sideways, noticing that the peephole, which had returned to carpet color, suddenly turned white again with a protruding eyeball."

                            "That thing is definitely still there!"

                            mermaid "After waiting a while, it seemed unwilling to give up and still wanted to come in. The doorknob was suddenly twisted into a protruding broken shape, wobbling as if it was about to fall from the door."

                            "The mermaid sculpture outside the door is coming in!"

                            bl "Bai Liu’s mind raced, and his breathing slowed."

                            "The game clearly told him that these ghostly monsters had weaknesses. Players could use the weaknesses to escape from these monsters. So the current way to break the stalemate was to find the weakness that restricted this thing’s movement."

                            bl "Bai Liu closed his eyes and recalled the entire process of checking in tonight."

                            "As long as it’s a game, there must be a solution. A game without a solution is the worst. Bai Liu had played horror games for so many years and was certain that somewhere, there had to be a clue pointing to the mermaid sculpture’s weakness."

                            bl "What exactly was it….\nBai Liu calmly began to organize all the scenes where he had encountered the mermaid sculpture."

                            bl "The first time was outside the hotel fountain. Jeff exclaimed that he saw the mermaid sculpture move. The movement was silent, just like it was following the car. The sculpture didn’t look directly at them, only at the water."

                            bl "The second time was in the hotel lobby, with numerous mermaid sculptures. They looked directly at them but didn’t move."

                            bl "The third time was inside the hotel room. Except for the giant mermaid sculpture looking in the mirror, the other mermaid sculptures all stared at Bai Liu. After Bai Liu fell asleep, they began to move. The mirror mermaid moved the fastest, but once Bai Liu woke up, those sculptures stopped moving."

                            "But clearly, Bai Liu staying awake wasn’t the condition to restrict the mermaid sculpture’s movement, because the mermaid sculpture outside the door was already preparing to break in."

                            bl "There cannot be an unsolvable situation in the game. He must have something that can restrict the mermaid sculpture’s movement."

                            bl "It’s not something in the room, nor in the hotel. It must be something Bai Liu brought with him. The hotel and room items couldn’t restrict the mermaid sculpture’s movement, as proven by the fact that the sculpture could freely enter and exit Jeff’s room before."

                            "What exactly is it?"

                            bl "Mirror… water… sleep… direct gaze!"

                            "Bai Liu knew what it was!"

                            bl "Bai Liu suddenly stood up, opened the door, and looked directly at the mermaid sculpture."

                            mermaid "The sculpture outside the door had come so close that, from Bai Liu’s perspective, this lifeless mermaid statue’s face seemed pressed against his nose. Its palm was still on Bai Liu’s doorknob, and its pure white, pupil-less eyes were looking through the peephole at the lower right corner—that was where Bai Liu was hiding."

                            "No wonder it wanted to come in. It should have seen Bai Liu hiding behind the door in the lower right corner."

                            mermaid "Its movement stopped. Its tail had touched Bai Liu’s toes, and just before stepping into Bai Liu’s room, it froze in front of the door."

                            bl "Bai Liu exhaled in relief. Sure enough, the weakness that made this thing stop moving was direct human gaze."

                            "Inferring the weakness—that being seen by human eyes would restrict the mermaid sculpture’s movement—was actually quite simple."

                            "Because after Bai Liu fell asleep, the sculptures began to move, and after waking up, they instantly stopped. The only difference before and after sleep was that his eyes were open, which meant 【human gaze] could restrict the mermaid sculpture’s movement."

                            "But here was a trap: looking at the thing through reflective objects only partially slowed some sculptures. Only direct gaze could completely stop them."

                            "Two sculptures could still move under direct human gaze: the fountain sculpture at the hotel entrance and the mirror mermaid sculpture in the room."

                            "The fountain sculpture at the hotel entrance looked into the water. So people were seeing it 【directly] through the water. The sculpture’s movement was restricted; it couldn’t move quickly, but could move slowly or rotate, which was why it rotated slowly at the door. The mirror mermaid in the room moved the fastest because it was looking into the mirror. The person’s gaze was indirect, so the restriction was limited, and that’s why it ran fastest."

                            "The mermaid just now was looking at Bai Liu through the peephole. So it could move. If Bai Liu only gazed at it through the peephole, it would impose some restriction, but the sculpture could still move."

                            "At such a close distance, looking through the peephole is definitely insufficient to stop it from breaking the door. If it got in, the player would lose the 【human gaze] condition and quickly die."

                            "But in this situation, very few new players would dare to open the door and look directly at the mermaid sculpture. Most would panic. Even if they deduced the 【human gaze] condition, they wouldn’t have the courage to test it. Only Bai Liu, reckless with money and life, could calmly test his theory even without 100\% certainty."

                            board "【‘Monster Book of Siren Town’ Mermaid Statue Panel Refresh】\n【Monster Name: Mermaid Statue (Pupa State), Talisman Statue (Cocoon State)】\n【Weakness: Direct Human Gaze (1/3)】\n【Attack Method: Hatch】"

                            mermaid "The mermaid sculpture’s eyes drooped slightly, head tilted slightly to the lower right, lips curling into a faint smile. Its tail was graceful, body pure white and flawless, posture exuding a secret beauty and divinity. Once frozen, the spine-chilling sense of possession disappeared, leaving a highly aesthetic mermaid sculpture silently standing in front of a stranger’s room at midnight on the seaside."

                            board "【Player Bai Liu gained 3 Charging Points, unlocked Game Item Shop】\n【Points too low to purchase any item. Player, keep trying!】\n【Points can be used to buy anything you want】."

                            "Bai Liu closed the shop and stared at the motionless mermaid sculpture in front of him.\nNow it really didn’t move, but Bai Liu couldn’t confront it all night. After this, he had a new understanding of its destructive power."

                            "He looked at the stainless-steel doorknob that was about to fall off."

                            "Judging by the behavior of the sculptures in his room, although this thing was highly destructive, it seemed only sensitive to vision. Once covered by a white cloth, it couldn’t locate Bai Liu, even in the same room."

                            "In other words, the mermaid sculpture seemed to have no auditory or olfactory senses."

                            "Otherwise, with so many mermaid sculptures in the same room, it could easily locate Bai Liu by his breathing and twist his head off like a doorknob. Its ability to break a doorknob bare-handed would prevent it from being trapped in the closet all this time."

                            bl "…So troublesome, and there are so many of them. Keeping them is really a burden."

                            bl "He squinted slightly, a mischievous thought forming—now he had a motionless sculpture before him. Could he experiment on it, test its weakness, maybe burn it or smash it…"

                            board "【Tip: Directly attacking this monster may cause it to hold long-term hatred toward the player, constantly attacking and reducing survival rate】"

                            bl "Bai Liu thoughtfully stroked his chin, smiling with a harmless dimple on his right cheek."

                            bl "“Directly attacking it will make it hold a grudge and seek revenge, huh…” Bai Liu muttered. “If it gets into trouble by itself, it can’t blame me.”"

                            bl "Bai Liu reused his trick: he wrapped the mermaid sculpture with a bedsheet, tied the bottom opening with a rope, and maliciously placed it at the hotel staircase entrance."

                            "If the mermaid sculpture cannot see, it walks headlessly. Bai Liu placed it there so it would fall down the stairs on its own."

                            "Given the hatred mechanic, Bai Liu wouldn’t smash these sculptures himself. If he could smash them directly, fine, but if not, it would cause trouble."

                            "But so many mermaid sculptures were a huge hidden danger. Bai Liu only had two eyes. If surrounded 360° in wooden-man mode, and human eyes’ horizontal vision is at most 188°, he couldn’t see all the sculptures behind him. He would surely die."

                            "Bai Liu liked cost-effective solutions. Although the game said using weaknesses to escape monsters was enough, he wanted to know if he could destroy them directly or if there were other lethal weaknesses."

                            "He wouldn’t risk smashing or attacking them himself."

                            "But if a mermaid sculpture fell down the stairs due to poor eyesight, it wouldn’t be his problem."

                            bl "Bai Liu just wanted to test if it could be smashed. He retreated to his room, and sure enough, the sculpture began moving shortly after. Bai Liu observed thoughtfully. Although he was watching, the sculpture’s head was covered by a white cloth, unaware it was being observed, so it moved on its own."

                            "This proves that 【direct human gaze] is only an objective condition. The mermaid sculpture must subjectively feel it is being watched to stop moving."

                            "With so many sculptures in his room, Bai Liu couldn’t keep staring. Previously, when he woke up, they stopped moving before he could look around."

                            "So as long as a mermaid sculpture 【felt] it was being watched, it would stop.\nBeing aware at this level shows these things are alive, with a certain degree of intelligence, though not very high."

                            mermaid "The mermaid sculpture at the staircase struggled, slid along the edge, and fell covered in a white cloth with a crashing, dust-filled noise. Bai Liu looked down from above, brushed dust off his hands, clicked his tongue in slight disappointment, and saw the sculpture below, unharmed, only slightly curled."

                            bl "…As expected, it can’t be broken… physical attacks are ineffective…"

                            bl "Bai Liu returned to his room. For safety, he covered the peephole with a white cloth to prevent the mermaid from spying and propped a cabinet against the door, hoping that if a mermaid broke in, it would make noise to wake him."

                            bl "His stamina was also drained. After all this, Bai Liu lay on the bed, closed his eyes, and slept through the night without dreams."  

                            jump true_ending

                "Save yourself, keep sleeping":
                    "The night passed with scares but no real danger."

                    board "【Player's mental points decreased by 20 due to the influence of the mermaid statue at night】"

                    jump normal_ending
        "Doesn't matter, go to sleep":
            "At night, the mermaid statue slowly approached you, but you failed to wake up in time."

            jump bad_ending
                    

label normal_ending:
    "Although you were slightly injured, you successfully made it through the night."

    "Congratulations, normal ending."

    return

label bad_ending:
    board "【Player's mental points dropped to 0, completely mutated by the monstrous mermaid statue, game failed】"

    "Bad ending"
    return

label true_ending:
    "Congratulations, you used your wisdom to get through the night with almost zero loss."

    "Well done, true ending."

    return

# label true_ending:
#     "The lips of the Siren King were soft and cold, with a very light smell of creeping grass, and they separated at the touch."

#     scene bg siren 67 32
#     s "The Siren King leaned on Bai Liu, his expression slightly strange and confused: \"You're temperature is warm'.\""
    
#     b "\"Of course.\" Bai Liu was a little amused, \"I am a warm-blooded animal. See you next time, Siren King.\""
    
#     s "The Siren King whispered in the light: \"See you next time, Bai Liu.\""

#     "True ending"

#     return