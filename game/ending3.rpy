label ending_kill: 

    scene core_main 
    with flash 

    play sound "gunshot.ogg" 
    play music "dark_rise.ogg" 

    "Satu tembakan." 

    pause 

    scene adrian_fall 
    with dissolve 

    "Adrian jatuh." 
    "Tanpa kata terakhir." 
    "Tanpa perlawanan." 
    "Seolah… itu bukan bagian penting dari sistem ini." 

    pause 

    # REAKSI NARA 
    scene core_silence 
    with dissolve 

    show nara shocked 
    show raka holding_gun 

    nara "Lu…" 

    pause 2.0 # pause panjang

    "nara mundur sedikit" 

    nara "Lu baru aja—" 

    "raka tidak menjawab" 

    nara "ITU BUKAN SOLUSI RAKA!!" 
    nara "Itu.. awal yang buruk." 

    pause 

    "nara menatap Raka dengan dingin" 

    nara "Lu pikir ini selesai?" 
    nara "Atau lu cuma pengen ngerasa punya kontrol?" 

    pause 

    raka (dalam hati) "Kontrol??" 
    raka (dalam hati) "Ini tujuan kitakan?" 

    # SISTEM TETAP BERJALAN 
    scene system_active 
    with dissolve 

    "Layar tetap menyala." 
    "Data tetap mengalir." 
    "Narasi tetap diproduksi." 

    pause 

    system "Node pusat aktif." 
    system "Protokol kepemimpinan ulang berjalan." 

    pause 

    "raka melihat layar" 

    raka "…Apa?" 

    "Sistem tidak berhenti." 
    "Karena sistem tidak pernah bergantung pada satu orang." 

    # NARA MENINGGALKAN RAKA 
    "nara menatap terakhir kali" 

    nara "Selamat atas control barunya Raka." 

    pause 

    nara "Sekarang lu ga ada bedanya dengan dia." 

    pause 

    "nara berbalik" 

    nara "Bedanya hanya satu…" 
    nara "dia tahu dia monster." 

    pause 

    nara "Sedangkan lu, berpura-pura suci." 

    scene nara_exit 
    with fade 

    "Nara pergi." 
    "Dan untuk pertama kalinya…" 
    "Raka tidak menghentikannya." 

    # TRANSISI — PEMERINTAH MASUK 
    scene core_breach 
    with flash 

    play sound "door_break.ogg" 

    guard "Area diamankan!" 

    "Unit masuk." 
    "Cepat." 
    "Efisien." 
    "Tanpa emosi." 

    pause 

    "guard melihat Adrian" 

    guard "...Target eliminasi." 

    pause 

    "guard melihat Raka" 

    guard "...Subjek teridentifikasi." 

    pause 

    # MASUK PEJABAT / SISTEM 
    voice "Biarkan saja dia." 

    scene official_shadow 
    with dissolve 

    "Seseorang berbicara." 
    "Bukan tentara." 
    "Bukan operator." 
    "Lebih tinggi." 

    voice "Dia yang paling mengerti sistem ini sekarang." 

    pause 

    voice "Dan sekarang…" 
    voice "dia satu-satunya yang tersisa." 

    "raka diam" 

    raka (dalam hati) "Ini… bukan yang aku mau." 
    raka (dalam hati) "Atau… mungkin ini yang dari awal aku inginkan?" 

    # TRANSISI WAKTU 
    scene city_ordered_again 
    with fade 

    play music "cold_control.ogg" 

    "Beberapa waktu kemudian." 
    "Kota kembali stabil." 
    "Lebih cepat dari yang seharusnya." 
    "Lebih rapi dari sebelumnya." 
    "Lebih… kosong." 

    # RAKA DI RUANGAN ADRIAN 
    scene adrian_office 
    with dissolve 

    "Ruangan yang dulu dia benci." 
    "Sekarang… menjadi miliknya." 

    show raka_suit at center 

    "Pemandangan kota yang sama." 
    "Layar yang sama." 
    "Sistem yang sama." 

    pause 

    system "Kurasi narasi harian siap." 
    system "Segmentasi emosi warga selesai." 
    system "Rekomendasi distribusi Impor siap dijalankan." 

    pause 

    "raka duduk perlahan di kursi Adrian" 

    play sound "chair_sit.ogg" 

    pause 2.0 # pause panjang

    raka (dalam hati) "Dulu gue pikir… ini kekuasaan." 

    pause 

    raka (dalam hati) "Sekarang… ini hanya beban." 

    pause 

    # MOMEN IRONI TERAKHIR 
    scene screen_close 
    with dissolve 

    "Sebuah draft terbuka." 
    "Narasi baru." 

    text_on_screen "Produk lokal tidak relevan dengan kebutuhan modern." 

    pause 

    "raka menatap lama" 

    raka (dalam hati) "Ini mungkin salah.” 

    pause 

    raka (dalam hati) "Tapi…" 

    pause 2.0 # pause panjang

    raka (dalam hati) "kalau gue nggak… orang lain yang akan." 

    pause 

    "raka mengklik 'Confirm'" 

    play sound "click.ogg" 

    # FINAL SHOT 
    scene city_screens 
    with fade 

    "Iklan baru muncul." 
    "Lebih halus." 
    "Lebih meyakinkan." 
    "Lebih… efektif." 

    pause 

    scene raka_shadow 
    with dissolve 

    "Dan di balik semua itu… ada seseorang yang dulu ingin menghentikan semuanya." 

    pause 

    "Sekarang… memastikan semuanya berjalan." 

    scene black 
    with fade 

    "END — BECOMING THE MIRROR" 

    return