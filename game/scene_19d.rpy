## ============================================================
##  MIRROR — Scene 19D
##  Judul   : Tawaran
##  Karakter: Raka, Adrian
##  Latar   : minister_room
##  Flag    : loyalty / awareness / ambition
## ============================================================

label scene_19d:

    scene minister_room
    with dissolve

    play music "mind_game.ogg"

    show raka formal serius at left
    show adrian jas serius at right

    "Adrian mendekat."

    adrian "Aku akan jujur padamu, Raka."
    adrian "Orang seperti kau jarang."
    adrian "Cukup pintar untuk melihat retakan."
    adrian "Cukup ambisius untuk tidak langsung kabur."
    adrian "Dan cukup terluka untuk bisa dikendalikan."

    show raka formal serius at left

    raka "Saya tidak sedang dikendalikan."

    show adrian jas serius at right

    adrian "Semua orang sedang."

    play sound "drawer_open.ogg"

    "Ia mengeluarkan sebuah perangkat kecil."
    "Hitam. Tipis. Tanpa label."
    "Namun terasa berat meski belum disentuh."

    show adrian jas netral at right

    adrian "Ini."
    adrian "Elite Drive."

    "Ruangan terasa lebih sunyi."

    adrian "Akses tingkat atas."
    adrian "Bypass filter MIRROR."
    adrian "Data mentah."
    adrian "Keputusan sebelum dipoles."

    show raka formal serius at left

    raka "Kenapa saya?"

    show adrian jas serius at right

    adrian "Karena aku ingin tahu."
    adrian "Kau akan jadi apa kalau diberi lebih banyak pilihan."

    "Adrian mendekat."

    adrian "Ikut aku, Raka."
    adrian "Dunia tidak berubah oleh orang baik."
    adrian "Dunia berubah oleh orang yang berani memegang kendali."

    "Kalimat itu menggantung."
    "Berat."
    "Menggoda."

    menu:
        "Apa keputusan Raka terhadap Elite Drive?"

        "Tolak terang-terangan":
            $ loyalty += 2
            show raka formal serius at left
            raka "Saya tidak butuh itu."
            raka "Kalau sistem ini benar, saya tidak perlu jalan pintas."
            show adrian jas serius at right
            "Adrian menatap lama."
            show adrian jas senyum at right
            adrian "HAHAHAHAAAA.. Idealismemu... menarik."
            adrian "Biasanya tidak bertahan lama."
            "Drive tetap di meja. Tapi bayangannya ikut pulang."

        "Ambil untuk berjaga-jaga":
            $ awareness += 2
            show raka formal netral at left
            raka "Saya akan simpan."
            raka "Untuk memastikan semuanya sesuai."
            show adrian jas senyum at right
            "Adrian tersenyum tipis."
            adrian "Tentu."
            adrian "Selalu mulai dari memastikan."
            "Drive berpindah tangan. Alasan terasa tipis bahkan bagi dirinya sendiri."

        "Terima dengan bangga":
            $ ambition += 2
            show raka formal senyum at left
            raka "Kalau saya ingin naik, saya butuh aksesnya."
            raka "Saya tidak akan pura-pura suci."
            show adrian jas senyum at right
            "Adrian tersenyum puas."
            adrian "Akhirnya."
            adrian "Kau memang orang yang pantas untuk naik, Raka."
            "Drive terasa ringan di tangan. Seolah memang miliknya sejak awal."

    jump scene_19e
