## ============================================================
##  MIRROR — Scene 20B
##  Judul   : Kunjungan Malam
##  Karakter: Raka, Nara
##  Latar   : raka_apartement
## ============================================================

label scene_20b:

    scene raka_apartement
    with dissolve

    play sound "door_knock_slow.ogg"

    "Ketukan."

    show raka casual sedih at center

    "Raka diam."

    play sound "door_knock_slow.ogg"

    show raka casual netral at center

    "Raka bangkit."

    hide raka

    play sound "door_open.ogg"

    show nara eksplor serius at center

    "Raka membuka pintu."

    nara "Gue masuk."

    show raka casual terkejut at left
    show nara eksplor serius at right

    raka "KOK LO TAU DIMANA GUE TINGGAL? Lo nggak nunggu diundang ya."

    show nara eksplor netral at right

    nara "Lo kelihatan bukan tipe yang bakal undang, ataupun memberi tau lokasi rumah lo."

    "Dia masuk tanpa ragu."
    "Seperti biasa."

    jump scene_20c
