## ============================================================
##  MIRROR — Scene 20C (Updated Format)
##  Judul   : Konfrontasi
##  Karakter: Raka, Nara
##  Latar   : APARTEMEN RAKA
##  Flag    : loyalty / ambition / ruthless
## ============================================================

label scene_20c:

    scene APARTEMEN RAKA with dissolve

    # Menampilkan Raka dan Nara dengan koordinat presisi
    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Nara melihat sekeliling ruangan dengan teliti."

    nara "Rapih. Kosong."

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Fungsional."

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Persis kayak sistem yang lo bela."

    raka "Gue nggak lagi bela siapa-siapa."

    "Nara langsung menatap tajam ke arah Raka."

    nara "Lo bohong. Dan lo tahu itu."

    pause 1.0

    nara "Gue tahu lo siapa."

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Apa maksud lo?"

    # SFX Suara tablet dilempar ke meja
    play sound "thud.ogg"

    "Nara melempar tablet ke meja. Layarnya menyala, menampilkan data MIRROR, log akses, dan seluruh jejak digital Raka."

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Kurator Narasi. Divisi MIRROR."

    "Sunyi menyelimuti ruangan."

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Lo ngikutin gue?"

    nara "Gue nyambungin titik. Lo terlalu pintar buat nggak mencurigakan."

    raka "Gue bantu kasih informasi ke lo."

    nara "Lo bantu karena lo penasaran. Bukan karena lo peduli."

    "Kena lagi. Argumen Nara menusuk tepat sasaran."

    raka "Apa bedanya?"

    "Nara melangkah mendekat."

    nara "Beda. Orang penasaran berhenti kalau jawabannya bikin dia nggak nyaman."
    nara "Orang peduli tetap lanjut meski hancur."

    pause 1.0

    nara "Lo yang mana?"

    # Blok interaktif untuk menentukan arah kepribadian Raka
    menu:
        "Apa yang Raka katakan?"

        "Jujur soal semuanya":
            $ loyalty += 2
            show Casual_Sedih:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Gue bagian dari sistem itu. Dan gue mulai muak."
            raka "Tapi gue juga takut. Kalau gue keluar, gue kehilangan segalanya. Kalau gue tetap di dalam, gue kehilangan diri gue."
            
            show Eksplor_Senyum:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Akhirnya lu jujur. Itu awal yang bagus."

        "Setengah bohong":
            $ ambition += 2
            show Casual_Netral:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Gue cuma bagian kecil. Gue nggak tahu semua."
            raka "Gue cuma coba manfaatin posisi gue."
            
            show Eksplor_Serius:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Lo lebih pintar dari itu. Jangan pura-pura bodoh."

        "Tujuan menghalalkan cara":
            $ ruthless += 2
            show Casual_Serius:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Kalau sistem busuk, cara bersih nggak akan cukup. Gue pakai apa yang ada, termasuk sistem itu."
            
            show Eksplor_Marah:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Hati-hati. Kalau lo terlalu lama di dalam lumpur, lo berhenti sadar lo kotor."

    jump scene_20d
