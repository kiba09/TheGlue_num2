
define s = Character('Shika', color="#f08080",show_two_window=True)
define k = Character('Kotori', color="#ffa500",show_two_window=True)
define n = Character('Nami', color="#dda0dd",show_two_window=True)
define ai = Character('AI', color="#1e90ff",show_two_window=True)
define a = Character('Akane', color="#b22222",show_two_window=True)
define au = Character('Strange woman', color="#b22222",show_two_window=True)




define en = Character('Engineer', color="#c8ffc8",show_two_window=True)
define merc = Character('Mercenary', color="#c8ffc8",show_two_window=True)
define smerc = Character('Skeptical Merc', color="#c8ffc8",show_two_window=True)



label start:
stop music fadeout 2.0

scene bedroom with fade
play music day fadein 2.0
"An artificial light filters into my room, reminiscent of the sun's gleaming glory."
"I blink several times, rubbing the sleep out of my eyes."
"The window to the left of my bed displays a brilliant view of the stars."
"More and more lights switch on, preventing me from dozing off back into sleep."
call s_shika from _call_s_shika
ai "Good morning, Captain."
ai "It has been eight Terran hours. Now is the optimal time to wake up."
"Let's get the niceties out of the way."
s "Good morning to you too, AI."
"I let out a loud yawn and reach for the ceiling, stretching out my stiff body."
$ spose='1'
show shika at c2
s "What is today's schedule?"
ai "Displaying available bounty jobs in the current sector."
"... Not really what I had in mind, but maybe it would be fun."
ai "Displaying bounties from the lowest to the highest bounty."

s "Do it the other way around, please."
s "I think it's time we had a decent challenge."
ai "As you wish."
"I wander over to the kitchen bench and find a steaming cup of coffee waiting for me."
"Despite there being entire galaxies of exotic substances out there, nothing wakes me up the same way cheap coffee does."

ai "Would you like to view the list before or after breakfast?"
$ sface='smiling'
show shika at c3
s "Why not during breakfast?"
ai "As you wish."
"The projector on the kitchen table begins displaying a hologram of the list."
"Another day of hunting down bounties, projecting royalty and whatever else someone could want a mercenary for..."
"At least it never gets boring."
"I take a sip from my coffee. The bitter taste immediately clears the fog from my mind."

$ sbody='sb'
show shika at c4
s "Today feels like it's going to be a good day."
s "Alright, let's see what we've got on the..."
$ sface='shocked'
show shika flip at c3
"I trail off after seeing the top name on the list."
"My coffee mug nearly slips from my fingertips."
ai "Are you okay, Captain?"
$ sface='neutral'
show shika at c3
"I rub my eyes a little bit, trying to clear the sleep out of them."
"Just now, I swear they were playing tricks on me."
s "That number can't be right..."
"I look at it again to be sure."
"Still, the number looks the same as it did before."

$ sface='shocked'
$ spose='1'
show shika at c4
s "No way..."
s "That much money?"
s "This cannot be real..."
ai "No. The number that is displayed is correct."
ai "That particular bounty is the single highest one ever placed in this galaxy."
ai "One billion imperial dollars."
"It takes a moment for the reality of it to sink in."
"Before I take off and do anything, however..."
"I need a moment to let the shock dissipate."
"Let's think about this carefully."
menu:
    "Something doesn't seem right here.":
        $ investigate += 1
        $ sface='neutral'
        show shika flip at c3
        s "Doesn't this seem fishy to you?"
        s "Why would such a massive bounty just appear out of nowhere?"
        s "The next highest job is only about two hundred thousand imperial dollars..."
        $ sbody='sa'
        show shika at c2
        s "And that job requires you to hunt down someone on a planet torn apart by civil war."
        ai "There is no name provided for the bounty."
        ai "Only a location."
        $ spose='1'
        show shika at c3
        s "Hmm..."
        s "Have you checked to see if the offer is legitimate?"
        ai "Only legitimate offers make it to the job panel."
        ai "So this job really is one billion imperial dollars for capturing a single person."
        ai "Do you feel that you can make an informed decision knowing that?"
        "Well, even if this is some sort of trick..."
        "It would still be worth investigating."
        "But a bounty like this just doesn't simply appear out of thin air."
        "I'm going to have to be careful and approach this analytically."
    "One billion dollars...":
        $ spose='1'
        $ sface='neutral'
        show shika at c4
        "One billion imperial dollars..."
        s "Have you verified if the offer is legitimate?"
        s "I'm not entirely convinced yet."
        s "Is it really that much money?"
        ai "Yes. It really is one billion imperial dollars."
        ai "I understand if you may not believe it at first, Captain."
        show shika at c4
        "So it's actually the real thing..."
        "While I find the whole thing slightly questionable..."
        "I push those thoughts to the back of my mind."
$ spose='1'
show shika flip at c3
s "Please gather as much information as you can on the subject."
s "Prepare a file for me to inspect later."
ai "As you wish."
"One billion dollars..."
"Imagine the possibilities..."
"Although, I cannot just decide this without informing everyone else first."
$ sface='smiling'
show shika flip at c2
s "Please send an alert to all crew members."
s "There is to be a meeting at the bridge immediately."
$ sface='neutral'
$ sbody='sb'
show shika at c3
s "... Actually, cancel that."
ai "Acknowledged."
"Even if I tried to summon the other crew members for a meeting..."
"I doubt they would even turn up."
"Alas, you do not end up in this profession without picking up some eccentric crew members."
$ spose='1'
show shika at c4
s "What are the current locations of our crew?"
ai "Information unavailable."
"I cannot help but let out a weary sigh."
$ sbody='sa'
show shika at c3
s "Then I will just have to go find them."
s "When I get back, show me whatever information you have on the bounty."
s "I want to know what we're up against."
ai "Are you sure you do not wish to have your breakfast before you leave?"
ai "It is important for you to start your day properly."
s "Alright, alright..."
"The ship's AI acts like our nanny, but at least it has our best interests in mind."
"I take a seat at the table."
$ sface='smiling'
show shika at c2
s "What do you have for me today?"
"Several plates hover over to the table."
ai "Today's breakfast is wheat bread, orange juice, and ricotta cheese."

$ sface='neutral'
show shika at c3
s "Can't I have some bacon or something?"
ai "You have had far too much bacon lately."
ai "It is my responsibility to ensure that the captain's health is optimal."
ai "I am afraid I cannot comply with your request."
$ sface='angry'
show shika flip at c3
"... Why did I set up this AI to monitor the crew's health?"
"It's going to make me pull my own hair out."
"Sure, it has my best interests in mind, but it also doesn't have my best interests in mind..."
call h_shika from _call_h_shika_1
stop music fadeout 2.0
scene pool with fade

"After getting ready for the day, I waste no time hunting down the first important crew member."
"If I know her at all, then she will definitely be here."
"She is rather fond of physical activity, after all."
"Not to mention that she commissioned the construction of this swimming pool out of her own funds."

"A loud splash echoes through the otherwise still area."
call s_shika from _call_s_shika_1
s "I had a feeling you would be here, Kotori..."
play music ecchi fadein 2.0
scene cg8
if persistent.adult:
    scene cg8_A
with dissolve
pause

"She emerges from the swimming pool, seemingly going in slow motion."
"As she leans on the side of the pool, her chest squishes onto the floor beneath her."
"Her golden hair shimmers in the ship's lights as she shakes her head."
"A cheeky smile is on her face, her tongue sticking out at me."
k "Good morning, Captain!"
if persistent.adult == True:
    call scene8_A from _call_scene8_A
else:
    "She seems to love wearing tight fitting or skimpy bikinis when she does this."
"Honestly, a little bit of modesty can be alluring in its own way."
k "Oh? Like what you see, Captain?"
"She wiggles her behind at me."
"I cannot help but watch as beads of water trail down it."
"Her cheeky grin grows wider as she watches me."
k "It could be all yours whenever you want, you know..."
k "I know you can't stop looking at me!"
"You would not expect her to be competent, but she would not be on this ship if she weren't gifted."
s "Yes, you have a lovely figure. We have been through this before, Kotori."
k "I know I do!"
k "All of this exercise keeps it in perfect shape!"
"She lets out a small laugh."
"I find it hard to believe that she has the energy to do this every morning."
"She's the first one awake on the entire ship as well."
k "So why is our illustrious leader visiting me in the morning?"
k "Maybe you're finally ready to confess your undying love for me?"
"She gives me a sultry look and winks."
"Honestly, if she were in charge, nothing would ever get done."
k "I can be all yours if you're willing to say a few magic words..."

s "Maybe some other time, I will."
k "Aww, you're such a prude..."
"She makes a pouting face at me."
k "Why can't you just give in?"
s "You know that we have to maintain a semblance of professionalism at work."
"That just makes her wiggle even more."
"Ever the temptress, she is."
k "Well, if it isn't to admire my perfect figure..."
k "What could have our captain so possessed this morning?"
s "To answer your question, I have some news about our next job."
k "Oh? What sort of job are we doing this time?"
"She always gets excited whenever I mention it's time to go to work."

scene pool with dissolve
stop music fadeout 2.0

"She stops lying on the floor and picks herself up."
if persistent.adult==True:
    "She slips on the bottom of her bikini, just for the sake of preserving a tiny amount of modesty."
play music happy fadein 2.0
"Streams of water race down her body as she grins at me."
if persistent.adult==True:
    $ kbody='aa'
else:
    $ kbody='ba'
$ kface='smiling'
call s_kotori from _call_s_kotori
k "There's such a thrill in never knowing what we will do next!"
k "Maybe some corporate espionage? Or peacekeeping work?"
$ kface='happy'
show kotori at c2
k "Come on, don't keep me in the dark!"
$ spose='1'
show shika at c3
s "I will tell you more about it at the meeting."
s "I do not wish to repeat myself pointlessly."
$ kface='laughing'
show kotori at c3
k "Okay, okay! Got it, boss!"
k "Whatever it is, it must be a big job if you're taking it this seriously!"
"Her enthusiasm is certainly infectious."

"I do not think there is anyone else I have met who burns as brightly as Kotori the Golden does."
k "Let me finish my morning swim, then I will be right there!"
$ sface='smiling'
show shika flip at c3
s "As you wish."
s "Perhaps I will invite you to the captain's quarters if I decide to take you up on your offer."
k "You know where to find me when you do!"

call h_kotori from _call_h_kotori
call s_shika from _call_s_shika_2

"She slides back into the pool, filled to the brim with energy."
"There probably isn't a single person I know who is blunter than Kotori."

$ spose='1'
show shika at tcenter
"It has gotten us into trouble more than a few times, because she cannot help but say what she is thinking."

"Oh well. Kotori is a valuable crew member nonetheless."

"Tolerating a bit of eccentricity is necessary at times."
"My next crew member is precisely the opposite..."

"Someone who guards their thoughts very carefully."
"Knowing her, she could be hiding anywhere inside the ship."
call h_shika from _call_h_shika_2
stop music fadeout 2.0

scene hallway with fade
play music day fadein 2.0

show shika at ltl
"Passing through the ship's living quarters, I've decided on the first place to check."
"Chances are she will be in her room."
show shika at tcenter
"I knock on her door, waiting for her to respond."
"Oh... Right."
"There's no point in doing that."
"I open the door with the ship's master key."

scene namiroom with dissolve
$ huer = 1.0
$ hueb = 1.3
$ hueg = 1.0
call s_shika from _call_s_shika_3
"As to be expected of her, her room is completely orderly and tidy."
"Kotori's room is filled to the brim with stuffed toys casually discarded everywhere."
"The cool, blue lights create a cold, calm atmosphere in here."
ai "Please inform me if you wish to bypass someone's security locks."
ai "This is a violation of company policy."
$ spose='1'
show shika at c2
s "I am afraid it was necessary."
ai "Professionalism in the workplace is necessary to ensure a productive environment."
ai "A good leader also leads by example."
$ sbody='sb'
show shika at c1
"I'm just going to ignore the AI for a moment."
"I cannot help but pause whenever I enter her room."
"Just like her, her room is a wonder."
"It feels so cold and tranquil in here."

$ spose='1'
show shika at c2
"Even though there is little decorating it, something about it just makes you pause."
"You just feel like there is something to be in awe of as you sit here."
"Kotori's room has its charm, but so does this room."
"I have lingered here long enough, however."

"There is nowhere that she could be hiding in here."

show shika at rtr
"So, if she is not in her room, then where should she be?"
call h_shika from _call_h_shika_3

scene hallway with dissolve
$ huer = 1.0
$ hueb = 1.0
$ hueg = 1.0
call s_shika from _call_s_shika_4
ai "Keep in mind that you already have a number of jobs to complete around this particular sector."
ai "Your schedule for today includes-"
$ sbody='sb'
show shika flip at c3
s "Cancel all of our current jobs."
s "They aren't necessary."
ai "Are you sure you wish to terminate them immediately?"
ai "This bounty could be months, or even years, of work before you get paid."

ai "I would suggest that you find some sustainable work before you pursue this."
"A weary sigh escapes my lips."
$ spose='1'
show shika at c2
s "I don't have time for sustainable work."
s "If we don't get this bounty first, chances are someone else will."
ai "I do not wish to question your command, but why do you think this bounty is so high?"
ai "It would be a wise decision to let me finish assembling your dossier on the target first."
ai "Making informed decisions is the key to success."

menu:
    "There are plenty of reasons why it would be high.":

        $ investigate += 1
        $ sbody='sa'
        show shika at c3
        s "Well, it is obvious that, judging by the circumstances..."
        s "Our target would either be highly dangerous or someone with political value..."

        s "It is as you say, that kind of bounty would be risky."
        "I stop for a moment to think about it further."
        $ spose='1'
        show shika at c4
        s "Not many people have that kind of money lying around either."
        ai "Correct."
        ai "Now that you're aware of that, do you still wish to proceed with canceling your current jobs?"

        "Now that I'm thinking with a clear head..."
        "Would this really be the wisest choice to make so quickly?"
        "Wisdom dictates that it would be better to analyse the situation fully before stepping into it..."

        "For all I know, I'm about to enter a dangerous game of politics."
        "If this bounty happens to be the wrong person, that could come back on me."
    "The reasons are irrelevant.":

        $ sbody='sa'
        show shika at c3
        s "I don't want anything else getting in the way before we head off."
        s "So just delete the schedule."
        ai "I will ask one more time for confirmation."
        ai "Are you sure that you want to do this, Captain?"
        $ spose='1'
        show shika at c4
        "The reasons for why the bounty is so high doesn't really matter."
        "What's important is the bounty itself."
        "I do not care if I have to wade through the sulfur choked depths of Hell to get this job done."

        "It's going to happen."
$ sbody='sb'
show shika flip at c3
"I am not someone who enjoys taking unnecessary risks."
"But this could be the biggest score of our lifetime."
s "Please proceed with deleting the schedule."
ai "Very well. I shall delete your current job schedule altogether."
ai "Are you sure you want to do this?"
$ sbody='sa'
show shika at c2
s "Of course I'm sure."
"The AI settings for the ship ensure that the AI is allowed a minimum of input regarding decisions."
"It usually gives good advice, so I've never seen the need to turn this setting off."
ai "Just keep in mind that you advertise yourself as having integrity and ensuring that the job gets done."
ai "Hurting your own reputation would be a poor choice."
$ spose='1'
show shika at c3
s "I only get paid after the job is done."

s "They don't lose anything, and I'm free to pursue this bounty."

s "Everyone should be fine with it."
ai "Schedule deleted."
ai "Would you like to schedule your meeting?"

$ spose='1'
show shika at c2
s "That won't be necessary."
"Knowing those two, getting them both into the same room at a specific time is going to be hard enough..."
"Let alone getting both of them to follow a schedule."
ai "As you wish."
stop music fadeout 2.0
call h_shika from _call_h_shika_4
scene pilot with dissolve

call s_shika from _call_s_shika_5
play music night fadein 2.0
"Since we are on a capital ship, it actually requires many different pilots to manage different sections of the ship."

"One of my crew manages a part of it herself in our quarters."
"It's part of company policy. One pilot to every crew."
"My pilot, much like my other crew member..."
"She has her eccentricities."
"But she is the best at what she does."


scene cg9_1
if persistent.adult == True:
    scene cg9_1A
with dissolve
pause
"Nami looks out at the void in front of her."
"Her eyes regard it analytically..."
"Yet somehow, she seems to be filled with awe."
"She is someone who carefully guards her thoughts, so it's often hard for strangers to read her."
"As the ship's pilot, she often has a lot of time to herself, so she tends to space off just like this."
"Usually, she just switches on the autopilot and goes off to do something else."

"If she's sitting here, then there must be something on her mind."
"I am only a few feet away from her, and yet she still hasn't noticed me standing there."
n "Hmm..."
n "Another galaxy..."
n "The stars are as beautiful as ever..."
"She could stare into that blank void for eternity, no doubt."
n "Just what could be out here..."
n "I want to see all of it."
"Ah. Yes. She is always chasing something."
"Whenever I asked what it was, she said that she didn't know."
"Despite the calm facade she wears, I know that she is truly an explorer at heart."

"Someone who is trying to find their answer among the stars."

"When you do not know the question, however..."
"How exactly do you find the answer?"
scene cg9_2
if persistent.adult == True:
    scene cg9_2A
with dissolve

n "Oh..."
n "Captain..."
n "I didn't know that you had come in."
"Her face turns red."
s "I swear, Nami... When are you going to learn to wear clothes?"
n "I... I just find it more comfortable like this..."
n "I-It's not a problem if there's only the three of us, r-right?"
"I can only shake my head."
s "Professionalism, Nami."
s "That is what separates us from the animals."
n "Right, right..."
n "Is... Is there something you needed?"
"She tries to position herself at such an angle that I can't get a good look at her figure."

"It doesn't really help much, for obvious reasons."
s "Do you have a moment? I have some important news that I need to share with everyone."
n "Ah... Yes... I do..."
n "Just... Let me... Let me sort things out around here..."
"It's not just that she isn't wearing much at all."
"She is often used to spacing out since the AI does not disturb her and there are so few crew members on this ship."
"Although, I have to admit that she is rather shy when it comes to being... seen like this."
s "I understand."
s "Please put on something appropriate before we begin our meeting."
n "W-Will do..."
s "Kotori will be meeting us ahead of time."
s "You can walk with me."
n "O-Okay..."

scene hallway with fade
play music day fadein 2.0
"After getting dressed in her suit, Nami seems to regain her composure."
"Despite the suit not being much better than being nude, she seems to focus when she's wearing it."
call s_nami from _call_s_nami
n "So what is this about, Captain?"
n "It is very rare for you to come fetch me personally."
$ spose='1'
show shika at c2
s "There was no other way for me to contact you."
n "Well, yes..."
$ npose='1'
show nami at c4
n "But at this hour?"
n "It is only the morning."
"I will never get used to how we still refer to morning and night..."
"When neither of these things even exist on this ship."
"But I guess that's just to maintain an understanding of time's passage."
n "Normally, you just leave the dossier for our latest job and retreat into the captain's quarters."

$ nbody='sb'
show nami at c3
n "What is so important about this job that requires all of us to be present?"
$ sface='smiling'
show shika at c3
s "Let's just say that I have found a job. A very well paying job."
n "How well paying, exactly?"
n "It must be very important if you're this excited about it."
"Even though she does not show what she is thinking, she can pick up on subtle expressions from other people."
"Secretly, I am so excited for this job that I can barely contain myself."
"And she picked up on that right away."
$ spose='1'
show shika at c2
s "You would be right about that."
s "This job might be the hardest job we ever do..."
s "But it's going to be worth it."
$ npose='1'
show nami at c4
n "Is it going to be anything like the last big job we did?"
s "No, no. No corporate espionage this time."
s "I think all of us are tired of work like that."
n "I would think so too."
hide nami
hide shika
with dissolve

scene meetingroom with fade
play music serious fadein 2.0
call s_crew from _call_s_crew
s "... So that is it, everyone."
s "This is the single largest bounty ever issued for a target in this galaxy."
s "Do you think you're all up for the job?"

$ npose='1'
show nami at c2
n "While I would normally say no..."
n "The stakes are high here."
n "This much money for one job..."
"Nami seems to be interested."
$ kface='happy'
show kotori at c4
k "Wow... We could plate this entire ship in gold with that money!"
k "Just imagine it..."
"Kotori is already drifting off into her little fantasy."
$ nbody='sb'
show nami at c3
n "Just who is this target?"
$ spose='1'
show shika at c2
s "We've been assembling whatever information we can get."
s "We should have a dossier available."
ai "Yes, Captain. The dossier is now available."
s "Please project it on the table."
ai "Acknowledged."
"Soon, the information is displayed before us."
ai "Alias: Akane. Real name: Unknown."
ai "Subject is a notorious criminal who has committed an intergalactic crime spree."
ai "Her weapon of preference appears to be a whip."
ai "Further information on the target is unavailable."
$ kface='neutral'
show kotori at c3
k "A whip?"
k "How can she do anything with a whip?"
"The AI continues, politely ignoring her."
ai "Subject is to be captured alive and delivered in person to the designated location."
ai "She was last seen on this planet."

"The AI displays a map of this sector, highlighting a particular planet."
$ npose='1'
show nami at c4
n "A fully urbanised world on the edge of the galaxy...?"
n "It is little wonder that she is hiding out there."
$ nbody='sa'
show nami at c3
n "Is there any information available on the planet itself?"
ai "The planet is known as a hub for outlaws in this sector."
ai "So she could be potentially using it as a hideout."
menu:
    "We should investigate there, then.":
        $ spose='1'
        show shika at c4
        s "Then how long would it take to reach this planet?"
        s "Are there any eyewitnesses or anyone we can question when we get there?"

        ai "I am afraid that this report was made quite some time ago."
        ai "Also, it would take a very long time for us to reach it from here."

        $ sbody='sb'
        show shika flip at c3
        s "Right. Pardon me."
        s "That wouldn't be practical at all."
        n "Excuse me, Captain..."
    "I don't think she would be hiding there.":
        $ investigate += 1
        $ spose='1'
        show shika at c4
        s "I don't think she would be hiding there right now."
        n "I am in agreement."
        n "Judging by the patterns of her crimes, she hops from planet to planet."
        $ npose='1'
        show nami at c4
        n "She never commits a crime on the same planet twice."
        n "So, it would be reasonable to presume that she wouldn't be there anymore."
        $ sface='smiling'
        show shika at c2
        s "My thoughts exactly."
        s "Rather than following her where she was, we should try to work out where she's going."
        s "It won't be easy, but if we can find some pattern to her crimes."

        $ sface='neutral'
        show shika at c3
        s "Well, we need more information, of course."
        n "I do not wish to distract you from your train of thought, Captain..."
        n "However, there is a pressing issue here which I feel needs to be addressed."

$ npose='1'
$ nbody='sb'
show nami at c2
n "Do we have any other jobs we have to do in the meantime?"
s "I have cleared our entire schedule."
"Nami seems taken aback."

$ nface='shocked'
show nami at c3
n "So we are focusing all of our efforts on this particular mission?"
$ sface='smiling'
show shika at c4
s "Exactly."
s "I know that this seems like a daunting job..."
$ spose='1'
show shika at c3
s "But I am confident that we will be able to pull it off."
$ nface='neutral'
show nami at c2
n "I see..."
"Nami seems to be mulling over the idea."
"I can already tell that Kotori is onboard, however."
$ kface='happy'
show kotori at c3
k "I want to do it!"
k "We have some money saved up, don't we?"
$ spose='1'
show shika at c4
s "That is correct. We have enough money to be able to survive for months if we have to."
s "We have the time we need to execute this job properly."

s "As more information becomes available, we can adjust our plan accordingly."
$ kface='laughing'
show kotori at c4
k "We can't just ignore one billion imperial dollars!"
k "I could buy a pool the size of a lake for that kind of money!"
$ npose='1'
show nami at c3
n "While I disagree with the notion of abandoning a steady income..."
n "I believe that this is the sort of opportunity that you simply cannot pass."
$ nbody='sa'
show nami at c4
n "So, I want to see how this develops."
s "Then everyone is in agreement?"
s "We are going to pursue the single largest bounty ever set in this entire galaxy together?"
$ kface='smiling'
show kotori at c3
k "No complaints over here!"
n "I find this pursuit agreeable."
$ sface='laughing'
show shika at c2
s "I believe there is nothing else to be discussed then."
s "Meeting adjourned."
$ kface='neutral'
show kotori at c3
k "Wait, wait..."
$ sface='neutral'
show shika at c4
s "What is it, Kotori?"
k "We do have one important topic to discuss."
$ kface='happy'
show kotori at c3
k "How do we spend all of that money?"
k "I want a swimming pool that's three times as large as the one we already have!"
$ spose='1'
show shika at c2
s "I am not sure if this is a topic suitable for a meeting."
s "And we haven't got that money yet."
$ kface='laughing'
show kotori at c4
k "It's not a question of if we get the money..."
k "It's a question of when!"
"Kotori's confidence is practically radiating from her."
k "So it's best to start planning ahead!"
$ spose='1'
show shika at c3
s "Yes, we do need to plan ahead..."
s "But we have to make plans to ensure that this actually works out the way we want it to."
$ nbody='sb'
show nami at c4
n "If the target has such a high bounty on their head, then they would not be easy to catch."
n "Especially being involved with planetary government collapses..."
$ npose='1'
show nami at c3
n "I do not think we can take this lightly in any regard."
$ spose='1'
show shika at c2
s "Exactly."
s "Meeting is adjourned for now, everyone."
s "Continue to gather information on the target."
ai "Acknowledged."
stop music fadeout 2.0
call h_crew from _call_h_crew
scene bedroom with fade
play music night fadein 2.0
"I have spent several hours sitting in my quarters, attempting to piece together whatever information is available on the target."
call s_shika from _call_s_shika_6
s "Do we have anything that we can use to identify her?"
show shika at c4
s "Any known preferences, mannerisms, anything at all?"
ai "The only consistent trait to her appearances is the use of a whip as a weapon."
ai "Judging by what little security footage is available, her weapon is capable of incapacitating anyone it wraps around."

$ spose='1'
s "I suppose that is as good a lead as any..."
menu:
    "Perhaps the reports are exaggerated.":
        $ sbody='sb'
        show shika at c3
        s "Don't you think that the reports might not be what they seem?"
        s "They all mention a whip, but there is no way that a whip could be used so effectively in this day and age."
        $ sbody='sa'
        show shika at c2
        s "It's not a weapon of war, so perhaps she is using a weapon that may seem like a whip?"
        ai "Again, judging by security footage, it is a ninety-nine percent possibility that she is indeed using a whip."
        ai "Nothing about the weapon or the way she uses it suggests that it's anything but."
        s "Right..."
        s "Now that is interesting."
    "She must be well trained if she can use a whip like that.":

        $ investigate += 1
        $ sbody='sb'
        show shika at c3
        s "While we have nothing about her background..."
        s "We do know one thing."
        ai "What that might be, Captain?"
        s "To use a whip in such a way..."

        s "Mastering such a weapon, let alone using one in this day and age..."
        s "Not to mention being able to incapacitate armed targets with it..."
        $ sbody='sa'
        show shika at c2
        s "Our target obviously has training of some sort."
        s "Perhaps she is ex-military? A mercenary, maybe?"
        ai "Once again, your observations are impressive, Captain."
        ai "The target does have some sort of training, and she moves fast enough to be able to defeat armed targets in combat."
        ai "Security drones have also proven to be useless against her."
        ai "So, she is not an opponent to be taken lightly."
        s "I understand that..."
        s "I still don't understand why she would be using a whip, though."
$ spose='1'
show shika at c4
s "How many people would still use a whip these days?"
ai "I might also remind you that whips were rarely used as actual weapons, but instruments of torture."
ai "So the probability of whips being used as weapons is exceptionally low."
$ sface='smiling'
show shika at c3
s "Right, right..."
s "So we have a decent lead."
"The next thing we need to work out is the motive behind her crimes."
$ sbody='sb'
show shika at c2
s "Display a list of sightings and their positions throughout the galaxy."
ai "Acknowledged."
"Looking more closely, I do see a distinct pattern of movements."
ai "She has been mostly sighted in this particular sector."

"Which just so happens to be one of the most uncivilised parts of the galaxy."
"With only a few bastions of civilisation dotted here and there."
"No one said this job was going to be easy, I suppose."
$ sface='neutral'
show shika at c3
s "Hmm..."
s "I think I see a distinct pattern."

"The timing between each crime is roughly sixty days."
"The travel time between the planets would be forty-five days on average."

"So, she stays for a little longer than two weeks on each planet."
"There's only a small number of ships which would be able to travel that quickly between the stars."
$ spose='1'
show shika at c4
s "I think we should start on this planet next."

"I point to one in particular in the sector."
s "Judging by the average time between the crimes, her travel time would indicate that she would approach this planet next."
"Wait..."
menu:
    "This seems too obvious.":
        $ investigate += 1
        "With such a simple pattern, anyone could have guessed her course."

        "It's almost as if it's deliberate."
        "But why would she be doing that deliberately?"
        $ spose='1'
        show shika at c3
        "If she's doing it on purpose, perhaps it is some sort of challenge or taunt?"
        "And we obviously wouldn't be the first ones who have seen this bounty..."
        "So, I cannot help but wonder at the deeper implications of what she is doing..."
        "And I can only make vague guesses as to why she is doing this."
        "Somehow, I feel like this is going to be a difficult case."
    "I still don't know where she is going to show up on that planet.":
        $ spose='1'
        show shika at c2
        "Even if I know the destination, a planet is not a small place to keep looking."
        "There are some major docking bays and locations for her to land in, but since she's an outlaw..."
        "There's no assurance that she would use these at all."
ai "Is something the matter, Captain?"
$ spose='1'
show shika at c3
s "Just thinking things through."
s "I believe we should go the next planet it looks like she's going to land on."
$ sbody='sb'
show shika at c4
s "We might not be able to catch her, but we would be close enough to get fresh interviews."
s "So, we should prepare to set a course when we are ready."
ai "Excellent choice, Captain."
ai "Their memories of the target would be the freshest."
ai "Details are lost as time passes, after all."
$ sface='smiling'
show shika at c3
s "Good. We should be able to dock there."
s "Could I request that you return to orbit when you drop us off?"
ai "Acknowledged."
ai "I will remain in-orbit above your position."
ai "If you require assistance, I will not be far away."
ai "With that out of the way..."
ai "Will you be sticking to your regular schedule for today?"
$ sface='neutral'
show shika flip at c2
s "You mean our weekly pool party?"
ai "Yes. You do seem fond of the pool party."
ai "Kotori is especially fond of it."
"It's true. Kotori loves her pool parties."
"She loves spending a lot of money and time on them too."
"It seems like kind of a waste, considering that she only invites Nami and I..."
$ spose='1'
show shika at c3
s "I am afraid that we cannot do that today."
s "We only have a few hours left until we arrive."
ai "Do you wish to be the one to inform her of the party's cancellation?"
$ spose='1'
show shika at c4
s "... Not particularly, no."
ai "Well, I do not wish to be the one to do it either."
ai "So we will have to decide who has to do it."
$ sbody='sb'
show shika at c3
s "No, I'm not doing it."
s "This is why I have you onboard."

