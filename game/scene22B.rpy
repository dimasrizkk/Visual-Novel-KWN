label scene_22b_raka_sendiri:

    scene raka_walk_morning 
    with dissolve 
    show raka tired at center 

    "Raka berjalan tanpa tujuan." 
    
    raka "(Ini yang gue mau?)" 
    raka "(Atau ini cuma akibat dari semua yang gue lakukan?)" 
    
    pause 1.0

    # Logika Percabangan Berdasarkan Variabel
    if betrayal >= 2: 
        "Ia mencoba meyakinkan dirinya sendiri." 
        raka "(Ini perlu.)" 
        raka "(Kalau nggak, semuanya kacau.)" 

    elif doubt >= 2: 
        "Keraguan tidak lagi bisa disembunyikan." 
        raka "(Gue lihat semuanya...)" 
        raka "(...tapi gue nggak ngapa-ngapain.)" 

    else: 
        "Wajah-wajah itu muncul lagi." 
        "Orang-orang yang ditangkap." 
        "Orang-orang yang hilang." 
        raka "(Gue bantu…)" 
        raka "(tapi cukup nggak?)" 

    play sound "message_ping.ogg" 
    "Pesan masuk." 

    # Logika Pesan dari Nara
    if loyalty >= 2 or rebellion >= 1: 
        nara_text "Lokasi baru. Datang sendiri." 
        nara_text "Kita nggak punya banyak waktu." 

    elif doubt >= 2: 
        nara_text "Raka…" 
        nara_text "Ini terakhir kali gue hubungi." 
        nara_text "Datang kalau lo udah mutusin." 

    else: 
        nara_text "Jangan datang." 
        nara_text "Serius." 
        nara_text "Ini udah beda." 

    "Raka menatap layar lama." 
    
    raka "(Udah terlalu jauh...)"

    return