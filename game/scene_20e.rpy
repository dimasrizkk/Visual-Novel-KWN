## ============================================================
##  MIRROR — Scene 20E
##  Judul   : Foreshadow Penggerebekan
##  Karakter: Raka, Nara
##  Latar   : raka_apartement
## ============================================================

label scene_20e:

    scene raka_apartement
    with dissolve

    show raka casual serius at left
    show nara eksplor serius at right

    play sound "distant_siren.ogg"

    "Suara sirene jauh terdengar."
    "Tidak keras."
    "Tapi cukup untuk membuat suasana berubah."

    show nara eksplor terkejut at right

    nara "...Mereka mulai."

    show raka casual terkejut at left

    raka "Secepat ini?"

    show nara eksplor serius at right

    nara "Gue bilang kan."
    nara "Ini cuma soal waktu."

    "Nara berjalan ke pintu."

    hide raka

    show nara eksplor serius at center

    nara "Gue cabut."
    nara "lo sebaiknya tutup mulut."

    "Nara berhenti sebentar."

    nara "Dan Raka.."
    nara "Jangan kira lo bisa netral di cerita ini."

    hide nara

    play sound "door_close.ogg"

    jump scene_20f
