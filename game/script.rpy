# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

from unittest.mock import call

from game import scene1, scene2


define e = Character("Eileen")

# Deklarasi Karakter
define raka = Character("Raka")
define worker = Character("Worker")
define system = Character("System", color="#00ff00")
define adrian = Character("Adrian")
define ayah = Character("Ayah", what_italic=True) #deklarasi utk suara memori scene5
define worker1 = Character("Worker 1") #deklarasi utk scene 8
define worker2 = Character("Worker 2")
define worker3 = Character("Worker 3")
define penjaga = Character("Penjaga") #deklarasi utk scene 9
define old_woman = Character("Nenek Tua")
define pedagang = Character("Suara Pedagang", what_italic=True)
define anak_kecil = Character("Suara Anak Kecil", what_italic=True)
define kerumunan = Character("Kerumunan") #deklarasi utk scene 10
define anak = Character("Anak Kecil")
define ibu = Character("Ibu")
define nara = Character("Nara") #deklarasi utk scene 11
define penyiar = Character("Penyiar Radio", what_italic=True) #deklarasi utk scene 12
define analyst = Character("Senior Analyst") #deklarasi utk scene 17


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
