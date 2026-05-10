label scene14:
    scene quiet_bench with dissolve
    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    show nara bengkel netral:
        xalign 0.95
        yalign 1.6
        zoom 0.85    

    # Mematikan BGM perdebatan dengan cepat dan menggantinya dengan lagu yang lebih intim
    stop music fadeout 1.0
    play music soft_truth fadein 2.0
    
    nara "Namamu siapa?"
    
    raka "Raka."
    
    nara "Nama lengkap."
    
    raka "Kenapa?"
    
    nara "Karena orang yang hanya menyebut nama depan biasanya sedang menyembunyikan sesuatu."
    
    raka "...Raka Pradana."
    
    "Nara berhenti."

    show nara bengkel terkejut:
        xalign 0.95
        yalign 1.6
        zoom 0.85
    
    nara "Pradana?"
    
    raka "Ya."
    
    nara "Pembuat sepatu dari Pasar Timur?"

    show raka formal serius: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    "Raka tegang."
    
    raka "Kau kenal?"

    show nara bengkel netral:
        xalign 0.95
        yalign 1.6
        zoom 0.85
    
    nara "Aku pernah lihat karyanya."
    nara "Jahitannya rapi."
    nara "Sedikit terlalu keras di tumit."

    show raka formal senyum: 
        xalign 0.2
        yalign 1.2
        zoom 0.4

    "Raka tak sengaja tersenyum kecil."
    
    raka "Ia selalu bilang kaki harus dipaksa jujur."
    
    nara "Ayahmu terdengar keras kepala."
    
    raka "Ia bangkrut."
    
    nara "Banyak orang baik bangkrut."
    
    raka "Itu bukan pembelaan."
    
    nara "Bukan."
    nara "Itu data."
    
    "Sunyi turun lagi."
    "Namun kali ini tidak canggung."

    return
