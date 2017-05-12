# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character('Koji', color="096c74")
define h = Character('Hanako', color="ffc0cb")
define n = Character('Nanami', color="fa8072")
define b = Character('Hiro', color="daa520")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "Music is an interesting thing."
    "It's an art that works in many different ways, giving life to ideas that may never have existed before."
    "In music, feelings can be conveyed that could never be understood through visuals alone."
    "Just like how a picture says a thousand words, a song can say a million."
    "Music is my everything."
    "All day, I want to write music."
    "All I want to do is listen to it."
    "My life is consumed by music to the point that it's probably pretty unhealthy."
    "Well, at least it used to be."
    
    "..."
    
    "???" "Hey, Koji, are you there?"
    "A somewhat irritated voice shakes me from my stupor."
    k "Huh?"
    "I blink, and I suddenly remember where I am."
    "That's right."
    "Tenomori University."
    "One of the largest universities for miles around, and the one I worked my ass off to get into."
    "Even though it's several hours from my hometown, I couldn't pass up the opportunity."
    "???" "Hey, earth to Koji? You alright?"
    "I glance down, and there stands my childhood friend, Hisawa Nanami."
    k "Ah, yeah, sorry, just spaced out for a bit... haha..."
    "She raises an eyebrow quizzically."
    n "Well, if you say so."
    "As she turns back to walking, my other friend, Tsukasa Hiro, catches up to me."
    b "C'mon man, what're you doing? Spacing out on the first day? Not looking good man."
    "I give him a weak elbow."
    k "Yeah, yeah, worry about yourself, bud."
    "He throws his hands up in surrender as he smiles."
    b "If you insist, your Highness."
    "I smirk."
    "Maybe calling them childhood friends is a bit of a stretch, since I've only known them since the start of high school."
    "But they're the closest friends I have. We've been through thick and thin, and know almost everything about each other."
    "For example, I know that Hiro, protest as he might, has a real soft spot for shoujo manga."
    "'It's just too damn cute man!'"
    "That's what he always tells me when I bring it up."
    "Or as another example, I happen to know that if you ever offer Nanami some food she'll always eat it, even if she's on a diet."
    "They're a bit quirky, and they aren't without flaws, but they're my best friends."
    "Not a day goes by where we don't talk, since we see each other practically every day."
    "At least in high school, we would spend every day hanging out and goofing off."
    "And I don't think there's really any reason that would change now."
    "In fact, I'm glad that they were both able to get into Tenomori."
    "I don't know what I'd do without them."
    n "Hey, Koji! Are you spacing out again?"
    b "Man, what's up with you? Stayed up too late playing games again?"
    k "Nah, it's nothing like that."
    "Hiro smirks."
    b "Oh, maybe it was something else?"
    k "What do you mean, something else?"
    b "You know, something else keeping you up late at night?"
    n "You guys are idiots."
    "Her words barely reach my ears before both of us get a quick punch to the shoulder."
    k "Hey, what was that for?"
    b "What, you didn’t get it?"
    n "It’s not like I just punch people for fun, you know. Well, not THAT much."
    "Hiro giggles, and suddenly I feel like I want to punch him too."
    b "You really didn’t get it?"
    k "No, what’s so funny?"
    "Hiro sighs, and then proceeds to shrug."
    b "I guess you just can’t beat an innocent heart."
    k "What?"
    "Nanami sighs behind us and I almost feel like I can hear her mentally facepalm."
    n "You guys are really stupid. Koji, bless your heart, he means adult material. Like you know, that kind."
    "."
    ".."
    "..."
    b "Come on man, it was a funny joke! Dirty humor is the best kind of humor!"
    "I can't help but smirk."
    k "Says the guy who can’t stop reading cutesy shoujo manga."
    "His face turns red and he shushes me loudly."
    b "Shhhh! I told you not to talk about that!"
    "Nanami chuckles, before letting out a long sigh and giving him a comforting pat on the back."
    n "Oh you poor child, you still think it's a secret..."
    b "Wait, wait, what?! Who else knows?!"
    k "Well, new school now, so probably no one but us."
    "He lets out a sigh of relief."
    b "Thank god, it’s too early for my reputation to already be ruined."
    k "Ha, what reputation? As far as I’m concerned, you didn’t much of a reputation to protect in the first place."
    "He slows down and grins."
    k "Oh yeah? How about you put your money where your mouth is and take me head on in some games later?"
    "I step up, squaring myself up against him. He’s a little taller than me, but that doesn’t mean I’ll back down. I grin."
    k "You know I don’t turn down a challenge."
    b "Well, better see you after class."
    "Behind us, a cough draws us back to reality."
    n "Ehem, if you boys don’t mind, we have classes to get to. I’m as much a fan of you two being children as the next girl but I’d rather not be late to my first day of university."
    
    "I check the time."
    k "Yeah, I guess we should get going. Where’s our first class again?"
    n "You sure you’re okay? I can’t imagine what you would do without me. It’s over on the west side of campus."
    b "You really must be out of it man."
    "He laughs, and Hiro and Nanami begin walking off."
    "It was a rhetorical statement, but I wonder the same thing sometimes."
    "Although Hiro is a great friend, Nanami has always been super responsible."
    "She’s always been the one who watches over us, and is the logic behind our actions."
    "I really am grateful to know someone like her, and that someone like her puts up with our stupid antics every day."
    b "Anyways, you guys wanna grab dinner after our first day of classes?"
    k "Yeah, sure."
    n "I’m game. What are we going to eat?"
    k "Hm, I haven’t really studied the area. Do you know any good places, Hiro?"
    k "Preferably somewhere cheap for the sake of my wallet, please."
    n "Ah, mine too. Unless it’s really good. I guess I’d be willing to pay if it was really good…"
    b "Well, if you want cheap, I happen to know a great place around here! Or at least, I’ve heard about it."
    n "Really? Where?"
    "Nanami already has an excited glint in her eye. Her inner foodie is showing already."
    "But Hiro is grinning devilishly. Something is up...."
    b "Yeah, it’s this Chinese place near campus. I hear they have really great roast duck."
    "Suddenly Nanami seems to get it and glances at me, grinning."
    n "Really? Sounds awesome! We should go!"
    "..."
    "Yeah, sometimes I wonder why I’m still friends with them."

    #------------------------------------------------------------------------------------------------------------

    "Professor""-And remember to do your homework. The worksheets are online, refer to your textbooks if you’re confused with the material. Dismissed."
    "I close my laptop with a heavy sigh, and beside me both Nanami and Hiro are doing something similar."
    b "Homework on the first day, huh? C’mon prof, give us a break…"
    "Storing my laptop back in my backpack, I grin."
    k "What, is it too hard for you? It was honestly pretty basic stuff."
    b "Wha-"
    "He raises a fist."
    b "Nah, it wasn’t hard. I can do this easily, hahaha!"
    "From my left, Nanami chuckles."
    n "Oh, it’s that easy? Then I guess you wouldn’t mind doing it for us?"
    b "Ha, fat chance."
    "She shrugs and smiles."
    n "Eh, it was worth a shot."
    "The three of us start leaving the lecture hall and step out into the bright sunlight."
    "All things considered, for a first day the weather is quite nice."
    "Although I’ve never been one for being outside too much, so I squint when the bright lit hits my eyes."
    k "When did it get so sunny? It wasn’t like this in the morning."
    "Despite my complaint, Nanami is basking in it, arms outstretched and a wide grin on her face."
    n "Why are you complaining? The sun feels so nice, and it’s so pretty!"
    b "Besides, my dear friend, you know what it means when it’s nice and sunny!"
    k "I do?"
    "Hiro grins and strokes his chin."
    b "But of course, my good man! The summer clothing comes out!"
    "..."
    b "The short skirts! Short shorts! Summer dresses and midriffs! It’s every man’s dream come true!"
    "I let out a sigh and clasp him on the back."
    k "Normally, I’d have words to say to you, but in this case I must agree. Short skirts and short shorts are a treat for the eyes…"
    n "Glad to know I’ve got such mature friends by my side…"
    "Nanami massages her temples as she continues to step in front of us."
    k "Hey, that’s not fair. You know that you’d do the same if it were you talking about cute guys!"
    "With that line, she turns a little pink and looks me in the eye."
    n "And is that a problem?"
    "I smirk."

    menu:

        "Of course not. Don’t let it get to your head.":
            jump toyourhead

        "Of course. The only guy you should be looking at is me.":
            jump smoothaf

