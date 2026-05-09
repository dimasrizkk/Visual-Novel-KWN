## ============================================================
##  MIRROR — Scene 20B (Updated Format)
##  Judul   : Kunjungan Malam
##  Karakter: Raka, Nara
##  Latar   : APARTEMEN RAKA
## ============================================================

label scene_20b:

    scene APARTEMEN RAKA with dissolve

    # SFX Ketukan pintu yang memecah kesunyian malam
    play sound "door_knock_slow.ogg"

    "Ketukan."

    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka diam."

    play sound "door_knock_slow.ogg"

    show Casual_Netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    "Raka bangkit perlahan."

    hide Casual_Netral with dissolve

    play sound "door_open.ogg"

    show Eksplor_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka membuka pintu."

    nara "Gue masuk."

    # Mengatur posisi keduanya saat Nara sudah berada di dalam ruangan
    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "KOK LO TAU DIMANA GUE TINGGAL? Lo nggak nunggu diundang ya."

    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Lo kelihatan bukan tipe yang bakal undang, ataupun memberi tau lokasi rumah lo."

    "Dia masuk tanpa ragu. Seperti biasa."

    jump scene_20c
