label scene10:
    # Memutar SFX kerumunan dari kejauhan dan BGM upacara
    play ambient crowd_far.mp3 fadein 1.0 volume 0.5
    #play sound crowd_cheer fadein 2.0 volume 0.5
    
    scene distribution_square with fade
    
    play music public_ceremony fadein 2.0
    
    "Keramaian terdengar dari alun-alun distribusi."
    "Ratusan warga berkumpul di depan panggung digital."
    "Drone kamera melayang seperti serangga yang lapar."
    
    system "Upacara pembukaan Pusat Arus Barang Nasional akan dimulai."
    
    "Raka berhenti."
    "Di layar raksasa, wajah Adrian muncul setinggi gedung."
    
    show adrian formal at center with dissolve
    
    kerumunan "Hidup Menteri Adrian!"
    kerumunan "Nawasena maju!"
    
    adrian "Warga Nawasena."
    adrian "Dua puluh tahun lalu, kota ini dikenal karena antrean panjang, barang rusak, dan janji yang tak pernah tiba."
    adrian "Hari ini, kebutuhan kalian sampai sebelum kalian memintanya."
    
    # SFX Tepuk tangan
    play sound applause volume 0.5
    "..."
    
    adrian "Dulu, kualitas ditentukan siapa kenal siapa."
    adrian "Hari ini, standar ditentukan data."
    adrian "Dulu, rakyat dipaksa menunggu."
    adrian "Hari ini, dunia menunggu kita."
    
    "Kata-katanya presisi."
    "Tidak berlebihan."
    "Justru itu yang berbahaya."
    
    adrian "Sebagian orang berkata kita kehilangan identitas."
    adrian "Aku bertanya: identitas yang mana?"
    adrian "Identitas yang membuat barang mahal dan gaji murah?"
    adrian "Identitas yang membiarkan anak-anak mewarisi kegagalan?"
    adrian "Jika masa lalu tak mampu memberi makan kalian, mengapa kalian menyembahnya?"
    
    play sound crowd_cheer
    "Kerumunan bersorak."
    
    "Raka ikut diam."
    "Ia tahu retorika bagus saat mendengarnya."
    "Ia juga tahu retorika bagus bisa lebih mematikan dari kebohongan kasar."
    
    adrian "Mulai hari ini, seluruh jalur impor strategis dikelola langsung negara."
    adrian "Tidak ada tengkulak."
    adrian "Tidak ada hambatan."
    adrian "Tidak ada kekacauan."
    adrian "Setiap barang yang masuk akan memperkuat kestabilan kita."
    
    "Di balik kalimat itu, Raka mendengar versi lain yang tak diucapkan."
    "\"Setiap barang yang masuk melewati tangan kami.\""
    
    adrian "Sebagian dari kalian menyebut ini kontrol."
    adrian "Aku menyebutnya tanggung jawab."
    
    play sound applause_loud
    "Tepuk tangan membesar."

    scene raka_crowd with dissolve
    
    "Seorang anak kecil menarik baju ibunya."
    
    anak "Bu, dulu kita bikin barang sendiri ya?"
    
    ibu "Ssst."
    
    anak "Kenapa sekarang beli semua?"
    
    ibu "...Karena lebih gampang."
    
    anak "Kalau gampang terus, kita bisa apa?"
    
    "Ibunya tak menjawab."
    "Tak ada menu pilihan untuk pertanyaan seperti itu."

    scene adrian_stage_close with dissolve
    
    adrian "Kemajuan selalu menuntut sesuatu untuk ditinggalkan."
    adrian "Pastikan yang kalian tinggalkan hanyalah beban."
    
    play sound crowd_cheer
    "Sorak-sorai kembali pecah."
    
    "Raka melihat wajah-wajah di sekelilingnya."
    "Mereka tampak percaya."
    "Sebagian karena setuju."
    "Sebagian karena lelah berharap pada hal lain."
    
    # Suara pidato dan kerumunan diinterupsi oleh perangkat Raka
    play sound device_glitch_soft
    
    "Perangkat rusaknya kembali berkedip."
    
    system "Teknisi independen: 400 meter."
    system "Belok kiri menuju gang servis."

    scene alley_entrance_far with dissolve
    
    "Di sisi alun-alun yang gemerlap, sebuah gang sempit terbuka di antara dua gedung baru."
    "Gelap. Basah. Nyaris tak terlihat."
    "Seolah kota sengaja menaruh masa lalunya di tempat yang tak difoto siapa pun."
    
    "Raka menatap panggung, lalu gang itu."
    
    raka "..."
    
    "Di satu sisi berdiri lelaki yang hampir meyakinkan seluruh kota."
    "Di sisi lain, lorong kecil menuju alamat yang sistem sendiri sebut tak signifikan."
    
    "Raka melangkah ke arah gang."

    # Menghentikan musik dan suara kerumunan perlahan saat Raka menjauh
    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene alley_dark with fade
    
    "Bau oli, hujan, dan besi tua menggantikan parfum kota."
    "Untuk pertama kalinya hari itu, suara iklan tak terdengar."
    "Hanya suara tetesan air."
    "Dan sesuatu yang belum ia sadari: rasa ingin tahu."

    scene black with fade
    
    # Memberikan jeda sejenak sebelum masuk ke Scene 11
    pause 1.0

    return