ai "This is not a pleasant task..."
$ sface='angry'
show shika at c2
s "But I'm the captain of this ship."
s "I order you to deliver the news."
ai "As you wish."
$ sface='neutral'
show shika at c3
"Well, with that sorted..."
"I suppose I can move onto more important matters."
$ spose='1'
show shika at c2
s "Is there anything else which requires my attention?"
stop music fadeout 2.0
ai "There is one thing, my captain."
s "What might that be?"
$ sface='shocked'
show shika at c3
"Within a few moments, I hear a loud banging at my door."
ai "There it is now."
"I swear..."
$ sface='neutral'
show shika flip at c3
s "Bypass security protocols."
ai "Acknowledged."
"As soon as the door opens, she bursts into the room."
play music funny fadein 2.0
$ kface='shocked'
call s_kotori from _call_s_kotori_1
k "Shhikkkkaaaa!"
k "What do you mean that tonight's pool party is canceled?!"
$ kpose='1'
show kotori at c4
k "You aren't serious, are you?!"

"Kotori looks very upset."
"She does like her pool parties..."
"So I can understand why she would be upset to hear that they have been canceled."

$ spose='1'
show shika at c3
s "Now, now... We don't have the time for a pool party."
$ kbody='sb'
show kotori at c3
k "Can't we make time? Pleaaaaaaase?"
k "We can do that, right?"
$ sbody='sb'
show shika at c2
s "Not really..."
s "We don't exactly have a steady income right now."
s "And pool parties are expensive."
"Her cheeks puff up as she pouts."
$ kface='angry'
show kotori at c4
k "But they're fun!"
k "Having fun is more important than being rich!"
"Being the one in charge of the books around here isn't an easy task."
"Whenever you have to cut back on... certain activities..."
"You end up becoming the villain."
$ kpose='1'
show kotori at c3
k "You used to be fun, Shika!"
$ spose='1'
show shika at c2
s "Now, now, Kotori..."
s "You already spend a lot of time in the pool."
$ sbody='sa'
show shika at c4
s "Having a pool party every week, especially ones as expensive as yours..."
s "They simply aren't sustainable with our current budget."
"Since we're going to be boarding a strange new world soon..."
"We need to save every imperial dollar we can get."
$ kface='neutral'
show kotori flip at c3
k "You're going to have to make up for this..."
s "How exactly do you want me to do that?"
$ kface='laughing'
show kotori at c2
k "I'll be happy with having a kiss on the cheek..."
k "You will be forgiven if you do that!"
"She leans in, presenting one cheek."
k "Come on... You know you want to..."
"I give her a small peck on the cheek."
$ kface='neutral'
show kotori at c3
k "..."
k "That's it?"
$ kface='angry'
show kotori at c4
k "Captaaaaaain..."
"She pouts again."
$ sface='smiling'
show shika at c3
s "Like I said, we have to remain professional around here."
"She only ever calls me by my actual name when she's mad at me."
"The fact that she's calling me Captain is a good sign."
$ kface='neutral'
$ kpose='1'
show kotori at c3
k "Fiiiiiine. Good enough for now, I guess."

k "Our next pool party had better be the best pool party ever, though."
$ kbody='sb'
show kotori at c2
k "Otherwise I will never forgive you."
s "Noted."
$ kface='smiling'
show kotori at c3
k "With one billion imperial dollars..."
k "Our next pool party will be one that is out of this world!"
$ sface='neutral'
"... Well, yes. Since it will be onboard the ship."

call h_kotori from _call_h_kotori_1
show shika at tcenter
"She slips out of the room."
ai "That went better than expected. Don't you think, Captain?"
$ sface='angry'
show shika at c2
s "I was wondering why she came to my room instead of talking to you..."
ai "Well, I simply passed your message along."
ai "And said that she could take it up with the captain."
s "You do that to me every time..."
call h_shika from _call_h_shika_5
"I can only shake my head and laugh a bit."
"The ship's AI can be a pain..."
"But at least it doesn't lack personality."

stop music fadeout 2.0

scene hallway with fade

play music space fadein 2.0
call s_shika from _call_s_shika_7
"I wonder how Nami is doing."
"Kotori and her are as different as the sun and the moon."
$ spose='1'
show shika at c3
"... Such an expression really doesn't make sense outside of the Milky Way."
"Oh well."
"Nami is quite different, to say the least."
"I can hear loud echoes coming from the training room."
"Let's see what's going on in there."

scene simulation with dissolve

call s_shika from _call_s_shika_8
"I step inside the training room's observation deck."

"Sure enough, there she is."
call s_nami from _call_s_nami_1
"Quietly, she stands to attention."
ai "So what settings would you prefer for this particular combat scenario, Nami?"
$ npose='1'
show nami at c4
n "Medium difficulty this time."
n "I need a warm up before I really get into it."
ai "Acknowledged."
ai "Preparing simulated environment..."
"As the AI speaks, a number of different hills, objects and obstacles begin to emerge around Nami."
"In addition to that, I begin to see a number of different drones lazily drifting through the air around her."
"They dive in between cover and obstacles, like how a fish would hide underneath a rock in an aquarium."
stop music fadeout 2.0
"It sets the stage for quite an interesting engagement."
scene cg1
if persistent.adult==True:
    scene cg1_A
with dissolve
play music battle fadein 2.0
"Unlike how awkward she was before, Nami's eyes are filled with clarity."
"She carefully analyses her environment, fully prepared for any threats coming her way."
ai "Beginning combat exercise in ten seconds."
"As the AI counts down, she seizes her blade and enters a battle stance."
ai "3... 2... 1..."
ai "Begin."
"Holographic enemies appear in the room."
"A complete circle of security drones surrounds her."

"They begin to home in, unleashing a barrage of holographic pellets."
"Nami does not miss a beat."
"With a fluid movement, Nami strikes down the holographic drones without missing a single beat."
"Her plasma cutter hums and sings as it flashes through the air."
"A flash appears behind her as one of the drones fires a holographic missile."
"With incredible reflexes, she dodges the rocket completely."
"Holographic sparks spray through the air as she slices through the drone."
"Her body moves with perfect precision, beautiful and graceful."
"A larger drone appears, two miniguns sitting on either side of its hulking shape."
"It unleashes a figurative death storm of bullets, practically filling the entire room with holographic sparks."

"Even through that digital haze, Nami does not lose her cool."
"She slides underneath the drone as it continues to fire, slicing open its belly."
"It disappears in a burst of pixelated explosions."
"More and more virtual drones continue to pour into the room."
n "Increase difficulty."
ai "Acknowledged."
"The drones immediately respond."
"They move in ever-shifting patterns, actively attempting to flank and keep their distance away from Nami's deadly blade."

"Yet it does not seem to help at all."
"Nami moves like a blur, cutting them down within seconds of materializing."
"Bit by bit, the stream of virtual combatants begins to slow down."
"Until no more enter the room at all."
"Without much more fanfare, she cleans up the remaining drones."
"Soon, it is just her standing in the room."
"She does not even appear to be breathing particularly hard."
n "How are my results?"
ai "Your combat performance was exceptional, Nami."
ai "The time between an enemy entering the room and being eliminated is only a few seconds."
ai "All hostile entities in the simulation were eliminated with little to no delay."
ai "You are in peak condition for combat operations against nonorganic targets."
ai "Overall, this has been your best performance since you helped quell that robotic uprising."
n "Good."
n "We may need to defend ourselves at a moment's notice."
n "Especially against nonorganic foes."
"She holsters her sword and stretches."
n "I think it would be good to take a short nap now."
n "It has been some time since I have gotten a good night's sleep, after all."
ai "That would be a good idea."
ai "You did not sleep particularly well last night. I can tell."
stop music fadeout 2.0
scene simulation with dissolve

"Slowly, the virtual environment around her dissipates into pixels."

$ nface='shy'
$ npose='1'
call s_nami from _call_s_nami_2
play music day fadein 2.0
n "Oh... Captain..."
n "I didn't know you were watching..."
$ sface='smiling'
show shika at c2
s "That was a very impressive performance, Nami."
s "It always amazes me to watch you fight."
$ nbody='sb'
show nami at c3
n "R-Right, thank you..."
"She gets awkward when she realizes someone has been watching her do something."

$ npose='1'
show nami at c4
n "C-Could you please let me know if you're watching?"
n "It... It just throws me off a bit..."
$ sface='neutral'
show shika at c2
s "I didn't want to interrupt you when you looked so focused."
s "You are a stellar combatant, Nami."
$ nbody='sa'
show nami at c3
n "T-Thank you..."
"I swear. Nami really is too shy for her own good."

"How is it that she is unable to handle someone looking at her while she works?"
"I suppose it's just part of her personality..."
"We have been working together for a very long time, and I have yet to see her act any differently."

$ nface='neutral'
show nami at c4
n "I... I wanted to get ready for when we confront our bounty."
n "After all, practice does make perfect, doesn't it?"
$ sface='smiling'
show shika at c2
s "You are right."

"Nami always practices."
"She is, by definition a perfectionist."
$ spose='1'
show shika flip at c3
s "So what scenario did you use the simulation room for this time?"
"Considering that the simulation room can simulate anything you can imagine..."

"There is no lack of choices for training."
$ npose='1'
show nami flip at c4
n "Full-scale invasion of Earth."

n "It's like the one from that old game we used to all play together..."
n "You remember how we used to do that one dungeon where robots invaded Earth?"
$ sface='neutral'
show shika at c3
s "Oh yeah. I remember that."
s "When is the last time they have made a decent MMO in the Milky Way, anyway?"
$ nbody='sb'
show nami at c2
n "You know what it's like with the industry these days."
n "No innovation. Nothing new."
n "Just the same old boring grinding."
$ sbody='sb'
show shika at c4
s "It's true."
$ nface='smiling'
show nami at c3
n "We should find another game, though."
n "It was fun back in the day..."
n "Although this onboard simulator is amazing too."
$ sface='smiling'
show shika at c3
s "Definitely the best purchase we have made."
$ sface='neutral'
show shika at c2
s "Training before this thing was a nightmare..."
"It sends shivers down my spine as I remember how badly Nami and Kotori damaged the ship with their sparring matches."
s "What else have you tried simulating on it?"
$ nface='neutral'
show nami at c2
n "Just combat situations, mostly."
n "Nothing too special."
$ sface='smiling'
show shika at c4
s "You aren't even pushing this thing to the limits of its hardware."
s "Maybe you could even simulate entire dungeons from the games we used to play..."
n "Well, I don't want to run the risk of burning it out."
n "Remember what happened when Kotori tried to simulate an entire MMO?"
$ sface='neutral'
show shika at c3
s "Yes. And that is why Kotori is no longer allowed in the simulation room."
"At least she's content to spend most of her time at the pool instead of breaking the ship's hardware these days..."
$ npose='1'
show nami at c3
n "So the target uses a whip as her weapon?"
s "That's what the reports say."
$ nbody='sb'
show nami at c4
n "Why a whip, of all things?"
n "What about it is so special?"
$ spose='1'
show shika at c2
s "It is a massive universe we live in, Nami."
s "Finding someone proficient enough with a whip to use it in combat..."
s "It is not exactly impossible."
$ nbody='sa'
show nami at c4
n "While true, anyone could apply themselves to learning any other weapon..."
n "And overall end up being much more effective."
n "Simulate: Humanoid with whip weapon."
ai "Acknowledged."
n "Simulate: Unarmed humanoid."
"For a few moments, we watch the simulation."
"The armed humanoid attacks the other one with its virtual whip."
"Nami analyses it carefully, noting which angles and methods the whip-wielding simulation uses."

$ npose='1'
show nami at c3
n "Hmm..."
n "This is only a very basic simulation, but it gives me a rough idea of how she could approach combat."
"She nods to herself."
$ nface='smiling'
show nami
n "I have a few ideas for countering it now."
menu:
    "There is more to her than a whip.":
        $ spose='1'
        show shika at c2
        s "Do not get over confident."
        s "There is a lot more to Akane than a whip."
        "Considering that she threw an entire army of drones at me from out of nowhere..."
        "We have to be careful that she doesn't try to attack us in other ways."
        "Waging a war with nothing but proxy drones is something she is capable of."

        $ nface='neutral'
        $ npose='1'
        show nami at c4
        n "I think so too."
        n "Although she is overconfident and would readily show her face whenever she wants..."
        $ nbody='sb'
        show nami flip at c3
        n "That does not mean she lacks the resources to be able to defeat us without revealing herself."
        n "Perhaps it would be better to focus on my training against the sentinels..."
        s "There is nothing wrong with training to prepare yourself for both possibilities, however."

        $ nface='smiling'
        show nami at c3
        n "Definitely, Captain."
        n "I will make sure that I am prepared to fight against anything that she throws at us."
        $ sface='smiling'
        show shika at c3
        s "I have no doubt that you will, Nami."
    "I think so too.":
        "I think that being able to simulate the basic aspects of her fighting style would be useful."

        "Whips are uncommon weapons."
        "Especially in this era."
        $ sface='smiling'
        s "Keep up the training. It is a good idea."
        $ npose='1'
        $ nface='neutral'
        $ npose='1'
        show nami at c4
        n "Hmm..."
        n "I think that I should not invest too much confidence into this, however."
        n "Don't you think that she could easily use other weapons too?"
$ npose='1'
$ nbody='sa'
show nami flip at c3
n "Do we have any more information since we left that meeting?"
$ sface='neutral'
$ spose='1'
$ sbody='sa'
show shika at c2
s "Deducing what we have observed, she is obviously someone with training."
s "You cannot simply commit crimes in broad daylight and evade the police like that."
$ spose='1'
show shika flip at c3
s "It could be chalked up to luck, but she has managed to do it consistently."
s "So, we can presume that she is armed, dangerous, and very competent."
$ nface='smiling'
show nami at c3
n "That is a good presumption."
n "Is there anything else notable that you have managed to deduce?"
$ sface='smiling'
show shika at c2
s "We have worked out a rough estimate of where she might appear next."
s "Once more information is available, we will proceed to where she's expected to appear next."
$ sbody='sb'
show shika at c3
s "The first part of our bounty hunt will be an investigation."
s "We need to work out where she is before we can attempt to take her down."
$ nface='neutral'
show nami at c4
n "Not only that, but we do not know anything about her connections."
n "She could have an entire cartel of criminals at her beck and call."
$ sface='neutral'
show shika at c4
s "Are you having second thoughts about this bounty, Nami?"
$ npose='1'
show nami at c3
n "Not second thoughts..."
n "We will probably never see another job like this again."
$ nbody='sa'
show nami at c2
n "But it is a good idea to plan ahead for potential danger."
s "I agree."

$ nface='smiling'
show nami at c3
n "Anyway, I would like to get some more practice in."
n "I will speak to you later, Captain."
$ sface='smiling'
show shika flip at c3
stop music fadeout 2.0
s "Until then, Nami."
hide shika
hide nami
with dissolve
scene bedroom with fade
play music night fadein 2.0
$ sface='neutral'
$ spose='1'
$ sbody='sa'
call s_shika from _call_s_shika_9
"My mind has been in a rush since this whole thing began."
"I need a moment to clear my head."
"Another cup of cheap coffee, and plenty of time to myself."
$ spose='1'
show shika at c2
"I haven't started anything yet. Nothing has been set in stone."
"This is very deliberate on my part."
"Since I have rushed to get ready for this job, I am going to end up doing a poor job of it if I keep this up."
$ sbody='sb'
show shika at c3
"I have made plenty of observations and presumptions..."
"But what I really need to do now is clear my head."
"At least, I think that would be the best course of action."
menu:
    "Yes, it would be.":
        $ investigate += 1
        "Right. I need to calm down."
        "Unless I look at this with a clear head, all I am going to end up with is a jumbled mess."
        "I need just to sit back and carefully analyse the whole situation."
    "I cannot afford to rest just yet.":

        "No, no. This isn't the best time to relax."

        "I'm already through several cups of coffee."
        "How could I possibly relax after that?"
        "I cannot afford to rest right now."
        "What else needs to be done? How else can I possibly plan for this?"
$ sbody='sa'
show shika at c4
"Fortunately, I have turned off the speakers in my room."
"While our AI is always helpful, I do not think I need to speak with it right now."
"What would be best for me right now is to be by myself."
"I do not need anyone distracting me from my own thoughts."
"Let me think, let me think..."
$ spose='1'
show shika at c3
"She has been sighted on multiple planets, but she only ever revealed herself once..."
"And wherever she went, chaos followed in her wake."
"Judging by that information, she must work systematically."
$ sbody='sb'
show shika at c2
"That little bit of information will be handy if it is true."
"With a bit of work, I have already noticed a pattern in between her crimes."
"There is a delay as she travels in between these planets."
"However, the crimes themselves..."
$ sbody='sa'
show shika flip at c3
"There does not appear to be any real link between any of them."
"Sometimes it's significant property damage... Sometimes it is merely stealing something petty..."

"She did take some artwork from a local art gallery once, but it was a piece not done by anyone special."

$ spose='1'
show shika at c3
"Who is she? And why is she doing this?"
"This is what I cannot work out."
$ sbody='sb'
show shika at c2
"And none of her crimes seem to be worthy of intergalactic attention..."
"Now that I think about it, everything about this bounty seems bizarre."
"Just who is she?"
show shika at ltl
"I pull out a digital pen and a pad."
"One of the ways that I work out something is with a pen."
"It's impossible to buy paper these days, so I just make do with a digital pad."
show shika at tcenter
"Sitting back down at my desk, I begin to draw out my thoughts."
"So, her first notable crime started on this planet, in this city..."
"But none of the businesses or places she was sighted had any connection to each other, as far as I can tell."
$ sface='shocked'
show shika at c3
"Wait... Where were these places located?"
"Was there something close to them that I could connect them to?"
"Now that I think about it..."
$ sface='neutral'
show shika at c2
"The locations of the crimes were always close to... police stations?"
"Then perhaps her motive is mocking law enforcement?"
"Or is it for the thrill?"
"But these details would have become readily apparent to anyone else investigating the case..."
"So why hasn't anyone stopped her yet?"
$ sface='shocked'
show shika at c3
"All of the details swirl around in my head..."
"I have to stop for a moment and calm myself down."
$ sface='neutral'
$ spose='1'
show shika at c4
s "There are patterns..."

s "But surely someone else would have observed these..."
stop music fadeout 2.0
s "So what does all of this mean..."

scene black with dissolve

"...?!"
"What?! Someone's in the room!"
"Whoever they are, they've blocked my vision!"
"Did someone slip onto the ship when I wasn't looking!"
s "Who's there?!"
"I immediately reach for my pistol."
"Before I can do so, they pull their hands away."

scene bedroom with dissolve

"With lightning reflexes, I turn around to see who's there."
$ sface='angry'
$ kface='laughing'
$ spose='1'
$ sbody='sa'
call s_kotori from _call_s_kotori_2
play music funny fadein 2.0
k "Guuuuuuuess who!"
"She's pulling a silly grin at me."
$ sface='neutral'
show shika at c2
s "... Nice to see you too, Kotori."
"I was so deep in my own thoughts that I did not hear her enter the room."
"I pull my hand away from my pistol."
$ kface='happy'
show kotori at c4
k "You should have seen the look on your face!"
k "It's so much fun to see our cool Captain lose her composure!"
"Kotori is always doing things like this."
$ kface='smiling'
show kotori at c3
k "But it was kind of nice just to sit there and watch you thinking to yourself..."
$ spose='1'
show shika at c3
s "Right..."
"She's fully dressed in her battle gear."
s "I see that you're wearing your equipment..."
$ kpose='1'
show kotori at c2
k "Well, it's been a while since we've had a big job..."
k "So I've been doing some training!"
"Her daggers are glowing, obviously a sign that they've been used recently."
$ kface='happy'
show kotori at c3
k "I've gotten a bit rusty, but that's nothing a little effort won't fix!"
"When she gets the motivation to do something, Kotori does it like no one else ever could."
"Whether that is a good thing or bad thing... Only time can tell."
$ kface='smiling'
show kotori at c2
k "I was just wondering what our illustrious captain was thinking about!"
s "Just working out the details on our bounty..."
"I've bet everything on this case."
"Not only that, but it's going to be a difficult case to crack."
"With space travel as fast as it is these days, she could be anywhere in this sector."
"I only have very vague information to work with too."
"So what do I do?"
$ kface='happy'
show kotori at c3
k "I know you can work it out."
k "After all, you just need to wait!"
$ kpose='1'
show kotori at c4
k "She will slip up somewhere, and you will get more and more info as time goes on."

$ spose='1'
show shika at c4
s "I do not know if we will be so lucky..."
s "The trail is a bit stale, even if we arrive there soon..."
$ kface='smiling'
show kotori at c3
k "You're overthinking it!"
k "Just relax for a moment!"
k "I could see you working yourself into a frenzy!"
"She does have a point."
"Even when I'm sitting up here, my thoughts are far too erratic."
"I need to calm myself down."
$ sface='smiling'
show shika at c3
s "I think I shall take your advice."
$ kface='laughing'
show kotori at c4
k "Happy to help out, Captain!"
k "I expect another kiss as a thank you since you're such a generous and kind-hearted Captain..."

$ sface='laughing'
show shika at c2
s "Don't push your luck."
$ kface='neutral'
show kotori flip at c3
k "Yes, yes, professionalism..."
"She winks at me."
$ kface='smiling'
show kotori flip at c4
k "You will give it up one day. I'll charm you out of it."
call h_kotori from _call_h_kotori_2
"She disappears as silently as she arrived."
if persistent.adult==True:
    call scene17_A from _call_scene17_A
else:
    stop music fadeout 2.0
    "Maybe I will give up one day..."
call h_shika from _call_h_shika_6

scene shop with fade
if persistent.adult==True:
    "It always helps to have some time to yourself..."
    "I feel thoroughly refreshed."
    "But it's best not to dwell on that for the whole day."
play music day fadein 2.0
"The ship we live on is quite a sizeable one."
"Since the operations of this mercenary company span across many parts of the galaxy, there are many different teams who live onboard."

"Every team has their own living quarters, and there are even onboard shops."

"They can even have AIs which act as administrators in their quarters if they so wish."
"Our AI signals us as we step out."
ai "Keep in mind that you currently do not have an income."
ai "This job you have picked is not going to pay for some time."
ai "So do be careful with your budget."
$ npose='1'
$ nbody='sa'
$ nface='shy'
$ sface='smiling'
$ kface='smiling'
call s_crew from _call_s_crew_1
s "Thank you again."
s "Come on, everyone."
"Nami stands there awkwardly in her suit."
n "Do... Do we have to?"
$ sface='neutral'
show shika at c2
s "Well, if you do not want to go, then you can just stay in our quarters."
n "No, no... I want to go..."
"When she isn't training or on a mission, Nami is very awkward around other people."
"She's trying to get better at it, however."
"Kotori, on the other hand, has to be restrained when she's around other people."
"She acts too much like an overly friendly labrador when she's in public."

$ kface='happy'
show kotori at c4
k "I wonder how everyone is doing today!"
$ spose='1'
show shika at c3
s "Remember, you are representing the pride of our company when you're out in public, Kotori."
s "You must act in a dignified, professional manner."
"She's not listening, however."
$ kface='laughing'
show kotori at c3
k "Come on! Let's see what new gadgets they have here!"
"She's practically pulling me by my arm, with Nami trailing close behind."
"Perhaps it would have been a better idea to stay in our quarters after all..."
"Then again, most of the company are familiar with their shenanigans."
"So perhaps this won't be too much of a problem."
"These two cause such a scene between the both of them."
"I will just have to roll with the punches this time."
"As we pass by a cafe, I can hear the mercenaries chatting amongst themselves."
merc "So have you heard about that one billion dollar bounty?"
smerc "Who hasn't heard about it?"
merc "Everyone here wants to have a crack at it, you know."
"Well, it looks like the bounty has not gone unnoticed."
"This means we will have to be careful too."
smerc "It sounds like a whole lot of talking about nothing to me."
merc "What, one billion imperial dollars is nothing?"
"The mercenary snorts."
merc "Sorry that we aren't all driving diamond encrusted ships like you are."
smerc "You know that diamonds are worthless in this galaxy."
smerc "They've been mining a damn planet made of the stuff for years."
merc "You know what I mean!"
merc "The point is that even if it turns out to be a hoax, it's worth having a look."
smerc "That would just be a waste of everyone's time."
smerc "There's no way of knowing if the bounty is legit or not."
smerc "They probably wouldn't pay up at the end of it either."
smerc "If someone has that kind of dough just lying around..."
smerc "Then they probably have the kind of hired muscle to ensure that the merc who claims the bounty mysteriously disappears."
merc "Well, when you put it like that..."
merc "Maybe it'd be better to stick to a safer job."

smerc "There's no replacement in this world for hard work, sadly."
$ kface='smiling'
show kotori at c2
k "Looks like everyone is excited about this bounty!"

$ sface='neutral'
$ spose='1'
show shika at c4
s "It would seem that way..."
merc "Hey, you lot, do you mind?"
smerc "We're trying to have a conversation here!"
$ spose='1'
show shika at c2
s "My apologies, gentlemen."
"No point in starting a fight."
"Passing by the electronics shop, Kotori's eyes glimmer with excitement."
$ sbody='sb'
show shika at c3
s "Remember that we have to be careful with our budget for the time being."
s "Only buy things which are essential."

$ kface='happy'
show kotori at c2
k "All of this looks fairly essential to me!"
"I just shake my head."
"Nami, however, does not appear to be interested in any of it."
s "Is there something that you wanted to see while we're here, Nami?"
s "There are a number of different things you can buy here..."
$ nface='neutral'
show nami at c4
n "I want food."
n "We have not restocked in ages."
"She makes a fair point."

$ sface='smiling'
show shika at c4
s "Oh... Right."
s "That is an excellent idea."
s "We have to restock on bacon, first and foremost..."
$ npose='1'
show nami at c3
n "You should really cut back on the bacon."
s "Not you too..."
$ kface='smiling'
show kotori at c3
k "If you plan to have so much bacon, you should really do swimming with me!"
k "It will be a great way to burn off all of that fat!"
$ sface='angry'
show shika at c3
s "It isn't that bad!"
s "And I do plenty of work!"
"Everyone in my crew is so carefree."

"I sometimes wonder if there is any point in me being the captain at all..."
$ npose='1'
show nami at c3
n "What we need to do is buy an array of healthy, fresh ingredients."
n "I know many diet plans which would be perfect for energy and combat awareness."

$ nbody='sb'
show nami at c2
n "Perhaps you would like to try it, Captain?"
n "What about you, Kotori?"
$ kface='happy'
show kotori at c4
k "Nope! I am just fine as I am!"
n "But your diet is far from optimal..."
$ kpose='1'
show kotori at c3
k "My stomach works very different from everyone else's..."
k "You see, it's highly important that I get the right amount of sugar daily!"
k "How else do you think I have all of this energy?"
"It would explain a lot, in retrospect."
$ sface='neutral'
show shika at c3
s "Anyway, that will not be necessary."
s "Just stock up on a variety of different supplies."
$ spose='1'
$ sface='smiling'
show shika at c3
s "If you can make something healthy from our stores, then great."
s "If not, then we will just make due."
"Earth-like ingredients are few and far between on this ship."
"Since we pass by all sorts of different places, you can end up with some... exotic ingredients."
"Let's just hope that no one decides to pick up a piece of fruit because it looks pretty."
stop music fadeout 2.0
$ sface='neutral'
show shika at c2
s "..."
$ kface='neutral'
show kotori at c4
k "Is something wrong, Captain?"
$ nbody='sa'
show nami at c3
n "You seem troubled."
s "I just remembered that I had something I needed to do."
$ spose='1'
show shika at c4
s "You two go ahead without me."
$ kpose='1'
show kotori at c3
k "Are you sure it's nothing?"
$ sface='smiling'
show shika at c3
s "Yes, yes. Please, I'll be fine."
"The two of them seem reluctant, but they don't say anything."
$ kface='smiling'
show kotori at c3
k "Okay! We'll be back before you know it!"
k "Let's go buy dinner, Nami!"
$ npose='1'
show nami at c2
n "Understood..."
hide nami
hide kotori
$ sface='neutral'
show shika at tcenter
"The two of them disappear out of sight."
"Good."
call h_shika from _call_h_shika_7
scene backalley with fade

play music serious fadein 2.0
"I go to an isolated part of the ship, where I'm sure no one else is around."
call s_shika from _call_s_shika_10
s "Alright. You can come out now."
s "Now what business do you have with me?"
"It's probably just my imagination."
"Maybe those two mercenaries who we were listening to earlier..."
"Around here, people tend to solve their disputes that way."
"Strictly nonlethal, of course."
"It goes against company policy to injure other employees."
"For a long time, there appears to be no one there."
"I then hear a giggle echo through the hall."
au "Oh... I am just curious about you..."
"It's a woman's voice."
"I know better than most people that you get a lot of strange people on this ship..."
"It's massive, and it passes by many different space stations and hubs throughout the galaxy."

"However, something about this woman..."
"It makes me uneasy."
$ spose='1'
show shika at c4
s "If you were just curious about me, you could have simply approached me."
s "And yet you followed me all the way here."
s "I cannot help but doubt that you have good intentions..."
au "You possess a very analytical mind."
au "Tell me, Captain Shika..."
au "Who do you think I am?"
$ sbody='sb'
show shika at c3
s "You must be a drifter of some sort..."
s "I am not good with faces, but I'm familiar with the teams who work around here..."
s "Anyone who knows me also knows better than to try and start a fight with me."
$ spose='1'
show shika at c2
s "I find it hard to believe that a random drifter happens to have business with me..."
s "So just who are you meant to be?"
au "Oh, believe me, we are connected."
au "You took up a bounty job recently, didn't you?"
au "Like everyone else here, you do odd jobs, and I'm sure that such a massive bounty would be irresistible to you..."

$ sbody='sa'
show shika flip at c3
s "You seem to know a lot about me..."
"That's a bit unsettling."

"Some strange woman followed me like this and I was only able to get a vague feeling of being watched."
"Whoever this person is, they are excellent at concealing themselves."
"That is cause for concern."

"I cannot help but let my hand rest on my pistol."
au "You would be surprised at how popular your crew is."
au "It does not matter what job you do, you always do it."
au "You have something of a cult following throughout the galaxy..."
au "What I find odd, however, is that you're completely unaware of this."
au "There are people who report sightings of your crew everywhere you go!"
$ sface='shocked'
show shika at c3
"... This is the first time I have ever heard of this."
"Just what kind of fan base do we have then?"
"I do not exactly glue myself to a digital pad like Kotori does..."

$ sface='neutral'
show shika flip at c4
"But that's something I have to worry about later."
au "There's also another detail."
au "Isn't it publicly available information when a team picks up a job?"
"That's right..."
"You have to make a declaration to the company when you take up a job."
"Every other employee onboard the ship can find out who is doing what job if they look it up..."

"So somehow, this woman has gotten that information..."
"And she became aware that my team has chosen this case."
"However, there would be hundreds of names on it by now, judging by the interest generated."

$ spose='1'
show shika at c4
s "So why did you single my crew out then?"
s "What exactly makes us stand out among the hundreds who are taking up that job."
au "Oh, but you are very special, Captain..."
au "No other mercenary company onboard has a success rate as high as yours, do they?"
$ aface='smiling'
call s_akane from _call_s_akane
"It's then that the woman finally steps out from the shadows."
"Her appearance..."
"Wait, what's that she's holding?"
"It all suddenly clicks into place."
$ sface='shocked'
show shika at c2
s "So you must be Akane then..."
s "But how did you end up here?"
"She looks interesting, to say the least..."
"The whip that is her signature rests in one of her hands."
$ aface='smiling'
show akane at c4
a "I have no doubt that you figured out the pattern..."
a "But there was one other small detail you missed."
a "A company ship also happened to visit the planets you are talking about..."
"It's then that it hits me."
$ sface='neutral'
show shika at c3
s "So a company employee has been the one causing this mayhem..."
s "Something about it did seem familiar to me."
s "In other words, it was you."
$ apose='1'
show akane flip at c3
a "Precisely."
a "You're a sharp one, aren't you?"
a "That ship just so happens to be docked on this capital ship..."
"She's just giving all of this away so easily..."
$ spose='1'
$ sbody='sb'
show shika at c2
s "You wouldn't reveal this information unless you were supremely confident that you wouldn't be caught..."
"Although I am not certain that this woman is really who she claims to be yet..."
"What she is doing does fit in with my previous theories about her."

