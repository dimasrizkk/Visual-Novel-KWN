label ending_true: 
    scene core_main_alert 
    with flash 

    play music "core_alarm.ogg" 
    play sound "alarm.ogg" 

    "Sebuah bunyi tajam memecah ruangan." 

    system "Pelanggaran inti terdeteksi." 
    system "Unit penertiban dikerahkan." 
    system "Estimasi waktu: 90 detik." 

    scene core_lights_red 
    with dissolve 

    "Lampu berubah merah." 
    "Pintu-pintu terkunci otomatis." 
    "Langkah kaki mulai terdengar dari lorong luar." 

    play sound "distant_steps.ogg" 

    nara "Raka. Sekarang atau tidak selamanya" 

    pause 

    show adrian calm at center 
    show raka at left 
    show nara at right 

    "adrian tetap tenang" 

    adrian "Bagus Raka." 

    pause 

    "raka menatap tajam" 

    raka "Kau nggak bakal ngehentiin semua ini?" 

    "adrian menggeleng pelan" 

    adrian "Tidak Raka." 
    adrian "Aku ingin melihat semuanya." 

    pause 

    adrian "Melihat seberapa jauh kau berani menanggung konsekuensi dari pilihanmu sendiri." 

    nara "Jangan dengerin dia Raka" 

    "adrian tidak melihat Nara, hanya Raka" 

    adrian "Kau ingin membuka semuanyakan Raka?" 
    adrian "Silakan saja." 
    adrian "Bongkar. semuanya" 
    adrian "Hancurkan kepercayaan mereka semua." 
    adrian "Biarkan mereka melihat dunia tanpa ada arah." 

    pause 

    play sound "door_impact.ogg" 

    "Pintu luar mulai dihantam." 

    system "Unit mendekat." 

    adrian "Ingatlah Raka, saat mereka panik…" 

    "adrian sedikit tersenyum" 

    adrian "mereka akan Kembali mencari stabilitas." 

    pause 

    adrian "Dan saat itu tiba" 
    adrian "Nama yang mereka benci hari ini" 
    adrian "Akan menjadi satu-satunya nama yang mereka ingat untuk menyelamatkan mereka dari kekacauan semua ini." 

    raka diam 

    raka (dalam hati) "Apa dia tidak takut?" 
    raka (dalam hati) "Apa dia menunggu momen ini." 

    nara "Raka, jangan dengarkan dia!" 
    nara "Ini bukan soal dia RAKA!" 
    nara "Ini soal diri lu dan mereka yang ingin bebas!" 

    system "30 detik menuju intervensi paksa." 

    # AKSI RAKA — BROADCAST 
    scene core_overload 
    with flash 

    play music "uprising.ogg" 

    "Raka bergerak." 
    "Bukan karena yakin." 
    "Tapi karena akhirnya memilih." 

    raka "Kalau semua harus hancur dulu…" 
    raka "setidaknya orang-orang bisa memilih pilhannya sendiri…" 
    raka "SELESAIII." 

    play sound "system_override.ogg" 

    "Akses dibuka." 
    "Semua data." 
    "Semua manipulasi." 
    "Semua kebohongan." 
    "Dilepaskan." 

    # REAKSI ADRIAN 
    pause 

    "adrian tidak panik" 
    "tidak marah" 
    "tidak bergerak" 
    "adrian hanya melihat" 

    adrian "Bagus Raka." 

    pause 

    adrian "Sekarang lihat dan nikmatilah kebebasanmu." 

    # KOTA MELIHAT 
    scene city_screens 
    with dissolve 

    "Seluruh kota melihat." 

    ad_voice "Preferensi Anda telah dioptimalkan." 

    " *glitch* " 

    data_voice "Anda diarahkan." 
    data_voice "Pilihan Anda telah disesuaikan." 
    data_voice "Identitas Anda telah dimodifikasi." 

    pause 

    # GUARD MASUK 
    scene core_breach 
    with flash 

    play sound "door_break.ogg" 

    "Pintu jebol." 

    guard "Amankan mereka!" 

    nara "Kita harus pergi sekarang RAKA!" 

    "raka masih melihat layar" 

    raka (dalam hati) "Inilah pilihan yang telah aku buat" 

    "adrian tetap berdiri" 
    "tidak melawan" 
    "tidak kabur" 

    adrian "Lanjutkan saja Raka." 

    pause 

    "Untuk pertama kalinya…" 
    "ia tidak mengontrol hasilnya." 

    # KOTA DALAM CHAOS 
    scene chaos_city 
    with fade 

    play music "aftermath_chaos.ogg" 

    "Kota tidak runtuh." 
    "Mereka kehilangan arah." 
    "Orang-orang berhenti." 
    "Orang-orang berteriak." 
    "Orang-orang menolak." 
    "Marah." 
    "Takut." 
    "Bingung." 

    pause 

    "Dan untuk pertama kalinya…" 
    "mereka sadar." 

    # AFTERMATH 
    scene small_workshop 
    with dissolve 

    play music "quiet_rebuild.ogg" 

    "Tidak semua memilih benar." 
    "Tidak semua mencoba." 
    "Tidak semua bertahan." 

    pause 

    "Tapi beberapa… mulai." 
    "Memperbaiki." 
    "Mencoba lagi." 
    "Tanpa diarahkan." 

    # RAKA & NARA 
    show nara calm 
    show raka tired 

    raka "Ini bukan kemenangan ya?" 
    nara "Emang bukan." 
    nara "Ini sebuah awal, awal yang baik." 

    pause 

    # ADRIAN (DITANGKAP) 
    scene adrian_arrest 
    with dissolve 

    guard "Target diamankan." 

    "Adrian dibawa pergi." 
    "tidak melawan" 
    "tidak bicara" 
    "hanya melihat Raka" 

    pause 

    adrian "Kau telah membuat pilihanmu." 

    pause 

    adrian "Sekarang hiduplah dengan itu." 
    adrian "Nikmati dan lihatlah…" 
    adrian "apa yang akan lahir dari kekacauan ini." 

    pause 

    adrian "Karena ketika mereka sudah lelah…" 
    adrian "mereka akan kembali mencari seseorang seperti aku." 

    scene black 
    with fade 

    "Scene menunjukan warga yang Kembali membangun sektor lama yang sudah dibersihkan, membuka berbagai toko lama, pasar Kembali ramai, toko-toko local bermunculan dan membuat produk-produk dan dipakai masyrakat, billboard menampilkan berbagai produk local, banyak mural yang menulis “ANTI MIRROR” dan disebelahnya banyak pedagang tradisional di kerubungi pembeli." 

    scene black 
    with fade 

    "Raka membuka toko Sepatu kulit disebelah bengkel Nara, banyak pengunjung yang memperbaiki barang di bengkel Nara dan pembeli Sepatu di toko Raka, diakhir scene menunjukan Raka dan Nara duduk diatas balkon apartemen Raka, melihat kota yang sudah lebih bernyawa, berwarna, dan billboard produk-produk local dan billboard anti MIRROR." 

    "END - MIRROR" 

    scene black 
    with fade 

    if has_drive: 
        jump ending_secret 
    else: 
        return