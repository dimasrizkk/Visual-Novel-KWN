label scene7:
    scene city_night_rain with fade
    play ambient rain fadein 2.0 volume 0.5
    play music mystery_low fadein 2.0
    
    "Di tempat lain, hujan turun di gang tua yang nyaris hilang dari peta digital."
    "Lampu kecil menyala di balik papan kayu usang."
    
    scene ruang_sisa_outside with dissolve
    
    "Tulisan di pintu hampir pudar."
    "\"RUANG SISA\""
    
    # SFX orang memperbaiki barang (logam)
    play sound metal_fix
    
    "Di dalam, seseorang sedang memperbaiki benda yang kota anggap selesai."
    
    show nara silhouette at center with dissolve
    
    "Dan tanpa mengetahui namanya, masa depan Raka sedang menunggu."
    
    stop ambient fadeout 3.0
    stop music fadeout 3.0
    
    scene black with fade
    pause 1.0

    return