# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Koji")
define h = Character("Hanako")
define n = Character("Nanami")
define b = Character("Hiro")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

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
    "One of the largest universities for miles around, and the one I worked my ass of to get into."
    "Even though it's several hours from my hometown, I couldn't pass up the opportunity."
    "???" "Hey, earth to Koji? You alright?"
    "I glance down, and there stands my childhood friend, Hisawa Nanami."
    k "Ah, yeah, sorry, just spaced out for a bit... haha..."
    "She raises an eyebrow quizzically."
    n "Well, if you say so."
    
    
    
    
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
