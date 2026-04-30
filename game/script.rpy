# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    #
    # SCENE !
    #
    call scene1


    show eileen happy

    # These display lines of dialogue.

    e "tes tes tis tes"

    e "jakang sf terbagus"

    # This ends the game.

    return
