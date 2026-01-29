# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Birdman")
define a = Character("Player")
define o = Character("Tweet")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene empty_school_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show neutral_birdman

    # These display lines of dialogue.

    e "Hello! My name is Dr. Birdman."

    e "I am the headmaster of this school."

    show neutral_grace at left

    a "What am I doing here?"

    e "You are a student, of course!"
    e "Why else would you be here?"

    a "Uh..."
    menu:
        "To investigate you!":
            jump investigation
        "I guess you have a point.":
            jump school

    label investigation:
        show angry_grace at left
        a "I'm here to investigate you!"
        show craw_birdman
        e "To do what?"
        hide craw_birdman
        show neutral_birdman

        a "You heard me!"
        a "I found this dead body outside!"
        hide neutral_birdman
        show neutral_birdman at right
        show bb_dead at truecenter
        a "Explain yourself."
        hide neutral_birdman
        show craw_birdman at right
        e "Darn it."
        return
    label school:
        show sigh_grace at left
        a "I guess I am a student here..."
        hide sigh_grace
        show neutral_grace at left
        a "Say, are there any other students here?"
        a "It looks pretty empty."
        hide neutral_birdman
        show craw_birdman
        e "No, no there are not."
        hide craw_birdman
        show neutral_birdman
        a "Hm..."
        menu:
            "I could've sworn I saw something down that hallway...":
                jump hallway
            "This feels weird...":
                jump weird
        label hallway:
            scene empty_hallway
            show neutral_grace at left
            hide neutral_birdman
            show craw_birdman at right
            show bb at truecenter
            o "What's up guys?!?!?!?!"
            o "My name's Tweet-"
            hide craw_birdman
            show angry_birdman at right
            e "CAWWWWW!!!!!!"
            hide bb
            show bb_dead at truecenter
            hide neutral_grace
            show shocked_grace at left
            a "What the $#$$#$!?!?!?!?!"
            return
        label weird:
            show neutral_grace at left
            a "I think I'm gonna go actually."
            show craw_birdman
            e "Oh, okay."
            return
            

            
    
    # This ends the game.

    return
