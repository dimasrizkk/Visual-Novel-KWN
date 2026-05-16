label scene_21f_penutup_babak_2:

    # Menampilkan lanskap kota malam hari secara luas
    scene city_wide_night with fade 
    
    # Memutar BGM bertema akibat/pasca-kejadian dengan transisi lambat
    play music "aftermath.ogg" fadein 3.0 

    "Malam itu, sesuatu yang berharga telah hilang dari Nawasena." 
    "Tidak semua orang sadar. Tidak semua orang peduli." 
    "Tapi bagi mereka yang tahu... ini bukanlah sebuah akhir." 
    
    "Ini adalah sebuah peringatan." 
    "Bahwa sistem tidak hanya mengarahkan jalannya kota, ia juga menghapus apa pun yang dianggap mengganggu jalannya." 

    # Beralih ke sudut pandang dekat dan gelap pada Raka
    scene raka_close_dark with dissolve 

    # Menampilkan Raka di posisi tengah, mengekspresikan beban batin yang berat
    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Dan di tengah semua badai yang tidak terlihat itu, Raka berdiri diam." 
    "Bukan lagi sebagai pengamat yang pasif. Bukan lagi sekadar sebagai pekerja yang patuh." 
    "Tapi sebagai seseorang yang akhirnya dipaksa harus memilih..." 
    "apa yang benar-benar layak untuk dipertahankan." 

    # Menghapus karakter secara halus sebelum layar gelap total
    hide Casual_Sedih with dissolve

    # Transisi ke layar hitam (End of Chapter)
    scene black with dissolve

    # Menghentikan BGM secara perlahan untuk menutup babak secara sempurna
    stop music fadeout 3.0

    # Akhir dari Babak 2
    return
