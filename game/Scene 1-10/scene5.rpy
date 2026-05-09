label scene5:
    # Memutar BGM "Lonely Room" untuk membangun suasana sepi
    play music lonely_room fadein 2.0

    scene apartment_dark with fade
    
    "Malam."
    "Apartemen Raka terlalu rapi untuk disebut rumah."

    show raka formal tired:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "..."
    
    "Ia melepaskan jas. Menyalakan lampu. Mematikan lagi."
    "Sunyi."

    scene shelf_old_box with dissolve
    
    "Di sudut lemari, sebuah kotak tua."
    
    raka "...Masih ada."
    
    # Memutar SFX suara kotak dibuka
    play sound box_open

    scene white
    with Fade(0.1, 0.0, 0.5)
    scene old_shoes with dissolve
    
    "Sepasang sepatu kulit."
    "Buatan tangan."
    "Sedikit retak. Jahitannya masih kokoh."

    # Menggunakan suara memori/flashback ayah Raka
    ayah "Barang bagus kalah bukan karena jelek..."
    ayah "Karena tak diberi kesempatan."

    "Raka menunduk."
    
    raka "Kesempatan tidak datang."
    raka "Ia dibeli."

    "Entah ia sedang menyangkal ayahnya."
    "Atau dirinya sendiri."

    stop music fadeout 2.0

    return