"She leaves visible trails and clues on purpose."

"She must believe herself to be untouchable, even by people who are extensively trained."
"Now that is a bit worrying, considering that I'm facing her by myself."
$ aface='laughing'
show akane at c3
a "Also correct."
a "But I don't think I'll tell you why I'm untouchable by you."
$ aface='smiling'
show akane at c2
a "You enjoy a bit of detective work, don't you, Captain?"
"Well, my job does often require me to employ using detective skills..."
$ sbody='sa'
show shika at c4
s "That's already something else that I have an idea of."
s "You have training. I can tell by the way you move."
"Even now, she has cat-like grace."
"She's carefully poised, just standing in the right position."
"Judging by the length of her whip, I would guess she has about a three-metre reach."

"And she just happens to be roughly that close to me right now."
$ apose='1'
show akane at c1
a "You would be correct, once again."
a "Before, you asked me why I picked your crew."
a "What do you think is the answer?"
menu:
    "A potential threat.":
        $ investigate += 1
        $ spose='1'
        show shika at c3
        s "If I were to think about it logically..."
        s "You would view us as a potential threat."
        s "You mentioned that we have the highest success rate of missions among this company's mercenaries."
        s "So, if I were going to protect myself, I would eliminate my most dangerous opponents first."
        $ sbody='sb'
        show shika at c2
        s "How far am I off the mark?"
        a "You would be right..."
        a "However that is not the only reason."
    "Perhaps selected at random?":

        $ spose='1'
        show shika at c3
        s "You said that we have a high success rate..."
        s "But there are many other competent mercenary companies here."

        $ sbody='sb'
        show shika at c2
        s "So, perhaps you selected someone at random?"
        a "Not at all."
        a "I picked you very much on purpose."
$ abody='sb'
show akane at c2
a "Despite everything, I am a very big fan of yours."

a "Wouldn't it be fun to get involved with one of your adventures, I thought to myself..."
$ spose='1'
show shika at c4
s "Did you set up this bounty deliberately, just to lure me out?"
a "Oh no, it wasn't me."
a "I'm just taking advantage of the situation."
"Her whip begins to crackle with power."
$ apose='1'
show akane at c3
a "So can the great Captain Shika and her crew capture Akane, the enigma?"
"I can't help but let a smirk form on my face."
$ sface='smiling'
show shika flip at c3
s "Akane the enigma..."
s "Quite a grandiose title you've given yourself."
$ aface='laughing'
show akane flip at c3
a "From what I've seen, your adventures are the definition of grandiose."

a "So I would not want to disappoint."
a "I can't wait to see what sort of fun we will have together."
"She already sounds like she's sure of her victory."

$ sface='smiling'
show shika at c3
s "However, there is just one detail that you overlooked."
s "And that will ultimately be your downfall, Akane."
$ aface='smiling'
show akane flip at c2
a "Whatever might that be, Captain?"
s "You just saved me the trouble of finding you myself."
s "Are you sure that you're ready to play a game of cat and mouse with my crew?"
$ spose='1'
show shika at c4
s "Because I don't think you are."
s "You have training and experience, but you're way too early to be able to beat some of the best in the business..."
s "If you know me, then you know that you're going to be in for quite the fight."
"Akane just giggles."
$ aface='laughing'
show akane at c4
a "Oh, I most certainly am ready."
a "After all, you still have a lot of missing pieces to the puzzle."
a "All you know at the moment is my alias."
$ abody='sb'
show akane at c5
a "I'm just a drifter who came onto this ship recently."
a "No one else here knows my face or my name."
"She begins to slip back into the shadows."
call h_akane from _call_h_akane
a "I will see you soon, Shika."

a "I cannot wait to see what sort of fun we will have together..."
"It's then that I see many security drones drifting in from the hallways."

"All of them look like newer models."
"Faster reflexes, better networking, more precision..."
"Not the kind of thing you can just find lying around."
$ sface='laughing'
show shika at tcenter
s "Oh? You were even kind enough to leave me some target practice..."
"I have to take a moment to analyse them before I strike."
"As far as I can see, they're equipped with non-lethal weapons."
"She said she was a fan, so I'm just going to presume that she isn't out to kill us..."
"But if I actually got hit by those drones, it would be rather humiliating."

stop music fadeout 2.0
"Reputation is everything in this line of work, after all."
call h_shika from _call_h_shika_8

play music battle fadein 2.0
scene cg11
if persistent.adult==True:
    scene cg11_A
with dissolve

"I retreat and pull out my pistol."
"A barrage of paralysing rounds rains down from above."
"I dive behind cover."
"They're only robots, so I don't have to adjust my pistol's destructive power."
"Squeezing the trigger, I feel a powerful blast erupt from its barrel."
"An explosion takes out a portion of the drones, but more and more arrive from seemingly out of nowhere."
"Ahh, they're the compact model."
"So they shouldn't be too hard to deal with."
"But overwhelming numbers may be a problem..."
"I duck from cover to cover, firing at drones whenever I get a clear shot."
"I'm not taking them down, however..."
s "Pistol configuration: Fully automatic."
"Instead of concentrating all of the energy into pistol shots..."
"I fire a spray of deadly pellets at the enemy."
"They pierce through the drone's light plating, destroying large quantities of them every time I come back out from behind cover."
"It's then that the drones begin to change their tactics."
"They begin firing shots which have an arc, attempting to shoot me while I'm still behind cover."
"I'm forced to roll out into the open to avoid being stunned."

s "Pistol configuration: EMP."
"Most drones these days are shielded from EMP-type attacks."
"My pistol doesn't have enough punch to be able to destroy them..."
"But this should be enough to stun them while I find new cover."
"For a moment, the drones scatter in the air erratically."
"Several of them crash into each other, causing them to fall onto the metal floor in a crumpled heap."
"But that still leaves a sizeable number of them."
"Unleashing another barrage of automatic fire, it's soon down to just a few of them."
"The AI which runs these networked drones seems to be in disarray."
"The drones are retreating from the hall, regrouping at the end of it."
"This time, they approach slowly."
"It's a systematic approach, slowly eliminating potential places where I can take cover."
"But it isn't going to help."
"Now that there's only a few of them left..."
"I do not have to worry about cover as much."
"As soon as I step out, all of them lock their targeters onto me."
"Fortunately, paralysis rounds move a bit slower than conventional bullets."
"I'm able to stand out in the open, dodging the projectiles with ease."
stop music fadeout 2.0
"I fire back, and it is over."


scene backalley with dissolve
play music serious fadein 2.0
call s_shika from _call_s_shika_11
"Among the twisted metal husks of the drones, I cannot help but let a grin spread on my face."
"It's been a long time since I've enjoyed myself like this."
"Not only is this job going to pay really well..."
"It's also going to be a lot of fun."
"But..."
$ spose='1'
show shika at c2
"I need to think about this more carefully."
"If she's using nonlethal weapons, then what does that mean?"
menu:
    "She wants a hostage.":
        "Maybe she wants to take me as a hostage."
        "She said that she knew me, so perhaps she has worked out someone she can ransom me to..."
        "No. That wouldn't work."
        $ spose='1'
        show shika at c3
        "The only people who would be willing to pay that in this galaxy would be my own crew members."
        "She also obviously has a lot of resources at her disposal."
        "So why would money be her goal?"
        "I guess I can scratch out that theory, then."
    "She is testing me.":
        $ investigate += 1
        "She said that she wanted to have a lot of fun..."
        "So naturally, she wouldn't want it to end quickly by using lethal weapons."
        $ spose='1'
        show shika at c3
        "This is some sort of elaborate game to her."
        "Hmm... That would make sense."
        "Piecing it together, it would also explain a lot about her actions."
$ kface='scared'
$ nface='shocked'
call s_crew from _call_s_crew_2
k "Captain? Are you here?"
n "Where did you go?"
"Those two must have been wondering where I went."
$ sface='smiling'
show shika at c4
s "I am fine. Do not worry about me."
$ kface='shocked'
show kotori at c2
k "What happened here?!"
"She looks around at all of the smoldering drone scraps on the ground."
s "I had a run-in with our target."
$ kpose='1'
show kotori at c3
k "Our target?!"
k "You mean she's here?!"
s "Let's get back to our quarters."
stop music fadeout 2.0
s "I'll explain everything when we get back."
scene meetingroom with fade
play music space fadein 2.0
$ apose='1'
$ abody='sa'
$ aface='neutral'
$ kface='neutral'
$ kbody='sa'
$ kpose='1'
$ nface='neutral'
call s_crew from _call_s_crew_3
s "So, here is what I have determined..."
s "Our target... She's a company employee. A mercenary, just like us."

$ spose='1'
show shika at c2
s "And it seems that she is aware of who we are, and that we have taken up her bounty..."
s "Also, she has described herself as a 'fan' of ours."

"Kotori seems to be taking it seriously for a change."
$ kpose='1'
show kotori at c4
k "If she's on this ship..."
k "Then it's going to be dangerous."
"Nami nods in agreement."
$ npose='1'
show nami at c2
n "We have to heighten our security measures in our quarters."
n "There could be traps waiting for us in here."
k "Those drones I saw..."
k "All of them were equipped with non-lethal weaponry."
$ kpose='1'
show kotori at c3
k "So does that mean she isn't out to kill us?"
$ spose='1'
show shika at c3
s "It doesn't appear that way."
s "If I were to take a guess, this is all just a big game to her."
s "She said she was a fan of our work, and that we apparently have a cult following..."
$ sbody='sb'
show shika at c4
s "If I were to take a guess at her motives, the crimes, her appearing here and confidently declaring herself out in the open..."

s "It's all just a game to her."
$ npose='1'
show nami at c3
n "Just a game...?"
n "Now that I think about it, none of her crimes resulted in any casualties..."

$ kpose='1'
show kotori at c2
k "So this is all about feeding her own ego?"
k "She thinks she's proving how talented or resourceful she is?"
"When Kotori starts taking things seriously, she really is sharp."
$ kbody='sb'
show kotori at c3
k "Well, she is a mercenary like us, so her reputation would be everything..."
k "And what better way would she be able to prove her own capabilities than by beating us, her own idols?"
$ sface='smiling'
show shika at c4
s "Exactly. She said she was a fan, as I mentioned before..."
s "I guess this means this job is going to come down to a battle of wits."
$ sface='neutral'
show shika at c3
s "If we fail, then she will make sure to humiliate us in front of the entire company..."
s "Our reputation would be forever tarnished."
"I have heard about workers in the film industry who messed up once and were never able to find a job again..."
"Life as a mercenary is no different from that in this part of the galaxy."
"If you cannot get task job done, then you might as well look for a new job."
$ spose='1'
show shika at c2
s "So, we understand her motives, and we know that she is somewhere on this ship..."

s "But we can't simply confront her out in the open."
$ npose='1'
show nami at c2
n "Right. 'Akane' is an alias, as we determined earlier."
n "There is no concrete evidence linking her to her crimes."
$ nbody='sb'
show nami at c3
n "So if we confronted her out in the open and beat her senseless..."
$ kbody='sa'
show kotori at c4
k "It would seem like that we're just attacking a fellow employee for no particular reason."
k "Which means we need evidence first."
$ spose='1'
show shika at c3
s "That is precisely the problem."
s "She says that she drifted in aboard a company ship."
s "If we can just find out more information about her, then we can determine who she is..."
$ sbody='sb'
show shika at c2
s "And find a way to beat her."
s "As it stands, she probably knows where our quarters are..."
s "So she can afford to wait and let us come to her."
$ nbody='sa'
show nami at c4
n "You said that this is about her ego..."
n "So perhaps we can bait her like that."
$ npose='1'
show nami at c3
n "If you got her to confess and recorded it..."
n "Then you could go forward with claiming the bounty."
n "On the other hand, if it became public knowledge that the single highest bounty in the galaxy is on this ship..."
$ spose='1'
show shika at c2
s "It would throw everything into chaos."
s "Every single team here would be mobilising to take her down..."
s "And in that chaos, she would easily slip away, off to cause mayhem somewhere else."
s "So we have to handle this with discretion, above all else."
$ sbody='sa'
show shika at c3
s "If we pull this off, then we're set for life."
s "No one is to breathe a word of this to anyone outside of these quarters. Okay?"
"Both of them nod in agreement."
$ sface='smiling'
show shika at c4
s "Good. That's an order from your captain."
"Kotori puts her hand on her chin."
$ kpose='1'
$ kbody='sa'
show kotori at c3
k "We have to remember that she's confident enough to reveal herself to us..."
k "So she would obviously have traps in wait."
k "This is going to be difficult to approach..."
$ kface='smiling'
show kotori at c4
k "It would be best to have time to think about our next move."
s "Exactly."
s "For now, I am going to declare our meeting adjourned."
$ spose='1'
show shika at c3
s "I want everyone to be ready for battle at a moment's notice."
s "I will be setting the security systems to red alert."
s "If even a rat finds its way into our quarters, we will know about it."
ai "Acknowledged."
ai "Security level on red alert."
s "Good."
s "Make sure to check your rooms before you go to bed."
s "We do not want her to strike when we're most vulnerable."
$ sbody='sb'
show shika at c2
s "While we should be relatively safe in our quarters, it's better to be safe than sorry."

s "the captain declares this meeting to be adjourned."
hide kotori
hide nami
with dissolve
"As the two of them leave the room, the AI begins to speak."
ai "I will keep an eye out for any reports or unusual problems arising onboard."
ai "My guess is that she will not be able to remain out of trouble."
ai "Or she will be applying incredible restraint on her compulsions."

s "I agree."
stop music fadeout 2.0
call h_shika from _call_h_shika_9

scene pool with fade
play music night fadein 2.0
"It's been rather difficult to relax since what happened."
"I'm here at the pool with Nami."
"She hasn't left my side since Akane had singled me out."
"For the longest time, we just sit here together, not saying a single word."
if persistent.adult==True:
    $ nbody='aa'
    $ sbody='aa'
else:
    $ nbody='ba'
    $ sbody='ba'
call s_nami from _call_s_nami_3
n "Captain..."
n "I want to ask you a question."
$ spose='1'
show shika at c2
s "Ask away."
n "Why is it that you chose to walk away from us when you thought you were being followed?"
$ spose='1'
show shika at c3
s "At the time, I thought it might have just been those mercenaries from earlier."
s "People around here do take such things personally, you know."
$ npose='1'
show nami at c4
n "Even if it was just them, there is no point in needlessly risking yourself like that."
if persistent.adult==True:
    $ sbody='ab'
else:
    $ sbody='bb'
show shika at c2
s "Well, if we had remained in a group, they might not have revealed themselves and simply waited for a better opportunity to strike."
s "So, I thought the best course of action was to lure them out myself."
if persistent.adult==True:
    $ sbody='aa'
else:
    $ sbody='ba'
show shika at c3
s "Akane did reveal herself too."
$ nface='angry'
show nami at c3
n "Next time, please try to let your crew know if you're planning something like that."
n "She isn't out to kill you, but still..."
$ npose='1'
show nami at c2
n "What if she decided to stun you, then capture you?"
n "That would really put things into disarray for us."
s "I'm sorry, Nami..."
s "But I really did feel that it was the best course of action."
$ nface='neutral'
show nami flip at c4
n "Well, we have to accept the captain's orders."
n "And you did try to protect us."
s "Exactly."
"I sit down at the water's edge, just letting the warm water soak my feet."
"Nami relaxes in much the same way."
$ nface='smiling'
show nami at c3
n "Kotori did pick an excellent place to put this pool."

n "You can get a perfect view of the cosmos from here."
$ npose='1'
show nami at c2
n "Why is it that space is so fascinating to us?"
n "Even in the olden days, mankind looked up at the stars in wonder."
"That same look of wonder is in Nami's eyes as the twinkling stars shine in front of us."
$ spose='1'
show shika at c4
s "You're still searching for it, aren't you?"
n "Yes..."
n "An answer."
if persistent.adult==True:
    $ sbody='ab'
else:
    $ sbody='bb'
show shika flip at c3
s "Have you worked out the question yet?"
n "No, I have not..."
n "Here I am, still chasing a vague feeling of longing after so many years..."
if persistent.adult==True:
    $ nbody='aa'
else:
    $ nbody='ba'
show nami at c3
n "There's something out there among the stars that I am looking for."
n "I do not know what that is..."
n "There's some desire in me, something I cannot comprehend..."
n "I ask myself every day..."
$ npose='1'
show nami at c3
n "'What is it that I'm chasing?'"
n "'What does all of this mean?'"
$ sface='smiling'
show shika at c4
s "That's why you became a pilot, isn't it?"
s "You wanted to see what was out there."
n "Exactly."
"Among the three of us, we all come from radically different walks of life."
"Nami was a former pilot, one of Earth's best and brightest."
"I come from a mundane background."
"No one back on Earth could have imagined that things would turn out like this for me."
"And not for Nami, either."
$ nface='neutral'
show nami at c2
n "Although my time spent in that career was unforgettable..."
n "It did not give me the freedom that I was craving."
n "You could only be in a few places at once."
$ npose='1'
show nami at c3
n "I wanted more. I wanted to spread my wings and fly across the cosmos."
n "I wanted to know if I could find what I was looking for out here."
"She lets out a small laugh."
$ nface='smiling'
show nami flip at c4
n "I guess, in the end, what I am chasing is some enlightenment."

n "Do you think that there could be a profound experience out there, one which would change how you saw everything in life?"
$ sface='neutral'
show shika at c3
s "It is a wide universe, Nami."
s "That experience is out there somewhere. I am certain of it."
$ spose='1'
show shika at c2
s "But it's a little hard to look if you don't know where it is."
n "Perhaps you don't find it all at once."
n "Perhaps it is something that you slowly accumulate over time."
n "Perhaps this enlightening experience..."
$ npose='1'
show nami at c2
n "Is merely the sum of everything that you have done."
s "Perhaps it is..."
"Normally, Nami isn't so open about her thoughts."
$ sface='neutral'
$ spose='1'
if persistent.adult==True:
    $ sbody='aa'
else:
    $ sbody='ba'
show shika at c4
s "Are you afraid, Nami?"
$ nface='neutral'
show shika at c3
n "Eh? Of what?"
s "You are worried about me."
n "Well, of course I am."
n "If something happened to our Captain, I doubt this company would remain together."
$ npose='1'
show nami at c3
n "So, it would be wise to ensure that nothing happens to you."
n "Akane obviously does not desire to harm you in any real sense."
$ nface='shocked'
show nami at c4
n "But even so, if it had been someone who was actually out to harm you..."
n "Then what would become of all of us here?"
$ sface='smiling'
show shika at c2
s "Even if I was not here, I think both of you would do fine."
s "You're some of the finest mercenaries in the business."
$ sface='neutral'
show shika at c4
s "But... I understand where you're coming from."
"Although she is exceptionally intelligent, Nami does need guidance from time to time."
"People with these eccentric personalities tend to be difficult to work with if you do not understand them."
s "If Akane tries to strike again, I promise that I will not isolate myself on purpose."
s "All of us need to be united if we're going to beat her, I think."
$ nface='neutral'
show nami at c3
n "Did she actually try to fight you, or were those drones the only weapons she used?"
$ spose='1'
show shika at c2
s "Just drones."
s "But judging from the way she moved, she is definitely going to be a dangerous opponent."
s "She slipped into the shadows as easily as a ghost might slip through a wall."
s "Whoever she is, she knows how to use her environment fully to her advantage."
"Everything about her is strange, to say the least."
n "If you were going to pick out one detail about our bounty which stands out above all else..."
$ npose='1'
show nami at c4
n "What do you think it would be?"
menu:
    "Her ego.":
        $ investigate += 1
        if persistent.adult==True:
            $ sbody='ab'
        else:
            $ sbody='bb'
        show shika at c3
        s "I would say that her most defining trait is her ego."
        n "What makes you say that, Captain?"
        s "Well, not only did she come all of this way just to mess with us..."
        s "She was also confident enough to reveal herself to me."
        s "If she had not done that, then she would have been able to take us down at her own pace."
        s "But it's as if she's deliberately giving us the heads up."
        s "Above all else, it is her ego that defines her."
        $ spose='1'
        show shika at c4
        s "She will deliberately leave behind clues, slip up, and taunt us."

        s "Because she believes in her superiority over us, even if she's supposedly our fan."

        $ nface='smiling'
        show nami at c2
        n "Yes... It does make sense."
        n "Why would you bother traveling all of this way if you didn't think you could emerge the victor?"
        n "In addition, she's not only challenging just you..."
        n "But all three of us."
        $ npose='1'
        show nami at c3
        n "Our reputations precede us wherever we go, so if she thinks she can somehow beat all of us together..."
        n "Then no matter how skilled she is, she must have an incredible ego."
        s "That is my thought exactly."
        $ sface='smiling'
        show shika at c3
        s "With that in mind, we can discern how she may behave in the future."
        n "Good thinking, Captain."
    "Her whip.":
        if persistent.adult==True:
            $ sbody='aa'
        else:
            $ sbody='ba'
        show shika at c4
        s "I think that one of the most obvious traits about her is her whip."
        s "She doesn't ever seem to leave it behind, no matter where she goes."

        $ spose='1'
        show shika at c3
        s "Perhaps there is some sort of emotional attachment to it."
        $ npose='1'
        show nami at c3
        n "I don't think that would be right."
        n "Akane does not seem like the type to be sentimental about her whip."
        n "It's a tool to her, a means to an end."
        n "Besides, if she simply chose not to take the whip with her and we fixated on that one particular detail..."
        if persistent.adult==True:
            $ nbody='ab'
        else:
            $ nbody='bb'
        show nami at c2
        n "Then she could easily fool us."
        s "You're right. My apologies."
        "Nami is right. If I just focus on one superficial detail like that, I could easily mislead myself."
        "I must think about my conclusions more carefully in the future."
        $ nface='smiling'
        show nami at c3
        n "There is no need for you to apologise, Captain."
        n "We have a tough opponent that we are up against."

        n "There could be any number of different ways this could play out, so it's best to consider many different ideas."
$ npose='1'
if persistent.adult==True:
    $ nbody='aa'
else:
    $ nbody='ba'
$ nface='neutral'
show nami at c2
n "No matter what way this plays out..."
n "We have to remain careful."
$ npose='1'
show nami at c4
n "Even if she looks like she does not wish to hurt us..."
n "We cannot trust anything that she says."
$ sface='smiling'
show shika flip at c3
s "You're be right about that."
n "So, next time something like that happens..."
n "Please don't do anything reckless."
if persistent.adult==True:
    $ nbody='ab'
else:
    $ nbody='bb'
show nami at c3
n "I am only your crew member, so you have the final say in what you do..."
n "But please..."
"Nami pulls her feet out of the water and wanders over to a nearby chair."
"She lays herself out, looking out at the stars."
$ nface='shocked'
show nami at c2
n "I..."
n "I do not know what I would do if we lost you, Captain."
n "So, I want to resolve this bounty as soon as possible."
$ sface='neutral'
show shika at c4
s "I understand how you feel, Nami."
s "I do not think I could stand the feeling of losing either of you."
"We have all been together for a long time."
"The idea of us carrying on if one of us was missing..."
"Well, it just does not seem plausible."
"I get out of the water too, walking over to Nami."
"She suddenly seems to get really awkward."
$ nface='shy'
show nami at c3
n "Cap... Captain..."
n "You're... You're standing fairly close to me."
n "I... I can't stop myself looking..."
$ npose='1'
show nami flip at c2
n "I..."
$ sface='shy'
show shika at c3
s "Oh..."
s "Are you feeling lonely, Nami?"
n "Yes..."
"She just lays there awkwardly, unsure of how to express her feelings."
$ sface='smiling'
show shika at c2
s "There's no need to be shy then."
s "I know how you feel..."
n "I... I know you do..."
stop music fadeout 2.0
s "Then why don't we let our passion talk?"
call h_shika from _call_h_shika_10
call h_nami from _call_h_nami

scene cg14
if persistent.adult==True:
    scene cg14_A
    pause
    "We discard our bikinis with little hesitation."
with dissolve
play music ecchi fadein 2.0
"As I walk over, she spreads out before me."
"I slowly settle on top of her, gazing longingly into her eyes."
"I can feel hether heat radiating from her body as her breathing becomes heavy."
"Her luxurious thighs feel like the finest velvet as I slip over them."
n "Shika..."
n "What happened to professionalism..."
s "We aren't working right now."
s "So we can worry about professionalism another time."
n "I'm glad..."
"Her soft lips slowly press against mine."
"I can feel her heart beating faster as she lies by my side."
"We share a long, passionate kiss."
"Her gentle hands move around my body slowly, her fingertips pressing into my soft skin."
"They slowly trail down my back."
"The heat, her breath, the feeling of her skin against mine..."
"All of it sends shudders and shivers through me."
"Nami is a rare jewel, someone of incredible strength, beauty, and intelligence."
"Someone like her is one in a billion."
"I am so lucky to have met her."
"Her hand slowly slides down my back, until it settles on my behind."
"It begins to squeeze."
"I can tell she is relishing how it spills in between her fingers."
"Her other glides up my back and her arms slowly wrap around my waist, pulling me closer to her."

"It's exhilarating to feel every bump, every caress, every rub as we lie entangled together."
"Her bright eyes do not leave mine for a moment."
"It's as if I can see into her soul."
"It's bright, it's burning, it's filled with passion..."
"Our lips seperate for the smallest moment, just long enough for her to draw a long, deep breath."
"She gently whispers into my ear."
n "Please, Captain..."
n "Don't ever leave me."
n "Don't ever leave us."
n "We need you."
n "Don't ever forget that we need you."
s "How could I possibly forget you, Nami?"
s "I'll be here for as long as you need me..."
"She relocks her lips with me, letting her passion say everything that needs to be said."
"I won't leave any of you behind..."
"No matter what happens, I will always be here for both of you."
"That is my promise to this company, and to you..."
"Nami... My precious jewel."
"For the longest time, we simply lie there together..."
stop music fadeout 2.0
"As the stars around us continue their cosmic dance in the void."

scene hallway with fade
play music day fadein 2.0
$ sface='smiling'
call s_shika from _call_s_shika_12
"Well, Nami should be in high spirits now."
"I wonder where Kotori is in the midst of all of this?"
"She is probably in her room, knowing her."
"I wander up to her room and knock."
$ sface='neutral'
show shika at c2
s "Kotori?"
s "Are you in there?"
"Deathly silence."
s "Kotori?"
stop music fadeout 2.0
"I find that the security on the door isn't active."

scene kotoriroom with dissolve

play music space fadein 2.0
"Walking inside, I find that she's nowhere to be found."
call s_shika from _call_s_shika_13
s "Kotori? Are you hiding among all of these animals?"
"She probably could be..."

"There's enough of them to bury someone in."
$ spose='1'
show shika at c4
s "Come on, Kotori."
s "You know better than to ignore your captain."
"Still no response."
"She must not be in here then."
"I cannot help but take a moment to look more closely at her stuffed animals."
"Every single one is from a different planet we have visited."
"In her own way, Kotori is collecting little memories from across the cosmos."
"Nami's room is impressive in how pristine it is..."

$ sbody='sb'
show shika at c3
"Kotori's is interesting in the sheer chaos that manifests itself in here."
"You can learn a lot about someone just by having a closer look at where they live."
"My room is rather plain compared to theirs."
$ spose='1'
show shika at c2
"A series of bunks and nothing particularly personal standing out in it."
"Even though I'm chasing this insanely huge bounty..."
"I've never lived as though I am rich."
"I do not even know what I would do once I get all of that money."
"Underneath the mound, I pull out a teddy bear."
$ sface='smiling'
show shika at c1
"That's right..."
"This bear was from that one planet we stayed on."
"It's hard to believe that you could find such a beautiful place in the universe."
$ sbody='sa'
show shika at c2
"It was advertised as a luxury planet."
"But I suppose that isn't particularly relevant."
"Kotori loved that world..."
"She didn't want to leave it at all."
$ spose='1'
show shika at c5
"Crystal clear lakes, several multicolored moons which sailed through the night sky..."
"Every day was like a pleasant summer's day."
"It's amazing to believe that terra-morphing technology is capable of altering a planet to such an incredible degree."

$ sface='neutral'
show shika at c3
"But alas, I'm not sticking to the task at hand."
"I still need to find Kotori."
stop music fadeout 2.0
call h_shika from _call_h_shika_11

scene hallway with dissolve

call s_shika from _call_s_shika_14
play music serious fadein 2.0
"Wait..."
"I do not want to make myself panic, but maybe Kotori has already been attacked by Akane?"
"How plausible would that be?"
menu:
    "It's plausible.":
        $ spose='1'
        show shika
        "Hmm..."
        "Akane could have sneaked in here somehow..."
        "But if she did, how come there were no alarms triggered or anything?"
        "The entire security system is fine tuned to trigger upon even the slightest suspicious thing happening."
        $ sbody='sb'
        show shika at c2
        "It's too unlikely for me to consider it."

        "I am just jumping to conclusions at this point."
    "It isn't plausible.":
        $ investigate += 1
        $ spose='1'
        show shika at c2
        "No... That's just jumping to conclusions."
        "It has been eeriely quiet around here."
        "If Akane somehow managed to get inside of our quarters and attacked one of us already..."
        "That would be putting her on the same level as a ghost."
        "And Kotori would have raised the alarm right away."
        "I know that Kotori is no pushover, so this just doesn't make sense."
        $ sbody='sb'
        show shika at c3
        "So far, I think I have a firm grasp on my enemy's capabilities."
        "And I know these quarters better than anyone else on this ship."
        "So no, it's not plausible."
        "The probability of it happening is incredibly unlikely."
        "So, I shall just put it aside for now."

$ spose='1'
show shika at c4
"Kotori could just be having a swim at this hour."
"She does not have a lot to do at the moment, so she would be trying her best to stay active."
stop music fadeout 2.0
"It's then that I hear noises coming from the simulation room."
ai "Simulation scenario over."
ai "Perfect score."
play music day fadein 2.0
$ kface='laughing'
call s_kotori from _call_s_kotori_3
k "Alright!"
"Kotori bounds out of the room happily and pumps her fists in the air!"
$ kface='smiling'
show kotori at c2
k "I finally did it!"
"She sees me standing there."
$ kpose='1'
show kotori at c3
k "Oh, Captain!"
k "Came to see me, did you?"
$ sface='smiling'
show shika at c3
s "Just checking up on you, Kotori."
$ sface='neutral'
show shika flip at c3
s "I thought that you weren't allowed in the simulation room after the last... incident."
$ kface='neutral'
show kotori at c2
k "Well, we're currently on high alert..."
k "And swimming didn't really help put me at ease."
$ kface='smiling'
show kotori at c1
k "So I thought a good old fashioned dungeon crawl would help!"
$ sface='scared'
show shika at c3
s "Please don't tell me that you burned out the simulation room again..."
$ kface='neutral'
show kotori at c4
k "No, no! It was that one dungeon that we spent heaps of time on!"
k "Do you remember that one?"
$ sface='neutral'
show shika at c3
s "The Overgrown Undergrowth dungeon?"
s "Please don't remind me of those days..."
$ kface='laughing'
show kotori at c3
k "But I had so much fun in that dungeon!"

