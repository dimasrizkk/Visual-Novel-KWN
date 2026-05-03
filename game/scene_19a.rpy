## ============================================================
##  MIRROR — Scene 19A
##  Judul   : Kantor yang Tidak Pernah Gelap
##  Karakter: Raka, Adrian
##  Latar   : nawasa_city_night → minister_room
## ============================================================

label scene_19a:

    scene nawasa_city_night
    with fade

    play music "ominous_clean.ogg"

    "Malam di Nawasena tidak pernah benar-benar gelap."
    "Lampu gedung kementerian tetap menyala, seolah pekerjaan tidak mengenal waktu."
    "Atau mungkin, kontrol tidak boleh tidur."

    scene minister_room
    with dissolve

    "Langkah Raka menggema di lantai marmer yang terlalu bersih untuk disebut alami."

    system "Selamat datang, Raka Pradana."
    system "Akses tingkat menengah dikonfirmasi."
    system "Silakan menuju lantai 47."

    "Tak ada penjaga yang benar-benar melihatnya."
    "Semua digantikan oleh sistem yang tidak pernah lupa."

    "Lift transparan naik menembus kota."
    "Dari sini, Nawasena terlihat seperti diagram sempurna."
    "Jalur distribusi. Lampu sinkron. Pola konsumsi."
    "Semuanya rapi."
    "Semuanya terkendali."

    show raka formal serius at left

    raka "(dalam hati) Dan semuanya mulai terasa... salah."

    play sound "elevator_ding.ogg"

    "Pintu terbuka."
    "Sepi."
    "Terlalu sepi untuk lantai dengan kekuasaan sebesar ini."

    show adrian jas netral at right

    adrian "Masuk saja, Raka."

    jump scene_19b
