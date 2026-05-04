label scene11:
    scene alley_dark with fade
    
    # Memutar BGM gang sunyi
    play music quiet_alley fadein 2.0
    
    "Gang itu lebih sempit dari yang terlihat dari luar."
    "Dinding-dinding lembap dipenuhi pipa tua dan kabel yang tak lagi terhubung ke pusat kota."
    "Tidak ada kamera pengawas."
    "Tidak ada layar iklan."
    "Tidak ada suara sistem yang menebak apa yang harus ia rasakan."
    "Hanya langkah kaki dan bunyi logam dipukul perlahan dari kejauhan."
    
    # SFX ketukan logam dari kejauhan
    play sound metal_tap

    scene ruang_sisa_outside with dissolve
    
    "Di ujung lorong berdiri bangunan kecil dengan pintu kayu kusam."
    "Lampu kuning redup menggantung di atas papan nama yang nyaris pudar."
    "\"RUANG SISA\""
    "Cat hurufnya mengelupas. Namun papan itu masih bertahan lebih lama dari banyak gedung baru."
    
    raka "Tempat ini?"
    
    system "Teknisi independen ditemukan."
    system "Peringatan: kualitas layanan tidak terverifikasi."
    
    raka "Seperti seluruh masa lalu."
    
    # SFX bel pintu toko tua berbunyi
    play sound door_bell_old
    
    # Menghentikan BGM gang sunyi sebelum masuk ke dalam
    stop music fadeout 1.5

    scene ruang_sisa_inside with fade
    
    # BGM berubah menjadi hangat saat masuk ke bengkel
    play music workshop_warm fadein 2.0
    
    "Udara di dalam berbeda."
    "Hangat."
    "Bukan karena mesin pendingin otomatis."
    "Karena ruang ini dipenuhi benda yang pernah disentuh manusia."
    "Rak-rak kayu berisi radio tua, kipas angin, mesin jahit, sepatu kulit, jam dinding, lampu meja, bahkan ketel penyok yang dipoles bersih."
    "Di meja kerja, percikan kecil muncul dari solder."
    
    show nara work at center with dissolve
    
    "Seorang perempuan menunduk, fokus memperbaiki papan sirkuit tanpa menoleh sedikit pun."
    "Tangannya cepat. Gerakannya tenang."
    "Seolah dunia di luar tak cukup penting untuk mengganggu ritmenya."
    
    nara "Kalau mau lihat-lihat, jangan sentuh rak kiri."
    
    raka "...Kau bahkan belum lihat siapa yang datang."
    
    nara "Orang yang berdiri ragu di pintu biasanya salah satu dari tiga hal."
    nara "Kurir."
    nara "Petugas."
    nara "Atau orang yang belum terbiasa masuk tempat tanpa kaca."
    
    "Ia akhirnya menoleh."
    
    show nara neutral at center
    
    "Tatapannya tajam, tapi tidak sibuk menghakimi."
    "Itu justru lebih membuat Raka tak nyaman."
    
    nara "Ternyata jenis ketiga."
    
    raka "Perangkatku rusak."
    
    nara "Selamat."
    
    raka "Apa?"
    
    nara "Berarti kau masih punya kesempatan merasakan dunia tanpa bantuan benda itu."
    
    raka "Aku datang untuk diperbaiki, bukan diceramahi."
    
    nara "Kalau begitu taruh di meja."

    # Blok interaktif pilihan respons Raka
    menu:
        "Apa reaksi pertama Raka terhadap Ruang Sisa?"

        "Tempat kumuh.":
            $ ambition += 1
            raka "Jujur saja, aku tak menyangka masih ada tempat seperti ini di kota."
            nara "Banyak hal bertahan, tanpa disangka-sangka."
            "Raka tetap berdiri, enggan menyentuh apa pun."

        "Menarik... semuanya diperbaiki?":
            $ loyalty += 1
            raka "Semua ini masih bisa dipakai lagi?"
            nara "Sebagian benda rusak. Sebagian hanya ditinggalkan terlalu cepat."
            "Untuk pertama kalinya, rasa penasaran menang atas gengsi."

        "Kenapa tempat ini belum ditutup?":
            $ awareness += 1
            raka "Zona seperti ini harusnya sudah dibersihkan."
            nara "Kadang penguasa butuh satu sudut kotor agar pusat kota tampak suci."
            "Jawaban itu terlalu cepat untuk dianggap kebetulan."

    nara "Sekarang, perangkatmu."
    
    "Raka menyerahkan device-nya."
    
    "Nara memeriksa."
    nara "Model baru. Sengaja dibuat sulit dibuka."
    
    raka "Bisa diperbaiki?"
    nara "Bisa."
    
    raka "Berapa lama?"
    nara "Tergantung."
    
    raka "Tergantung apa?"
    nara "Tergantung kau bisa diam atau ga?"

    # Kembali ke script utama (script.rpy)
    return