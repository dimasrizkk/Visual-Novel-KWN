label scene8:
    # Memutar BGM kesibukan kota yang mekanis
    play music city_hum fadein 2.0

    scene mirror_tower_evening with fade
    
    "Sore turun perlahan di Nawasena."
    "Di ketinggian, cahaya matahari terakhir memantul pada dinding-dinding kaca, membuat seluruh kota tampak seperti istana yang dibangun dari cermin."
    "Dari jauh, semuanya terlihat sempurna."
    "Dari dekat, semuanya bekerja terlalu keras agar terlihat sempurna."

    scene elevator_inside with dissolve
    
    show raka formal tired:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve
    
    play sound lift_tertutup fadein 1.5
    "Pintu lift menutup."
    "Untuk pertama kalinya hari itu, tak ada yang meminta keputusan darinya."
    
    raka "...Hah."
    
    system "Selamat sore, Raka Pradana."
    system "Tingkat stres Anda meningkat 12%%."
    system "Disarankan membeli paket relaksasi premium."
    
    raka "Bahkan lelah pun dijual."
    
    system "Maaf, saya tidak memahami nada sarkasme."
    
    raka "Tentu saja."
    
    "Di kota ini, mesin mengenali detak jantung."
    "Tapi belum belajar privasi."

    play sound langkah_kaki_banyak fadein 2.0
    scene lobby_future with dissolve
    
    "Lobi gedung dipenuhi orang-orang berpakaian rapi yang berjalan cepat dengan wajah kosong."
    "Semua terlihat sibuk."
    "Tak satu pun terlihat hadir."
    
    worker1 "Meeting besok dimajuin."
    worker2 "Aku udah dipesenin makan malam sama sistem."
    worker3 "Saham impor naik lagi."
    worker1 "Bagus. Negara makin sehat."
    
    "Di Nawasena, kesehatan negara sering terdengar seperti kesehatan neraca."

    scene street_modern with dissolve
    
    "Pintu otomatis terbuka."
    "Udara kota menyambutnya dengan aroma logam basah dan parfum sintetis dari billboard jalanan."

    
    system "Raka, berdasarkan pola langkahmu, kau tampak letih."
    system "Kopi spesial tersedia 40 meter di depan."
    system "Gunakan poin loyalitasmu."
    
    raka "Tidak."
    
    system "Penolakan tercatat."

    show raka formal marah: 
        xalign 0.5
        yalign 1.1
        zoom 0.43
    with dissolve
    
    raka "Aku bicara sendiri sekarang."
    
    "Ia mulai berjalan."
    
    # SFX Sistem mulai bermasalah
    play sound device_glitch
    
    system "..."
    system "..."
    system "Koneksi terputus."
    
    
    "Langkah Raka terhenti."

    show raka formal terkejut:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "Hm?"
    
    # SFX Error utama
    play sound [device_error_1, device_error_2]
    
    "Perangkat di pergelangan tangannya berkedip merah."
    
    system "ERROR 17."
    system "Sinkronisasi identitas gagal."
    system "Layanan publik dibatasi."
    
    raka "...Jangan bercanda."
    
    "Ia mencoba membuka dompet digital."
    system "Akses ditolak."
    
    "Mencoba memanggil kendaraan."
    system "Akses ditolak."
    
    "Mencoba membuka pintu stasiun."
    system "Akses ditolak."

    show raka formal marah: 
        xalign 0.5
        yalign 1.1
        zoom 0.43
    with dissolve

    raka "Serius?"
    
    "Untuk sesaat, seorang pria dengan gaji tinggi dan akses luas berubah menjadi seseorang yang tak bisa membeli air."
    "Begitu cepat harga diri modern runtuh ketika baterai padam."

    scene roadside_people with dissolve
    
    "Orang-orang di sekitarnya melintas tanpa menoleh."
    "Sebagian terlalu sibuk."
    "Sebagian terlalu terbiasa."
    "Sebagian takut jika masalah orang lain menular pada skornya."
    
    raka "...Hebat."
    raka "Kota penuh koneksi."
    raka "Tak ada satu pun hubungan."
    
    # SFX Pesan darurat masuk
    play sound message_ping
    
    system "Alternatif layanan tersedia."
    system "Pusat perbaikan resmi penuh hingga 3 hari."
    system "Teknisi independen terdekat ditemukan."
    
    "Sebuah alamat muncul."
    "Zona Tua. Sektor Pinggiran."

    show raka formal netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "Masih ada tempat seperti itu?"
    
    system "Catatan: area tidak direkomendasikan."
    system "Nilai keamanan rendah."
    system "Nilai estetika rendah."
    system "Nilai ekonomi tidak signifikan."
    
    raka "Cocok."

    # Menghentikan lagu untuk mempertegas Raka yang kini "terputus" dari sistem kota
    stop music fadeout 2.0

    return
