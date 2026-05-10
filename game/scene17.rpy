label scene17:
    scene mirror_office_morning with fade
    
    # Memutar BGM bernuansa dingin dan analitis
    play music cold_data fadein 2.0 #pake 424631__hobotrails__realizing-the-realization.mp3
    
    "Pagi di Divisi MIRROR selalu datang tanpa matahari."
    "Lampu putih menyala lebih dulu daripada langit."
    "Deretan meja kerja sudah penuh oleh wajah-wajah yang menatap layar seperti sedang beribadah pada sesuatu yang tak pernah menjawab."

    scene raka_desk with dissolve
    
    show raka formal netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka duduk di tempatnya."
    "Perangkat di tangannya kembali normal."
    "Kalender kerja kembali padat."
    "Notifikasi kembali tak kenal privasi."
    
    system "Selamat pagi, Raka Pradana."
    # Menggunakan %% untuk escaping karakter persentase
    system "Produktivitas Anda turun 4%% sejak kemarin."
    system "Disarankan mengurangi distraksi non-esensial."
    
    raka "...Non-esensial."
    
    "Ia tidak perlu bertanya apa yang dimaksud."
    "Di kota ini, rasa penasaran sering dianggap pemborosan."
    
    worker1 "Bro, kampanye sepatu impor lo gila sih."
    worker2 "Naik 31%% seminggu."
    worker1 "Kapan traktir?"

    show raka formal marah:
        xalign 0.5
        yalign 1.1
        zoom 0.4
    
    raka "Kalau kalian berhenti ngomong."
    
    worker2 "Wah, galak."
    worker1 "Pantes disayang menteri."
    
    "Mereka tertawa."

    show raka formal senyum:
        xalign 0.7
        yalign 1.1
        zoom 0.4

    "Raka ikut tersenyum tipis."
    "Tubuhnya masih hafal cara menyesuaikan diri."

    scene monitor_dashboard with dissolve
    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve
    
    "Layar utama menampilkan dashboard kota."
    "Angka bergerak. Grafik naik. Warna hijau mendominasi."
    
    system "Laporan Harian Nawasena"
    system "Konsumsi Rumah Tangga: +18%%"
    system "Kepatuhan Pembelian Otomatis: +26%%"
    system "Retensi Brand Impor: +34%%"
    system "Kepuasan Umum: Stabil"
    
    "Stabil."
    "Kata favorit birokrasi."
    "Artinya baik."
    "Atau disembunyikan cukup rapi."
    
    # SFX Suara ketikan keyboard
    play sound keyboard_click
    
    "Raka membuka tab yang jarang disentuh pegawai lain."
    
    system "Akses Internal - Psikometri Populasi"
    
    raka "..."
    
    "Grafik baru muncul."
    
    system "Rasa Keterhubungan Sosial: -21%%"
    system "Makna Kerja Personal: -17%%"
    system "Optimisme Jangka Panjang: -14%%"
    system "Kesepian Perkotaan: +39%%"
    system "Ketergantungan Konsumsi Emosional: +42%%"

    show raka formal terkejut: 
        xalign 0.0
        yalign 1.6
        zoom 0.85

    raka "...Apa?"
    
    "Ia memperbesar data."
    "Semakin konsumsi naik, semakin banyak warga merasa kosong."
    "Semakin nyaman layanan, semakin rendah rasa memiliki."
    "Semakin efisien kota, semakin rapuh orang-orang di dalamnya."
    
    raka "Ini nggak mungkin nggak ada yang lihat."
    
    show senior analyst: 
        xalign 0.9
        yalign 1.3
        zoom 0.85
    with dissolve

    senior_analyst "Ada yang lihat."
    senior_analyst "Cuma nggak semua orang dibayar untuk peduli."

    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    raka "Kenapa data beginian disimpan kalau nggak dipakai?"
    
    senior_analyst "Dipakai."
    
    raka "Buat apa?"
    
    senior_analyst "Supaya tahu titik lemah berikutnya."
    
    "Pria itu menyesap kopi dingin."
    
    senior_analyst "Orang kesepian lebih gampang diarahkan."
    senior_analyst "Orang yang kehilangan makna lebih gampang beli identitas."
    senior_analyst "Orang yang capek mikir lebih suka dipilihkan."
    
    "Raka menatap layar."
    
    raka "Dan kita nyebut ini pelayanan."
    
    senior_analyst "Kita nyebut ini pekerjaan."
    
    "Pria itu pergi."
    "Meninggalkan kalimat yang terlalu tenang untuk dilupakan."    
    "Kursor berkedip di atas file."
    "Untuk pertama kalinya, data di hadapannya tidak terasa seperti angka."
    "Tapi korban."

    # Blok interaktif penentuan poin
    menu:
        "Apa yang dilakukan Raka?"

        "Tutup file.":
            $ ambition += 1
            raka "..."
            "Ia menutup jendela data."
            "Beberapa kebenaran tidak perlu dibeberkan."
            "Kebebasan hanya akan mendatangkan kehancuran."

        "Simpan diam-diam.":
            $ awareness += 1
            "Ia menyalin file ke folder tersembunyi."
            "Kalau sistem berbohong, bukti adalah bentuk napas."

        "Kirim ke Nara.":
            $ loyalty += 1
            "Ia membuka kontak baru yang tadi malam ia simpan tanpa alasan jelas."
            "\"Ruang Sisa.\""
            "File terkirim."
            "Jari bergerak lebih cepat dari logika."

    scene raka_desk with dissolve
    show raka formal netral: 
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve    

    # SFX Notifikasi masuk yang mengejutkan
    play sound message_ping
    
    system "Undangan rapat evaluasi pukul 20.00."
    system "Pengirim: Kantor Menteri."
    
    raka "...."
    
    "Ia tidak tahu apakah itu penghargaan."
    "Atau panggilan."

    # Menghentikan BGM perlahan sebelum kembali ke file utama
    stop music fadeout 2.0

    return
