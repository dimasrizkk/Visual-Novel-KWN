## ============================================================
##  MIRROR — Scene 19A (Updated Format)
##  Judul   : Kantor yang Tidak Pernah Gelap
##  Karakter: Raka, Adrian
##  Latar   : KOTA NAWASENA → minister_room_(adrian)
## ============================================================

label scene_19a:

    scene KOTA NAWASENA with fade

    # Memutar BGM bernuansa firasat buruk dengan transisi halus
    play music "ominous_clean.ogg" fadein 3.0

    "Malam di Nawasena tidak pernah benar-benar gelap."
    "Lampu gedung kementerian tetap menyala, seolah pekerjaan tidak mengenal waktu."
    "Atau mungkin, kontrol tidak boleh tidur."

    scene minister_room_(adrian) with dissolve

    "Langkah Raka menggema di lantai marmer yang terlalu bersih untuk disebut alami."

    system "Selamat datang, Raka Pradana."
    system "Akses tingkat menengah dikonfirmasi."
    system "Silakan menuju lantai 47."

    "Tak ada penjaga yang benar-benar melihatnya."
    "Semua digantikan oleh sistem yang tidak pernah lupa."

    "Lift transparan naik menembus kota."
    "Dari sini, Nawasena terlihat seperti diagram sempurna."
    "Jalur distribusi. Lampu sinkron. Pola konsumsi."
    "Semuanya rapi. Semuanya terkendali."

    # Raka muncul dengan pakaian formal
    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "(dalam hati) Dan semuanya mulai terasa... salah."

    # SFX Ding elevator untuk menandai kedatangan
    play sound "elevator_ding.ogg"

    "Pintu terbuka."
    "Sepi. Terlalu sepi untuk lantai dengan kekuasaan sebesar ini."

    # Adrian muncul sebagai antagonis/mentor dengan wibawa tinggi
    show Jas_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    adrian "Masuk saja, Raka."

    # Persiapan transisi musik untuk konfrontasi di scene berikutnya
    stop music fadeout 2.0

    jump scene_19b
