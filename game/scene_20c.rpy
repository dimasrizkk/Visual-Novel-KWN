## ============================================================
##  MIRROR — Scene 20C
##  Judul   : Konfrontasi
##  Karakter: Raka, Nara
##  Latar   : raka_apartement
##  Flag    : loyalty / ambition / ruthless
## ============================================================

label scene_20c:

    scene raka_apartement
    with dissolve

    show raka casual netral at left
    show nara eksplor serius at right

    "Nara melihat sekitar."

    nara "Rapih."
    nara "Kosong."

    show raka casual serius at left

    raka "Fungsional."

    show nara eksplor serius at right

    nara "Persis kayak sistem yang lo bela."

    show raka casual serius at left

    raka "Gue nggak lagi bela siapa-siapa."

    show nara eksplor serius at right

    "Nara langsung menatap."

    nara "Lo bohong."
    nara "Dan lo tahu itu."

    pause

    nara "Gue tahu lo siapa."

    show raka casual terkejut at left

    raka "...Apa maksud lo?"

    play sound "thud.ogg"

    "Nara melempar tablet ke meja."
    "Data MIRROR."
    "Log akses."
    "Jejak Raka."

    show nara eksplor serius at right

    nara "Kurator Narasi."
    nara "Divisi MIRROR."

    "Sunyi."

    show raka casual serius at left

    raka "...Lo ngikutin gue?"

    show nara eksplor serius at right

    nara "Gue nyambungin titik."
    nara "Lo terlalu pintar buat nggak mencurigakan."

    show raka casual serius at left

    raka "Gue bantu kasih informasi ke lo."

    show nara eksplor serius at right

    nara "Lo bantu karena lo penasaran."
    nara "Bukan karena lo peduli."

    "Kena lagi."

    show raka casual serius at left

    raka "Apa bedanya?"

    show nara eksplor serius at right

    "Nara mendekat."

    nara "Beda."
    nara "Orang penasaran berhenti kalau jawabannya bikin dia nggak nyaman."
    nara "Orang peduli tetap lanjut meski hancur."

    pause

    nara "Lo yang mana?"

    menu:
        "Apa yang Raka katakan?"

        "Jujur soal semuanya":
            $ loyalty += 2
            show raka casual sedih at left
            raka "Gue bagian dari sistem itu."
            raka "Dan gue mulai muak."
            raka "Tapi gue juga takut."
            raka "Kalau gue keluar, gue kehilangan segalanya."
            raka "Kalau gue tetap di dalam, gue kehilangan diri gue."
            show nara eksplor netral at right
            "Nara diam."
            show nara eksplor senyum at right
            nara "Akhirnya lu jujur."
            nara "Itu awal yang bagus."

        "Setengah bohong":
            $ ambition += 2
            show raka casual netral at left
            raka "Gue cuma bagian kecil."
            raka "Gue nggak tahu semua."
            raka "Gue cuma coba manfaatin posisi gue."
            show nara eksplor serius at right
            "Nara menatap lama."
            nara "Lo lebih pintar dari itu."
            nara "Jangan pura-pura bodoh."

        "Tujuan menghalalkan cara":
            $ ruthless += 2
            show raka casual serius at left
            raka "Kalau sistem busuk, cara bersih nggak akan cukup."
            raka "Gue pakai apa yang ada."
            raka "Termasuk sistem itu."
            show nara eksplor marah at right
            "Nara dingin."
            nara "Hati-hati."
            nara "Kalau lo terlalu lama di dalam lumpur.."
            nara "lo berhenti sadar lo kotor."

    jump scene_20d
