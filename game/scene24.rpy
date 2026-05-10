label scene_24_penjaga_core:

    scene core_corridor 
    with fade 
    play music "tension.ogg" 
    
    show guard_core at center 
    
    guard_core "Berhenti." 
    nara "Kita nggak punya waktu." 
    raka "Kita nggak punya pilihan." 
    
    play sound "fight_short.ogg" 
    
    "Pertarungan cepat." 
    "Tidak indah." 
    "Tidak bersih." 
    "Cukup untuk bertahan." 
    
    "Guard core jatuh." 
    
    play sound "metal_drop.ogg" 
    
    "Sebuah pistol terjatuh dari tangannya." 
    
    pause 

    menu:
        "Apa yang dilakukan Raka?":
            pass

        "Ambil pistol":
            $ has_gun = True 
            "Raka mengambilnya." 
            "Dingin." 
            "Berat." 
            "Nyata." 
            raka "(Cuma buat jaga-jaga…)" 

        "Biarkan":
            $ has_gun = False 
            "Raka melewatinya." 
            raka "(Gue nggak butuh itu…)"

    return