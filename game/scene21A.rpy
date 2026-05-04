label scene21A:
    scene city_midnight 
    with fade 
    play music "ominous_silence.ogg" 

    "Malam di Nawasena terasa... berbeda." 
    "Bukan karena lebih gelap." 
    "Tapi karena terlalu rapi." 
    "Lalu lintas tetap berjalan." 
    "Lampu tetap sinkron." 
    "Iklan tetap tersenyum." 
    "Namun di bawah semua itu.." 
    "ada sesuatu yang sedang bergerak."

    scene raka_apartment 
    with dissolve 
    show raka alert at center 
    sound "device_alert.ogg"

    system "Peringatan aktivitas tidak biasa terdeteksi di beberapa sektor." 
    system "Operasi stabilisasi sedang berlangsung." 
    raka "Stabilisasi..." 
    "Kata lain untuk sesuatu yang tidak ingin disebut dengan jujur." 

    sound "message_ping.ogg" 

    "Pesan masuk." 

    if loyalty >= 2 or rebellion >= 1: 
        nara_text "Raka. Sekarang." 
        nara_text "Mereka mulai bergerak." 
        nara_text "Kalau lo masih mau bantu, ini waktunya." 

    elif doubt >= 2: 
        nara_text "Raka..." 
        nara_text "Gue harap lo udah mutusin." 
        nara_text "Karena kita kehabisan waktu." 

    else: 
        nara_text "Jangan datang." 
        nara_text "Terlalu berbahaya." 
        nara_text "Serius."

    raka menatap layar 

    "Pilihan." 
    "Bukan lagi teori." 
    "Bukan lagi diskusi." 
    "Sekarang, aksi." 

    menu: 
        "Apa yang dilakukan Raka?": 

        "Pergi ke Ruang Sisa": 
            active_path += 1 
            "Ia tidak berpikir lama." 
            "Tubuhnya bergerak lebih dulu dari ketakutannya." 

        "Diam dan memantau dari jauh": 
            passive_path += 1 
            "Ia membuka dashboard internal." 
            "Memilih melihat daripada terlibat." 

        "Hubungi pihak kantor": 
            betrayal += 2 
            "Jarimu bergerak." 
            "Lebih cepat dari nurani." 
            "Atau mungkin... itulah nurani yang tersisa." 

    return