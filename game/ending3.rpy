label ending_kill: 

    scene core_main with flash 

    # SFX Tembakan dan pergantian BGM klimaks yang kelam
    play sound "gunshot.ogg" 
    play music "dark_rise.ogg" fadein 1.0 

    "Satu tembakan menggema keras memutus segalanya." 

    pause 1.0 

    scene adrian_fall with dissolve 

    "Adrian jatuh." 
    "Tanpa kata terakhir. Tanpa perlawanan." 
    "Seolah… kematiannya pun bukan bagian penting yang bisa menghentikan sistem ini." 

    pause 1.0 

    ## ── REAKSI NARA ──
    scene core_silence with dissolve 

    # Menampilkan Nara dan Raka berdampingan di titik konfrontasi akhir
    show Eksplor_Shocked:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    
    show Casual_HoldingGun:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Lu…" 

    pause 2.0 

    # Menggerakkan Nara mundur sedikit secara visual
    show Eksplor_Shocked:
        xalign 0.90
        yalign 1.1
        zoom 0.85
    with ease

    nara "Lu baru aja—" 

    raka "..." 

    show Eksplor_Shocked:
        xalign 0.90
        yalign 1.1
        zoom 0.85

    nara "ITU BUKAN SOLUSI RAKA!!" 
    nara "Itu... awal yang buruk." 

    pause 1.0 

    nara "Lu pikir ini selesai? Atau lu cuma pengen ngerasa punya kontrol?" 

    pause 1.0 

    raka "(dalam hati) Kontrol??" 
    raka "(dalam hati) Ini tujuan kita kan?" 

    ## ── SISTEM TETAP BERJALAN ──
    scene system_active with dissolve 

    "Layar tetap menyala rapi. Data tetap mengalir deras. Narasi baru tetap diproduksi otomatis." 

    pause 1.0 

    system "Node pusat aktif." 
    system "Protokol kepemimpinan ulang berjalan." 

    pause 1.0 

    # Raka kembali dimunculkan sendiri di depan layar raksasa
    show Casual_HoldingGun:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "…Apa?" 

    "Sistem tidak berhenti. Karena sistem ini dari awal tidak pernah bergantung pada nyawa satu orang." 

    ## ── NARA MENINGGALKAN RAKA ──
    show Eksplor_Shocked:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Selamat atas kontrol barunya, Raka." 

    pause 1.0 

    nara "Sekarang lu nggak ada bedanya dengan dia." 

    pause 1.0 

    nara "Bedanya hanya satu… dia tahu dia monster." 

    pause 1.0 

    nara "Sedangkan lu, berpura-pura suci." 

    hide Eksplor_Shocked with dissolve
    scene nara_exit with fade 

    "Nara pergi melangkah menjauh." 
    "Dan untuk pertama kalinya… Raka tidak melakukan apa pun untuk menghentikannya." 

    ## ── TRANSISI — PEMERINTAH MASUK ──
    scene core_breach with flash 

    # SFX Suara pintu didobrak paksa
    play sound "door_break.ogg" 

    guard "Area diamankan!" 

    "Unit penertiban masuk dengan cepat, efisien, dan tanpa emosi." 

    pause 1.0 

    "Guard menatap tubuh Adrian yang tergeletak." 

    guard "...Target eliminasi." 

    pause 1.0 

    "Guard kemudian berbalik menatap Raka yang masih memegang senjata." 

    guard "...Subjek teridentifikasi." 

    pause 1.0 

    # Suara pejabat misterius masuk dari luar layar
    voice "Biarkan saja dia." 

    scene official_shadow with dissolve 

    "Seseorang berbicara dari balik kegelapan lorong. Bukan tentara, bukan operator kementerian. Seseorang dari hierarki yang jauh lebih tinggi." 

    voice "Dia yang paling mengerti sistem ini sekarang." 

    pause 1.0 

    voice "Dan sekarang… dia satu-satunya pilihan yang tersisa." 

    # Raka mematung terpaku
    show Casual_HoldingGun:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    raka "..." 

    raka "(dalam hati) Ini… bukan yang aku mau." 
    raka "(dalam hati) Atau… mungkin ini yang dari awal diam-diam aku inginkan?" 

    ## ── TRANSISI WAKTU ──
    scene city_ordered_again with fade 

    # Mengubah BGM ke tema kontrol yang dingin dan mutlak
    play music "cold_control.ogg" fadein 3.0 

    "Beberapa waktu kemudian." 
    "Kota kembali stabil. Lebih cepat dari yang seharusnya, lebih rapi dari sebelumnya. Dan terasa jauh lebih… kosong." 

    ## ── RAKA DI RUANGAN ADRIAN ──
    scene KANTOR ELITE_ RUANG ADRIAN with dissolve 

    "Ruangan yang dulu amat dia benci. Sekarang… sepenuhnya menjadi miliknya." 

    # Raka muncul di tengah menggunakan pakaian jas menteri (Formal_Menteri)
    show Formal_Menteri:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Pemandangan kota yang sama. Layar monitor yang sama. Sistem kendali yang sama." 

    pause 1.0 

    system "Kurasi narasi harian siap." 
    system "Segmentasi emosi warga selesai." 
    system "Rekomendasi distribusi Impor siap dijalankan." 

    pause 1.0 

    # SFX Suara kursi menteri diduduki
    play sound "chair_sit.ogg" 

    "Raka duduk perlahan di kursi kebesaran milik Adrian." 

    pause 2.0 

    raka "(dalam hati) Dulu gue pikir… ini kekuasaan." 

    pause 1.0 

    raka "(dalam hati) Sekarang… gue tahu ini hanya beban." 

    ## ── MOMEN IRONI TERAKHIR ──
    scene screen_close with dissolve 

    "Sebuah draf narasi baru terbuka di hadapannya." 

    text_on_screen "Produk lokal tidak relevan dengan kebutuhan modern." 

    pause 1.0 

    "Raka menatap layar tersebut untuk waktu yang sangat lama." 

    raka "(dalam hati) Ini mungkin salah.” 

    pause 1.0 

    raka "(dalam hati) Tapi…" 

    pause 2.0 

    raka "(dalam hati) ...kalau gue nggak klik, orang lain yang akan menggantikan gue di sini." 

    pause 1.0 

    # SFX Suara klik tetikus penentu narasi kota
    play sound "click.ogg" 

    "Raka mengklik 'Confirm'." 

    ## ── FINAL SHOT ──
    scene city_screens with fade 

    "Iklan baru bermunculan di seluruh sudut kota Nawasena. Lebih halus, lebih meyakinkan, dan jauh lebih… efektif." 

    pause 1.0 

    scene raka_shadow with dissolve 

    "Dan di balik semua ilusi itu… ada seseorang yang dulu pernah bertaruh nyawa ingin menghentikan semuanya." 

    pause 1.0 

    "Kini berdiri tegak di puncak kekuasaan, memastikan semuanya tetap berjalan sempurna." 

    scene black with fade 

    # Teks penutup rute cerita
    "END — BECOMING THE MIRROR" 

    # Menghentikan seluruh audio saat game berakhir
    stop music fadeout 3.0
    stop sound fadeout 1.0

    return