$ spose='1'
show shika at c2
s "I didn't..."
s "How exactly did you get a perfect score in a simulation of that dungeon by yourself?"
$ kface='smiling'
show kotori at c4
k "Well, I decided that I have to start taking things more seriously!"
k "This Akane character sounds like she's going to be bad news, no matter what way you look at it!"
k "So I want to be ready!"
$ kpose='1'
show kotori at c3
k "I need to protect everyone with these two daggers!"
"She flashes them in the air."
k "Did you see that?"
$ sface='smiling'
show shika at c2
s "See what?"
$ kface='laughing'
show kotori at c4
k "Exactly!"
"Kotori laughs at her own bad joke."
"I can't help but smile too."
"Playing along with her ridiculous jokes is fun."

$ kpose='1'
show kotori at c3
k "You really do get me, Captain!"
k "That's why it's important that we beat Akane!"
k "I like the way things are around here, and we don't need someone like her ruining it for us!"
k "Don't you think?"
$ sbody='sb'
show shika flip at c3
s "Exactly."
s "It's good to know that you're in good health, Kotori."
s "Just try not to burn out the simulation room."
$ kbody='sb'
show kotori at c2
k "I will try not to!"
"Before I can turn to leave, she puts her hand on my shoulder."
$ kface='neutral'
show kotori at c3
k "Can I come with you for a moment, Captain?"
$ sface='neutral'
show shika at c3
s "Permission granted."
"Kotori seems to be thinking about something."
k "I have been looking into this cult following we apparently have..."
k "And it's silly!"

$ spose='1'
show shika at c2
s "How did none of us here know about it in the first place?"
k "All I do with my digital pad is play online games..."
k "You and Nami wouldn't bother looking up anything like this, either."
"It's more or less true."
"I tend to avoid any pop culture news like the plague."

"I only ever look up information on politics."
$ kface='smiling'
show kotori at c4
k "This means I have fans!"
k "How exciting is that?!"
k "Imagine, there's probably an entire galaxy's worth of people out there following our adventures!"
k "That's cool, don't you think?"

$ spose='1'
show shika at c3
s "It is cool, I suppose..."
"But..."
"Doesn't that warrant some scrutiny?"

"Is it possible that this cult following we have could interfere with our current bounty?"
"Let me think..."
menu:
    "We should keep a low profile.":
        $ investigate += 1
        $ spose='1'
        show shika at c2
        s "I don't like it, to be honest."

        $ kface='neutral'
        show kotori at c3
        k "Why is that, Captain?"
        s "This Akane somehow knows everything there is to know about us."

        s "All of this information is just out there, ready for her to access at any given moment."
        $ sbody='sa'
        show shika at c3
        s "While we are still aiming to complete this bounty, we should keep as low a profile as we can."
        s "She wouldn't even have to monitor us herself if there are tons of people out there watching our adventures."
        $ kpose='1'
        $ kbody='sa'
        show kotori at c2
        k "That's a good point..."
        k "Then again, if she didn't have access to all of this information..."
        k "She would not have turned up on our doorstep."
        $ kface='smiling'
        show kotori at c3
        k "So there's a silver lining to all of this!"
        $ spose='1'
        show shika at c4
        s "I do not know if that is worth sacrificing the element of surprise."
        s "She has the advantage right now, no matter what way you look at it."
    "I suppose it's nice.":

        $ spose='1'
        show shika at c2
        s "I suppose it is nice..."
        s "We really should have capitalised on this, though."

        s "Maybe we could have done some merchandising and earned ourselves a steady income."
        $ kface='neutral'
        show kotori at c3
        k "I guess so..."
        k "On the other hand, don't you think that it's weird that people have been reporting sightings of us all over the galaxy?"

        $ spose='1'
        show shika at c3
        s "That's true..."
        s "That also means that we cannot operate or do anything with any real discretion."
        "If Akane is using this information to her advantage, then it is troubling."

        s "It's a wide galaxy, and there aren't any intergalactic laws forbidding this..."

        s "Considering the massive cultural differences between many of the empires here."
        s "So I guess that there's not much we can do about it."
        $ kface='smiling'
        show kotori at c2
        k "Even if we can't do anything about it, we should enjoy it!"
        k "We're intergalactic stars, Captain!"

        "Somehow, that does not comfort me at all."
$ kpose='1'
$ kbody='sa'
show kotori at c4
k "Either way, I'll make sure that you're safe, Captain!"
k "You can trust me to get the job done every time!"
$ sface='smiling'
show shika at c2
s "I am most certain that I can."
s "But I do not wish to be a burden."
s "Perhaps I should go practice my skills in the simulation room too."
$ kface='laughing'
show kotori flip at c3
k "It always pays to practice, Captain!"
k "If you don't, then that amazing precision of yours will slowly wear away!"
k "And we wouldn't want that!"
$ kpose='1'
show kotori at c3
k "After all, you are so delicate with your fingers..."
k "They always touch all of the right-"
$ sface='neutral'
show shika at c3
s "Professionalism, Kotori."
s "Let's not forget professionalism."
$ kface='angry'
show kotori at c2
k "Fiiiiine."
k "But you'll give in one day."
k "That professionalism of yours cannot keep me away forever!"
"So carefree, this girl..."
"If only I could live my life as she does."
$ kface='smiling'
show kotori at c1
k "Above all else..."
k "I will protect everything here!"
k "Even if it meant laying down my life, I would protect the pride of our company!"
k "That is my sworn duty!"
$ sface='smiling'
show shika at c2
s "There's no need to be so dramatic."
s "Akane isn't out to kill us."
$ kface='neutral'
show kotori at c3
k "Even so..."
k "I do not want to lose to the likes of her!"
k "And I won't! None of us will!"

scene cg5
if persistent.adult==True:
    scene cg5_A
with dissolve

"She pulls out her daggers and shows them to me."
k "See these two blades, Captain?"
k "I've repaired them, looked after them and used them ever since we've all been together."
k "I wield these blades for you, Captain!"
k "There is no one else in this whole universe that I would wield them for!"
"She flashes them through the air, streaks of golden light illuminating the area around her."
k "While I have these, there's nothing I won't be able to beat!"
k "I'm sure of it!"
"When Kotori gets fired up, you can't help but feel energised too."
k "So, don't you worry about a thing, Captain!"
k "You can believe in me!"
k "Akane won't know what's about to hit her!"
"She happily twirls the blades around in her hands."

k "As sure as the sun rises from the horizon on Earth..."
k "I will capture her and earn us the one billion imperial dollars!"
s "I do have faith in you, Kotori."
"I do."

"No matter what happens from here, I'm glad Kotori will be by my side for the whole thing."
"Despite her personality quirks, she is one of the most reliable people I have ever met."
"When she says that she's going to do something, she does it."
"And she does it to the best of her ability."
"Seeing her standing there in front of that glass window, the cosmos her backdrop..."
"It creates an almost surreal image in my head."
"She does look rather stunning in that body suit as well..."
"I cannot help but let my imagination start running off by itself."
k "Captain? Hello?"
k "You're spacing off!"
s "Pardon me."
k "As I was saying, there's no way that a whip, of all things, could beat these daggers!"
k "All it would take is a single cut and she would be unharmed!"
s "At the same time, you shouldn't underestimate her."
s "If she somehow managed to snare your arms with her whip..."
k "Don't worry about that!"
k "I am prepared, Captain!"
k "That's why I was training!"
k "AI, what was my score again?"
ai "Kotori achieved a perfect score in the simulation."
ai "She is more ready for combat than ever."
k "See? Now just don't worry!"
s "Remember that overconfidence can very easily be your downfall."
s "Our opponent isn't going to be easy to defeat like a simulation."
stop music fadeout 2.0
"Long after that, we continue to talk."
scene hallway with fade
play music night fadein 2.0
call s_shika from _call_s_shika_15
"Kotori eventually heads back to her room, leaving me to go elsewhere."
"Now that I've had a moment to relax, I can focus on the task at hand."
"It's important to take breaks to remain at peak performance."

$ spose='1'
show shika at c2
"If you leave a machine on for too long, it eventually burns itself out."
"People aren't so different."

"It's been silent despite us being on high alert."

"As we discussed, she must be taking her time."

$ sbody='sb'
show shika at c3
"We don't know where she is hiding, so she can wait until we're vulnerable."
"I see someone walking down the hallway."
$ sbody='sa'
$ spose='1'
call s_nami from _call_s_nami_4
n "Captain."
s "Nami."
"After what only happened about an hour ago, both of us have gone back to being professional."
"I think that was just what Nami needed to focus too."

$ spose='1'
show shika at c4
s "Have you seen anything unusual?"
$ npose='1'
show nami at c2
n "Not at all."
n "It has been very quiet around here."
"She looks around her."
$ npose='1'
show nami at c3
n "It's been too quiet, you know."
n "I do not think I have even heard a mouse moving around onboard."

$ spose='1'
show shika at c4
s "It doesn't feel right, I agree."
n "It... It puts me off, you know."
s "What does, exactly?"
n "The idea that she could be watching us this entire time."
s "Well, it's possible that she's watching us, at least..."
$ sbody='sb'
show shika at c3
s "But I understand you."
"Nami is someone who takes her privacy quite seriously."
$ npose='1'
show nami at c2
n "Now that I think about it, the fact that we have a cult following is also strange."
s "I suppose it is, but you know how it works."
s "We're living in a massive galaxy with a lot of bored people in it."
$ spose='1'
show shika at c4
s "So the idea of people following our shenanigans... It isn't that far fetched."
s "We do lead an unusual life, after all."
$ npose='1'
show nami at c3
n "I don't like it, either way."
s "I know..."
s "But we can't do anything about it right now."

s "We don't know when Akane is going to strike."
$ nbody='sb'
show nami flip at c3
n "She must be confident that she can trade blows with us if she revealed herself."
s "That is exactly what I thought at the time."
n "Also, all of those drones she sent you..."

n "How do you suppose she got those on such short notice?"
$ npose='1'
show nami flip at c2
n "They were a newer model too, one which was only recently imported onto this ship for sale."
menu:
    "They must have all belonged to her.":
        $ investigate += 1
        $ spose='1'
        show shika
        s "I think that she must have owned all of them."

        n "She has enough money to purchase that many bots for her own personal use?"
        s "Well, they must have been purchased off world."

        s "You said yourself that this model was only recently imported and made ready for sale."
        $ sbody='sa'
        show shika
        s "Someone buying such a large quantity of these drones with her funds would not have gone unnoticed..."

        s "Neither would she have been able to steal this many on such short notice, not to mention reprogram them..."
        $ spose='1'
        show shika
        s "So, she had to have brought them with her when she arrived here."
        $ nface='smiling'
        show nami
        n "Yes... I think that you're onto something, Captain."
        n "We're beginning to form a profile of her now."
        n "She must be someone with status or wealth."
        $ npose='1'
        show nami
        n "In addition to her training."
        "I nod in agreement."
        $ sface='smiling'
        s "That forms a fascinating profile, doesn't it?"

        n "It does..."
        n "This bounty is turning out to be interesting."
    "She stole them.":
        $ spose='1'
        show shika
        s "She's a criminal. She wouldn't exactly be above stealing them."
        s "You said yourself that there was only recently a shipment for this new model."
        $ sbody='sa'
        show shika
        s "We do not know how long she has been on the ship for, so perhaps she stole them before this?"

        $ npose='1'
        show nami
        n "No... I do not think so."
        n "Suppose that she did manage to pull that off and keep a low profile..."
        n "Such a large theft of military grade hardware wouldn't have gone unnoticed on here."
        $ nbody='sb'
        show nami
        n "News travels quickly, and we would have heard about it."

        s "Right... Pardon me."
        n "It's not a problem, Captain."
"A drop of water falls from the ceiling, interrupting our train of thought."
$ spose='1'
show shika at c4
s "Huh... Damn, there must be a hole in the pipe system somewhere."
s "I guess we'll have to get someone to..."
"I trail off as I look more closely at the 'water' drop."
stop music fadeout 2.0
$ sface='shocked'
show shika at c2
"It doesn't look like water at all, but some vividly colored blue gel."
"It's sticky and has a strange consistency."
"What on Earth could it be?"
"To my surprise, the drop on my finger begins to move ever so slightly."
"At first, I think my eyes are playing tricks on me."
"But no matter how many times I blink, it's still moving."
$ npose='1'
show nami at c3
n "Captain? Is something wrong?"
$ sface='neutral'
show shika at c3
s "Nami... Do not move."
s "I think there's something in the pipes."
$ nface='shocked'
$ nbody='sa'
show nami at c4
n "What do you mean by 'something'?"
s "Just hold still."
"I move my hand slowly, ever so slowly towards the small puddle of blue gel that has accumulated on the floor."
"When I tap it with my finger..."
$ sface='shocked'
show shika at c3
play music serious fadein 2.0
"It starts to move!"
"My reflexes kick in, and I quickly pull my hand away."

"A flood of blue gel erupts from the opening above me."
$ npose='1'
show nami at c2
stop music fadeout 2.0
n "Captain! Get out of the way!"

play music funny fadein 2.0
scene cg4
if persistent.adult==True:
    scene cg4_A
with dissolve

"Nami shoves me, just in time for the blue gel to ensnare her."
"Writhing and entrapping, the blue gel quickly envelopes her legs and chest."
"It quivers and vibrates as sticky tendrils begin to prevent Nami from moving."
"More and more ooze drips from the ceiling, piling on top of her."
"It settles on her chest, squeezing and touching her."
n "W-What is this thing doing?"
"The gel appears to be... massaging her."
n "Get it off me!"
"The ooze seems to be coating her all over."
"Once it's thoroughly enveloped her body, it begins to vibrate slowly."
"Small quivers and movements are visible through the gel's surface."

"Nami tries to scrape it off herself, but it's useless."
"Every time she pushes it away, it just makes its way back."
"Two strands of gel bind her arms to the ground, preventing her from resisting."
n "It's... It's touching me all over!"
"I move towards her with my hands out, hoping that I can succeed where she failed."
n "No! Don't touch it! You'll just be dragged in too!"
"A small gasp escapes her lips as the slime clamps down hard around her chest."
"I cannot help but notice how it is creeping in between her thighs too."
"The entirety of its mass is caressing, touching, and massaging her all over..."

"Soon, her face turns bright red and I can hear her breathing become heavy."
n "W-What is this thing..."
n "Why... Is it doing this..."
s "Just hold still, I have an idea."
n "I... Okay..."
n "This... This is so embarrassing... So hurry up..."
"I pull my pistol from my belt."
s "Pistol configuration: EMP."
"All living things have some form of electrical current moving through their body."
"There's two possibilities with this gel."
"It's either a living thing, or it's some sort of nanotechnology."
"Either way, the EMP should at least get it to let go."
"It probably won't deliver enough of a punch to destroy it."
s "Close your eyes, Nami."
"She's panting heavily due to the gel's movements."
"But she complies."
"I squeeze down on the trigger, and the EMP wave erupts from its barrel."
"The gel stops moving for a moment."
n "Did... Did it work?"
s "Don't move."
"I keep an eye on the gel."
"It begins to condense itself on top of Nami's chest."
stop music fadeout 2.0
"Then it erupts, showering the entire hall with its goo."

scene hallway with dissolve
play music serious fadein 2.0
"Sticky globs of gel slide lifelessly down the walls of the hallway."
$ sface='shocked'
$ spose='1'
$ sbody='sga'
$ nface='neutral'
$ npose='1'
$ nbody='sga'
call s_nami from _call_s_nami_5
s "Are you alright, Nami?!"
n "I'm fine..."
"She gets back up on her feet slowly."
$ npose='1'
show nami at c2
"She wipes some off the goo off her suit."
n "I remember where I've seen this gel before."
n "It's a brand of massage gel from another galaxy."
$ sface='neutral'
show shika at c3
s "Massage gel? I have not heard of such a thing before..."
n "I'm surprised that you haven't. It's a very popular item for relieving stress."
$ nface='shy'
show nami at c2
n "Especially some... variants of it."
$ sbody='sgb'
show shika at c4
s "This is obviously an attack by Akane."
s "She must have trapped some of this gel in the piping above us."
"A completely nonlethal, yet completely humiliating attack."
$ nface='angry'
show nami flip at c3
n "Damn her..."
s "Nami. Don't get angry."
s "Akane is attempting to throw us off."
s "Even if our reputation takes a blow, it doesn't matter if we pull this job off."
$ nface='neutral'
show nami at c3
n "It's apparent that I have not been taking her seriously enough..."
n "For now, let's get something to repair this leak."
"Nami's eyes wander over to a nearby ventilation shaft."
$ npose='1'
show nami at c2
n "Do you think she might have used the vents to get in here?"
s "Possibly... It's company policy not to obscure or place any objects in the vent system."

s "So we couldn't place any security countermeasures there..."
s "We'll have to talk about this somewhere else."
s "That probably isn't the only camera that's watching us."
stop music fadeout 2.0
n "Agreed."
call h_nami from _call_h_nami_1
call h_shika from _call_h_shika_12

scene meetingroom with fade
play music day fadein 2.0
$ kface='shocked'
call s_crew from _call_s_crew_4
k "She attacked you... with massage gel?"
$ kface='neutral'
show kotori at c2
k "If only I were there to be attacked... Massage gel is expensive..."
k "It would have been heavenly..."

$ kface='angry'
show kotori at c3
k "How come Nami is the lucky one all the time?"
"I can't believe that she's pouting over this, of all things."
$ spose='1'
show shika at c2
s "Now isn't a good time for jokes, Kotori."
s "She is obviously aiming to tarnish our reputation."
$ sbody='sb'
show shika at c3
s "If word got out that we were taken by surprise by massage gel, of all things..."
s "It would be a devastating blow."
"Her methods of attack are ridiculous and wouldn't be able to injure a fly..."
"And yet, it's still somehow menacing."
"We don't know where we're going to be hit from next..."
"And in what way."
$ npose='1'
show nami at c4
n "We're presuming for the time being that she's going to try and throw us off with similar attacks like this."
n "Nothing lethal, but traps which will make us seem weak, useless or helpless."
n "With that in mind, it does not mean that our lives are at risk, and we can take on new identities if worst came to worst..."
$ nbody='sb'
show nami at c3
n "However, that scenario is one that I would personally desire to avoid."
n "It would mean abandoning everything we have built up here and, ultimately..."
$ nface='angry'
show nami at c2
n "That we lost to Akane."
"Nami seems a bit annoyed by her whole ordeal."

"She gains a certain kind of focus once something has made her angry."
$ kface='neutral'
show kotori at c4
k "I will not let that happen!"
k "The stakes are high, but we've gotten through worse together."
k "I know exactly what we can do!"
"You might not know it at a glance, but Kotori is sharp."
$ kpose='1'
show kotori at c3
k "If there was a hole in the roof, and one in the pipes..."
k "That means she was somehow able to access it without going through the front door."
$ kbody='sb'
show kotori at c2
k "You mentioned a ventilation shaft before, but I don't think that was it."
$ nbody='sa'
show nami at c3
n "You don't? What do you propose it was then?"
$ kface='smiling'
show kotori at c3
k "Well, keep in mind that there are cameras in the main halls right now, and our AI has not reported any unusual activity..."
k "The AI in our quarters is a closed system, which means it cannot be modified by outside interference."
$ kbody='sa'
show kotori at c4
k "Unless she somehow got into the AI core and modified the program's settings manually, there was no way she could pass by those cameras."
k "Even if she damaged them or the feed was cut off from our AI, it would issue an alert."
k "Wasn't that hole in a camera's blind spot, too?"
$ spose='1'
show shika at c2
s "Yes... It was..."
s "So the placing of it was very deliberate..."
menu:
    "She must have known we would stop there somehow.":

        $ spose='1'
        show shika at c3
        s "Do you think that she might have known that we were going to stop there somehow?"
        $ kface='neutral'
        show kotori at c3
        k "Eh? How could she have possibly known that?"
        s "It just seems like that the slime was just too deliberately placed..."
        $ npose='1'
        show nami at c2
        n "I do not think so, somehow."
        n "I imagine that the massage gel was primed to react when someone touched a larger portion of it."
        $ nbody='sb'
        show nami at c3
        n "So, it was just a matter of us being in the wrong place at the wrong time."
        s "Yes... That makes more sense..."
        "It was only a vague guess."
        "But when I think about it, she wouldn't be able to know about things like that."
        "The trap was obviously set up in advance."
    "It was just a simple trap.":
        $ investigate += 1
        $ spose='1'
        show shika at c3
        s "The gel only reacted when I touched it."
        s "She must have primed it as some sort of trap."
        $ kface='neutral'
        show kotori at c3
        k "Now that you point it out..."
        k "Massage gel uses nanotechnology. It can be programmed with commands."
        k "So, she must have set it up to react to being touched by organic matter."
        $ kface='smiling'
        show kotori at c4
        k "I swear, Captain, what would we do without you?"
        $ kface='laughing'
        show kotori at c3
        k "You're so smart!"
        $ sface='smiling'
        show shika at c2
        s "There's no need for flattery, Kotori."
        $ kface='smiling'
        show kotori at c4
        k "Come on, you know it to be true!"
        s "In addition, she knew the layout of our quarters somehow."
        s "How else would she have drilled it somewhere where people would walk by?"
$ kface='neutral'
$ kpose='1'
show kotori at c2
k "So, she had to have accessed the maintenance shafts to drill through the roof."

k "In addition, she has to have some knowledge of the ship's ins and outs."
$ kpose='1'
show kotori at c3
k "There are a number of access points to the shafts throughout the ship, but only a few which would enable her to access our quarters."
k "So with this attack, she has helped us find her."

k "Keep in mind that anyone apart from company approved engineers accessing the maintenance shafts is also a gross violation of company policy."
k "If we can work out what shaft she is using to access our quarters, and time our attack at the right moment..."
$ kface='smiling'
show kotori at c4
k "We will be able to catch her in the act! Bam! One billion imperial dollars!"
"Kotori takes a deep breath."
$ kface='laughing'
show kotori at c3
k "Sorry, I know I have a bad habit of talking too much."
$ spose='1'
show shika at c2
s "No, no. Your reasoning is completely sound."
"Although she is often carefree, Kotori has good theory-of-mind."
"She often makes fine observations when people least expect her to."
$ sface='neutral'
show shika at c3
s "So now that we know that she's sneaking around the ship through the maintenance shafts..."
s "She probably knows that too."
$ spose='1'
show shika flip at c3
s "But you cannot access the maintenance shafts without proper authorization..."
s "So, the question is how she managed to get in there."
$ npose='1'
show nami at c2
n "The only people who would know the passcodes for accessing those shafts would be the ship's engineers."
n "And they're carefully guarded."
$ npose='1'
show nami at c3
n "So, she either managed to coax one of the engineers in this sector into telling her the code..."
n "Or she skipped that part and managed to convince an engineer to let her come and go."
s "It's time to do some investigating."
s "Kotori, where is the closest maintenance shaft to our quarters?"
"She quickly pulls out a digital pad and begins scanning through it."
$ kface='smiling'
show kotori at c4
k "It should be in the shopping district!"
"She seems excited now."
k "It was so boring waiting around for her to make a move, you know!"
k "Now we can really take the fight to her!"
$ kface='happy'
show kotori at c3
k "I'm going to get ready."
$ nbody='sb'
show nami at c2
n "Remember to be discreet about it."
n "If we go out there flailing our weapons around, then it's going to attract attention."
k "Okay!"
"Kotori takes off."
call h_kotori from _call_h_kotori_3
$ sface='smiling'
show shika at c4
s "By the way, Nami..."
s "Thank you for protecting me from that massage gel."
$ nface='smiling'
show nami at c3
n "And thank you for getting it off me."
n "I'm surprised that an EMP blast was so effective against it."
s "I was surprised too."
s "Anyway, we'd better catch up with Kotori."
stop music fadeout 2.0
s "She'll leave us behind if we remain idle for too long."
hide nami
hide shika
with dissolve
if persistent.adult==True:
    scene bedroom with dissolve
    $ spose='1'
    $ sbody='sa'
    $ sface='neutral'
    call s_shika from _call_s_shika_16
    "There's some time before we head to the engineering quarters..."
    "And it has been passing very slowly."
    "It's awfully quiet around here. Too quiet."
    "So, maybe I should just quickly check in on the others."
    "I don't have to go barging into their rooms to do that, however..."
    "It can be done from here."
    call scene18_A from _call_scene18_A

scene shop with fade
play music night fadein 2.0
"It's a later hour, so the shops are not nearly as busy."
"With fewer people around, it should be easier to approach the maintenance shaft."

"While it was not wholly within company policy, we managed to go through rosters for this sector's engineers."
"Our next engineer should be approaching soon enough."
$ npose='1'
$ nbody='sa'
$ nface='neutral'
$ spose='1'
$ sbody='sa'
$ sface='neutral'
call s_crew from _call_s_crew_5
s "Remember, everyone..."
s "Discretion."
"Sure enough, he's approaching."
s "Leave this to me."
"Both of them nod and step back."
hide nami
hide kotori
with dissolve
$ sface='smiling'
call s_shika from _call_s_shika_17
s "Greetings. I was wondering if you had a moment to spare?"
en "What do you want? I'm about to go to work..."
$ sface='neutral'
show shika at c2
s "I was just wondering if anything unusual has happened lately..."
s "Have you seen anything at all?"
"He eyes us for a moment."
en "Not that I can recall."
$ spose='1'
show shika at c3
s "Really? It's just that my friends and I have some concerns regarding security..."
en "Eh? How so?"
$ sbody='sb'
show shika at c4
s "There was a hole in our quarters, carved through the roof..."
s "And it was deliberately cut as well. No way steel that thick would just get a hole in it."

en "What time did that happen?"
$ sbody='sa'
show shika at c3
s "It was about an hour ago..."
en "Wait, I know the guy who usually gets his shift then."
en "He's been acting a bit weird lately..."
en "And I did notice that a cutter had gone missing from the engineering supplies room too..."
en "I'm guessing you're all looking into it yourselves?"
$ spose='1'
show shika at c2
s "That is correct."
s "We take any threats to our own security very seriously."
en "Well, I don't do any of the mercenary work around here..."
en "I just repair things if they break."
"He just shrugs."
en "There's not a lot else I can tell you."
en "At least, not without breaking company policy."
en "Either way, I've got to get to work."
en "I don't remember anything else weird happening."

menu:
    "Are you sure?":
        "Perhaps I should press him just a little bit more and see if he has anything else to add."
        "Pressuring people isn't the way I prefer to work, but sometimes it's better to do that."
        "The last thing I want is for Akane to get any more of an edge than she already has."
        $ spose='1'
        show shika at c3
        s "Are you sure that there isn't anything else you can remember?"
        en "Come on, I've already told you everything I know."
        en "I know that you're concerned and all, but trying to interrogate me isn't going to get you anywhere."
        en "So just leave me alone and I'll let you know if I see anything else, alright?"
        s "Alright. Sorry."
        "Well, it looks like that backfired."
        "He's obviously a bit cranky, so I do not think he's actually going to tell us anything if he sees anything else."
    "Please let us know if you see anything.":
        $ investigate += 1
        "He's obviously not having a good start to his job."
        "What I think would be better for now is to just leave him alone and wait for further information."
        "Trying to push him right now will just backfire on me."
        $ spose='1'
        show shika at c3
        s "If you see anything else, please let us know."
        en "Yeah, that's no problem."
        en "I've seen you ladies around before, so I know that I can trust you."
        en "Most of us in the engineering quarters don't really pay much mind to the mercs, but you three stand out for some reason."
        $ sface='smiling'
        show shika at c4
        s "Well, I'm glad we can reach an agreement."
        en "Yeah, I'll let you know if anything crops up."
        en "You do see a lot of weird stuff happening in the unused maintenance shafts and back alleys of this ship..."
        en "So if I see anything else, you guys will be the first to know."
        en "I'll make sure that these incidents get reported to my superiors too."
$ spose='1'
show shika at c2
s "Thank you for helping."
en "Eh, I just hope that it doesn't land me in hot water."
en "It sounds like someone has it out for you, and I'm probably going to get targeted too."
"He just sighs."
en "Oh well. It won't be the first time."
en "Good luck on your hunt. Time to head to work."
"With little fanfare, he disappears down the maintenance shaft."
call s_crew from _call_s_crew_6
n "So we have to find that engineer then."
n "He would be able to tell us more if we can convince him to talk."
n "What we can presume for now is that Akane is using him as a pawn in her game."
n "What methods she used to convince him to go along with her plans are irrelevant."
$ kface='smiling'
show kotori at c2
k "Even if we don't catch her this way, this will prevent her from getting into our quarters again."
k "It's the perfect plan!"
$ sface='neutral'
show shika at c3
s "It seems like this is too easy, though..."
s "And we don't know if Akane has been watching us this whole time."
stop music fadeout 2.0
"It's then that we hear slow clapping."
$ spose='1'
show shika at c4
s "... I think we have our answer then."
play music serious fadein 2.0
a "Well done, well done!"
a "You certainly are all very sharp!"
a "Did you enjoy my massage gel, Nami?"
a "I made sure to get the erotic kind, just for all of you!"
"I can see Nami's brow twitch with irritation, but she manages to keep her composure."
$ nface='angry'
show nami at c2
n "She somehow knew that the massage gel had snared me as its target."
n "The gel is programmable, so it must have sent a signal to her."
"Nami looks around at the shifting shadows, trying to pinpoint where she is."
n "Where is she?"
"Kotori seems excited."
$ kface='angry'
show kotori at c3
k "Come on! Show yourself!"
k "I want to see what kind of skills you have!"
a "Ah yes, Kotori! You always remind me of an overly friendly labrador..."
a "Always so eager and filled with life."
$ kface='smiling'
show kotori at c4
k "There is no better way to live life!"
k "But you're dodging the important thing here!"
k "Show me where you are!"
a "I swear, it's always 'rush, rush, rush' with you."
call s_all from _call_s_all
"Akane appears from the shadows, her whip ready to strike."
$ nface='neutral'
show nami
n "So this is her, Captain?"
$ spose='1'
show shika at c3
s "There is no mistaking it."
"Kotori seems really eager to start a fight."
$ aface='laughing'
show akane at c4
a "Now now, everyone..."
a "This is all just a game."
a "There's no need for such hostility, is there?"
$ kface='angry'
show kotori at c3
k "You sent a swarm of attack drones after my captain..."
k "Let's just say that I take that pretty personally!"
$ aface='smiling'
show akane at c3
a "She didn't have any trouble taking them down at all."
a "So I am not seeing the issue here."
a "Surely a mercenary company of your caliber would be able to handle some robots on auto pilot?"
a "Or are you implying that your captain isn't good enough to do that?"
$ aface='laughing'
show akane at c2
"Akane lets out a mocking laugh."
a "Seriously, you really are the little attack dog of the group, Kotori."
a "Too easy to rile up with a bit of teasing."
"Kotori's brow twitches with anger."
"She leans over to whisper to me."
$ kpose='1'
show kotori at c2
k "Permission to engage..."
menu:
    "Hold back for now.":
        $ investigate += 1
        "I need more time to analyse Akane and her equipment."
        "She's out in the open here."
        "So, as angry as it makes Kotori..."
        $ spose='1'
        show shika at c4
        s "Please hold back for now."
        $ kface='shocked'
        show kotori at c3
        k "Why?! She's right in front of us!"
        k "If we take her down now, the money's in the bag!"
        s "She would not reveal herself unless she had a plan, Kotori."
        s "I know you're angry, but if you act now, you might be falling into a trap."
        $ spose='1'
        show shika at c3
        s "So please, hold back just a little longer."
        a "What's the matter? Sweet talking your guard dog into not attacking?"
        $ aface='happy'
        show akane at c3
        a "How adorable... She really is a big labrador!"
        "Kotori finally snaps at that moment."

        $ kface='angry'
        show kotori at c4
        k "I have had just enough of you and your big mouth!"
        "Looks like it was futile."
        "However, I have gotten a better impression of Akane from this short time."
        "She's employing her training even now."
        "As I noticed before, she is exactly three metres away from us."
    "Permission granted.":
        "She's in front of us right now."
        "Even if she has a trap, it's three versus one."
        "I rest my hand on my pistol."
        "If Kotori can create an opening for me, then I should be able to get a clear shot at Akane."
        "I turn to Nami, who seems to share the same thoughts with me as well."
        $ sface='smiling'
        show shika at c2
        s "Permission granted, Kotori."
        "I whisper into her ear."
        s "Set up a distraction while we take her down."
        $ kface='angry'
        show kotori at c3
        k "No way. I'm going to handle her by myself."
        $ sface='neutral'
        show shika at c3
        s "I know that you take being insulted very personally..."
        s "But you're going to play into her hands unless you approach this a different way."
        $ apose='1'
        show akane at c2
        a "Come on, Kotori..."
        a "I'm right here, standing out in the open."
        a "Can you just imagine those billion dollars in your pocket right now?"
        a "I can't. I don't think you could beat me in one-on-one combat..."
        "Kotori gives up on trying to hold back at that moment."

