label scene2:
    # Memutar BGM atau SFX suasana kantor
    play music office_ambience fadein 1.0

    scene mirror_office_day with fade

    "Lantai 77. Gedung Integrasi Narasi Konsumen."
    "Divisi MIRROR."

    show raka neutral at center

    "Di tempat ini, kata-kata lebih tajam dari pisau."

    worker "Raka, target kampanye sektor timur turun 8%%."
    worker "Mereka mulai membeli barang rakitan lokal."
    worker "Kita butuh slogan baru."

    hide worker

    raka "...Baik."

    scene computer_screen with dissolve

    "Kursor berkedip. Sebuah kota menunggu kalimat berikutnya."

    # Blok interaktif penentuan poin
    menu:
        "Bagaimana Raka menulis slogan?"

        "Buat mereka merasa tertinggal.":
            $ ambition += 1
            raka "Kalau tak ikut tren, kau akan ditinggalkan."
            "Rasa takut selalu menjual lebih cepat daripada kualitas."

        "Buat mereka merasa ini pilihan cerdas.":
            $ ruthless += 1
            raka "Orang sukses tahu standar yang pantas."
            "Ego adalah pasar yang tak pernah sepi."

        "Kenapa kita harus manipulatif?":
            $ loyalty += 1
            raka "...Kenapa semua harus dimulai dari rasa kurang?"
            "Pertanyaan itu muncul pelan. Nyaris tak terdengar."

    worker "Apa?"
    raka "Tidak ada. Pakai draft pertama."

    scene office_large_screen with dissolve

    system "Kampanye diterima."
    system "Prediksi peningkatan pembelian: 34%%"

    worker "Gila... kamu memang monster."
    raka "Monster yang dibayar tepat waktu."
    worker "Haha."

    "Semua tertawa."
    "Raka tidak."
    
    stop music fadeout 2.0

    return