label scene12:
    scene workshop_corner with dissolve 
    show nara bengkel netral: 
        xalign 0.95
        yalign 1.6
        zoom 0.85

    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85
    
    "Nara kembali bekerja."

    how nara bengkel serius:
        xalign 0.95
        yalign 1.6
        zoom 0.85

    "Raka menunggu sambil memandang sekeliling."
    "Tak ada satu pun benda di sini terlihat baru."
    "Namun semuanya terasa lebih hidup dari pusat kota."

    # Blok interaktif pilihan eksplorasi Raka
    menu:
        "Apa yang diperhatikan Raka?"

        "Sepasang sepatu kulit tua":
            $ loyalty += 1
            scene shoes_close with dissolve 
            "Jahitannya rapi. Solnya diganti manual."
            "Ia teringat ayahnya."
            raka "..."

        "Radio lawas yang masih menyala":
            $ awareness += 1
            scene radio_close with dissolve 

            # SFX Suara frekuensi radio tua yang mendengung/statis
            play sound radio_static
            
            "Suara penyiar tua memecah dengung statis."
            penyiar "..dan pasar pagi dibuka pukul enam...."
            "Rekaman masa lalu. Disimpan, bukan dibuang."

        "Mesin kopi manual":
            $ ambition += 1
            scene coffee_manual with dissolve 
            raka "Masih ada yang pakai beginian?"
            nara "Masih ada yang suka cara tradisional, bukan seperti orang malas yang tinggal tekan tombol."

    scene workshop_corner with dissolve
    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    show nara bengkel serius:
        xalign 0.95
        yalign 1.6
        zoom 0.85    

    raka "Kau simpan semua barang rongsokan kota di sini?"
    
    nara "Salah."
    nara "Aku simpan bukti bahwa rusak tidak selalu berarti selesai."
    
    raka "Puitis."
    nara "Efisien."
    
    raka "Itu bukan arti efisien."
    nara "Semua bisa dipelintir kalau cukup sering dipakai pejabat."
    
    "Raka menahan senyum kecil."
    "Ia tak yakin kapan terakhir kali percakapan terasa seperti duel dan hiburan sekaligus."

    # Scene ini tidak mematikan BGM karena alur ceritanya langsung berlanjut ke perdebatan di Scene 13
    return