label toyourhead:

    "Nanami lets out a huff."
    n "I could say the same to you, Mr. Afraid of Ducks."
    "She grins and continues walking."
    k "Man, I thought we were over that."
    "Turning back to me, she flashes a mischievous grin."
    n "Oh, I’m never letting that go, so don’t expect to be free from me anytime soon."
    k "Whatever you say, Princess Pink."
    "Instantly, she turns around and walks up to me, a pleading smile on her face."
    n "Hey, best friend, my favorite person who I totally love and hold near and dear to my heart! Anything I can do for you?"
    "That’s right. Nanami, the practical, mischievous, high school friend of mine has a few secrets of her own…"
    "Namely that even to this day, she follows the popular children’s series Prismatic Magic Rangers with a passion. And even when she was a second year in high school, she secretly cosplayed as the character Princess Pink at conventions."
    "I wink."
    k "Don’t worry, Nanami. You’re never getting rid of me either, right?"
    "She smiles a rather artificial smile and walks on, humming as if nothing had happened."
    b "Did… Did I miss something?"
    "I pat him on the back."
    k "Don’t worry about it man. This level of interaction goes beyond your comprehension."
    "He eyes me with a raised eyebrow but shrugs and keeps walking."

    jump continueone

label smoothaf:
    
    "..."
    "For a moment, she seems startled and a little pink, but she recovers and grins almost instantly."
    "It’s so fast that I wonder if maybe I was seeing things."
    n "Don’t be so full of yourself. I’ll check out whatever guys I want, thank you very much."
    k "Mmhm, sure you will."
    "She raises an eyebrow."
    n "What is THAT supposed to mean?"
    k "Oh please, Nanami, we both know the only guy you can look at is me."
    n "Oh really?"
    k "Absolutely. How could anyone resist…"
    "I throw my arms out and bask in the sunlight."
    k "This beautiful bod?"
    "It’s stupid, but it’s enough to elicit a chuckle out of her."
    n "Good to see you haven’t changed, but knowing you I don’t think you ever will."
    n "You’ll always be a big, dumb, lovable idiot…"
    n "MY big, dumb, lovable idiot."
    k "Excuse me, I’m not anyone’s property."
    n "Fair enough, but I still have to check up on you every now and then to make sure you aren’t doing something stupid, don’t I?"
    n "If I’m not there for you, I’m not sure anyone else will be."
    b "Hey, what about-"
    k "Of course, of course."
    "She might have a point, but before I can think too long about what she said, Nanami grins."
    n "Anyways, ever since when were you a smooth talker?"
    "I tilt my head thoughtfully."
    k "You know, good question. I just sorta do what this voice in my head tells me to do every now and then."
    "There’s a short pause as she takes in what I said, before she laughs."
    n "Yup. Still the same old Koji."
    k "Um, you know, I actually wasn’t joking-"

    jump continueone

label continueone:


    b "So what’s your next class?"

    
 #  "As cliche as it sounds, it all really did start with a message."
  #  "It was my third video, and my crowning achievement at that point." 
   # "I still remember how excited I was when I clicked on the first comment."
   # "How excited I was when I saw what it said."

   # "???" "'Hey, this song is really really good! I love it a lot!'"

    #"???" "'If you don't mind, would it be okay if I could sing with you?'"
    
    #"To any other content creator, especially big ones, this might not seem like much."
    #"But to me, a small name musician with less than a hundred followers, it was the best compliment I'd ever heard."

    # This ends the game.

return
