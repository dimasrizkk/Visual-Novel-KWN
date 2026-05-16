label ending_chaos: 

    # DETIK SEBELUM KEHANCURAN 
    scene core_main_alert 
    with flash 

    play music "collapse_build.ogg" 
    play sound "alarm.ogg" 

    system "Pelanggaran kritis." 
    system "Stabilitas jaringan menurun." 
    system "Kegagalan sistem berantai terdeteksi." 

    scene core_lights_flicker #bg blum ada
    with dissolve 

    "Lampu berkedip." 
    "Data mulai tidak sinkron." 
    "Sistem yang selama ini terlihat sempurna… mulai retak." 

    show nara eksplor serius:
        xalign 1.0
        yalign 1.6
        zoom 0.9
    with dissolve
    
    show raka rebel serius:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    show adrian kantor netral: 
        xalign 0.5
        yalign 1.1  
        zoom 0.85
    with dissolve

    nara "Raka… lo yakin?" 

    pause 

    "raka tidak langsung jawab" 

    raka "Mungkin ini satu-satunya cara." 
    nara "Atau satu-satunya cara paling gampang buat hancurin semuanya?" 

    pause 

    "adrian melangkah sedikit" 

    adrian "Akhirnya." 

    pause 

    adrian "Kau berhenti berpura-pura memperbaiki." 
    adrian "Dan memilih… memilih menghancurkan segalanya." 

    raka "Sistem ini sudah tidak bisa diperbaiki." 

    adrian "Kau tepat sekali Raka." 

    pause 

    adrian "Tapi kau sudah tahu konsekuensinya." 
    adrian "Kau memilih untuk tidak memikirkannya." 

    pause 

    nara "Raka, ini masih bisa.." 
    raka "TIDAKK, gua tau dan ini sudah telat." 

    # AKSI — HANCURKAN CORE 
    scene core_destroy #bg blum ada
    with flash 

    show nara eksplor serius:
        xalign 1.0
        yalign 1.6
        zoom 0.9
    
    show raka rebel serius:
        xalign 0.0
        yalign 1.6
        zoom 0.85

    show adrian kantor senyum: 
        xalign 0.5
        yalign 1.1  
        zoom 0.85

    play sound "system_break.ogg" 
    play music "collapse.ogg" 

    "Raka menekan perintah terakhir." 
    "Bukan membuka." 
    "Bukan memperbaiki." 
    "Menghancurkan." 

    pause 

    system "Kesalahan fatal." 
    system "Node pusat gagal." 
    system "Pemadaman total dalam 10 detik." 

    # Implementasi Poin 2: Tensi Visual dengan Guncangan Layar
    countdown "10… 9… 8…" 

    show nara eksplor marah:
        xalign 1.0
        yalign 1.6
        zoom 0.9

    nara "Raka!" 

    countdown "7… 6…" 

    "adrian tetap diam" 
    "menatap" 

    countdown "5… 4…" 

    adrian "Lihat dan saksikan baik-baik Raka." 

    countdown "3… 2…" 

    adrian "Inilah yang kau pilih." 

    countdown "1." 

    # BLACKOUT 
    scene blackout_city 
    with flash 

    # Implementasi Poin 2: Audio mendadak mati untuk kehampaan
    stop music fadeout 1.0
    play sound "power_down.ogg" 

    "Gelap." 
    "Total." 
    "Tanpa transisi." 

    pause 3.0 # Pause diperpanjang untuk efek hampa

    "Untuk pertama kalinya…" 
    "kota berhenti." 

    # KEHENINGAN SEBELUM CHAOS 
    play music "empty_wind.ogg" 

    "Tidak langsung rusuh." 
    "Tidak langsung panik." 
    "Hanya… hening." 

    pause 

    "Karena tidak ada yang tahu harus berbuat apa." 

    # CHAOS DIMULAI 
    scene city_confusion #bg blum ada
    with dissolve 

    play sound "crowd_murmur.ogg" 

    "Lalu suara muncul." 
    "Pertanyaan." 
    "Kebingungan." 
    "Lalu… ketakutan." 

    scene riots #sm kayak city_confusion
    with fade 

    play sound "chaos.ogg" 

    "Dan akhirnya… kekacauan." 
    "Toko dijarah." 
    "Distribusi berhenti." 
    "Obat tidak sampai." 
    "Makanan tidak datang." 
    "Sistem hilang." 
    "Dan tidak ada yang siap hidup tanpa itu." 

    # KONFRONTASI RAKA & NARA 
    scene fire_city #bg blum ada
    with dissolve 

    play music "burning_truth.ogg" 

    show nara eksplor terkejut:
        xalign 1.0
        yalign 1.6
        zoom 0.9
    with dissolve
    
    show raka rebel terkejut:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    nara "Lihatlah." 
    nara "Lihat apa yang lu sudah lakukan." 

    pause 

    "raka melihat sekitar" 

    raka "(Ini… bukan yang gue bayangin)" 

    nara "Lo bilang ini kebebasan?" 
    nara "Ini bukan kebebasan, Raka." 
    nara "Ini… kehancuran." 

    pause 2.0

    raka "Kalau sistemnya tetap ada…" 
    raka "mereka nggak akan pernah punya pilihan." 

    nara "Dan sekarang?" 
    nara "Mereka bahkan tidak punya kesempatan memilih!" 

    pause 

    # ADRIAN — DIALOG TERAKHIR 
    scene core_ruins #sama kayak core_destroy 
    with dissolve 

    show adrian kantor netral: 
        xalign 0.5
        yalign 1.1  
        zoom 0.85
    with dissolve

    "adrian masih berdiri" 
    "di tengah kehancuran" 
    "tenang" 

    adrian "Akhirnya kau mengerti." 

    pause 

    show nara eksplor marah:
        xalign 1.0
        yalign 1.6
        zoom 0.9
    with dissolve
    
    show raka rebel marah:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    "raka menatap" 

    raka "Ngga, Ini salah." 

    adrian "Tidak." 
    adrian "Kau yang salah… inilah konsekuensinya." 

    pause 

    adrian "Kau menghilangkan arah." 
    adrian "Dan manusia tanpa arah…" 
    adrian "tidaklah menjadi bebas." 
    adrian "Mereka akan saling menghancurkan." 

    pause 

    nara "Lu sengajakan membuat sistem seperti ini!" 

    adrian "Aku menjalankan system MIRROR…" 
    adrian "karena aku tahu seperti apa dunia tanpa sistem." 

    pause 

    "adrian menatap Raka" 

    adrian "Dan sekarang…" 
    adrian "kau telah menunjukkannya ke mereka Raka." 

    pause 

    "adrian sedikit tersenyum" 

    adrian "Terima kasih Raka." 

    # TITIK TERENDAH 
    scene burning_streets #sm kaya fire_city
    with fade 

    "Api menyebar." 
    "Tidak ada yang memadamkan." 
    "Tidak ada yang mengatur." 
    "Tidak ada yang tahu harus mulai dari mana." 

    pause 

    "raka berdiri" 
    "diam" 
    "tidak bergerak" 

    raka "(Aku… menang?)"

    pause 2.0

    raka "(Atau… Aku cuma ngerusak semuanya?)"

    # PENUTUP 
    scene distant_city_ruin 
    with fade 

    play music "ashes.ogg" 

    "Sistem runtuh." 
    "Pemerintah runtuh." 
    "Kontrol hilang." 

    pause 

    "Dan dari abu itu…" 
    "tidak ada yang langsung tumbuh." 

    pause 

    "Hanya sisa." 
    "Dan pertanyaan…" 
    "apakah kebebasan selalu layak dibayar semahal ini." 

    scene black 
    with fade 

    "END — ASHES OF FREEDOM" 

    return