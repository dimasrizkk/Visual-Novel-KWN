# SCENE 21C — KONFRONTASI SEMPIT

label corridor_escape:

    scene bg corridor_escape
    with dissolve

    play music "tight_escape.ogg"

    "Lorong sempit."
    "Lampu berkedip."
    "Langkah kaki mendekat."

    nara "Kita nggak bisa lawan."
    nara "Kita cuma bisa keluar."

    raka "Yang lain?"

    nara "...Udah jalan masing-masing."

    "Itu jawaban yang tidak menjawab."

    play sound "voice_radio.ogg"

    agent "Sektor terkunci."
    agent "Target terdeteksi."
    agent "Eksekusi prosedur."

    raka "Target?"

    show nara concerned

    nara "Kita."

    # PILIHAN KRITIS — DI TITIK TERDESAK
    menu:
        "Apa yang dilakukan Raka saat terdesak?"

        "Bantu Nara kabur":
            $ rebellion += 2

            "Ia menggenggam tangan Nara."
            "Tidak banyak bicara."
            "Keputusan sudah dibuat."

        "Suruh Nara pergi, Raka tertinggal":
            $ sacrifice += 2

            raka "Lo pergi."

            nara "Jangan sok pahlawan."

            raka "Gue serius."

            "Untuk pertama kalinya, ia memilih kehilangan kendali."

        "Ragu sesaat":
            $ doubt += 2

            "Langkahnya melambat."
            "Cuma satu detik."
            "Tapi di dunia seperti ini..."
            "satu detik cukup untuk mengubah segalanya."

    return