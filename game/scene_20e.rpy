## ============================================================
##  MIRROR — Scene 20E (Updated Format)
##  Judul   : Foreshadow Penggerebekan
##  Karakter: Raka, Nara
##  Latar   : APARTEMEN RAKA
## ============================================================

label scene_20e:

    scene APARTEMEN RAKA with dissolve

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    # SFX Sirene jauh untuk memberikan tekanan mendadak
    play sound "distant_siren.ogg"

    "Suara sirene jauh terdengar. Tidak keras, tapi cukup untuk membuat suasana di dalam ruangan berubah seketika."

    show Eksplor_Terkejut:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "...Mereka mulai."

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Secepat ini?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Gue bilang kan. Ini cuma soal waktu."

    "Nara berjalan terburu-buru ke arah pintu."

    hide Casual_Terkejut with dissolve

    show Eksplor_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Gue cabut. Lo sebaiknya tutup mulut."

    "Nara berhenti sebentar di ambang pintu, menoleh sekali lagi."

    nara "Dan Raka..."
    nara "Jangan kira lo bisa netral di cerita ini."

    hide Eksplor_Serius with dissolve

    # SFX Pintu ditutup dengan cepat
    play sound "door_close.ogg"

    "Langkah kakinya menghilang di lorong, meninggalkan Raka sendirian dengan peringatan yang menggantung di udara."

    jump scene_20f
