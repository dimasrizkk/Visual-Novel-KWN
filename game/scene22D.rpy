label scene22D:

    # Mengasumsikan posisi sprite masih dari scene sebelumnya
    # Jika Raka perlu menghadap Nara (kanan), gunakan xzoom -1
    show raka rebel serius:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    hide nara

    menu:
        "Apa keputusan Raka?" # Ini adalah caption menu

        "Gue ikut sampai akhir.":
            $ rebellion += 1
            raka "Gue udah terlalu jauh buat berhenti."
            
        "Gue mau bantu… tapi gue masih mikir.":
            $ doubt += 1
            raka "Gue ikut."
            raka "Tapi gue nggak janji apa-apa."
            
        "Ini salah.":
            $ betrayal += 1
            raka "Lo sadarkan ini akan menghancurkan semuanya?"
            nara "Kadang itu yang dibutuhin."

    # Keluar dari menu, cerita berlanjut di sini
    "Suasana di ruangan itu terasa semakin berat."
    
    return