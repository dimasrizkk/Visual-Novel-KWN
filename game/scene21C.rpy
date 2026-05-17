label corridor_escape:

    # Menampilkan latar belakang lorong pelarian
    scene bg corridor_escape with dissolve

    # Memutar BGM dengan nuansa kepanikan di ruang sempit
    play music "tight_escape.ogg" fadein 1.0

    "Lorong sempit."
    "Lampu berkedip."
    "Langkah kaki mendekat dari arah belakang."

    nara "Kita nggak bisa lawan. Kita cuma bisa keluar."

    raka "Yang lain?"

    nara "...Udah jalan masing-masing."

    "Itu jawaban yang tidak menjawab."

    # SFX Suara dari radio HT milik Unit Penertiban
    play sound "voice_radio.ogg"

    agent "Sektor terkunci."
    agent "Target terdeteksi."
    agent "Eksekusi prosedur."

    raka "Target?"

    # Nara muncul dengan ekspresi cemas/khawatir
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Kita."

    # PILIHAN KRITIS — DI TITIK TERDESAK
    menu:
        "Apa yang dilakukan Raka saat terdesak?"

        "Bantu Nara kabur":
            $ rebellion += 2
            
            show Casual_Serius:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            
            "Ia menggenggam tangan Nara. Tidak banyak bicara."
            "Keputusan sudah dibuat."

        "Suruh Nara pergi, Raka tertinggal":
            $ sacrifice += 2
            
            show Casual_Serius:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            raka "Lo pergi."

            show Eksplor_Serius:
                xalign 0.85
                yalign 1.1
                zoom 0.85
            nara "Jangan sok pahlawan."

            raka "Gue serius."

            "Untuk pertama kalinya, ia memilih kehilangan kendali."

        "Ragu sesaat":
            $ doubt += 2
            
            show Casual_Sedih:
                xalign 0.15
                yalign 1.1
                zoom 0.85
            
            "Langkahnya melambat. Cuma satu detik."
            "Tapi di dunia seperti ini... satu detik cukup untuk mengubah segalanya."

    # Menghentikan audio secara perlahan sebelum transisi bab berikutnya
    stop music fadeout 2.0
    stop sound fadeout 1.0

    return