"Her blades light up as if ignited by the flames of her rage."

$ kpose='1'
show kotori at c4
k "I'm going to take you down right away!"
stop music fadeout 2.0
a "Let's see if you can..."
play music battle fadein 2.0
"Before I can react, Kotori is already in striking distance of Akane."
"All I saw was a yellow blue in front of my eyes."
"With a quick glance, I can see her blades have their stunning configuration on."
"She's planning to capture Akane alive."
"Considering how angry she is, I'm surprised she has that configuration on."
$ kbody='sb'
show kotori at c3
k "Take this!"
"Kotori's blades sing through the air, but Akane manages to evade them."
"She leaps away, getting out of Kotori's reach."
$ kbody='sa'
show kotori at c2
k "Get back here! I'm not done with you yet!"
"Akane's whip snaps as it snakes through the air, but Kotori is too fast for it."
"She easily deflects it, once again getting within striking distance."
$ nface='shocked'
show nami at c2
n "Kotori! Don't engage her alone!"
k "No, I don't need any help!"
k "She's mine!"
$ aface='laughing'
show akane at c3
a "Am I, Kotori?"
a "I have spent a lot of my time analysing your fighting style..."
a "No matter how fast you are, it doesn't help when I know exactly what you're going to do."
$ kbody='sa'
show kotori at c3
k "Oh yeah?"
"Kotori begins spinning through the air, becoming a whirlwind of blades."
k "Configuration: Non-organic cutting!"
"Her blades form a whirling barrier, and they still have their stun setting on."
"Since it will cut non-organic material, that whip should be no problem."
"Acquiring anything except synthetic materials in this day and age is extremely expensive..."
$ aface='smiling'
show akane at c2
a "I have some bad news for you..."
a "But your little whirling barrier isn't going to protect you."
"Akane's whip shoots out again..."
"But it isn't cut by Kotori's blades!"

scene cg7_1
if persistent.adult==True:
    scene cg7_1A
with dissolve

"Wrapping itself around Kotori's body, the whip restrains her from moving."
"I cannot help but notice that it wraps around her in a very... particular way."
k "B-But how?!"
a "My whip is covered in organic leather."
a "I was waiting for you to use that attack."
a "If I had used synthetic materials, you would have cut it to pieces before it hit you."
a "But as it is, you actually did my work for me."
a "Your daggers wrapped my whip all around you without me putting in any effort at all!"
a "Normally you would be too fast to catch, but you put so much confidence in that blade barrier of yours..."
"Akane looks down at her while she struggles."
a "I like the way it's wrapping around you..."
a "Wouldn't you say it's squeezing you in all of the right places?"
k "Grr, get off me!"
"Kotori struggles against the binding whip, but it doesn't seem to help."
s "Get your hands off my crew member!"
"I reach for my pistol."
a "You'd better not do that, Captain."
a "Otherwise..."
"Akane pulls out a camera."
a "I'll record her when I turn on the whip's vibration mode."
k "V-Vibration mode?!"
a "So, just let me enjoy myself for a moment, and I will let you get away with no one else seeing this little embarrassing moment."
"It seems she has a kink for these things..."
k "N-No way! My body is for the captain only!"
k "All of my hard work will not be for your pleasure!"
"I swear, Kotori says some of the most embarrassing things sometimes..."
a "Oh really?"
a "Let me try another setting..."
scene cg7_2
if persistent.adult==True:
    scene cg7_2A
with dissolve
"Kotori's space suit suddenly splits open."
a "Nanotechnology sure is great..."
k "H-How dare you...!"
a "I think I might enable the vibration mode now..."
a "Since you're putting up sigh a fight, Kotori..."
"Soon enough, the whip begins to hum."
"Kotori makes some interesting expressions as the quivers of the whip shake through her body."
k "Urrr... I'll get you back for this!"
k "This labrador isn't to be underestimated!"
a "Oh, be a good labrador and don't pull on your leash so much..."
"The whip tightens, particularly around Kotori's chest."
"Although it's causing her face to blush, she seems to be resisting the entire time."
a "You really are a defiant one, aren't you?"
a "All of you are very tough! That's what I like about all of you!"
a "Since you're not going to give in, I guess I've had my fun."
a "Next time, I'm not going to be so generous."
stop music fadeout 2.0
a "Your humiliation will be thorough!"


scene shop with dissolve
play music serious fadein 2.0
"Akane disappears into the shadows again, leaving her whip behind."
$ sface='angry'
$ spose='1'
$ sbody='sa'
$ nface='neutral'
$ npose='1'
$ nbody='sa'
call s_nami from _call_s_nami_6
s "Get back here! We aren't done yet!"
a "No... Not yet."
a "But we are done for now."
"We rush over to Kotori and free her from the snaring whip."
$ kface='angry'
call s_crew from _call_s_crew_7
"She's a little groggy from the whip's stunning effects, but she manages to stand up by herself."
k "Grrr, I really want to punish her good..."
k "I can't believe that I lost so badly!"
$ sface='neutral'
show shika
s "It's fine, Kotori."
s "She's trying to get us angry so that we're going to make more mistakes."
$ kpose='1'
show kotori at c2
k "And it's working! I'm really, really, really mad!"
"Kotori pouts grumpily."
$ kbody='sb'
show kotori at c3
k "I'm going to show her who's a labrador when I find her..."
k "Just you wait, Akane..."
k "You're going to see what a labrador can do when they have you cornered..."
"Nami seems more interested in the whip she left behind."
$ npose='1'
show nami at c2
n "So that's how she fights..."
n "Although that entire situation was... unfortunate..."
$ nbody='sa'
show nami at c3
n "We have an idea of how she works now."
s "Wait... Why did she leave the whip behind?"
menu:
    "It's obviously some sort of trap.":
        $ investigate += 1
        $ spose='1'
        show shika at c3
        s "It's a trap."
        s "That's the only reason that she could have left it behind."
        n "Do you really think so?"
        $ spose='1'
        show shika at c4
        s "We don't know what configurations this whip could potentially have."
        s "For the time being, we shouldn't touch it."
        $ npose='1'
        show nami at c2
        n "That's a fine observation, Captain."
        n "For the time being, we should take a moment to have a closer look at the whip."
    "Maybe she left it to keep Kotori ensnared.":
        "Perhaps she left it to keep Kotori ensnared while she escaped."
        "That would be a fair presumption, given that Kotori is out for blood right now."
        "Even a few seconds would mean the difference between escape and capture."
        $ spose='1'
        show shika at c3
        s "I think she left it so that she could get a few seconds before she escaped."
        n "Somehow, I do not think so."
        n "Kotori could have struggled free of it when she let go."
        n "Perhaps there is another motive to letting go of it so easily..."
        $ npose='1'
        show nami at c2
        n "Either she does not care about it and has many whips..."
        n "Or she did it on purpose for some reason we cannot discern right now."
$ npose='1'
show nami at c3
n "This whip must have some level of different configurations in it."
n "Chances are that she wants us to take it inside our quarters."
$ pose='1'
show shika at c4
s "That would be a fair presumption..."
"With how compact technology is in this galaxy, you could easily add an audio or video recording configuration to just about any kind of device."
"Although it is covered in leather, this whip must have some form of nanotechnology inside of it."

$ kface='neutral'
show kotori at c2
k "There are nano-receptors embedded in the leather."

k "I felt them when she had me bound with the whip."
$ kpose='1'
show kotori at c3
k "All of those receptors could reconfigure themselves into cameras, giving her a perfect analysis of the insides of our quarters."
k "That's why she left it behind."
"Kotori huffs."
$ kface='angry'
show kotori at c4
k "What an obvious trick."
k "She had better not keep underestimating us..."
k "She's really going to get it the next time I see her."
$ kpose='1'
show kotori at c3
k "I will take this as a vow on my very life..."
s "Perhaps we are the ones underestimating her."
"She probably won't try to use the maintenance shafts again."
"Since it's been compromised."
"Wisdom would dictate that she's going to take some other approach with next attack."

"So, perhaps the best thing we can do is try and get the jump on her."
"But how are we going to do that?"
s "We can only speculate what she'll try to do next."
"We'd better head back to our quarters and lick our wounds."
"Kotori is going to need a lot of time for her pride to recover from Akane's blow."
"Looking back, I swear that I see someone moving around in the shadows."
stop music fadeout 2.0
call h_crew from _call_h_crew_1
"A disembodied giggle echoes throughout the empty shops."
scene kotoriroom with fade
play music night fadein 2.0
call s_shika from _call_s_shika_18
s "Kotori? Are you in here?"
"I haven't heard from her since that incident from before."
"Sure enough, there she is, sitting with a stuffed toy in between her arms."
$ kface='angry'
$ kbody='ba'
call s_kotori from _call_s_kotori_4
"She's still pouting grumpily."
s "Hey, are you alright?"
k "No."
k "Never before have I been so easily tricked like that."
$ kpose='1'
show kotori at c2
k "She knew just how to push my buttons and lure me into her trap."
k "labrador, huh..."
"The doll in her arms is being squeezed tighter and tighter."
$ spose='1'
show shika at c2
s "Careful, you're going to make him pass out."
"She just pouts even harder."
$ kbody='bb'
show kotori at c3
k "He can take it..."
k "I just want to smack Akane in the face..."
k "It's not just about the money anymore."
"One thing Kotori cannot handle is failure."
"Or being made fun of."
"It's been some time since we've suffered a defeat like this, so it probably hit her hard."
"Overconfidence tends to do this, sadly."
$ sface='smiling'
show shika at c3
s "It's not a total defeat."
s "You realized that she had those nano-receptors imbedded into the whip."

$ spose='1'
show shika at c4
s "If you had not done that, she would have gotten a perfect analysis of our quarters."
k "But she still knew where to strike with that massage gel..."
$ sface='neutral'
show shika flip at c3
s "I imagine that was just a random attack."
s "She only knew there was a hallway and nothing else."
$ sface='smiling'
show shika at c3
s "So, given the circumstances, you did well."
$ kface='neutral'
show kotori at c2
k "I guess so..."
"She slumps over on her bed, the doll still trapped in her arms."
k "She knows everything about us..."
k "And she targeted us, out of all of the mercenaries here..."
$ kpose='1'
show kotori flip at c3
k "What does that mean, Captain?"
menu:
    "She considers us a threat.":
        $ sface='neutral'
        show shika at c2
        s "She obviously considers us a threat to her."
        s "That has to be something, right?"
        k "If we're such a threat, how come she was so easily able to beat us?"
        k "No... It's not like that."
        $ kbody='ba'
        show kotori at c3
        k "She's supremely confident that she can beat us."
        k "There has to be something else at work as a motive here..."
        k "But I can't work it out!"
        k "This is so frustrating!"

        "She lets out a grumpy sounding sigh."
    "Perhaps she's connected to us, somehow.":
        $ investigate += 1
        $ sface='neutral'
        show shika at c2
        s "She described herself as one of our biggest fans..."
        s "Perhaps there's some sort of emotional connection she feels with us?"
        s "It's not even a matter of her ego..."
        k "Hey... You might be right."
        k "She obviously holds a high opinion of us, for the most part."
        $ kbody='ba'
        show kotori at c3
        k "You don't just randomly pick a group of mercenaries to stalk."
        k "There has to be something more to her actions..."
        k "I can't work it out right now though."
$ kpose='1'
show kotori at c2
k "She must have known that I get really angry when people taunt me..."
$ kface='angry'
show kotori at c3
k "People like her are the worst!"
k "They rely on cheap tricks and cheap words to win fights..."
k "The worst part is that we're among the best mercenaries in the business, and yet such cheap tricks actually worked on me!"
"Kotori grabs her stuffed toy and throws it at the wall."
"It lands on top of her precariously balanced pile of toys, causing the entire thing to come tumbling down."
$ spose='1'
show shika at c2
s "The only reason why it bothers you so much is because it was personal, don't you think?"
s "She knew how to push your buttons."

$ kface='neutral'
show kotori at c4
k "I know, I know..."
k "But I have to do better than that."
k "If every bounty we came across knew about me, I would end up falling for the same trap over and over again..."
$ sbody='sb'
show shika at c3
s "I know how it feels."
s "All you can do is accept your flaws and try to improve on them."
$ spose='1'
show shika at c4
s "You could spend all day on reflecting on how things can go wrong..."

s "Or you can take steps to ensure that it will not go wrong in the future."
$ kpose='1'
show kotori flip at c3
k "I know, I know..."
"She lets out another deep sigh."
"Reaching over to her shelf, she grabs another stuffed toy and crushes it in between her arms."

$ kbody='bb'
show kotori
if persistent.adult==True:
    call scene19_A from _call_scene19_A
else:
    k "I need some more time..."
    k "I'll be out soon enough, okay?"
    "Leaving her alone would be the best option for now."
    "She needs time to collect her thoughts."
    stop music fadeout 2.0
    "Perhaps I should check on Nami."

scene hallway with fade
$ spose='1'
$ sbody='sa'
$ sface='neutral'
call s_shika from _call_s_shika_19
if persistent.adult==True:
    "After finishing up that pool party with Kotori..."
    "I decided to go check on Nami."
"Nami's not in her room, so perhaps she is somewhere else."
"These quarters are not very large, so I can only think of one place she might be."
"She's training in the simulation room again."

scene simulation with dissolve

"Sure enough, as I step inside, I see her inside the room."

scene cg2
if persistent.adult==True:
    scene cg2_A
with dissolve
play music battle fadein 2.0

"This time, she's sitting on her knees."
"I wonder what sort of exercise she could be doing?"
ai "Confirm: Enable electrically charged rounds?"
n "Confirm."
n "I must feel the sting of failure."
"Sure enough, all of the virtual drones begin to hover around her."
"However, she's still not moving."
"She rests one hand on the hilt of her plasma cutter."
"The drones begin opening fire."
"And still, she does not move."
"Instead, she moves her hefty blade, deflecting the shots as they come at her."
"From all angles, they rain down those electrically charged shots."
"If she gets hit by those, it won't be lethal."
"But it's going to sting a bit."
"Even so, she does not miss a beat."
"It's always amazed me how swiftly she can move her sword."
"She could have been a dancer instead of a mercenary, and yet somehow, she ended up here."
"All she's doing is sitting there and deflecting, however."
"It's then that I see it."
"She's trying to deflect the bullets in a particular way."
"Making them ricochet off the walls of the simulation room."
"She's trying to destroy the drones while remaining on the defensive."
"The shots are ricocheting everywhere, in completely unpredictable patterns."

"It's a storm of electrically charged projectiles."
"In that storm, the drones are swept up."
"The virtual bullets smash through them, spitting pixelated sparks everywhere."
"And even in the midst of all of that chaos, she still doesn't move."
"Her eyes remain focused, filled with determination."
"Although more and more drones fill the simulation room, she still does not move."
ai "Confirm: Increase difficulty?"
n "Confirm."
"The bullets in the room begin to accelerate."
"Nami still manages to keep up, although she seems to be exerting a lot more effort."
n "Still not good enough..."
n "I need to be faster... Stronger..."
n "I must do better if I'm to triumph over Akane!"
"She's pushing herself so hard."
"With renewed effort, she begins to focus on her deflections."
"It's then that she begins to strike the drones with perfect precision."
"Each reflection downs one of her digital combatants."
"Soon, there is only silence in the room."
"She looks around her, confirming that there are no drones left."
ai "Exceptional performance, as always."
ai "Would you like to try again with increased difficulty?"
"Nami shakes her head."
n "No. This is fine for now."
n "I need to rest and collect my thoughts."
ai "Understood."
stop music fadeout 2.0
ai "Releasing the locks on the simulation room."

scene simulation with dissolve
play music day fadein 2.0
call s_nami from _call_s_nami_7
n "Watching again?"
"She's obviously a bit uncomfortable, but she seems to be remaining steady."
$ sface='smiling'
show shika at c2
s "Yes."
s "I'm amazed that you managed to do that without moving."
$ npose='1'
show nami at c4
n "It's a necessary exercise."
n "Akane's attacks aim to bind or disable."
n "So I need to learn how to defend myself even if I can't move."
$ nbody='sb'
show nami at c3
n "With that deflection technique I have been working on, she won't be able to strike me with that whip."
n "What do you think?"
menu:
    "We have to consider other possibilities.":
        $ investigate += 1
        $ sface='neutral'
        show shika flip at c3
        s "Akane casually discarded her whip before, just to lure us into a trap."
        s "Somehow, I do not think that she is attached to it as we might have thought earlier."
        $ nbody='sa'
        show nami at c2
        n "Now that you mention it..."
        n "She wouldn't have trained with just that weapon."
        n "Even Kotori and I know how to use firearms, albeit not nearly as effectively as you."
        $ npose='1'
        show nami at c3
        n "Akane obviously knows how to use that whip, but she would surely have some other kind of weapon training..."
        n "I suppose it cannot hurt to practice, nonetheless."
        $ sface='smiling'
        show shika flip at c4
        s "Not at all."
        s "Just remember that if you become too fixated on countering her whip..."
        s "She might pull out something else and completely surprise you."
        $ nface='smiling'
        show nami at c2
        n "That is a fine observation."
        n "Perhaps I should start simulating a wider variety of opponents."
        $ npose='1'
        show nami at c3
        n "Attack drones of this caliber, no matter how fast or intelligent they are..."
        n "It does not change their own limitations."
    "I think so too.":
        $ sface='neutral'
        show shika flip at c3
        s "Well, as far as we know, Akane does not appear to use any other weaponry."
        s "Focusing on how to beat it is probably your best bet."
        $ npose='1'
        show nami at c2
        n "Perhaps it is..."
        n "But perhaps it would be smarter to consider other possibilities?"
        n "Akane has training. You and I could both clearly see how skilled she was."
        $ npose='1'
        show nami at c3
        n "Just because she is good with a whip doesn't mean that it's the only weapon she would use."
        s "You're right..."
        s "But learning to deflect bullets could help you learn how to deflect other things too."
        n "That is true enough."
        n "Practice is practice, no matter what way you look at it."
$ spose='1'
show shika at c3
s "However, Nami..."
s "There is one thing which I think must be addressed."
$ sbody='sb'
show shika at c4
s "Was it really necessary to make the virtual rounds charged?"
"When something is 'charged' in a simulation, that means that it carries a slight electrical charge."
"And when that hits you, it stings."
"If too many of them hit you, you would have been sore in the morning."

"Considering the current circumstances, I cannot help but feel that it's unwise."
"We need everyone at peak performance at the moment."
"While it wouldn't be lethal, being hit by that many electrical charges would put you out of commission for a while."
$ nface='neutral'
show nami at c4
n "You need to have some risk if you want to push yourself."

n "If nothing is at stake, then you will simply remain mediocre."
$ sbody='sa'
show shika at c3
s "Even so, there is wisdom in assuring your safety first."

n "I understand, Captain..."
n "For your sake, I will not undergo any more charged simulations."
"Well, that was easy to settle."
"If it were Kotori, it would have taken ages to argue my point."
$ nbody='sb'
show nami at c2
n "So, about Akane..."
n "After that last defeat we had, she said that she's going to start recording."
n "Why is she giving us so many chances?"
$ npose='1'
show nami at c3
n "Obviously, her goal is to eventually triumph over us."
$ spose='1'
show shika at c4
s "She obviously has an incredible ego."
s "One sign of arrogance is to keep giving your opponents extra chances to beat you."
s "However, this does also prove that she isn't as ruthless as we thought."
$ nbody='sa'
show nami at c2
n "That is another point we should discuss."
n "She obviously isn't consumed by her desire to defeat us."
n "She has even stated that she does not want this to end so early."
$ npose='1'
show nami at c4
n "So, that means that she is deliberately dragging this out."
n "But why would she want to do that?"
$ spose='1'
show shika at c3
s "We already know that she is a fan..."
s "So that must mean that she sees this as inserting herself into one of our adventures."
"That is one theory I have thought about, at least."
"There is still a lot that we do not know about Akane."
"It's rather frustrating, to say the least."
"Usually, we wouldn't need to create such an extensive psychological profile of our bounty target."
"Most of the people who we have hunted were just warmongers or criminals who couldn't cover their tracks."
"Akane, however, has proven that she is resourceful, difficult to trace, and nearly impossible to catch."
"She could disappear right now, having defeated us..."
"And we would probably never see her again."
$ npose='1'
show nami at c3
n "I think I also recall that she sees this as some sort of game."
n "What you said does make sense in that regard."
n "She is trying to become 'part of the story' in other words."
$ nbody='sb'
show nami at c2
n "But that just seems like a rather unusual thing to do."
n "And not much of a motive for someone who traveled all of this way just to have this mock battle with us..."
n "So, she is either a very petty person..."
n "Or she must be obsessed with us on some level."
"Obsession..."
"Now that would explain a lot."
$ sface='smiling'
show shika at c4
s "I think that's it."
s "She's obsessed with us."
$ sface='neutral'
show shika flip at c3
s "But the reason why..."
$ npose='1'
show nami at c3
n "Well, we cannot discern that right now."
n "We don't know where she is, we don't know what she's planning, and we don't know how to fight back."

$ nbody='sa'
show nami at c2
n "Until we sort out what we're going to do right now..."
n "There is no point in asking why."
s "But of course."
"We normally do not take much interest in our targets..."

"It's all part of the challenge, I suppose."
$ nbody='sb'
show nami at c3
n "Do you have a plan?"
s "Yes. Trying to search for her ourselves isn't going to work."
s "We will just play into her hands like we did last time."
$ spose='1'
show shika flip at c4
s "So, the question is how we can bait her..."
n "That is what I was thinking too."
n "If we made a trap, even if she saw it..."
$ npose='1'
show nami flip at c3
n "I do not think she would be able to ignore it."
n "Her ego is too big for that."
$ sface='neutral'
show shika at c3
s "I think so too."
"She is trying to prove her superiority. So, of course she would turn up even to an obvious trap..."

"Just so that she could prove that she is completely capable of outwitting us."
n "We cannot make the bait too irresistible, that would just make our intentions obvious."

n "What we need is something subtle..."
$ nbody='sa'
show nami at c2
n "Something which seems to be of no consequence."
s "She is a fan of ours, apparently."
s "So what would lure her out?"
"I look down at the pistol on my belt."
s "No... That wouldn't work."
s "That would be too obvious."
$ sface='smiling'
show shika at c4
s "But... Maybe..."
"Nami looks at me quizzically."
n "What is on your mind, Captain?"
$ spose='1'
show shika at c2
s "I think I might have a plan."
s "Doesn't our simulation room have deployable modules?"
"Nami immediately realizes what my plan is."
$ nface='smiling'
show nami at c4
n "They only have a certain range."
n "And this plan relies on her knowing that we don't have a simulation room."
s "Don't worry..."
stop music fadeout 2.0
s "We just need to think one step ahead of her."
if persistent.adult==True:
    call scene16_A from _call_scene16_A
scene shop with fade
if persistent.adult==True:
    "Well..."
    "That was refreshing for my senses."
    "That will make this even easier to pull off."
else:

    "Well, this is it."
    "The trap has been set and now we just have to wait."
play music night fadein 2.0
$ sface='neutral'
call s_shika from _call_s_shika_20
"The shops are empty at this hour, so it's ideal for her."
stop music fadeout 2.0
"Sure enough, a shadow begins to emerge."
play music serious fadein 2.0
$ aface='neutral'
$ apose='1'
$ abody='sa'
call s_akane from _call_s_akane_1
a "Hello, 'Captain'."
a "So nice to see you this evening."
$ spose='1'
show shika at c2
s "Nice to see you too, Akane."
s "I was not expecting you to come out like this."
a "Weren't you, now?"
"She slowly takes deliberate steps, moving closer and closer."
"Until we're standing face to face."
a "So, 'Captain', what brings you out on this evening?"
a "You wouldn't happen to be doing some midnight shopping, would you?"
$ apose='1'
show akane at c4
a "Or maybe, you're out here for another reason."
a "I wonder whatever that could be."
a "Somehow, it's all very..."
$ abody='sb'
show akane at c3
a "Suspicious, don't you think?"
$ sbody='sb'
show shika at c3
s "Perhaps it would be..."
"She just shakes her head at me and lets out a loud sigh."
$ abody='sa'
show akane at c2
a "Are you really going to keep up this charade, 'Captain'?"
a "Do you honestly think that I'm going to fall for something like this?"
a "I know that you're listening in right now..."
$ spose='1'
show shika at c4
s "'Captain'... You keep putting so much emphasis on that."
a "Oh, come on..."
"She seems more disappointed than annoyed."
a "There is no way that you would just walk out here by yourself and stand out in the open brazenly after what happened last time."
a "Furthermore, the crew allowing their captain just to step out exposed like this..."

$ apose='1'
show akane at c3
a "It just doesn't make sense."
a "So, I cannot help but presume that this is obviously some trick."

$ aface='smiling'
show akane at c2
"She giggles to herself."
$ spose='1'
show shika at c3
s "And if it was a trick, what would you do?"
$ aface='neutral'
show akane at c4
a "Do not rush me. I am getting to that part."
a "Since you obviously cannot outsmart me, then I guess I should just explain it to you."
a "If I remember correctly, you had a simulation room which was destroyed in mysterious circumstances..."
$ apose='1'
show akane at c3
a "But recently, you have been earning a tidy little profit from your jobs."
a "So naturally, I presumed that you had gotten the best simulation room money could buy..."
$ aface='smiling'
show akane at c2
a "One that comes with deployable modules."
a "How far am I off the mark, 'Captain'?"
"She notices a bead of sweat."
$ aface='laughing'
show akane flip at c3
a "Oh my, you really are worried, aren't you?"
a "It's almost as if you have something to hide..."
$ aface='joking'
show akane at c4
a "I bet you're standing in that simulation room quivering in your boots."
a "How unsightly, Captain."
a "If this is how you're going to conduct yourself, then I have no reason to prolong this any longer."
$ aface='laughing'
show akane at c3
a "It's clear who the victor is in our little game."
"She laughs to herself."
$ aface='smiling'
show akane at c2
a "in short, your plan was to bring me out into the open with no risk to yourself."
a "Perhaps to track me or ambush me?"
$ sface='shocked'
show shika flip at c3
s "You knew all of this and still chose to reveal yourself?"
s "Isn't that a bit egotistical?"
a "But of course."
a "We both know which of us is superior at this point."
$ apose='1'
show akane at c2
a "Even with all of you combined, I have managed to outwit you at every turn."
a "A canister of massage gel was all it took to take down Nami..."
a "And Kotori took herself down with that silly spinning move of hers."
a "The only one which I haven't managed to best yet is you, Captain."
$ abody='sa'
show akane at c3
a "Since you're not actually here, I think we can let this game play out a little longer..."
a "But do not get too comfortable."
"She smiles at me with arrogance."
$ apose='1'
show akane at c4
a "I know all of you better than you know yourselves."
a "This hologram you put in front of me was to lure me into a trap."
"She motions at a dark corner of the shops."
$ apose='1'
show akane at c3
a "Now who is waiting there for me? Nami, I'm guessing?"
a "Once again, that is really obvious."
$ aface='neutral'
show akane at c2
a "Why would someone be sitting at a table when the food court is closed?"
"She lets out a small huff."
a "How stupid do you think I am?"
a "No one in the world would fall for a trap as obvious as this..."

"She pulls her whip out and examines it."
$ abody='sb'
show akane at c3
a "Kotori would be too busy sulking in her room right now to be here..."
a "So there is only one of you here."

a "Which means that it isn't even a challenge."
"Akane lets out a loud yawn."
$ apose='1'
show akane at c4
a "I expected better of you, but you're all proving to be very boring."
$ sface='neutral'
show shika at c3
s "Don't think I'm going to let you get away with this."
s "That chain of petty crimes on those planets while you were working under our company's name..."
s "Phobos VII, Aesir IV, Pantheon III..."
$ spose='1'
show shika at c2
s "And your tampering with the maintenance shafts and engineers..."
s "We will bring you to justice."
a "Why are you making yourself try to sound like a hero?"
$ apose='1'
show akane at c3
a "It's almost like you're trying to distract me from something..."
a "What? Nami?"
a "She's too far away from me to be able to do anything..."
a "And my crimes?"
$ aface='smiling'
show akane flip at c3
a "Yes, I have committed all of these crimes."
a "You need not remind me of it."
"She just smugly grins."
a "Enough of this charade then."
a "I'll be gone before Nami can catch me."
a "But as a parting gift..."
"She pulls out a pistol."
$ apose='1'
$ abody='sa'
show akane flip at c2
a "I think I'll fry your little hologram module."
a "This will be your punishment for trying to fool me with such a petty trick."
$ abody='sb'
show akane at c3
a "Maybe I could even fry your whole hologram room when I eventually breach your defences..."
a "Configuration: EMP blast."
"The pistol begins to hum softly."
"Its firing light immediately turns green."
"She points it, closing her eyes for a moment..."
stop music fadeout 2.0
$ aface='laughing'
a "Enjoy, Captain!"
"Then pulls the trigger."

"The blast causes the ceiling lights to dim for a moment before emergency power kicks in."

$ aface='joking'
show akane at c4
a "Ha... That should..."
$ aface='shocked'
show akane at c2
a "Eh?"
"She looks again with disbelief."
a "Is this hologram reinforced against EMP or something?"
show akane at c1
a "It should have been disabled by that blast..."
"I pull out my pistol."
$ sface='smiling'
show shika at c2
s "Think again."
s "Configuration: Stun."
"Akane realizes our trick too late."
play music battle fadein 2.0
"She turns to move, only to take a stunning round in the back."
"It doesn't hurt, but it will make her move a lot slower."
$ apose='1'
show akane at c2
a "Ack!"
"She's still fast, however."
"But someone steps in her path."
$ nface='neutral'
show shika at ltl
show akane at tcenter
show nami at rtr
with dissolve
n "Going somewhere?"
a "B-But you shouldn't have caught up this quickly!"
"She glances again to see Nami still sitting in the corner of the shops."
$ aface='neutral'
show akane at c3
a "Oh..."
a "That's how it is."
$ npose='1'
show nami at c2
n "Configuration: Non-lethal."
"Nami brings her blade down, Akane barely dodging it in time."
$ aface='happy'
show akane at c4
a "This is great! I was right to have faith in you!"
"Instead of panicking, Akane seems to be getting excited."
$ apose='1'
show akane at c3
a "All of you are so clever!"
$ nface='angry'
show nami at c3
n "Just be silent."
n "There are a billion imperial dollars on your head."
n "I wish to be done with this mess immediately."
"But Akane is not giving up."
"Her whip lashes out, Nami avoiding it with great effort."
"Despite being hit with a stunning round, she actually seems to be fighting harder than before."

