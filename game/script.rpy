# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

from unittest.mock import call

from game import scene1, scene2


define e = Character("Eileen")

# Deklarasi Karakter


# Inisialisasi Variabel Poin (Sangat penting agar tidak error saat ditambah)
default ambition = 0
default ruthless = 0
default loyalty = 0
default trust_nara = 0 #variabel scene 16


# The game starts here.

label start:

    #
    # SCENE !
    #
    call scene1
    call scene2
    call scene3
    call scene4
    call scene5
    call scene6
    call scene7
    call scene8 
    call scene9
    call scene10
    call scene11
    call scene12
    call scene13
    call scene14
    call scene15
    call scene16
    call scene17


    show eileen happy

    # These display lines of dialogue.

    e "tes tes tis tes"

    e "jakang sf terbagus"

    # This ends the game.

    return
