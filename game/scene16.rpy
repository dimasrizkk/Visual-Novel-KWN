label scene16:
    scene alley_exit_night with fade
    show raka formal netral: 
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve
    
    # Memutar ambient suara kota yang bising
    play music city_hum fadein 2.0 #city_noise_loud gaada jadi pake city_hum
    
    "Raka keluar ke gang."
    "Suara kota kembali terdengar."
    "Namun terasa lebih berisik dari sebelumnya."
    
    play sound device_ping
    system "Rute tercepat ke rumah telah disiapkan."
    
    "Raka tidak bergerak."
    "Ia menoleh ke belakang."    
    "Lampu kecil di atas Ruang Sisa masih menyala."
    "Tempat itu tak megah."
    "Tak efisien."
    "Tak relevan."
    "Namun anehnya, lebih sulit dilupakan daripada seluruh alun-alun tempat menteri tadi berpidato."

    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    # Logika percabangan berdasarkan akumulasi poin
    if loyalty >= 2:
        "Langkahnya berhenti."
        
        raka "..."
        
        # Transisi audio kembali ke dalam ruangan
        stop ambient fadeout 1.5
        scene workshop_corner with dissolve
        play music workshop_warm fadein 2.0
        
        "Ia kembali masuk."
        
        show raka formal netral: 
            xalign 0.0
            yalign 1.6
            zoom 0.85
        with dissolve

        show nara bengkel netral:
            xalign 0.95
            yalign 1.6
            zoom 0.85
        with dissolve        

        nara "Perangkat rusak lagi?"
        
        raka "Tidak."
        
        nara "Lalu?"
        
        "Raka melihat radio tua."
        
        raka "Radio itu... benar-benar masih menangkap siaran?"
        
        nara "Kadang."
        
        raka "Bisa ajari aku menyalakannya?"
        
        "Nara menatap beberapa saat, lalu menggeser kursi kosong."
        
        nara "Duduk."
        
        # Menambahkan poin hubungan rahasia dengan Nara
        $ trust_nara += 1
        
        "Untuk pertama kalinya, Raka duduk di tempat yang tak dirancang untuk status."
        
    else:
        "Ia melangkah pergi."
        "Namun untuk pertama kalinya, rumah terasa lebih jauh."

    # Menghentikan semua suara untuk menutup Chapter I
    stop music fadeout 2.0
    stop ambient fadeout 2.0

    scene black with fade
    
    # Jeda layar hitam sebelum masuk ke Chapter II
    pause 1.5

    return
