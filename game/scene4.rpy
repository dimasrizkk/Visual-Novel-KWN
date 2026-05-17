label scene4:
    # Memutar BGM "Adrian Theme" sesuai instruksi naskah
    play music adrian_theme fadein 2.0

    scene minister_room with fade
    
    "Ruang kerja Adrian hampir kosong."
    "Tak ada lukisan mahal. Tak ada dekorasi mewah."
    "Hanya meja logam, dinding kaca, dan pemandangan seluruh kota."

    show adrian kantor senyum:
        xalign 0.9
        yalign 1.6
        zoom 0.9
    with dissolve

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    adrian "Indah, bukan?"
    raka "Ya."
    
    adrian "Dulu di bawah sana hanya banjir, kabel terbakar, dan orang saling menipu untuk bertahan."
    adrian "Sekarang kereta datang tepat waktu."
    adrian "Anak-anak pulang dengan aman."
    adrian "Obat tiba sebelum pasien mati."

    "Adrian menatap Raka."

    adrian "Semua itu lahir karena seseorang berani memilih efisiensi daripada nostalgia."
    raka "Dengan mengorbankan banyak hal."
    
    adrian "Banyak hal seperti apa?"
    raka "Usaha kecil. Pabrik lokal. Kebebasan."
    
    adrian "Kebebasan?"
    adrian "Kata yang indah."
    adrian "Biasanya diucapkan oleh orang yang belum pernah lapar."

    "Raka terdiam."

    adrian "Ayahmu pembuat sepatu, benar?"
    
    show raka formal terkejut:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve
    
    raka "Anda tahu soal itu?"
    
    adrian "Aku tahu semua orang yang layak diperhatikan."
    adrian "Dia berbakat."
    adrian "Tapi dunia tidak memberi hadiah pada yang lambat."

    "Kalimat itu menusuk lebih dalam dari hinaan."

    adrian "Jangan ulangi hidupnya."
    adrian "Naiklah."
    adrian "Jadilah orang yang menentukan pasar, bukan dihancurkan pasar."
    
    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve
    
    raka "...Kenapa saya?"
    
    adrian "Karena kau punya dua hal berbahaya."
    adrian "Luka."
    adrian "Dan kemampuan."
    
    "Adrian mendekat."
    
    adrian "Jika diarahkan dengan benar, keduanya bisa membangun negara."
    adrian "Atau membakarnya."

    stop music fadeout 2.0

    return
