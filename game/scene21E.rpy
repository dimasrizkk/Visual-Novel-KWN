label scene_21e_pengkhianatan:
    
    # Menampilkan latar belakang ruang kontrol kementerian
    scene ministry_control_room with fade 
    
    # Memutar BGM bertema pengkhianatan yang tenang namun dingin
    play music "betrayal_calm.ogg" fadein 2.5 
    
    "Raka berdiri terpaku di dalam ruangan kontrol kementerian yang megah." 
    "Di hadapannya, monitor raksasa menampilkan koordinat presisi dan visual langsung dari lokasi Ruang Sisa yang sedang dikepung." 
    
    # Dialog offscreen dari Adrian sebelum beralih scene
    adrian "Keputusan cepat."

    scene adrian_shadow with dissolve 
    
    # Adrian muncul dengan wibawa penuh di sisi kanan layar
    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve
    
    adrian "Aku menghargai itu, Raka." 
    
    # Raka muncul di sisi kiri dalam posisi formal namun tertekan
    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "..." 
    
    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Jangan khawatir. Kita tidak menghancurkan tempat itu." 
    adrian "Kita hanya... merapikan." 
    
    "Merapikan."
    "Kata yang berbeda, namun di kota Nawasena ini, keduanya memiliki makna akhir yang persis sama."

    # Menghentikan audio secara dramatis sebelum menutup babak
    stop music fadeout 3.0

    return
