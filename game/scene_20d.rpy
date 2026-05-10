## ============================================================
##  MIRROR — Scene 20D (Updated Format)
##  Judul   : Ajakan Pemberontakan
##  Karakter: Raka, Nara
##  Latar   : APARTEMEN RAKA
##  Flag    : rebellion / doubt / betrayal
## ============================================================

label scene_20d:

    scene APARTEMEN RAKA with dissolve

    # Memutar BGM bertema pemberontakan dan ketegangan
    play music "rebellion_seed.ogg" fadein 2.0

    # Menampilkan Raka dan Nara dalam posisi konfrontasi
    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Denger gue baik-baik. Ini bukan lagi soal diskusi."
    nara "Mereka mulai sadar. Pergerakan kecil mulai hilang satu-satu."
    nara "Ini cuma soal waktu sebelum tempat gue juga kena."

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Adrian tahu?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Belum. Tapi orang kayak dia nggak butuh bukti. Dia cuma butuh pola."

    pause 1.0

    nara "Dan pola mulai kebentuk."

    "Nara melangkah mendekat, memperpendek jarak di antara mereka."

    nara "Gue butuh lo."

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Dalam hal apa?"

    nara "Masuk lebih dalam ke MIRROR. Ambil data mentah. Bukti nyata."
    nara "Biar kita bisa bongkar semuanya."

    raka "Itu bunuh diri."

    nara "Semua perubahan itu bunuh diri versi pelan."

    raka "Kalau kita gagal?"

    nara "Kita udah gagal kalau kita nggak mulai."

    # Blok interaktif untuk menentukan loyalitas Raka
    menu:
        "Bagaimana sikap Raka terhadap pemberontakan?"

        "Langsung setuju bantu":
            $ rebellion += 2
            show Casual_Serius:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Gue bantu. Kita lakuin ini."
            
            show Eksplor_Serius:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Jangan setengah-setengah."
            "Jalan sudah dipilih. Tidak ada jalan mundur tanpa kehilangan sesuatu."

        "Ragu dan minta waktu":
            $ doubt += 2
            show Casual_Sedih:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Gue butuh waktu. Ini bukan keputusan kecil."
            
            show Eksplor_Sedih:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Waktu adalah hal pertama yang sistem ambil dari kita."
            "Keraguan mulai menjadi arah yang baru."

        "Tolak secara halus":
            $ betrayal += 2
            show Casual_Sedih:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Gue nggak bisa. Risikonya terlalu besar."
            
            show Eksplor_Sedih:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Ngerti. Semua orang punya harga."
            "Sesuatu retak. Pelan, tapi pasti."

    # Menghentikan musik perlahan sebelum transisi penutup
    stop music fadeout 2.0

    jump scene_20e
