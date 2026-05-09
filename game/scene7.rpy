label scene7:
    # Memutar BGM "Mystery Low"
    play music "audio/mystery_low.mp3" fadein 2.0
    
    # (Opsional) Memutar suara hujan di background jika kamu sudah mendaftarkan channel 'ambient'
    # play ambient "audio/rain_alley.mp3" fadein 2.0

    scene city_night_rain with fade
    
    "Di tempat lain, hujan turun di gang tua yang nyaris hilang dari peta digital."
    "Lampu kecil menyala di balik papan kayu usang."

    scene ruang_sisa_outside with dissolve
    
    "Tulisan di pintu hampir pudar."
    "\"RUANG SISA\""

    # Memutar SFX suara ketukan logam/memperbaiki barang
    play sound "audio/metal_fix.mp3"
    
    "Di dalam, seseorang sedang memperbaiki benda yang kota anggap selesai."

    show nara silhouette at center with dissolve
    
    "Dan tanpa mengetahui namanya, masa depan Raka sedang menunggu."

    # Menghentikan semua suara untuk memberi kesan misterius dan transisi babak
    stop music fadeout 3.0
    # stop ambient fadeout 3.0

    scene black with fade
    
    # Jeda sejenak dalam keheningan layar hitam sebelum masuk ke Chapter 1
    pause 1.0

    return