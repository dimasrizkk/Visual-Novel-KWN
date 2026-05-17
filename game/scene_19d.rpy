## ============================================================
##  MIRROR — Scene 19D (Updated Format)
##  Judul   : Tawaran
##  Karakter: Raka, Adrian
##  Latar   : minister_room_(adrian)
##  Flag    : loyalty / awareness / ambition
## ============================================================

label scene_19d:

    scene minister_room_(adrian) with dissolve

    # Menggunakan BGM Mind Game untuk suasana manipulatif
    play music "mind_game.ogg" fadein 2.0

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Adrian mendekat perlahan."

    adrian "Aku akan jujur padamu, Raka."
    adrian "Orang seperti kau jarang. Cukup pintar untuk melihat retakan."
    adrian "Cukup ambisius untuk tidak langsung kabur. Dan cukup terluka untuk bisa dikendalikan."

    raka "Saya tidak sedang dikendalikan."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Semua orang sedang."

    # SFX Suara laci dibuka
    play sound "drawer_open.ogg"

    "Ia mengeluarkan sebuah perangkat kecil. Hitam. Tipis. Tanpa label."
    "Namun terasa berat meski belum disentuh."

    show Jas_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Ini. Elite Drive."

    "Ruangan terasa lebih sunyi."

    adrian "Akses tingkat atas. Bypass filter MIRROR. Data mentah. Keputusan sebelum dipoles."

    raka "Kenapa saya?"

    adrian "Karena aku ingin tahu. Kau akan jadi apa kalau diberi lebih banyak pilihan."

    "Adrian mendekat. Jarak di antara mereka semakin menipis."

    adrian "Ikut aku, Raka."
    adrian "Dunia tidak berubah oleh orang baik. Dunia berubah oleh orang yang berani memegang kendali."

    "Kalimat itu menggantung. Berat. Menggoda."

    # Blok interaktif untuk menentukan arah cerita dan poin
    menu:
        "Apa keputusan Raka terhadap Elite Drive?"

        "Tolak terang-terangan":
            $ loyalty += 2
            $ has_drive = False
            show Formal_Serius:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Saya tidak butuh itu."
            raka "Kalau sistem ini benar, saya tidak perlu jalan pintas."
            
            show Jas_Senyum:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            adrian "HAHAHAHAAAA.. Idealismemu... menarik."
            adrian "Biasanya tidak bertahan lama."
            "Drive tetap di meja. Tapi bayangannya seolah ikut pulang bersamanya."

        "Ambil untuk berjaga-jaga":
            $ awareness += 2
            $ has_drive = True
            show Formal_Netral:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Saya akan simpan. Untuk memastikan semuanya sesuai."
            
            show Jas_Senyum:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            adrian "Tentu. Selalu mulai dari 'memastikan'."
            "Drive berpindah tangan. Alasan itu terasa tipis bahkan bagi dirinya sendiri."

        "Terima dengan bangga":
            $ ambition += 2
            $ has_drive = True
            show Formal_Senyum:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Kalau saya ingin naik, saya butuh aksesnya. Saya tidak akan pura-pura suci."
            
            show Jas_Senyum:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            adrian "Akhirnya. Kau memang orang yang pantas untuk naik, Raka."
            "Drive terasa ringan di tangan. Seolah memang miliknya sejak awal."

    # Menghentikan BGM sebelum transisi penutup scene
    stop music fadeout 2.0

    jump scene_19e
