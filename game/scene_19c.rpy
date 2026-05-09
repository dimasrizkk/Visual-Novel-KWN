## ============================================================
##  MIRROR — Scene 19C (Updated Format)
##  Judul   : MIRROR Diungkap
##  Karakter: Raka, Adrian
##  Latar   : minister_room_(adrian)
## ============================================================

label scene_19c:

    scene minister_room_(adrian) with dissolve

    # Menampilkan Raka dan Adrian dengan posisi yang tetap konsisten
    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Adrian mengaktifkan layar besar."

    # Menggunakan transisi dissolve untuk layar sistem agar terasa seperti hologram/layar digital
    system "Sistem MIRROR — Overview"

    "Jaringan kompleks muncul. Data perilaku, preferensi, hingga pola emosi semuanya terhubung dalam satu peta besar."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Ini bukan sekadar iklan. Ini adalah sistem navigasi manusia."
    adrian "Kita tidak memaksa. Kita mengarahkan."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Dengan memanipulasi persepsi."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Dengan memahami kelemahan."

    "Adrian menatap tajam."

    adrian "Kau pikir dunia di luar lebih jujur? Pasar bebas?"
    adrian "Itu hanya manipulasi tanpa koordinasi. Kita membuatnya... efisien."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Dengan mengorbankan pilihan."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Dengan menghilangkan ilusi pilihan yang salah."

    "Kalimat itu terlalu rapi. Dan terlalu berbahaya."

    adrian "Kau lihat data kesepian itu, kan?"

    show Formal_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "..."

    show Jas_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Tentu saja kau lihat. Aku sengaja tidak menyembunyikannya."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Kenapa?"

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Karena itu bukan kegagalan. Itu efek samping."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Manusia bukan angka sampingan."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Negara bukan ruang terapi."

    "Benturan pertama terasa nyata."

    # Menggunakan transisi cepat untuk menutup adegan ini
    with flash

    jump scene_19d