"Nami keeps up, however."
"The two of them seem to be stuck in a stalemate."
"I aim another shot and fire."
"Akane dodges it..."
"Only for Nami to hit her with the flat side of her plasma cutter."
"It sends her flying."
$ aface='laughing'
show akane at c4
a "This is fantastic!"
a "You have exceeded all of my expectations!"
a "But I don't want this to end just yet!"
"Akane begins retreating into the shadows."
$ apose='1'
show akane at c3
a "I want things to become even more exciting!"

hide akane
stop music fadeout 2.0
"Before we can react, she disappears again."
$ nface='neutral'
show nami
play music day fadein 2.0
"Nami wanders over to me, still wearing a focused expression."
n "Kotori, did you get all of that?"
"A head pops up from one of the shops."
$ kface='laughing'
$ kbody='sa'
call s_crew from _call_s_crew_8
k "Every minute of it!"
k "Including her confessing to those crimes she committed!"
n "Good."
$ kface='neutral'
show kotori at c2
k "It's a shame that I didn't get to fight her, though..."
$ sface='neutral'
show shika at c3
s "We needed someone to wield that bulky, EMP shielded camera."
s "It's the only one we had in our quarters."
$ kface='angry'
show kotori at c3
k "I know, but still..."
k "It would have been nice..."
"Kotori seems to be pouting a little bit."
"Oh well. It's what I expected to happen anyway."
$ sface='smiling'
show shika at c4
s "The important thing is that we have her confession..."
s "And we have some time before she fully recovers from those stunning hits."
$ nface='smiling'
show nami at c3
n "It was a brilliant plan, Captain."
n "How did you know that she was going to try something like that?"
$ sface='neutral'
show shika
s "I didn't. I just planned ahead in case she had some sort of device which could disable electronics."
s "I was not expecting her to pull out a pistol, however..."
s "I guess we will have to be careful about that in the future."
$ nface='neutral'
show nami at c3
n "Although we got an excellent result..."
n "It was still risky for you to stand out in the open like that."
n "Kotori or I could have done the same thing."
$ spose='1'
show shika at c4
s "I did not think it would work unless it was me doing it."
s "In her head, she has already 'beaten' both of you."
$ sbody='sb'
show shika at c3
s "She's bound to target me next, since I'm the only one she hasn't 'beaten'."
s "This job has its risks."
$ sface='smiling'
show shika at c4
s "But it paid off."
s "She has surveillance cameras at the entrance of our quarters, I'm certain of that."

s "So she will see Kotori's camera and know that we recorded her confession to her crimes."
s "Did you retrieve the holographic module too?"
$ nface='smiling'
n "Done and done."
$ sface='happy'
show shika at c3
s "Excellent."
"This has been our first real victory over her."
"If they're thinking ahead of you by one step, then you need to think ahead two steps."

$ sface='smiling'
show shika at c4
s "As long as we have her confession, she won't be able to leave this ship."
s "While the evidence still exists, we'll be able to catch her."
s "Now, we just have to wait for her to come to us."
$ kface='smiling'
show kotori at c3
k "Amazing, Captain!"
k "With this, we've taken her advantage straight out of her hands!"
$ sface='neutral'
show shika at c4
"Yes. But now comes the hard part..."
"Once she's licked her wounds, she's going to come straight for us."
stop music fadeout 2.0
"We had better be prepared when she does."
call h_crew from _call_h_crew_2

scene bedroom with dissolve
play music happy fadein 2.0
"Settling back into my quarters, I cannot help but grin to myself as I watch the footage."
$ sface='happy'
call s_shika from _call_s_shika_21
s "She really did fall for it."
s "Hook, line, and sinker."
ai "Don't you feel that you're enjoying it a bit too much?"
$ sface='laughing'
show shika at c2
s "Not at all."
s "It's fun to watch someone full of themselves fall flat on their face."
$ sface='neutral'
show shika at c3
s "However, since we've tricked her once..."
s "She's probably going to be a lot more wary in the future."
ai "This is also a good time for you to be careful too."
$ sface='smiling'
show shika at c4
s "That is true..."
s "Let me just rewatch it one more time..."
$ sface='neutral'
show shika at c3
"Wait..."
"Did I just hear the door open?"
s "Is someone there?"
"I make sure to pull out my pistol."
"I doubt it is Akane..."
"Maybe it is one of her robotic drones that got in here somehow..."
stop music fadeout 2.0
"I had better-"

play music funny fadein 2.0
scene cg12
if persistent.adult==True:
    scene cg12_A
with dissolve
pause
"A pair of hands seize my chest from behind me."
"For a moment, a wave of shock and embarrassment floods through me."
s "W-Who's there?!"
k "Who else, Captain?"
k "I just couldn't resist temptation anymore..."
k "You have such a great body, but you never answer my calls on a lonely night..."
k "So, as payback for making me take the camera..."
k "I'm going to make you pay with your chest!"
"She fondles my breasts greedily, seemingly relishing how it softly squishes in her fingers."

k "Ahh, so this is Captain's chest!"
k "It's as if my hands have sunk into heaven itself!"
s "T-That is enough of that unprofessional conduct, Kotori!"
k "Oh, we haven't even started being unprofessional!"
k "Just you wait and see the evening I have planned for us both!"
k "There will be wine, plenty of swimming..."
k "Without wearing anything, of course."
k "Back on Earth, they used to call that skinny dipping."
k "Why don't we do that together, while watching that big planet slowly orbit around us?"
k "What a romantic evening..."
"She begins to pinch the peaks of my fruit eagerly."
s "Stop it, Kotori!"
k "You're making such a scene, Captain!"
k "Is my technique making you that excited?"

s "I-I swear, you keep doing this to me!"
k "It's not my fault that you leave yourself vulnerable when you think you're alone..."
k "My incredible sneaking skills keep letting me catch you off guard like this!"

s "D-Does anyone around here have any respect for authority anymore?!"
k "Of course I respect you, Captain!"
k "But I cannot forgive you for letting her get away from my blades!"
k "So feel the taste of this punishment mandated by the heavens!"
"Always with the dramatic language when she does things like this..."
"I swear, I really must discipline her one day."
k "Besides, aren't we in your private quarters?"
"I feel her fingers slide up my chest and brush against my neck."
k "Where all kinds of private, intimate things can happen?"
k "Wouldn't that be right, my dear Captain?"
"I can feel her hot breath on my shoulder."

"Heavy sighs, filled with longing."
k "Come on, Captain..."
k "You can't keep a girl waiting forever, you know."
k "You know me, I live in the moment."
k "So why don't you live in the moment with me?"
stop music fadeout 2.0
"Her hands do not let go. Not for a single moment."
scene bedroom with dissolve
play music city fadein 2.0
$ sface='embarrassed'
$ spose='1'
$ sbody='sa'
$ kface='smiling'
call s_kotori from _call_s_kotori_5
s "Alright, enough of that."
s "You have extracted your price."
$ kface='happy'
show kotori at c2
k "And it was worth every grab!"
k "So soft and lovely..."
"I can see her hands making grabbing motions as she fondly recalls it in her head."
$ kface='laughing'
show kotori at c3
k "You really need to loosen up, Captain!"
$ sface='neutral'
show shika at c2
s "I swear, Kotori..."
s "What am I going to do with you?"
$ kface='laughing'
show kotori at c2
k "You don't have to do anything. I will do all of the work for you!"
"Again with the grabbing motions."
k "Like I always have!"
$ kface='smiling'
show kotori at c3
k "After all, letting such a nice chest go to waste is a crime against humanity!"
$ spose='1'
show shika at c3
s "I wouldn't say that it's that much of a big deal, you know..."
$ kface='laughing'
show kotori flip at c3
k "But it is!"
"While she's just talking nonsense, I'm happy to see that she's in high spirits again."
"Our victory over Akane must have perked her right up."
$ kface='neutral'
show kotori at c4
k "While not fighting her was a bit of a let down..."
$ kface='smiling'
show kotori at c3
k "Zooming in on her face when she realized that she fell for the trap completely was amazing!"
k "I saw that you were replaying that moment yourself!"
$ sface='smiling'
show shika flip at c3
s "Yes... I couldn't help but gloat a little bit about it."
$ kface='happy'
show kotori at c2
k "Nothing wrong with a little gloating, Captain!"
k "Especially when you're beating a little brat like her!"
"Kotori laughs heartily."
$ kface='laughing'
show kotori at c3
k "I can't stop myself, every time I think about that look on her face..."
"If there's one thing Kotori cannot stand, it's arrogance."
"Granted, she is a bit full of herself..."
"But she can't stand it when other people are the ones walking all over her."
"Then again, that's just natural, isn't it?"
stop music fadeout 2.0
"For a moment, I can't help but think to myself."
$ sface='neutral'
show shika at c3
play music sad fadein 2.0
s "Say, Kotori..."
$ kface='smiling'
show kotori at c4
k "Yes, Captain?"
s "What do you think of this life we have chosen?"
"She cocks her head to the right, a blank expression on her face."
$ kface='neutral'
show kotori at c3
k "Now why are you suddenly asking a question like that, Captain?"
s "Well..."
s "I've just been thinking to myself lately..."
"How can I put it into the right words..."
$ kpose='1'
show kotori at c2
k "Yes? What are you trying to say, Captain?"
$ kface='smiling'
show kotori flip at c3
k "I'm right here for when you want to share your deepest, darkest secrets!"
s "No, no, it's nothing quite like that."
$ kface='neutral'
show kotori flip at c4
k "Aww..."
k "Well, what is it then?"
"She's listening intently now."
$ spose='1'
show shika at c2
s "Let's say that everything goes according to plan..."
s "We capture Akane, turn in evidence of her guilt, and collect the bounty..."
$ sbody='sb'
show shika flip at c3
s "One billion imperial dollars could buy us our own capital ship with money to spare."
s "All three of us would never have to work another day in our lives again."
s "So, have you ever thought about how all of this ends?"
"That's something that I have thought a lot about myself."
"As the captain, it's my job to make ends meet."
"One day, we're going to have to give up this life we have chosen for ourselves."
"Kotori does not say anything."
"She just sits there, looking at me."
"Patiently waiting for me to continue."
$ spose='1'
show shika flip at c4
s "As it is, we're just drifting from job to job, from galaxy to galaxy."
s "Our line of work doesn't exactly leave a lot of time for introspection."
s "But we need to start thinking about what we should do in the future."
"I wander over to the window in my room, looking out at the vast void."
$ sbody='sa'
show shika flip at c3
s "If this job is successful, we will be some of the wealthiest people in this galaxy, for sure."
s "But the question is, what should we do from there?"
s "We can't just keep living in the moment."
$ spose='1'
show shika at c2
s "Have you ever thought about things like that, Kotori?"
"I make a gesture towards the window."
$ sbody='sb'
show shika at c3
s "There is a vast, vast, vast universe out there."
s "So vast that we could never explore all of it if we wanted to."
stop music fadeout 2.0
s "Don't you think that there might be something better out there for us?"
$ kface='laughing'
show kotori flip at c4
play music happy fadein 2.0
k "Oh, Captain! You sound like an old lady!"
$ sface='shocked'
show shika at c2
"Kotori starts laughing to herself again."
$ kface='happy'
show kotori at c3
k "Even if I were rich enough to never work another day of my life, I would still do it anyway!"
k "Some people win the lottery and choose to continue leading their lives as they always have!"

$ kface='smiling'
show kotori at c2
k "Why should we be any different?"
k "This is the life for me! There is no doubt about that!"
$ kface='laughing'
show kotori at c3
k "I can't think of any other job that my skillset would be suited for!"
$ sface='neutral'
show shika at c3
"Somehow, I think I already knew that was going to be her answer."
$ kface='smiling'
show kotori at c4
k "But... At the same time..."
k "I know that this isn't going to be all that there is in your life, Captain."
$ kface='happy'
$ kpose='1'
show kotori at c2
k "You're going to do something incredible. I just know it!"
k "If one billion imperial dollars is going to get you where you want to be, then we have to make sure that this job is a success!"
$ kbody='sb'
show kotori at c3
k "You know me better than anyone else, Captain..."
k "I am never going to live for anything but the moment."
$ kpose='1'
show kotori at c4
k "So I'm just going to leave those things to you!"
k "But don't think about leaving me behind!"
k "I want to be there for every step of the journey!"
$ kface='laughing'
show kotori at c3
k "All of us are bound together!"
$ sface='smiling'
show shika at c2
s "Yes... That's right..."
s "Ever since we all met, we have all been sailing on the same currents."
s "Just all drifting through this cold, vast universe together..."
"I cannot help but sigh as I reflect on it."
$ spose='1'
show shika flip at c3
s "How long ago was that now?"
$ kface='smiling'
show kotori flip at c3
k "That was back on Earth! Ages ago!"
k "Hard to believe that we all ended up somewhere so far away from there..."
$ sbody='sb'
show shika flip at c2
s "It really is hard to believe."
s "Viable space travel was thought to be impossible just a generation ago."
s "Now here we are."
$ kpose='1'
show kotori at c3
k "Yep..."
"Kotori rests one of her hands on my shoulder."
$ kbody='sb'
show kotori at c2
k "You're our driving force, Captain."
k "We never would have ended up here without you!"
k "Don't you think that is amazing somehow?"
"She points to the window."
$ kpose='1'
show kotori at c3
k "Earth isn't even a twinkle among those stars right now..."
k "That's how far we have all gone together."
$ kbody='sa'
show kotori at c4
k "And you're telling me that we have to give up this life?"
k "That doesn't have to happen at all."
$ kface='laughing'
show kotori flip at c3
k "So, even if we do become filthy rich..."
k "Let's just enjoy this life a little longer!"
$ spose='1'
show shika at c3
s "You're right..."
s "It's best to take the time to settle into things."
$ sbody='sb'
show shika at c2
s "Some people who win the lottery end up spending all of their money because they are not used to handling such finances..."

s "We won't rush into something new."
s "One small step at a time will be the best way to handle it."
$ kface='smiling'
show kotori at c4
k "Exactly!"
k "See, you're overthinking it again."
k "Someone has to be around to drag you back to..."
$ kface='neutral'
show kotori at c3
k "Well, I guess that expression doesn't work here."

k "But you get the idea, right?"
$ sface='laughing'
show shika at c2
s "Yeah, someone has to drag you back down to Earth."
$ kface='laughing'
show kotori at c3
"We both laugh together."
k "No matter what happens from here, it will work out fine!"
k "Akane either will have to destroy the evidence and retreat, or we capture her!"
$ kface='smiling'
show kotori at c4
k "We've proven that we can outsmart her, and what can happen once can happen again!"
"She appears to be fired up now."
k "No matter what Akane has in store for us, we have the advantage!"
$ sface='smiling'
show shika at c3
s "Yes..."
$ kpose='1'
show kotori at c2
k "Anyway, I need to go practice!"
$ kface='angry'
show kotori at c3
k "And Nami hasn't paid me back for making me hold the camera either..."
"I want to object, but I know that there will be no stopping her."
k "Don't stay in here overthinking things for too long, Captain!"
call h_kotori from _call_h_kotori_4
"Just as silently as she appeared, she disappears out the door."
ai "She appears to be in good spirits, Captain."
call s_shika from _call_s_shika_22
s "She most certainly does."
stop music fadeout 2.0
"Hopefully, we can enjoy a little more peace before Akane comes after us..."
call h_shika from _call_h_shika_13

scene hallway with fade

call s_shika from _call_s_shika_23
play music night fadein 2.0
"It's gotten fairly late now."
"The hours have passed by at a snail's pace."
"I can't bring myself to sleep, however."
"Akane must have something extravagant planned for us next."

menu:
    "It's probably fine for now.":
        $ spose='1'
        show shika at c2
        "It's probably fine for now."
        "She was still hit by that stunning round and took a few blows from Nami's blade."
        "That would mean that she is out of commission for a little while, at least."
        "Maybe I could get some sleep..."
        $ sbody='sb'
        show shika at c3
        "Then again, wouldn't this be the perfect opportunity for her to strike?"
        "While she wouldn't do anything, she could quickly send out more drones..."

        "She's proven that she has abundant resources."
        "So, no, I cannot relax just yet."
        $ spose='1'
        show shika at c4
        "Wisdom would dictate that now is a time where I definitely cannot relax."
        "Akane knows exactly how we think..."
        "So our only solution is to do things which she wouldn't first expect us to do."
    "I cannot let my guard down.":
        $ investigate += 1
        $ spose='1'
        show shika at c2
        "While I'm tired, that's nothing that some cheap coffee cannot cure for now."
        "Knowing Akane, she would have already started planning a counterattack."
        "In fact, making her less mobile probably made her more dangerous in other ways."
        $ sbody='sb'
        show shika at c3
        "She probably won't reveal herself again and will just send wave after wave of assault drones at us."
        "No matter how strong our defences are, they could not withstand a tide like that..."
        "Her ego has been bruised, so she will probably want to get her revenge sooner rather than later."
        "All in all, the best course of action for now would be not to let my guard down."

        $ spose='1'
        show shika at c4
        "If I do that and she chooses to strike then..."
        "Then I would be really disappointed in myself."
"So, for now, I'm going to take a long walk."
"And make sure that there is nothing amiss in the halls of our quarters."
ai "Is it really necessary for you to patrol the halls yourself?"
$ spose='1'
show shika at c3
s "We cannot afford to take any risks."
s "If a single thing looks out of place, I do not want to miss it."
s "Akane probably still has access to the maintenance shafts."
s "So she could easily burst through the roof or anywhere else."
$ sbody='sa'
show shika at c2
s "And I cannot sleep anyway..."
s "So I might as well do something useful, don't you think?"
ai "But it would be wise for you to get some rest."
ai "I can raise the alarm if anything unusual happens."
$ sbody='sb'
show shika flip at c2
s "I can rest when this is over."
s "We don't know when she's going to attack."
"It's not that I do not trust our AI..."
"But... A machine is fallible, no matter how intelligent it is."
"Akane would know that too."
ai "Even so, there is only so much that you can do alone."
$ sbody='sa'
show shika flip at c3
s "I am the captain of this company, and I will ensure their safety."
s "If that means that I have to lose a bit of sleep over it, then so be it."
"The AI becomes silent."
"It's then that I see my two crew members approaching me."
$ kface='angry'
call s_crew from _call_s_crew_9
stop music fadeout 2.0
k "Hey, Captain!"
n "Captain..."
s "Is something the matter, you two?"
k "Have a look at this!"
"Kotori is waving a digital pad in front of my face."
k "Akane sent us a message!"
$ spose='1'
show shika at c3
s "A message...?"
s "What kind of message?"
k "Just have a look for yourself!"
"She shoves the pad into my hands."
"A pre-recorded video begins playing before me."
call h_crew from _call_h_crew_3

play music serious fadein 2.0
scene cg3
if persistent.adult==True:
    scene cg3_A
with dissolve

a "Hey! It's nice to see all of you again!"
"Akane is spread out on the floor, her whip in one hand."
a "I would have delivered this message personally, but after what happened last time..."
a "It would be best to be a bit more cautious, don't you think?"
a "I really am tired after you hit me with that stunning round, Captain..."
a "Nami really managed to wear me out too."
a "I suppose I should be angry at myself for being fooled by your trick..."
a "But if anything, I'm really excited!"
"She has that same look of glee on her face that she did before."
a "I'm sure that you've already guessed that I know about Kotori recording me confessing."
a "That does put me in a rather tricky situation."
a "So, it looks like I have my back to the wall!"
a "Cornered like a wounded beast!"
a "But remember, it's when a beast is cornered that it's most dangerous..."
"She begins to slide her whip slowly down the centre of her chest."
a "I didn't want it to end so suddenly, anyway."
a "This little game has to play out a bit longer yet."
a "Even though you have that footage, you won't release it until you either capture me or I leave this ship."
a "After all, you wouldn't want someone else to snatch your bounty, would you?"
"Once again, she's proving to be sharp."
"She has pieced together our intentions."
a "So, there's only a few ways this can end."
a "I can't guess which way it will be..."
a "I knew that my idols wouldn't disappoint me!"
a "It's only been a short time, but I've had so much fun!"
"She seductively licks one of her fingers."
a "Believe me, we're all going to have a lot more fun together before this is over..."
a "I'm going to make sure of it."
a "So, don't get too comfortable in that little fortress of yours."
a "Any egg can be cracked open if you know how."
a "With that said, I'm going to go take a nap and sleep off this stunning round."
"She puts her fingers on her lips and then puts them towards us, blowing a kiss to the camera."
a "See you all veeeeery soon!"
a "I hope you all enjoy it. I know that I'm going to..."
a "Every single moment of it."

scene hallway with dissolve

$ kface='angry'
call s_crew from _call_s_crew_10
"With that, the digital pad goes silent."
"Kotori is quivering with rage."
k "Damn it..."
k "The worst thing is that she's right!"
$ kpose='1'
show kotori at c2
k "I want to fight her already! The suspense is killing me!"
"She's practically growling to herself."
k "Never have I met a bounty who was so annoying!"
$ npose='1'
show nami at c2
n "Even though we have the upper hand, it seems that the game isn't over yet."
$ spose='1'
show shika at c2
s "Do not concern yourselves with her taunting."
s "She hasn't told us anything that we don't already know."
"Kotori is having none of it, however."
k "We can't just keep ignoring these insults!"
$ sbody='sb'
show shika at c3
s "We have to, Kotori."
s "I know how you feel about it, but if you allow her to do this to you..."
"Nami nods in agreement."
$ npose='1'
show nami at c3
n "Do not worry about it, Kotori."
n "She will not be able to fool us if we keep our heads clear."
$ sbody='sa'
show shika at c4
s "Exactly."
s "If you let yourself fall for her taunts, she's going to trap you again and again."
$ kbody='sb'
show kotori at c3
k "Just knowing that makes me even angrier!"
k "She still has the gall to taunt us even though we managed to catch her with our trap before!"
"Kotori grits her teeth, but she regains her composure."
k "No... I'm not going to let her win."
"Nami just looks at it blankly."
$ nbody='sb'
show nami at c4
n "You cannot just sleep off a stunning round."
n "It will be a day or two before she can move unhindered again."
"Both of them look to me."
$ kface='neutral'
show kotori at c2
k "What do we do now?"
$ spose='1'
show shika at c3
s "For now, we wait."
s "If we don't hear from her again within the next three days, we should presume that she's fled."
s "I doubt that she is going to leave, however."
s "Her pride has been wounded, and we have hard evidence of her confession..."
$ sbody='sa'
show shika at c2
s "She has plenty of reason to stay."
s "So, we will wait for her to make her move."
s "Until then, we can only stay on alert."
$ sbody='sb'
show shika at c3
s "Kotori, hold onto that digital pad and see if she sends any more messages."

s "Let's do our best, everyone."
n "Acknowledged, Captain."
$ kface='smiling'
show kotori flip at c3
k "Got it, Captain!"
ai "Acknowledged."
hide kotori
hide nami
with dissolve
"The two of them quickly leave."
"If she's sending messages by digital means..."
"Then we can no longer rely on playing off her ego."
"That is a pity, but I suppose it cannot be helped."
stop music fadeout 2.0
"Even someone like her learns not to put their finger on a hot iron after getting burned."
call h_shika from _call_h_shika_14
scene meetingroom with fade
play music space fadein 2.0
call s_shika from _call_s_shika_24
"The meeting room seems to be the place where I can collect my thoughts."
"Another cheap cup of coffee helps too."
"As I take a deep sip from the cup, the caffeine seems to cut through the cloud around my mind."
"There is so much to consider..."
"So much that I have to plan for."
"The hours seem to be passing by slowly as my thoughts swirl through my head."
"Here I am, just waiting for something to happen..."
$ spose='1'
show shika at c2
"The anticipation in the air could be cut with a knife."
ai "Captain, will you be getting any rest soon?"
ai "As a reminder, I did suggest this to you hours ago."
ai "And you have not had any rest since then."
ai "Akane still has some time before she fully recovers from her stun round."
"I really do get tired of the AI playing as my nanny."
$ sbody='sb'
show shika at c3
s "I know, I know..."
s "But just because she isn't fully mobile doesn't mean she isn't a threat."
s "When we first met, she deployed a small army of attack drones."
$ spose='1'
show shika at c4
s "I don't know where she got them from, but I can't rule out her using drones or robots to soften our defences first."
s "Or maybe she will use the maintenance shafts again..."
ai "It is possible for her to use that, correct."
ai "But I can alert you as soon as something unusual appears."
ai "Your optimal health is my priority, Captain."
$ spose='1'
show shika at c3
s "Just leave me to my thoughts for a moment."
ai "As you wish."
"The AI goes silent again."
"I rub the sleep out of my eyes, trying my best to stay alert."
"Maybe it's right..."
"If I'm going to be dead tired by the time Akane finally makes a move, then what is the point?"
"Surely she's going to need to sleep at some time as well..."
$ sbody='sa'
show shika at c2
"Then again, she's not from around here."
"Her body clock is probably adjusted to an entirely different schedule to mine."

"I pull out my digital pad, getting ready to put down some thoughts."
"There are any number of techniques that Akane could employ to trick or disable our AI."
"She could cut our power. It would take a few seconds for the emergency power to come online..."
"Which would be plenty of time for her to slip in."
"Motion sensors, cameras, heat sensors..."
$ spose='1'
show shika at c3
"She isn't stupid. She would find a way to avoid all of these things."
"The ventilation system is also another place she could strike from, despite additional security measures..."
"I guess I won't know what she's going to do until she does it."
$ sface='angry'
show shika at c2
"That is the most frustrating thing about all of this."
"Perhaps it would be better to take some time to rest and get my wits back."
"I'm going to be a nervous wreck if I keep doing this to myself..."
"And what good would a nervous wreck be by the time Akane makes her move?"
stop music fadeout 2.0
ai "Captain. There appears to be an intruder in Nami's room."
$ sface='shocked'
show shika at c3
play music serious fadein 2.0
"Akane...!"
"With no hesitation, I immediately bolt out of the room."

scene hallway with dissolve

$ sface='angry'
show shika at tcenter
s "Bypass the security protocols on her door."
s "I need to get in there!"
ai "Acknowledged."
stop music fadeout 2.0
s "Nami, what is-"

play music funny fadein 2.0
scene cg6
if persistent.adult==True:
    scene cg6_A
with dissolve
pause

"... Oh."
"I'm... I'm not really sure what I just stumbled into."
"Kotori stands there, locking lips with her."
"For a little while, everything seems to go deathly quiet."
"Nami's eyes are wide with shock, the sheer surprise plainly visible on her face."

"Kotori pulls back."
k "Your lips are so soft, Nami!"
n "Are... Are they...?"
k "Yep! I could kiss you all day..."
k "And maybe even a little longer than that..."
"Kotori glances at me, recognising my presence."
k "Nice to see you, Captain!"
k "What are you doing here?"
s "The AI... said there was an intuder... in Nami's room..."
k "Yep, I sneaked in here!"
k "I said I would extract my price, after all..."
k "Don't think you're going to get away with making me hold the camera, Nami!"
n "K-Kotori... This... This isn't a good... a good time..."
n "Real... Really... Not a good time..."
n "What about... What about Akane..."
"Despite this entire absurd scene, there is something strangely cute about Nami when she's acting like this."
"Usually so cool and focused, she seems to become like an awkward teenage girl."
k "Stop being so shy! I'm not here to judge!"
k "You're just so cute, Nami!"
n "Y-You too..."
"Nami's awkwardness is at its peak."
"She just stands there, unsure of what she should do."
"Yet, she doesn't make any move to stop Kotori."
"Kotori's arm is tightly wound around her waist, making sure that she can't get away from her lips."
k "the captain already paid her price, so now you have to as well!"
"Kotori relocks lips with her eagerly."
"They stay that way for the longest time, with Kotori not letting Nami get away."
"Nami pulls away from Kotori's lips with considerable effort."
n "You're... You're making the captain... worry... Kotori..."
n "Can... Can we do this later..."
k "Oh, so you're admitting that you would like to do this..."
k "I am so lucky!"
k "We're going to have so much fun together, Nami!"
n "Yes... We will... have fun..."
k "That's right!"
"Kotori gives her one more small peck on the cheek."
k "Now then, you have paid your debt..."
k "... For now."
k "I had better get to have a fight with Akane, or I'm going to get both of you."
s "Next time, don't sneak into Nami's room when we're on high alert."
k "Got it, Captain!"
stop music fadeout 2.0
"Satisfied, Kotori leaves Nami's bedroom."


scene namiroom with fade
$ huer = 1.0
$ hueb = 1.3
$ hueg = 1.0
play music happy fadein 2.0
"After Nami gets her suit back on, she just awkwardly sits on her bed."
$ nbody='ba'
$ nface='embarrassed'
call s_nami from _call_s_nami_8
n "It's... It's embarrassing..."
n "To be seen like that..."
$ npose='1'
show nami at c2
n "Not a good time..."
n "Not a good time at all..."
$ spose='1'
show shika at c3
s "Then let's just pretend I didn't see that."
"That would be for the best, in all honesty."
s "Honestly, I got an alert that there was an intruder in your room..."
s "But I couldn't have known it would be Kotori."
$ nface='shy'
show nami at c4
n "I didn't know what was happening..."
s "Nami, please pull yourself together."
$ npose='1'
show nami at c3
n "R-Right... I'm sorry..."
n "I just need a moment..."
"She regains a bit of her composure."
$ spose='1'
show shika at c2
s "If there is another alert like that in any room, we shouldn't ignore it."
s "Akane could potentially exploit it."
$ nface='neutral'
show nami at c4
n "Yes. You're right."
"Nami touches her lips."
$ nface='embarrassed'
show nami at c3
n "I..."
"She just gets a flushed expression on her face again."
"I just shake my head."
$ spose='1'
show shika at c3
s "I think that you're going to have to overcome your awkwardness one day, Nami."
s "I might not always be around to do all of the talking for you when it needs to be done."
stop music fadeout 2.0
$ nface='shy'
show nami at c2
play music night fadein 2.0
n "You know me, Captain..."
"She slowly trails one finger down the window next to her bed."
$ npose='1'
show nami at c3
n "I enjoy my alone time."
n "When it's not about work, I just can't focus..."
"She is just so painfully shy."
"The polar opposite of Kotori."
$ nbody='bb'
show nami at c4
n "How does Kotori have so much confidence, Captain?"
n "She... She knew we were on high alert... And yet..."
n "She... She still..."
$ sface='smiling'
show shika at c2
s "It's like what you said. It's just how she is."
s "I know that it's hard to deal with, but you will just have to accept it one day."
$ spose='1'
show shika at c3
s "Besides, there is a certain charm to your awkwardness, Nami."
$ nbody='ba'
show nami at c3
n "D-Do you really think so?"
n "I... I don't really see, logically speaking..."
$ nface='embarrassed'
show nami at c4
n "How it would..."
"She starts stammering."
"I'm surprised at how cute she is when she acts like this."
$ sface='neutral'
show shika at c2
s "It's alright, you know."
s "Take a deep breath."
"She does so, calming herself down a bit."
$ nface='neutral'
show nami at c3
n "Right..."
n "My apologies, Captain."
n "I lost my composure there."
s "Well, considering that Kotori just invited herself into your room..."
s "That would take anyone by surprise."

