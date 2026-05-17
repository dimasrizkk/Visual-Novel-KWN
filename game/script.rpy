# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    call scene_18a
    call scene21a

    if active_path >= 1:
        call scene21b
        call corridor_escape
    elif passive_path >= 1:
        call scene21d
    else:
        call scene_21e_pengkhianatan

    call scene_21f_penutup_babak_2
    call scene_22a_sunyi_yang_tidak_normal
    call scene_22b_raka_sendiri
    call scene22C
    call scene22D
    call scene23A
    call scene23B
    call scene23C
    call scene24
    call scene25
    jump scene29_25

    return
