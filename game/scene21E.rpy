label scene_21e_pengkhianatan:
    # Logic 'else' ditangani oleh struktur menu/if di label sebelumnya
    
    scene ministry_control_room 
    with fade 
    play music "betrayal_calm.ogg" 
    
    "Raka berdiri di ruangan kontrol." 
    "Monitor menampilkan lokasi Ruang Sisa." 
    
    adrian "Keputusan cepat." (voice_tag="offscreen")
    
    scene adrian_shadow 
    with dissolve 
    
    adrian "Aku menghargai itu." 
    
    raka "..." # Mengganti 'raka diam' menjadi dialog titik-titik agar alur tetap terjaga
    
    adrian "Jangan khawatir." 
    adrian "Kita tidak menghancurkan." 
    adrian "Kita... merapikan." 
    
    "Kata yang berbeda." 
    "Makna yang sama."

    return