$ npose='1'
$ nbody='ba'
show nami at c2
n "Yes... it would."
n "Captain..."
s "Yes, Nami?"
n "Let's change the topic."
$ nbody='bb'
show nami at c3
n "I have been looking further into our bounty."
$ spose='1'
show shika at c3
s "What do you mean?"
n "What I mean is that I have been trying to find out who exactly placed this bounty in the first place."
n "With what available evidence we have, I have not seen anything which warrants her having a price like this on her head."
$ nbody='ba'
show nami at c2
n "Not to mention that the bounty specifically requested that she be brought in alive."
n "What do you make of that, exactly?"
$ sbody='sa'
show shika at c4
s "It's hard to say, Nami..."
s "There are any number of reasons why."
menu:
    "Maybe it is someone with a grudge.":
        $ sbody='sb'
        show shika at c3
        s "If I were to take a guess, it might be someone with a grudge."
        s "Her name is an alias and we know nothing about her past..."
        s "So maybe she has someone who is out to get her?"
        "That does not seem like an unreasonable presumption."
        "Putting a bounty on someone's head because you hate them."
        $ nbody='bb'
        show nami at c3
        n "But, Captain, why is it such a high amount?"
        n "There are many people who might bear a grudge against you, especially powerful people..."
        n "Not one of them has offered anything like this before."
        $ npose='1'
        show nami at c4
        n "No. I think that having a grudge is too petty of a motivation for something like this."
        "Now that I think about it that way..."
        "Even if you hated someone that much, it wouldn't be worth paying that much money."
        "She has to be significant to them in some other way."
        "That would be a more reasonable presumption to make."
    "Maybe she is important.":
        $ investigate += 1
        $ sbody='sb'
        show shika at c3
        s "The petty crimes she has conducted doesn't warrant having such a high bounty..."

        s "So, I can only imagine that she is someone important to the person setting the bounty."
        n "Important to them? In what way?"
        s "I do not know. But whoever they are, they seem not to care about how much money they have to spend to bring her to them."

        s "There could be other motives, but none of them seem fitting for this."
        s "We have seen that she has access to incredible resources, so I can only imagine that she has wealth to burn as well."
        $ nbody='bb'
        show nami at c3
        n "So you think that whoever placed the bounty is a benefactor of hers?"

        n "Or something along those lines?"
        s "Potentially."
        s "They value her enough to place the largest bounty ever in this entire galaxy."
        s "And with that much wealth, you would surely be in a position of power."
        s "So, maybe she is a runaway or something like that..."
        n "It does seem to add up..."
        $ npose='1'
        show nami at c4
        n "A wealthy, bored member of one rich family or another."
        "Nami nods."
        n "While we cannot confirm it right now, I think that we might be onto something."
$ npose='1'
$ nface='smiling'
show nami at c3
n "Despite how much trouble she has been causing us..."
n "I do want to find out the reason behind all of this."

$ nface='neutral'
show nami flip at c3
n "Kotori would probably be more interested in the one billion than the mystery, though..."

$ sface='smiling'
show shika at c2
s "We will cross that bridge when we get to it."
$ sface='neutral'
show shika at c3
s "For now, our main concern should be what we should do when she finally attacks."
$ npose='1'
show nami at c3
n "Of course."
$ nbody='bb'
show nami at c2
n "Can we talk later, Captain?"
s "As you wish."
s "Please inform me if you see anything unusual."
n "I will, Captain."
call h_nami from _call_h_nami_2

scene hallway with dissolve
$ huer = 1.0
$ hueb = 1.0
$ hueg = 1.0
call s_shika from _call_s_shika_25
"So it was just a false alarm."
"Although I question Kotori's timing, I'm relieved that it wasn't an attack."

"You're always at your most vulnerable in familiar settings."
"I don't know if Nami keeps her weapons in her room."
$ spose='1'
show shika at c4
"This also means that our AI is vigilant enough to be able to detect any unusual movement."

"Perhaps I can rely on it for now."
"Akane still has time before she recovers..."
"So that also gives me some time to relax."
stop music fadeout 2.0
"Back to brooding by myself, I suppose."
call h_shika from _call_h_shika_15

scene meetingroom with fade
play music space fadein 2.0
call s_shika from _call_s_shika_26
"The hours continue to drag along."
"No matter how much I glance at the clock, they do not seem to move any faster."
"They say a watched kettle never boils..."
"I'm inclined to believe it."
"Now then, I need to start thinking through my plans."
"When Akane attacks, I need to be prepared."
$ spose='1'
show shika at c2
"Just sitting here and waiting for something to happen isn't the correct way to approach it at all."
"First, I need to determine at what possible points she could strike from."
"The most obvious place would be the front door."
"But because it's the most obvious place she would strike from, would she choose that?"
"I'd better not linger on that for too long."
$ sbody='sb'
show shika at c3
"Second is the ventilation system."
"Not without its hazards and we could easily trap where the vents intersect."
"The only drones you could send through it would be fairly small."
$ sbody='sa'
"Even for someone of Akane's slim frame, it would be too hard to squeeze through."
"She has a good idea of what I'm thinking. So I think I will trap the vents anyway."
"The maintenance shafts are also going to be a problem..."
"She could easily launch an attack from there."
"I hope that engineer we spoke to has raised some complaints..."
$ spose='1'
show shika at c4
"I might have to contact him and ensure that nothing unusual has happened around there lately."
"But how can I contact him? We can't really leave our quarters right now."
"Well, that must mean that the maintenance shafts are going to be her ideal way to attack."
"But where else could she come from?"
$ spose='1'
show shika at c3
"There is only one other place she could attack from..."
"The outside of the ship."
"We have some windows that she could go through."

$ sbody='sa'
show shika at c2
"At the same time, I have to remember that she's not trying to kill us."
"Doing something that would potentially endanger us like that would be going too far, even for her."
"At the same time, I need to keep it in mind as a possibility."
"If I overlook any details and endanger my crew..."
$ sbody='sb'
show shika at c3
"What right do I have to be a captain?"
"Now then, I will position drones here, here, and here."
"Stunning rounds versus organic targets. EMP rounds for inorganic targets."
"I will set up some skuttlebots to patrol the vents and ensure that there isn't anything unusual..."
$ sface='smiling'
show shika at c4
"And the final stroke to our defences will be my secret weapon..."
"A mod on my pistol which not even Kotori or Nami know about."
"It's bound to take Akane by surprise."
"I'm sure of it."
stop music fadeout 2.0
"Maybe I should head over to the simulation room and see if it's not being used."
scene simulation with dissolve
play music serious fadein 2.0
"When I enter the room, I find that it's empty."

"Kotori and Nami must be in their rooms right now."
"That's fine by me."
"I need some practice."
$ sface='neutral'
call s_shika from _call_s_shika_27
s "Simulate firing range."
ai "Before you simulate anything, Captain..."
ai "Might I make a suggestion?"
$ spose='1'
show shika at c2
s "Go on..."
ai "I believe that I have collected enough footage of Akane to do a simulation of her."
ai "It will only be a rough estimate, but it would probably be a good way to prepare yourself for her attack."
s "Could you play that footage back to me? Simulate a 3D image of it."
ai "Acknowledged."
"The footage plays out before me."
"Akane moves incredibly fast."
"That's the first and most obvious thing about her."
$ spose='1'
show shika at c3
s "Slow it down."
"As the footage slows down, I can get an impression of how Akane moves."

s "I see, I see..."
ai "Using this footage here, and the few security camera reels of her on those planets..."
ai "I believe I can create a digital simulation of her."
$ sbody='sa'
show shika at c4
s "Why don't you show me?"
$ aface='smiling'
call s_akane from _call_s_akane_2
"Sure enough, a digital copy of Akane appears before me."
"It quietly stands to rigid attention, waiting for the next input."
"Despite myself, I am disturbed by its silence."

"I suppose I am too used to hearing Akane constantly whenever she shows her face."

$ spose='1'
show shika at c2
s "Pistol configuration: Stun."
s "Begin combat simulation."
$ sface='shocked'
show shika at c1
"Before I can even blink, the simulation bolts at me."
"I let off a few shots, but it nimbly evades them."
$ apose='1'
show akane at c1
"With her closing the distance so quickly, I have no choice but to retreat backward."
"Firing over my shoulder, I make sure not to stop moving."

$ sface='neutral'
show shika flip at c2
"Her whip is insanely fast..."
$ sface='shocked'
show shika at c3
"Much to my dismay, I feel something wrap around my leg."
$ apose='1'
show akane at c3
"The simulation stops then and returns to its rigid stance."
ai "Simulation over."
ai "You did not manage to land any hits on her."
$ sface='neutral'
show shika at c2
"As I thought, Akane is the worst possible opponent for me."

"My main advantage is my pistol."
"With that, I can usually put a significant distance between me and my opponents."
"But Akane has significantly less distance she has to close if she wants to snare me with her whip."
$ spose='1'
show shika at c3
"I am sure that if she's going to single anyone out, it's going to be me next."
"She said as much when we last met."
"So, I need to think of a solution to this."
$ sbody='sb'
show shika flip at c3
"What can I do to stop her from getting within her ideal range?"
"Perhaps I should try out the secret configuration..."
"No. Not yet."
"I need to try out other solutions first."
$ sbody='sa'
show shika at c3
s "Run the simulation again."
ai "Acknowledged."
s "Configuration: Buckshot."

"This will essentially turn my pistol into a shotgun."
"The spray of pellets should be wide enough to be able to hit her."
$ apose='1'
show akane at c2
"She's still as fast as ever."
"I suddenly turn around and open fire."
"In the time that I turn around, she's already in my face."
$ sface='shocked'
show shika at c2
"The whip wraps around my torso, making me drop my pistol."
ai "Simulation over."
$ apose='1'
show akane at c1
"She's just too damn fast..."
$ sface='neutral'
show shika at c2
s "I need to stay moving then."
s "I cannot get a clear shot while I'm doing that, however..."
"To hit a target like Akane will require an aimed shot."
"Unless..."
$ spose='1'
show shika at c3
s "Damn it all."
s "Run it one more time."
"I turn on the secret configuration."
ai "Running simulation."
call h_shika from _call_h_shika_16
stop music fadeout 2.0

scene simulation with fade

call s_shika from _call_s_shika_28
play music day fadein 2.0
ai "A most impressive performance, Captain."
ai "I have never seen you use that pistol configuration, however..."
s "Please do not tell anyone about it."
s "Delete any memory of it from your hard drives."
ai "Done."
$ sface='smiling'
show shika at c2
"Good. I don't want anyone to know about this configuration."
"Akane won't see it coming."
"Although what I beat was merely a simulation and could not possibly represent the real thing..."
"I feel a bit more confident that I will be able to go toe-to-toe with her."
stop music fadeout 2.0
"It's then that the alarm starts sounding."
ai "I have detected a fourth person present in our quarters."
ai "Drones are currently being dispatched to their location."
$ sface='neutral'
show shika at c3
s "Where is the intrusion?"
ai "It appears to be coming from your room, Captain."
$ sface='shocked'
show shika at c4
"... My room?!"
"How... How could it be?!"

scene hallway with dissolve

play music serious fadein 2.0
"I burst out of the simulation room."
"Kotori and Nami come running down the hall."
$ kface='shocked'
$ nface='shocked'
call s_crew from _call_s_crew_11
k "It's coming from your room, Captain?!"
n "How is that possible?"
s "I do not know..."
"All of us rush into my room..."

scene bedroom with dissolve

call s_crew from _call_s_crew_12
"Only to find that there is no one there."
s "Wait..."
s "Where is she?"
"There is not a single sign of another soul here."
$ nface='neutral'
show nami at c2
n "No..."
n "Something had to set off the alarm."
$ npose='1'
show nami at c3
n "There's nowhere she could be hiding in this room, with the size of her frame."
"Nami looks over to one of my spare coats."
$ kface='neutral'
show kotori flip at c3
k "Wait..."
k "Don't you hear a humming noise in the room?"
"Nami reaches in..."
"And pulls out a strange, metallic device."
$ npose='1'
show nami flip at c3
n "Oh..."
n "This was a device built to give off a heat signature."
$ nface='shocked'
show nami at c2
n "But how did it get here?"
"It's then that I realize it."
$ sface='angry'
show shika at c3
s "She must have slipped it into my coat when she was retreating."
s "Which means that this was a distraction...!"
$ kface='angry'
show kotori at c4
k "Damn her! Always with her sneaky tricks!"
"It's then that the alarm rings again."
ai "There are multiple inorganic intrusions through the front entrance."
ai "Countermeasures are failing."
ai "I would like to request assistance for holding off this attack."
stop music fadeout 2.0
"All of us nod in unison."
call h_crew from _call_h_crew_4

scene hallway with dissolve

call s_crew from _call_s_crew_13
play music battle fadein 2.0
"We rush back to the front door, only to see a huge variety of different drones swarming out from it."
"They've broken down our reinforced doors."
n "Let's do this."
$ kpose='1'
show kotori at c2
k "Right!"
"The two of them dive into the horde with no hesitation, their blades humming with energy."
"Their swift movements stem the tide."
"Although they strike down drones, it's akin to using two bullets against a swarm of bees."
$ npose='1'
show nami at c2
n "There's so many of these things..."
$ kface='smiling'
show kotori at c3
k "At least it's good exercise!"
"I pull out my pistol and provide supporting fire."
$ sface='angry'
show shika at c4
s "Hold fast, crew!"
s "We will see this metal tide driven away from our home!"
$ kface='happy'
show kotori at c2
k "Got it, Captain!"
$ npose='1'
show nami at c3
n "I understand, Captain."
"Their resolve renewed, they begin to make headway against the robotic swarm."
"Bit by bit, inch by inch..."
"We drive them away from the halls."
"Suddenly, a massive drone begins to barge its way through the swarm."
"It slams down two massive steel plates in front of it in a cone formation."
$ sface='shocked'
show shika at c3
s "It's a siege bot!"
"Kotori charges at it, striking at its shields."
"She barely manages to cut it."
$ kface='angry'
show kotori at c2
k "Damn...!"
"It swings one of its shields, forcing Kotori to retreat backward."
"Nami moves to strike it, but the robot immediately notices."
"She's met with an impenetrable wall of solid steel."

"She retreats as well."
"Soon, all three of us are at the other end of the hall, looking back at the robot."
$ npose='1'
show nami at c3
n "Our current weapons won't be able to penetrate through those shields."
n "And the hallway is too narrow for us to be able to evade its attacks."
n "We need to damage it somehow..."
$ sface='neutral'
show shika at c4
s "Hold on..."
"I begin to adjust the settings on my gun."
s "Configuration: Railgun."
"My pistol's minuscule size means that it won't pack much of a punch..."

"But it should be enough to be able to pierce through this thing's armour."
s "I need a moment for it to charge."
s "Cover me."
$ nbody='sb'
show nami at c3
n "Understood, Captain."
$ kface='smiling'
show kotori at c3
k "Right away!"
"The two of them defend me from the oncoming robot horde."
"The siege bot is still lumbering towards us, enabling the robots to reclaim territory they had lost."
"It's only a metre away before my pistol finishes charging."
$ sface='angry'
show shika at c2
s "Opening fire!"
"The super accelerated shot in my pistol blasts through its shield, shredding its insides as if they were butter."
"It stumbles from the force, its reactions extremely slow."
$ npose='1'
show nami at c2
n "It seems like you have hit one of its processing cores, Captain."
$ sface='smiling'
show shika at c2
s "That's what I was aiming for."
$ kface='happy'
show kotori at c3
k "Then what are we waiting for?!"
"With its reactions so much slower than before, the siege bot isn't able to move fast enough to keep up with my crew members."
"It tries to shield bash Kotori, only for it to miss completely and stumble."
"She elegantly evades its clumsy attack."
"Her daggers flash through the air, cleanly cleaving the machine's mechanical arm."
"Nami strikes from the other side, driving her blade into the robot's chassis."
"With considerable effort, she begins to force her blade upward, gradually cleaving it wide open."
"It's like watching someone with an oversized can opener."
"Unable to endure the assault, the machine stumbles and shuts down, its massive, metallic husk collapsing onto the floor."
"The rest of the robots are easily cleaned up."
stop music fadeout 2.0
"We take a moment to survey the aftermath of our battle."
$ kface='shocked'
show kotori at c4
k "How did Akane get this many robots?!"

k "There must be hundreds here, if not more!"
$ sface='neutral'
show shika at c3
s "And a siege bot..."
"Siege bots are typically used as enforcers or deployed during riots."
"They're expensive to produce, and I didn't even know that there were any on this ship..."
$ spose='1'
show shika at c2
play music serious fadein 2.0
s "Listen, you two..."
s "Since the name Akane is an alias..."
s "Who do you think she really is?"
$ nbody='sa'
show nami at c3
n "She has to have some sort of privileged background."
n "Even with our funds, we couldn't field a robot army like this..."
$ kface='neutral'
show kotori at c3
k "Especially not on such short notice!"
k "Not to mention her training... You do not see moves like that often in our line of work!"
k "Even the top mercenaries around here would have trouble facing off against her..."
$ kpose='1'
show kotori at c2
s "So, a privileged background, well trained, and exceptionally intelligent..."
s "Combined with a narcissistic personality and child-like way of mocking people..."

ai "Alert: There is another heat signature inside our quarters."
ai "Due to my updated search algorithms, I have ruled out the possibility of it being another distraction."
"All of us look at each other."
$ kface='angry'
show kotori at c3
k "She used the chaos the robots made just to get in here!"
ai "Signature lost."
"It's then that Kotori's digital pad lights up."
k "Another message..."
stop music fadeout 2.0
s "Open it up."
call h_crew from _call_h_crew_5
scene cg15
with dissolve
pause
play music funny fadein 2.0
a "Hey, just thought I would send you another message..."
"Kotori's eyes go wide with shock."
k "W-What on earth is she wearing?"
"A pair of mock cat ears rest on her head."
"And a metallic tail waves through the air as she lies there."
a "Well then..."
a "If you see this, then I've managed to get inside your quarters."

a "But congratulations on holding back the robotic attack!"
a "As a reward, I thought I would dress up for you all a little bit..."
"Her tail swishes from side to side."
a "Don't you love this cyber cat outfit?"
a "I most certainly do!"
a "Don't I look cute?"
"I swear that I can hear steam erupting from Kotori's ears."
k "She's mocking us! Again!"
k "Even after we managed to fool her like we did before!"
a "Now, I'm certain that Kotori is blowing her top off again..."
a "She needs to get a better grip on herself!"

a "Don't you think, Captain?"
"She wiggles her behind a little bit in front of the camera."
"I cannot help but notice how the camera zooms in slightly on that... part of her."
a "Now, now... Don't let yourself get too distracted."
"The camera zooms back to where it was."
a "Letting your eyes wander too much can't be too good for you!"
a "But that's besides the point, isn't it?"
a "I could be anywhere in here right now..."
a "Maybe even in the vents above you!"
"All of us look up for a moment, expecting to hear something."
a "Please tell me that you didn't fall for that!"
"Her mocking laughter echoes through the digital pad."
k "So annoying..."
a "Just remember that I merely need to find out where you're keeping that footage of me..."
a "Once I have that, then you have nothing."
"... Of course, this was her plan."

a "Remember, in the time you spent watching this video..."
a "I could have already found it!"
a "You really are giving me plenty of time to search every nook and cranny..."
"She laughs again."
a "Anyway, I don't want to take up too much of your time..."
a "Our little game has to go on, after all!"
a "I hope all of you are good at playing hide and seek..."
stop music fadeout 2.0
"The video slowly fades out then, going completely silent."

scene hallway with dissolve
call s_crew from _call_s_crew_14
$ spose='1'
show shika at c2
play music space fadein 2.0
s "Of course..."
s "Don't worry about the footage, anyone."
s "I have it on me right now."
n "Good."
k "Glad to hear that, Captain..."
"She's playing games with us."
"Now that we all know that she's somewhere in our quarters and about to strike..."
"None of us will be able to rest easy."
$ sbody='sa'
show shika at c3
s "Stay on alert, you two."
n "Understood."
$ kface='neutral'
show kotori at c4
k "Got it!"
call h_crew from _call_h_crew_6
stop music fadeout 2.0
scene meetingroom with fade

call s_shika from _call_s_shika_29
"Well..."
"She's here somewhere."
"But where?"
"Where could she be hiding in our home?"
"Maybe scurrying around the vents..."
"Or maybe hiding in plain sight..."
$ spose='1'
show shika at c2
"All of us have been patrolling the halls, keeping an eye out for her."
"I've had to take a short break."
"I cannot believe that she's been able to keep this up for so long..."
$ sface='angry'
show shika at c3
"Who is she? Who is Akane supposed to be?"
"I just can't piece it together."
$ sface='scared'
show shika at c4
"Wait..."
"Is that something moving in the vents?"
"I immediately pull out my pistol."
$ sface='angry'
show shika at c3
play music battle fadein 2.0
s "Show yourself, Akane!"
s "Where are you?!"
a "I'm here somewhere..."
a "Why don't you try and find me?"
"The voice is coming from somewhere else now..."
"She must have a speaker or something scattered in this room."

"I can't tell where she's coming from."
a "Now that you're isolated from those other two, you're going to be easy to pick out."
$ spose='1'
show shika at c2
s "But don't you want to triumph over all of us?"
s "Why not wait for a moment where you can defeat all of us at once?"
a "Honestly, I think I'll just defeat you, Captain."
a "Those other two were far too easy to beat."
a "All it took to take down Nami was a canister of massage gel..."
a "And Kotori is far too easy to read."
a "So, the only one I haven't beaten yet is you..."
a "I think I'll indulge myself a little bit."
$ sface='neutral'
show shika at c3
s "Who are you really, Akane?"
s "You aren't just some petty criminal, I'm certain of that..."
s "What would warrant having such a high bounty on your head?"
a "That's just Mother trying to bring me home."
$ sface='shocked'
show shika at c4
s "Mother...?"
"Wait..."
"This confirms our previous theory."
"Akane comes from a privileged background..."
"An extremely privileged one at that."
"Her mother has to be in charge of an intergalactic corporation..."
"Or perhaps she is royalty on an obscure planet or a major empire..."
"All this has done is make me even more confused about who she really is."
a "I knew that you were going to start overthinking it!"
a "It's so cute when you scrunch up your face like that, Captain!"
$ sface='neutral'
show shika at c3
"Damn it..."
"She just told me that to throw me off guard."
a "Anyway..."
a "Time for this to end!"
a "Oh, and don't think about calling for help."
a "No one can hear you right now."
a "Especially not with all of the doors locked."
"Well..."
"She's going to hit me from somewhere unknown..."
"I whisper into my pistol."
$ spose='1'
show shika at c2
s "Configuration: Railgun."
a "Where do you think you're going, Captain?"
"Her whip appears out of the darkness."
"I barely manage to evade it in time."
"If this is anything like the simulation..."
"Then I need to get out of this room immediately."
if persistent.adult==True:
    $ abody='aa'
else:
    $ abody='ba'
call s_akane from _call_s_akane_3
"She appears, striking at me with incredible ferocity."
a "Had to discard my battlesuit, which is a shame..."
a "Don't want your AI picking up any unusual readings, do we?"
"I can't hit her back right now, so all I can do is dodge!"
$ aface='laughing'
show akane at c3
a "Come on, hold still..."
a "It will be over in just a minute!"
"Like hell I'm going to stand still!"
"Her whip snags me on the arm."
"I immediately feel it going numb."
$ sface='shocked'
show shika flip at c2
s "Damn it..."
$ aface='happy'
show akane at c4
a "I've got you, Captain!"
"It's then that I see she has a camera mounted on her shoulder."
$ aface='smiling'
show akane at c3
a "I'm recording this too!"
a "Hundreds of thousands of potential employers are going to see just how incompetent you're going to look!"
$ sface='angry'
show shika at c2
"I pull a hidden knife from my boot, slicing her whip."
"The numb feeling persists in my arm."
"It's then that I notice the cut off tip of her whip snaking its way back to her."
"It attaches itself to the whip perfectly."

$ aface='laughing'
show akane at c4
a "Nanotechnology is great!"
a "Now that I've stunned you a little bit..."
$ aface='smiling'
a "This is going to be easy!"
"The lights on my pistol turn green..."
$ sface='smiling'
show shika at c3
s "Don't count on it."

scene hallway with dissolve

$ sface='neutral'
call s_shika from _call_s_shika_30
"I blast my way through the door's locks."
"Without any hesitation, I begin sprinting down the hall."
call s_akane from _call_s_akane_4
"Akane follows me, her whip snapping at my heels."
"If I turn around at this point, she will be right on top of me."
"I won't have enough time to aim a decent shot."
$ aface='laughing'
show akane at c2
a "It's over now, Captain!"
"No... Not yet..."
"I begin to aim my shots ahead of me."
$ sface='angry'
show shika at c3
s "Configuration: Stun!"
"I fire a couple of rounds off the walls, making them ricochet."
"Maybe one of them will hit Akane."
$ apose='1'
if persistent.adult==True:
    $ abody='ab'
else:
    $ abody='bb'
show akane at c3
a "Oh, Captain! How are you going to hit me when you aren't looking at me?"
a "I thought you were smarter than that!"
"It sounds like they aren't slowing her down at all..."
$ spose='1'
show shika at c4
"I have no choice."
"I have to use the secret configuration that no one knows about."
"It's not voice activated either."
"Fiddling around with my pistol, I enable the setting."
"Let's just hope that this works..."
"I turn around and fire."
"The projectile goes past Akane's head."
$ aface='smiling'
show akane at c3
a "Ha! You were expecting to hit me with that?!"
"It's then that she notices a strand of black material sticking out from the barrel of my pistol."
$ aface='neutral'
if persistent.adult==True:
    $ abody='aa'
else:
    $ abody='ba'
show akane at c2
a "Wait..."
$ sface='smiling'
show shika at c3
s "Recall!"
"The projectile I shot comes back to me."
"On its end is a glob of sticky residue."
"It catches onto Akane's back."
$ aface='shocked'
show akane at c2
a "W-What the-"
"Before she can react, I begin to fire additional strands, creating a long chain of strands."
stop music fadeout 2.0
"Eventually, she trips over on a strand."

scene cg10
if persistent.adult==True:
    scene cg10_A
with dissolve
play music funny fadein 2.0
"Although she's struggling in front of me in her bonds..."
"Akane is smiling the entire time."
a "I've never seen that configuration before!"
a "Did you really use that just for me?!"
a "I am so honoured!"
"I'm a bit surprised by her reaction..."
"I would have thought she would be more disappointed that she got caught..."
a "I knew that you had it in you, Captain!"
s "Well, it seemed like the only way I was going to capture you..."
"She tries to struggle against the bonds, but is unable to free herself from them."
a "Well..."
a "I guess this is over."
a "But it was a fun ride while it lasted!"
s "I'm very curious to know who exactly your mother is..."
s "And why she has gone to such extreme lengths to capture you."
a "She's a pain, you know."
"Well, it's obvious that she's not going to help me determine the identity of her mother."
"Now that I think about it, the person who put up that bounty didn't leave a name either."
"They simply stated the bounty and where to collect the money."
a "If you think about it, this is like bondage!"
a "That makes me really excited!"
a "Imagine how much fun it would be to use that gun like that..."
"I can only shake my head."
s "I get enough of that from Kotori."
s "I don't need you doing it to me as well."
a "Come onnnnn..."
a "We might as well have some fun together..."
s "AI: Please summon Kotori and Nami to my location immediately."
ai "Acknowledged."
ai "Passing the message along."
"I don't want to take anymore risks."
"We have to put Akane somewhere in our quarters where she can't escape."
"But where...?"
s "So..."
s "Did you think about what's going to happen next if you ended up being captured?"
a "I'll..."
"She looks away for a moment."
a "I'll work something out."
a "I always do."
"I realize that I completely forgot about the billion imperial dollars."
"It's actually going to be a reality..."
"We're about to become so incredibly wealthy."
s "Well then, Akane..."
s "You did well, but this game is over."
"I fire off a round and destroy the camera mounted on her shoulder."
stop music fadeout 2.0
s "We don't want anyone to find out about this, do we?"
scene meetingroom with fade
play music day fadein 2.0
"All of us gather for a final meeting regarding Akane."
call s_crew from _call_s_crew_15
k "So you managed to catch her with a configuration that no one here even knew about?"
s "Yes. I wanted it to be a surprise."
s "She knew every possible configuration that I had ever used on my missions."
$ sface='smiling'
show shika at c2
s "It worked fairly effectively, I think."
$ nface='smiling'
show nami at c2
n "It was a good idea, Captain."
$ kpose='1'
show kotori at c2
k "Have we figured out anything more about who she is?"
$ sface='neutral'
show shika at c3
s "She mentioned that her mother wants to bring her back with that bounty..."
s "Now then, how many people in the known galaxy have that kind of money lying around?"
$ kpose='1'
show kotori at c3
k "A high up government official, maybe..."
$ nface='neutral'
show nami at c3
n "Multi-galactic corporations."
k "Royalty from certain empires."
$ spose='1'
show shika at c4
s "There are several empires which have a strong influence in this galaxy."

s "Not to mention corporations which own entire planets..."
s "So it would be difficult to narrow down who it is."
$ sbody='sb'
show shika at c3
s "The only way we could determine who they might be is if Akane herself tells us."
k "While I would just say we should turn her in and be done with it..."
$ kface='smiling'
show kotori at c4
k "This is quite an exciting mystery!"
$ nface='smiling'
show nami at c4
n "Yes..."
n "Akane is an enigma."
n "At the very least, we should investigate her origins a bit further."
$ npose='1'
show nami at c2
n "We can turn her in at our own leisure, given the security measures we have taken."
n "So, even if it does not yield anything, it would not hurt to see what we can find."
k "Now then, we have missed the most important detail..."
$ sface='neutral'
show shika at c4
s "Yes?"
$ kface='happy'
show kotori at c3
k "We need to discuss is what we're going to spend the billion on now!"
k "We didn't get a chance to earlier!"
k "I suggest we buy our own capital ship!"
$ kbody='sb'
show kotori at c2
k "Or, maybe we could buy an entire island!"
k "Or start our own corporation!"
$ nface='neutral'
show nami at c3
n "I think I would like a bigger room."
n "Mine feels a bit small."
$ kface='angry'
show kotori at c4
k "Come on, Nami! You need to be more ambitious than that!"
$ npose='1'
show nami at c3
n "It's best to be conservative with your money. Small pleasures can be the best ones."
n "Limitations are often what yield the best results."
$ spose='1'
show shika at c3
s "Hold on, let's not get too far ahead of ourselves."
s "She might be able to get away. She's proven to be really resourceful in that regard."
s "Also, we still don't know anything about who she really is."

$ sbody='sa'
show shika at c2
s "We might have gotten ourselves involved with something that is far bigger than us..."
s "For now, we need to further investigate her background before we turn her in."
"I need to confirm my suspicions about her mother first."
ai "Captain, I have... acquired some inside information among the ship's engineers."
ai "There were suspicious reports regarding a 'shadow' seen in a particular section of the ship's engine rooms."
ai "I would suggest that you investigate it."
$ sface='smiling'
show shika at c3
s "Alright."
s "You two stay here and make sure she doesn't escape."
$ nface='smiling'
show nami at c4
n "Acknowledged, Captain."
$ kface='smiling'
show kotori at c3
k "No problem! I'm not letting that one billion slip away that easily!"
stop music fadeout 2.0
s "Good. I have the utmost faith in you both."
call h_crew from _call_h_crew_7

