## ============================================================
##  MIRROR — Scene 20D
##  Judul   : Ajakan Pemberontakan
##  Karakter: Raka, Nara
##  Latar   : raka_apartement
##  Flag    : rebellion / doubt / betrayal
## ============================================================

label scene_20d:

    scene raka_apartement
    with dissolve

    play music "rebellion_seed.ogg"

    show raka casual serius at left
    show nara eksplor serius at right

    nara "Denger gue baik-baik."
    nara "Ini bukan lagi soal diskusi."
    nara "Mereka mulai sadar."
    nara "Pergerakan kecil mulai hilang satu-satu."
    nara "Ini cuma soal waktu sebelum tempat gue juga kena."

    show raka casual terkejut at left

    raka "...Adrian tahu?"

    show nara eksplor serius at right

    nara "Belum."
    nara "Tapi orang kayak dia nggak butuh bukti."
    nara "Dia cuma butuh pola."

    pause

    nara "Dan pola mulai kebentuk."

    "Nara mendekat."

    nara "Gue butuh lo."

    show raka casual serius at left

    raka "...Dalam hal apa?"

    show nara eksplor serius at right

    nara "Masuk lebih dalam ke MIRROR."
    nara "Ambil data mentah."
    nara "Bukti nyata."
    nara "Biar kita bisa bongkar semuanya."

    show raka casual serius at left

    raka "Itu bunuh diri."

    show nara eksplor serius at right

    nara "Semua perubahan itu bunuh diri versi pelan."

    show raka casual serius at left

    raka "Kalau kita gagal?"

    show nara eksplor serius at right

    nara "Kita udah gagal kalau kita nggak mulai."

    menu:
        "Bagaimana sikap Raka terhadap pemberontakan?"

        "Langsung setuju bantu":
            $ rebellion += 2
            show raka casual serius at left
            raka "Gue bantu."
            raka "Kita lakuin ini."
            show nara eksplor serius at right
            "Nara menatap tajam."
            nara "Jangan setengah-setengah."
            "Jalan sudah dipilih. Tidak ada mundur tanpa kehilangan sesuatu."

        "Ragu dan minta waktu":
            $ doubt += 2
            show raka casual sedih at left
            raka "Gue butuh waktu."
            raka "Ini bukan keputusan kecil."
            show nara eksplor sedih at right
            "Nara menghela napas."
            nara "Waktu adalah hal pertama yang sistem ambil dari kita."
            "Keraguan mulai jadi arah."

        "Tolak secara halus":
            $ betrayal += 2
            show raka casual sedih at left
            raka "Gue nggak bisa."
            raka "Risikonya terlalu besar."
            show nara eksplor sedih at right
            "Nara diam lama."
            nara "Ngerti."
            nara "Semua orang punya harga."
            "Sesuatu retak. Pelan. Tapi pasti."

    jump scene_20e
