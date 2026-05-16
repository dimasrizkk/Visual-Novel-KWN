label scene_22b_raka_sendiri:

    scene raka_walk_morning with dissolve 
    
    # Raka muncul di posisi tengah dengan ekspresi lelah/tertekan
    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka berjalan menyusuri trotoar tanpa arah dan tujuan yang jelas." 
    
    raka "(dalam hati) Ini yang gue mau?" 
    raka "(dalam hati) Atau ini cuma akibat dari semua yang gue lakukan?" 
    
    pause 1.0

    # LOGIKA PERCABANGAN BATIN — Berdasarkan tindakan sebelumnya
    if betrayal >= 2: 
        "Ia mencoba keras meyakinkan dirinya sendiri di tengah rasa bersalah." 
        raka "(dalam hati) Ini perlu." 
        raka "(dalam hati) Kalau nggak, semuanya bakal jauh lebih kacau." 

    elif doubt >= 2: 
        "Keraguan yang mengendap kini tidak lagi bisa disembunyikan dari hatinya." 
        raka "(dalam hati) Gue lihat semuanya..." 
        raka "(dalam hati) ...tapi pada akhirnya gue tetep nggak ngapa-ngapain." 

    else: 
        "Wajah-wajah itu mendadak muncul lagi di benaknya." 
        "Orang-orang yang terpaksa ditangkap. Orang-orang yang mendadak hilang dari kota." 
        raka "(dalam hati) Gue emang bantu mereka…" 
        raka "(dalam hati) ...tapi pertanyaannya, apakah itu cukup?" 

    # SFX Notifikasi pesan masuk yang memecah monolog batin
    play sound "message_ping.ogg" 
    
    "Sebuah notifikasi pesan masuk di perangkatnya." 

    # LOGIKA PESAN MASUK — Variasi pesan dari Nara tergantung kepercayaan
    if loyalty >= 2 or rebellion >= 1: 
        nara_text "Lokasi baru. Datang sendiri." 
        nara_text "Kita nggak punya banyak waktu." 

    elif doubt >= 2: 
        nara_text "Raka…" 
        nara_text "Ini terakhir kali gue hubungi lo." 
        nara_text "Datang hanya kalau lo udah bener-bener mutusin." 

    else: 
        nara_text "Jangan datang." 
        nara_text "Serius." 
        nara_text "Situasinya udah jauh berbeda sekarang." 

    "Raka menatap layar perangkatnya dalam diam untuk waktu yang cukup lama." 
    
    raka "(dalam hati) Semuanya udah berjalan terlalu jauh..."

    # Menghentikan audio secara halus sebelum transisi scene
    stop music fadeout 2.0
    stop sound fadeout 1.0

    return