scene backalley with fade

call s_shika from _call_s_shika_31
play music night fadein 2.0
"After paying a few bribes, I've managed to sneak into the restricted areas of the ship."
ai "Captain, there should be a maintenance shaft to your right."
ai "I believe that this is where the 'shadow' was most frequently reported."
s "Well, if that shadow isn't Akane..."
$ spose='1'
show shika at c2
s "I cannot imagine who else it would be."
"It only makes sense."
"This is an out-of-commission shaft overdue for refurbishing."
"Considering the lengths I had to go to to find a password to access it..."

"It's the perfect place for someone to hide out."
s "There, it's open."
$ sface='angry'
show shika at c3
"It's really damn dark down here..."
$ sface='neutral'
show shika at c4
s "Configuration: Torch."
"After scanning the tunnels ahead of me, my torch begins to illuminate something unusual in the darkness."
call h_shika from _call_h_shika_17

scene hideout with dissolve

"Despite obviously being put up in a hurry, this base of operations is actually quite impressive."
"There is plenty of advanced equipment here."
call s_shika from _call_s_shika_32
s "So this is where she's been hiding this whole time..."
s "No one would even think of opening this particular shaft."
s "It's the perfect hideout."
"It's then that I find a digital pad lying on the ground..."
"Picking it up, I flick on its power."
"The words 'Enter password' light up on the screen."
$ sface='angry'
show shika at c2
s "Of course it has a password."
s "Can you brute force this for me, AI?"
ai "Acknowledged."
"After a few minutes, the pad unlocks."
"Scanning through the pad's contents, nothing particularly catches my eye."
"It's mostly videos of us."
$ sface='neutral'
show shika flip at c3
s "... Huh. It turns out that she's been watching us long before that bounty went public."
s "The dates of these go back way further."
s "I think this was around the time where we were doing mercenary work for that one empire..."
ai "Correct."
"Looking more closely, I cannot help but notice that there are a lot of photos of me..."
$ spose='1'
show shika flip at c4
s "More than anyone else in the crew, she seemed to be interested in me."
s "I wonder why that is..."
ai "Let's examine her profile."
ai "She has stated that she is a big fan of yours."
ai "And that all of you have something of a cult following."
ai "The question is when she started following your antics."
ai "If she did it from a young age and comes from a privileged background, perhaps she did not receive much parental affection."
ai "A lot of children who come from dysfunctional households tend to turn to other things for comfort."
$ sbody='sb'
show shika at c3
s "So, she watched our adventures from a young age and saw it as an escape from her life?"
"I really need to find out how our adventures have been broadcast without us being aware."
ai "This is merely conjecture, I may remind you."
ai "We won't know more until we analyse the contents of her digital pad more."
$ spose='1'
show shika at c2
s "Right, right..."
"It's then that I find a simple text file."
$ sbody='sa'
show shika at c3
s "'My dairy'..."
s "No... I don't think I should do this."
ai "Then what will you do, Captain?"
$ spose='1'
show shika at c2
s "I want to talk things out with her."
s "If she's really our fan, then she should be willing."
ai "I would strongly advise against giving her that opportunity, Captain."
s "I will take responsibility for anything that goes wrong."
ai "I will inform the crew of your decision."
stop music fadeout 2.0
s "Please do."
call h_shika from _call_h_shika_18

scene pool with fade

play music space fadein 2.0
"After negotiating with the crew..."
"I've now brought Akane to the pool."
"She seems bemused by me calling her out here."
$ aface='smiling'
call s_akane from _call_s_akane_5
a "So Captain... What is it that you're planning?"
a "After all, you already have me captured."
a "There's numerous points where I could have escaped."
$ sface='smiling'
show shika at c2
s "Then why haven't you?"
a "Because I was just curious..."
a "Why in this room, of all places?"
s "I just wanted you to appreciate the scenery."
"She looks out the windows, the splendour of space plainly visible."
$ aface='laughing'
show akane at c4
a "It is a beautiful room..."
a "Kotori has excellent taste in room design."
$ sface='neutral'
show shika at c3
s "So you know about that too."
$ aface='smiling'
show akane at c3
a "There is very little that I don't know about all of you."
a "I'm your biggest fan, after all."
s "Well... There is something I wanted to ask you."
$ spose='1'
show shika at c4
s "Just who are you, Akane?"
s "You're obviously someone with influence, training, and status..."
s "Why did someone like you choose to involve yourself with a band of mercenaries like us?"
$ aface='laughing'
show akane at c4
a "You brought me here just to ask me that?"
a "That seems a little irrational, Captain."
$ sbody='sb'
show shika at c3
s "Yes, it's irrational..."
"I then pull out her digital pad."
$ sface='smiling'
show shika at c2
s "But somehow... I just wanted to show some respect to our most loyal fan."
"I show her all of the pictures she took of us."
s "Wouldn't it be a treat for a fan to be here in person?"
$ aface='neutral'
show akane at c2
a "Yes... It would..."
"She grows quiet."
a "I..."
a "I suppose..."
$ apose='1'
show akane at c3
a "I became involved with you all because I admired all of you."
a "You were everything I had wanted to be."
$ abody='sb'
show akane at c4
a "Heroines who played by their own rules, dived into danger and came out on top..."
"She grows quiet and looks out the window."
a "I looked up at the stars from a window just like this one..."
a "It was my dream to explore them, just like you all did."
$ abody='sa'
show akane at c3
a "Watching all of you on my digital pad when I was in my cold, large room..."
a "It was almost like a dream was playing out before me."
"It's then that I notice how old the digital pad I'm holding is."
"The puzzle pieces begin to fit into place."
$ sface='neutral'
show shika at c3
s "So you're a run away then."
s "And you chose the same line of work as us."
s "That's why you're so interested in us."
$ spose='1'
show shika at c2
s "You want to be just like us, don't you?"
a "Yes..."
a "I want to be like all of you..."
$ apose='1'
show akane at c4
a "An adventurer, free to go wherever I please."
"She gazes longingly at the stars, watching the purple glow of the planet we're orbiting."
"Slowly, she reaches out to it."
$ sbody='sa'
show shika at c3
s "Well, you're obviously a sheltered child, someone who wanted to be free and choose their own path."
s "With a rich, powerful mother..."
s "But there's one last piece of the puzzle that I have not worked out."
$ spose='1'
show shika at c2
s "Why me?"
"I show her all of the pictures she has of me on her digital pad."
s "More than anyone else, it's me."
"It's a possibility that she's just fixated on me because I'm the captain of this company."
"Yes, that's the most likely reason."
"Wait..."
"What's with that look on her face?"
$ aface='shy'
show akane at c3
a "I..."
"It's then that I see a cylinder in her hands."
a "It's because..."
"She awkwardly fumbles around with the cylinder, unable to keep a firm grip on it."
$ apose='1'
show akane at c2
a "It's because I..."
"She doesn't finish her sentence, still fumbling around with the cylinder."
"The look on her face is akin to an awkward teenager."
$ sbody='sb'
show shika at c1
s "I what?"
s "Please just tell me what you're trying to say."
$ aface='embarrassed'
show akane at c3
a "I..."
a "What I am trying to say is..."
"The cylinder drops out of her hand."
"It clangs loudly as it hits the ground, its top flying off."
"I cannot help but look deeper into its depths, unsure of what its contents-"
$ sface='shocked'
show shika at c2
"Oh. That's what its contents are."
"I should have known."
"A torrent of massage gel erupts from within its depths, spreading along the ground where the cylinder landed."
"That must have been her escape plan..."
"She drops this canister of massage gel and it ensnares her opponents while she runs away..."
"In that moment, Akane rushes towards me with reckless abandon."
"I reach for my pistol, but then I see that she has her arms wide open..."
"My hand slowly leaves my pistol."
stop music fadeout 2.0
"It's then that the massage gel begins to take on a life of its own."

scene cg13
if persistent.adult==True:
    scene cg13_A
with dissolve
play music ecchi fadein 2.0
"The gel encases both of us, creating a translucent wall between her and me."

"In that moment, however, she manages to push through it..."
"And wraps her arms around me."
"Her body presses against mine, her warmth contrasting with the cool massage gel enveloping us."
"She looks me in the eyes."
"I swear I can see a small tear drop in the corners of hers."
a "Ever since I saw you on that digital pad..."
a "All of those long years ago..."
a "My heart couldn't stop beating so fast."
a "Just looking at you, so strong, so brave..."
"Even as the gel quivers and vibrates around us, she does not let go of me."
a "You're my idol..."
a "The one who I loved most."
a "So strong, so brave, everything that I wasn't..."
a "An inspirational leader..."
a "Everything I wanted to be."
"Her voice wavers as she tries to keep control."
"Yet her emotions are plainly visible to see."
"In this moment, her persona has completely broken."
"I'm seeing the real Akane now."
"There is no ego, no hubris..."
"Merely a vulnerable, fragile woman."
a "I know this sound ridiculous coming from someone who you don't know at all..."
a "I love you, Captain."
a "That is why it's you."
a "If I proved myself through this game, then maybe you would respect me like you do Nami and Kotori..."
a "Then maybe you would respect me too..."
"So that is the final piece of the puzzle..."
"And the reason why she came all of this way."
"It was obsession."
"It's me... It's me that she wanted to come see."
"More than anyone else, it was me."
"I stand there, stunned, as she continues to cling to me."
"Despite everything..."
"I did not really take the time to see how beautiful she is."
"Seeing her like this, so vulnerable..."
"There is something very alluring about it."
"The gel around us continues to vibrate and massage my bare skin."
"Slowly, my arms slip through the gel..."
"And softly wrap themselves around her waist."
"Pulling her towards me, she quivers anxiously."
s "Is that really how you feel, Akane?"
s "Is that really why you came all of this way?"
s "To see me?"
a "Yes..."
a "That is how I feel..."
a "You are everything I want to be, Captain..."
"Despite her being such a difficult opponent..."
"I cannot help but comfort her."

s "It's okay now, Akane..."
"I gently whisper in her ear."
stop music fadeout 2.0
s "It's okay..."
scene pool with fade
play music sad fadein 2.0
"After dealing with the massage gel, Akane quietly sits next to the pool."
"She hasn't said anything more."
$ aface='neutral'
$ apose='1'
$ abody='sa'
$ sface='neutral'
$ spose='1'
$ sbody='sa'
call s_akane from _call_s_akane_6
"Quietly, she drags her finger along the water's surface, watching the ripples slowly dissipate into the pool."
"There is something very melancholy about her."

$ aface='smiling'
show akane at c2
a "I didn't want this to end so soon..."
a "But it had to eventually."
a "What are you going to do now, Captain?"
$ spose='1'
show shika at c2
s "I do not know yet."
s "I want to understand why you're here."
s "Please, could you tell me who you really are, Akane?"
"I cannot be the only reason."
"There has to be something else driving her."
"Circumstances of some sort pushed her away from her home..."

"Before I make the choice to send her back, I want to know exactly where I'm going to send her back to."
$ aface='neutral'
show akane at c3
a "I see no point in avoiding it anymore..."
"She lets out a deep sigh."
a "Mother is an empress."
a "There is an entire empire at her beck and call..."
a "And I am the only heir to her cold throne."
$ sface='shocked'
show shika flip at c3
s "... You're the heir to an empire?!"
a "Yes. I am."
$ sface='neutral'
show shika at c4
"Now it begins to make sense."
"The bounty was placed to ensure that she would not escape..."
"At the same time, however, Akane has been going under an alias to ensure she would evade capture."
"You couldn't exactly go around spouting your imperial title if you wanted to be discreet."
"And surely, it would be an incident that would shake an empire to its very foundations..."

"The heir to the imperial throne simply slipped away into the night and there is no replacement."
"Such politics are not uncommon."
$ spose='1'
show shika at c3
"They would have had to be extremely discreet with this, ensuring that no one found out the truth about Akane."
"So, they did everything in the shadows."
"They placed a bounty on her alias, which people would hunt down..."
"And she would be returned home with no one the wiser."
$ apose='1'
show akane at c2
a "Does that change your opinion of me?"
$ spose='1'
show shika at c3
s "Well, I've never really been fond of imperialism..."
s "And I'm sure that you don't want to be treated that way."

$ aface='smiling'
show akane at c4
a "Not at all."
"She continues to run her finger quietly along the water's surface."

$ aface='neutral'
$ apose='1'
show akane at c3
a "I know that I'm being selfish."
a "There is no one else with the legitimacy to claim the throne."
a "My mother... I am her only child."
a "So, the burden falls to me."
$ apose='1'
show akane at c2
a "And I have run away to chase an idle dream..."
"She suddenly slams her hand in the water, making a small splash."
a "That isn't the life I want to lead..."
a "All of the politics, all of the lies..."
$ abody='sb'
show akane flip at c3
a "And the complete absence of any kind of motherly love."
a "Mother carries the burden of an empire, so she couldn't be the one to raise me."
a "Not enough time and not enough energy."
$ aface='smiling'
show akane at c3
a "One night, however..."
a "One of my maids gave me a digital pad."
a "And for me, who had been sheltered my entire life..."
a "It was as though I had been given a window into the world outside."
a "I had to hide it, but it was worth it."
"She begins to smile as she reminisces."
$ apose='1'
show akane at c2
a "One day, I stumbled upon this video of these mercenaries..."
a "They were popular in our empire. There was even a television series based off them..."
a "Those mercenaries were all of you."
$ abody='sa'
show akane at c3
a "On that cold night, hiding underneath the bedsheets of my all-too-massive bed..."
a "I felt a flame in my heart."
a "Lessons on combat, training to increase my stamina, reading to sharpen my mind..."
$ aface='laughing'
show akane at c4
a "All of these things became my life."
a "Because I wanted to be like my idols."
$ aface='smiling'
show akane at c3
a "I wanted to chase that distant dream."
a "With my own strength, I wanted to reach out to you..."
a "And seize you."
a "I wanted to prove to myself that I could be just like you."
$ apose='1'
show akane at c2
a "So, I chased this adventure."
$ aface='neutral'
show akane at c3
a "The crimes I committed along the way..."
a "I suppose it was to spite my own mother."
a "If the word ever got out that her illustrious daughter was a petty criminal..."
"She shakes her head."
$ apose='1'
show akane at c2
a "I suppose that does not matter now."
a "Every adventure has to end eventually..."
$ aface='smiling'
show akane at c1
a "I don't know how I thought I could best my idols."
"She lets out a small laugh."
$ aface='neutral'
show akane at c2
a "I know that I cannot stay here."
a "Everyone has heard about the bounty by now."
$ apose='1'
show akane flip at c3
a "The entire galaxy is probably looking for me."
"Sadly, she slides her hand down the window."
$ abody='sb'
show akane flip at c2
a "The only way this ends is with you sending me back to Mother."
a "You collect your bounty and you spend that one billion imperial dollars however you please..."

a "You have your entire future now, Captain."
$ apose='1'
show akane at c3
a "So of course that will be what you choose."

$ sface='smiling'
show shika at c2
s "Call me Shika, Akane."
$ aface='shocked'
show akane at c4
a "Is... Is that really okay?"
s "Of course it is."
$ aface='laughing'
show akane at c3
a "Okay then, Shika..."
a "I think we already know the outcome here."
$ aface='smiling'
show akane at c2
a "So, I am willing to go along with whatever you decide to do."
a "Please let me know when you're going to take me home."
a "I will go back with you to that room."
"She does think I'm going to do that."

"However, the truth is that I am not sure what I'm going to do next."
"I put my hand on her shoulder."
$ sface='neutral'
show shika at c3
s "I need to talk to my crew about something."
$ aface='smiling'
show akane at c3
a "Okay..."
a "I won't try to escape again. I promise."
a "I know that I cannot beat you."
"Now that we've broken down the shell of her ego..."
"It's so interesting to see who she is."

"To her, we are the ideal that she can never chase."
if persistent.adult==True:
    call scene20_A from _call_scene20_A
scene hallway
if persistent.adult==True:
    with fade
else:
    with dissolve

"Slowly, I guide her back to her room."
ai "Interesting conversation you had, Captain."
call s_shika from _call_s_shika_33
s "It was a private conversation."
s "You need to stop eavesdropping."

ai "Acknowledged."
s "Please inform Kotori and Nami that I am going to hold a meeting in one hour's time."
stop music fadeout 2.0
s "There is something urgent that we need to discuss."
call h_shika from _call_h_shika_19

scene meetingroom with fade
play music serious fadein 2.0
"After everyone has been caught up, we seem to be uncertain of what decision we should come to."
"This is probably going to be the most difficult decision of our careers."
call s_crew from _call_s_crew_16
s "Considering her circumstances..."
s "Do you want to send her back?"
$ spose='1'
show shika at c2
s "I will not judge either of you on your decision."
$ kface='angry'
show kotori at c2
k "I'm still mad at her..."
"Kotori pouts."
$ kface='neutral'
show kotori at c3
k "It's one billion imperial dollars..."
k "If we hand her in, there are infinite possibilities."
$ kpose='1'
show kotori at c4
k "If we don't, then we're letting a once in a lifetime opportunity slip through our fingers..."
$ kface='angry'
show kotori at c3
k "I wish this bounty was straightforward..."
k "Grab person. Dump person at pick up zone. Get money."
k "But this just turned out to be one of the most difficult bounties ever."
$ kface='neutral'
show kotori flip at c3
k "On the other hand, I've already told you that I wouldn't want to give up this life even if we had all of that money..."
k "Maybe it would be better to let this one go."
"Nami has not voiced her opinion yet."
s "What do you think, Nami?"
"She always makes reasonable judgments, regardless of the situation."
"Her opinion will carry a lot of weight for me."
$ npose='1'
show nami at c2
n "While she has caused a lot of trouble for us..."
n "We have to be fair."
n "Not once did she actually try to harm us."
$ nbody='sb'
show nami at c3
n "It really was just a game to her."
$ npose='1'
show nami flip at c3
n "Our reputations were on the line..."
n "But compared to losing our lives, that isn't the worst thing that could happen."
n "I think, even though this has been a long-winded and ultimately frustrating bounty..."

$ nbody='sa'
show nami flip at c4
n "The experience itself was more than enough payment for the trouble."
n "However, a billion imperial dollars..."
n "Even I can't ignore that much money."
$ nbody='sb'
show nami flip at c3
n "We're currently stuck on this company ship for our living quarters."
n "Being able to buy a ship that rivals this one in size..."
n "That could change our future entirely."
$ npose='1'
show nami at c3
n "So, this is not a decision that we can rush, in any regard."
$ kface='smiling'
show kotori at c3
k "I have to admit that it was kind of fun..."
k "It also put things into perspective."
k "I am too rash. I'm also far too easy to taunt..."
k "If our opponent had been someone out to hurt us..."
$ kface='neutral'
show kotori at c4
k "It could have ended a lot worse than it did."
"It's a fair observation."
"Akane has been the most challenging opponent we have had in a very long time."
"She's intelligent, she's well trained, and she has the resources to do a lot of damage..."

"Despite how elusive she proved, it was thrilling to play this game of cat and mouse with her."
"I just don't know..."
"We're holding not only our future in our hands..."
"But we're holding hers as well."
stop music fadeout 2.0
"Could we live with the fact that we sent that girl back to the cage she tried so desperately to escape from?"
call h_crew from _call_h_crew_8

scene bedroom with fade
play music night fadein 2.0
"As I walk into the room, Akane looks up at me."
$ aface='neutral'
$ apose='1'
$ abody='sa'
call s_akane from _call_s_akane_7
a "Captain..."
a "Is it time for me to go back?"
"I just quietly sit down next to her."
$ spose='1'
show shika at c2
s "What do you think is going to happen next?"
a "Well, of course, you're going to turn me in..."

a "What other choice is there to make?"
$ apose='1'
show akane at c3
a "It's the choice I would make in your position because I know how much freedom it would grant you."

$ aface='smiling'
show akane at c4
a "Please, don't feel guilty."
a "I've had my adventure, and I am content with that."

$ abody='sb'
show akane flip at c3
a "Even if I have to sit upon that cold throne for another fifty years..."
a "At least I will have this small moment of freedom to reflect back on."
$ sface='smiling'
show shika at c3
s "We aren't sending you back, Akane."
$ aface='shocked'
show akane at c3
"She just looks at me with shock."
a "B-But..."
a "You... You have to send me back!"
$ apose='1'
show shika at c3
a "People are looking for me everywhere in this galaxy!"

a "Probably beyond it too!"
a "If people found out that you were holding a fugitive with you, especially me..."
$ abody='sa'
show akane at c4
a "Do you know how much of a disaster that would be for all of you?!"
a "My mother would send an entire legion of imperial assassins to hunt you down!"
$ spose='1'
show shika at c3
s "Do you know this ship's next destination?"
s "We are going to be traveling to a galaxy far away from here."
s "Even if there are imperial assassins and bounty hunters..."
$ sbody='sb'
show shika at c2
s "It will take them a very long time to find us."
a "But... Why are you doing this for me?"
s "Because all of us here remember being like you."
s "All of us wanted freedom."
s "That's why we chose this career in the first place."
$ spose='1'
show shika at c3
s "Believe it or not, Akane..."
s "You aren't so different from us."
s "And it would be a waste to send such a talented person to rot on top of a throne..."

"I pull out a bundle of forms."

$ sface='neutral'
show shika at c4
s "I am going to leave this application form here."
s "These are papers which I have requested from the company manager on this ship."
s "As an employee, it will be rather easy for you to transfer into our team."
$ sbody='sa'
show shika flip at c3
s "I have spoken to Kotori and Nami about it..."
s "And they have agreed that you won't be sent away."
s "Of course, I do not wish to ignore your own wishes too."
"I stand up, leaving the papers on the bed."
$ spose='1'
show shika flip at c4
s "If you want to stay, simply sign these forms and present them before the ship's manager."
s "If you want to go back, then simply say so the next time I visit you."
s "Obviously, this is going to be a big decision for you..."
s "So, I want to give you time to think about it."
"She simply stares at the papers."
$ aface='neutral'
show akane at c2
a "I..."
a "I do need time to think about it."
"She quietly picks up the pen and twirls it around in her fingers."
$ sface='smiling'
show shika at c3
s "Remember, Akane..."
s "We will agree with whatever choice you make."
s "Your future is now in your hands."
$ aface='shocked'
show akane at c4
a "You would really... let me work with you all?"
a "Come with you on your adventures?"
$ sface='happy'
show shika at c3
s "I don't see why not."
s "With you on our team, I think our future would be brighter than ever."
"For the first time, I see a genuine smile on her face."
$ aface='smiling'
show akane flip at c3
a "Thank you, Captain..."
a "Thank you so much..."
"Having either another crew member or a future empress as our friend..."
"We've managed to ensure that our future is going to hold good things no matter what we do."
"And most importantly, we've allowed Akane to choose her own future."
"I know that it is going to be a difficult decision for her..."
"She either chooses duty or she chooses the freedom she has always craved."
"I cannot help but feel guilty for putting that burden on her..."
"But allowing her to choose for herself is the right thing to do."
$ sface='neutral'
show shika at c2
s "I will come back in a few hours."
s "I hope you will find the answer you want then."
$ aface='neutral'
show akane at c3
a "Yes..."
a "I hope that I will too."
"I slowly step out of the room, giving Akane time to think."

scene hallway with dissolve
call s_shika from _call_s_shika_34
"Well then..."
"I wonder what choice she will make?"
menu:
    "She will choose freedom.":
        $ investigate += 1
        "Well, I think that she will choose her own freedom."
        "If she has come all of this away from a palace, of all places..."
        "Then there is no way that she would be willing to give up her dream now."
        $ spose='1'
        $ sbody='sa'
        show shika at c2
        "It also fits her profile."
        "She does not want to be caged. She doesn't want that throne."
        "She will only go back there if she feels that she has to."

        "Given the circumstances and the fact that we're leaving this galaxy soon..."
        "I think she is going to stay with us."
    "She will choose duty.":
        "No one understands the reasons for going back better than her."
        "Even if someone doesn't want to accept that burden, she carries the weight of an entire empire on her back."
        "If she simply abandoned it, then there's no telling what kind of chaos would ensue."
        "She has not told me what empire it is, but all of the empires I know of in this galaxy..."

        "Well, let's just say that there is always internal strife within them."
        "Now, an empire with only a single heir to its throne..."
        $ spose='1'
        $ sbody='sa'
        show shika at c2
        "Unless she did go back, I can only imagine how much trouble it would cause."
        "The fact that she would always be chased wouldn't be comforting either..."
        "So, perhaps she really will choose to go back after all."
        "If she truly is content with just this one adventure."
$ spose='1'
show shika at c3
"Well, I suppose the only way I will know for sure is when the time comes."
"I just hope that she will be able to find happiness, no matter what she chooses."
ai "Now that went well, didn't it, Captain?"
$ sface='angry'
show shika at c4
s "Didn't I tell you to stop eavesdropping?"
ai "Acknowledged."
"Nami and Kotori come walking up the hall."
call s_crew from _call_s_crew_17
n "How did it go?"
k "Did you let her choose herself?"
$ sface='smiling'
show shika at c3
s "I've given her the papers."
s "What happens next is up to her."
n "This is going to be a long wait then..."
$ kpose='1'
show kotori at c2
k "To say the least..."
k "I need to go for a swim! The anticipation is killing me!"
"Despite all of the conflict we've had with her, everyone seems to hold her in high regard."
s "We can't do anything else for her."
stop music fadeout 2.0
s "So, all we can do is wait."
call h_crew from _call_h_crew_9
scene bedroom with fade
play music space fadein 2.0
"I enter the room slowly."
"Akane is exactly where I left her, still sitting there with those papers in her hands."
"The pen rests by her side."
$ aface='neutral'
$ apose='1'
$ abody='sa'
call s_akane from _call_s_akane_8
s "Akane?"
a "Captain."
s "Have you made a decision yet?"
"This is probably going to be the defining moment of her entire lifetime."
"What she picks now is going to change our lives, and hers, forever."
"With that in mind, I cannot help but wait with bated breath."
"Slowly, she stands up."
"She walks to me bit by bit..."
"And puts the papers in my hands."
$ apose='1'
show akane at c2
a "If it would not bother everyone onboard..."
a "I would like to stay."
a "I know that my responsibilities back home are going to be crushing..."

a "But I want to chase my dream, even if it's just for a little bit longer."
$ abody='sb'
show akane at c3
stop music fadeout 2.0
a "Is that fine with you, Captain?"
"I smile and put my hand on her shoulder."
$ sface='smiling'
s "That's fine by me, Akane."
$ aface='shy'
show akane at c4
"I cannot help but notice her blush when I touch her."
play music day fadein 2.0
a "It's... It's odd..."
a "Why am I feeling like this, just after being touched by you..."
"She puts her hands on her face, trying to hide her blushing cheeks."

a "Oh... I should be more composed than this..."
a "I..."
$ spose='1'
show shika at c2
s "It's fine."
s "You really do worry too much, Akane."
a "Maybe... Maybe I do."
$ sbody='sb'
show shika at c3
s "Nami is not so different from you in that regard."
$ aface='neutral'
show akane at c3
a "Really?"
s "Yep. There are some things about us which even our cult following can't work out."

$ sface='smiling'
show shika at c4
s "Anyway, since you have accepted our offer..."
s "There are some people I would like you to meet."
"I gesture towards the door as it slides open."

scene hallway with dissolve

"As we walk through the hall, Akane looks around curiously at her surroundings."
$ aface='laughing'
call s_akane from _call_s_akane_9
a "I once dreamed of being able to walk these halls freely."
a "Sometimes, dreams can come true."
"She smiles to herself."
$ aface='smiling'
show akane at c3
a "I cannot believe it..."
a "Is this really happening?"
a "Someone pinch me and make sure that I'm not asleep."
"I pinch her."
$ aface='shocked'
show akane at c4
a "Eeep! You actually did it!"
$ sface='laughing'
show shika at c3
s "Of course I did."
s "I cannot ignore the request of my newest crew member now, can I?"
$ aface='neutral'
show akane at c3
a "Crew member..."
a "This is really happening, isn't it?"
$ sface='smiling'
show shika at c2
s "Well, I just pinched you."
s "If this was a dream, you would have woken up by now."
s "Or am I wrong?"
$ aface='smiling'
show akane at c4
a "Well..."
a "I would like to give it a day or two before I conclude that it's the truth."
a "I can have really deep dreams sometimes."
s "That is fair enough."
"Another eccentric crew member to manage."
"But that's just part of the job, I suppose."

scene meetingroom with dissolve

"Eventually, we arrive at our destination."
"Kotori and Nami are waiting in the meeting room."
call s_all from _call_s_all_1
s "Say hello to our newest member, Akane!"
$ nface='smiling'
show nami at c2
n "Greetings, Akane."
n "I look forward to working with you."
n "I am sure that with your skills, we will be more successful than ever with our endeavors."
"Nami offers her hand to Akane."
"With a bit of awkwardness, Akane firmly clasps it."
$ aface='smiling'
$ apose='1'
show akane at c4
a "I'm going to be very pleased to work with you, Nami."
a "I always did think that you were brilliant."
$ nface='laughing'
show nami at c2
n "Why, thank you."
n "You have proven to be very resourceful too."
$ aface='laughing'
show akane at c3
a "I have had some training from the galaxy's finest."
"Kotori pouts a little bit, but she reluctantly offers her hand to Akane."
$ kface='angry'
show kotori at c2
k "I'm still mad at you..."
k "But it's nice that you're part of the team now."
k "I hate to admit it, but you're pretty skilled with that whip."
$ aface='smiling'
show akane flip at c4
a "I do not think I could have beaten you if I had not used organic materials in my whip, Kotori."
a "You are incredible."
$ kface='embarrassed'
show kotori at c3
k "Spare me the flattery!"
"Although Kotori is actually a bit bratty, I think that she's accepted that Akane is going to become a permanent part of our lives."
"Akane bows before me respectfully."
$ aface='laughing'
show akane at c3
a "I am in your hands, Captain."
a "Please show me the way to become a great mercenary, just like you."
$ sface='laughing'
show shika at c3
s "I think you will be able to figure it out yourself."
call h_all from _call_h_all
"Somehow, it just feels right having her here."
"Although there are going to be potential threats in the future..."
"Assassins, bounty hunters, and whatever else that Empress can throw at us..."

"I think that we have a bright future with Akane in our ranks."
"There are an infinite number of stars out there in the universe."
"Who knows where we will be drifting to next?"
"We may not have acquired one billion imperial dollars..."
"But we have gained a comrade who will be our side to the very end."
"With her in our team, the entire universe had better watch out."
"We're going to carve our legacy into the stars themselves."
"I do not know what the future holds..."
stop music fadeout 2.0
"But with all of these wonderful people by my side, I am sure that it will hold great things."

scene black with fade
"Your overall investigation score was [investigate] out of 21."
if investigate <= 5:
    "You only made a few correct guesses in unraveling the mystery."
    "Challenge yourself to do better next time."
elif investigate <= 10:
    "Some of your guesses were correct."

    "There's definitely room for improvement."
elif investigate <= 15:
    "You sit somewhere in the middle."
    "With a little practice, you could do great."
elif investigate <= 20:
    "You were right a lot more often than you were wrong."
    "You could make a good detective one day."
elif investigate == 21:
    "Perfect score!"
    "You're either a brilliant detective or you were cheating."
    "Let's hope that it's the former."

call credits from _call_credits



return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
