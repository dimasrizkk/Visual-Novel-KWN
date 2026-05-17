label scene21a:

    scene KOTA NAWASENA with fade 
    
    # Memutar BGM keheningan mencekam dengan transisi halus
    play music "ominous_silence.ogg" fadein 2.0

    "Malam di Nawasena terasa... berbeda." 
    "Bukan karena lebih gelap, tapi karena terlalu rapi." 
    "Luku lintas tetap berjalan. Lampu tetap sinkron. Iklan tetap tersenyum." 
    "Namun di bawah semua itu... ada sesuatu yang sedang bergerak."

    scene APARTEMEN RAKA with dissolve 
    
    # Raka muncul di tengah dengan pakaian casual dalam posisi waspada (alert)
    show Casual_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    # SFX Peringatan perangkat kementerian
    play sound "device_alert.ogg"

    system "Peringatan aktivitas tidak biasa terdeteksi di beberapa sektor." 
    system "Operasi stabilisasi sedang berlangsung." 
    
    raka "Stabilisasi..." 
    "Kata lain untuk sesuatu yang tidak ingin disebut dengan jujur." 

    # SFX Notifikasi pesan masuk
    play sound "message_ping.ogg" 

    "Pesan masuk dari Nara." 

    # Logika percabangan teks berdasarkan akumulasi flag dari scene sebelumnya
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
        nara_text "Terlahu berbahaya." 
        nara_text "Serius."

    "Raka menatap layar perangkatnya dengan banyangan kecemasan." 

    "Pilihan. Bukan lagi teori. Bukan lagi diskusi." 
    "Sekarang, aksi." 

    # Blok interaktif penentu rute jalan cerita (Pathing)
    menu: 
        "Apa yang dilakukan Raka?": 

        "Pergi ke Ruang Sisa": 
            $ active_path += 1 
            "Ia tidak berpikir lama." 
            "Tubuhnya bergerak lebih dulu dari ketakutannya." 

        "Diam dan memantau dari jauh": 
            $ passive_path += 1 
            "Ia membuka dashboard internal." 
            "Memilih melihat daripada terlibat." 

        "Hubungi pihak kantor": 
            $ betrayal += 2 
            "Jari bergerak. Lebih cepat dari nurani." 
            "Atau mungkin... itulah nurani yang tersisa." 

    # Menghentikan BGM sebelum berpindah ke konsekuensi pilihan
    stop music fadeout 2.0

    return
