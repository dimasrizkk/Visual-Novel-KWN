label scene13:
    scene workbench_tension with dissolve #bg blum ada
    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    show nara bengkel serius:
        xalign 0.95
        yalign 1.6
        zoom 0.85
    
    # Memutar BGM debat yang tegang namun bertempo rendah
    play music debate_low fadein 2.0 volume 0.5
    
    # SFX suara memasang obeng
    play sound screwdriver_turn
    
    "Nara memasang obeng, lalu bicara tanpa melihatnya."

    show nara bengkel netral:
        xalign 0.95
        yalign 1.6
        zoom 0.85
    
    nara "Kau kerja di pusat kota."
    raka "Keliatannya?"
    nara "Sepatu bersih, pundak tegang, dan cara melihat ruangan seperti sedang menilai harga."
    
    raka "Aku menilai kualitas."
    nara "Itu juga penyakit kota."
    
    "Nara berhenti bekerja, menatap Raka."
    
    nara "Kenapa kota ini diajari membuang sebelum memahami?"

    # Blok interaktif argumen Raka
    menu:
        "Jawaban Raka:"

        "Karena efisien.":
            $ ambition += 1
            raka "Karena waktu berharga. Lebih cepat untuk mengganti daripada memperbaiki."
            nara "Cepat untuk siapa?"
            nara "Murah untuk siapa?"
            nara "Untung untuk siapa?"
            "Tiga pertanyaan. Tak satu pun nyaman dijawab."

        "Karena orang dipaksa begitu.":
            $ loyalty += 1
            raka "Mungkin... karena mereka terus diberi tahu itu satu-satunya cara."
            "Nara menatap lebih lama."
            nara "Setidaknya kau masih bisa melihat sesuatu."

        "Karena ada yang diuntungkan.":
            $ awareness += 1
            raka "Karena kebiasaan beli lebih mudah dikendalikan daripada kebiasaan membuat."
            nara "Nah."
            nara "Sekarang kau terdengar seperti orang yang tahu terlalu banyak."

    nara "Dulu ayahku membuat mesin produksi kecil."
    raka "Ayahmu teknisi?"
    
    nara "Insinyur."
    nara "Ia merancang alat murah supaya bengkel kecil bisa produksi lebih cepat."
    nara "Bukan menggantikan manusia. Tapi membantu mereka."
    
    raka "Lalu?"
    
    nara "Negara mengambil desainnya."

    show raka formal terkejut: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    raka "Diambil?"
    
    nara "\"Dipinjam permanen\"."
    nara "Dipatenkan atas nama kemajuan nasional."
    
    raka "Dan ayahmu?"
    
    "Nara diam beberapa detik."
    nara "Menghilang."
    
    "Ruang itu mendadak lebih sempit."
    
    raka "Maaf."

    show nara bengkel marah:
        xalign 0.95
        yalign 1.6
        zoom 0.85

    nara "Jangan."
    nara "Kata itu tak ada arti kalau tidak mengubah apa pun."

    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    show nara bengkel netral:
        xalign 0.95
        yalign 1.6
        zoom 0.85

    raka "Kau selalu bicara seperti menuduh?"
    nara "Kau selalu bicara seperti membela sesuatu yang belum tentu layak dibela?"
    
    raka "Sistem lama punya banyak cacat. Tapi lihat kota sekarang."
    raka "Kereta tepat waktu."
    raka "Distribusi lancar."
    raka "Orang tidak antre berjam-jam."
    
    nara "Dan?"
    
    raka "Dan itu berarti sesuatu."
    nara "Benar."
    nara "Kandang yang dibersihkan tetap kandang."
    
    raka "Kau lebih suka kekacauan lama?"
    nara "Aku lebih suka pilihan yang tidak dimonopoli."
    
    "Nara berjalan ke rak, mengambil lampu meja tua."
    
    # SFX suara meletakkan barang usang berbahan logam/kayu ke atas meja
    play sound lamp_place_table #blm ada soundnya, jadi pake 554737__dynamique__moving-small-box
    
    nara "Lihat ini."
    nara "Dulu dibuat di blok selatan. Pabrik keluarga."
    nara "Tahan dua puluh tahun."
    
    "Nara menunjuk lampu modern di sudut."
    
    nara "Yang itu impor. Murah. Cantik."
    nara "Rusak dalam delapan bulan."
    
    raka "Kalau begitu orang tinggal beli lagi."
    
    nara "Tepat."
    nara "Dan mereka akan terus beli lagi."
    nara "Bukan karena butuh."
    nara "Karena diajari tak bisa selain membeli."
    
    "Raka ingin membantah."
    "Namun perangkat rusak di meja itu sedang menjadi saksi terburuk baginya."

    # Musik tidak dihentikan di sini karena alur langsung menyambung ke Scene 14 yang lebih intim
    return
