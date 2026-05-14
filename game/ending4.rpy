label ending_golden_silence: 

    scene core_main 
    with fade 

    play music "empty_victory.ogg" 

    "Raka mundur." 
    "Satu langkah." 
    "Cukup untuk mengubah segalanya." 

    pause 

    show nara shocked 
    show raka at left 

    "nara menatap" 

    nara "…serius?" 

    pause 

    "nara tertawa kecil" 

    nara "Gue kira…" 

    pause 

    nara "lo beda dari sistem." 

    pause 2.0 # pause panjang 

    "raka tidak menjawab" 

    "nara menatap lama" 

    nara "Ternyata lo cuma bagian paling lembutnya." 

    scene guard_enter 
    with flash 

    play sound "door_break.ogg" 

    guard "Amankan target!" 

    "Nara ditarik paksa." 
    "nara tidak melawan, tidak berteriak, hanya menatap Raka." 

    nara "Hebat kamu ya Raka" 

    pause 

    nara "Lu selalu berpura-pura." 
    nara "Nikmati pilihanlu Raka." 

    scene nara_taken 
    with fade 

    "Dan begitu saja…" 
    "ia hilang." 

    pause 2.0 # pause panjang 

    raka (dalam hati) "Ini pilihanku." 
    raka (dalam hati) "Ini… harusnya benarkan?" 

    # TRANSISI — KOTA MENJADI “SEMPURNA” 
    scene city_perfect 
    with fade 

    play music "controlled_peace.ogg" 

    "Beberapa waktu kemudian." 
    "Kota menjadi lebih rapi." 
    "Lebih tenang." 
    "Lebih efisien." 
    "Tidak ada protes. Tidak ada gangguan. Tidak ada… arah lain." 

    pause 

    "Semuanya berjalan." 
    "Persis seperti yang diinginkan sistem." 

    # RAKA MENJADI ELITE 
    scene elite_office 
    with dissolve 

    show raka_suit at center 

    "Raka naik." 
    "Lebih cepat dari yang ia bayangkan." 
    "Lebih tinggi dari yang pernah ia impikan." 

    system "Status: Kurator Utama MIRROR" 
    system "Akses penuh diberikan." 

    pause 

    "raka duduk perlahan di kursi besar" 

    play sound "chair_sit.ogg" 

    raka (dalam hati) "Aman." 

    pause 

    raka (dalam hati) "Semua… aman." 

    pause 

    # IRONI — NARASI TETAP BERJALAN 
    scene billboard 
    with dissolve 

    "Narasi tetap berjalan." 
    "Lebih halus. Lebih kuat. Lebih tidak terasa." 

    text_on_screen "Produk lokal = tidak relevan" 

    pause 

    "raka melihat layar" 

    raka (dalam hati) "Gue menang…" 

    pause 2.0 # pause panjang 

    raka (dalam hati) "iyakan?" 

    # KUNJUNGAN TERAKHIR — RUANG SISA 
    scene ruang_sisa_demolition 
    with fade 

    play music "lonely.ogg" 

    "Beberapa hari kemudian." 
    "Raka datang kembali." 
    "Untuk terakhir kalinya." 

    scene ruang_sisa_empty 
    with dissolve 

    "Ruang Sisa… kosong." 
    "Tidak ada suara mesin. Tidak ada cahaya hangat. Hanya debu." 

    pause 

    "raka berjalan pelan, setiap langkah bergema" 

    raka (dalam hati) "Dulu tempat ini… hidup." 

    pause 

    # RADIO (SISA TERAKHIR NARA) 
    scene old_radio 
    with dissolve 

    play sound "radio_static.ogg" 

    radio "…kalau lo denger ini…" 

    pause 

    radio "gue harap lo milih sesuatu." 

    pause 2.0 # pause panjang 

    radio "bukan, nunggu sampai semuanya dipilihin buat lo." 

    pause 

    "raka diam, tidak menyentuh radio" 

    raka (dalam hati) "Aku udah memilih." 

    pause 

    raka (dalam hati) "dan sepertinya pilihanku salah ya Nar?" 

    # PEMBONGKARAN TEMPAT 
    play sound "machine_start.ogg" 

    "Suara mesin dari luar." 
    "Proyek pembangunan." 
    "Zona ini akan ‘dimodernisasi’." 

    pause 

    scene demolition_begin 
    with dissolve 

    "Dinding mulai dihancurkan." 
    "Kenangan tidak dipindahkan. Tidak disimpan. Hanya… dihapus." 

    pause 

    "raka berdiri, tidak bergerak, tidak menghentikan" 

    # MOMEN TERAKHIR 
    raka (dalam hati) "Kalau gue berhenti sekarang…" 

    pause 

    raka (dalam hati) "apa yang berubah Nar?" 

    pause 2.0 # pause panjang 

    "raka berbalik, berjalan keluar tanpa melihat ke belakang" 

    # FINAL SHOT 
    scene city_screens 
    with fade 

    play music "empty_victory.ogg" 

    "Kota bersinar." 
    "Lebih terang dari sebelumnya. Lebih sempurna. Lebih… kosong." 

    pause 

    scene raka_reflection 
    with dissolve 

    "Dan di tengah semua itu… ada seseorang yang mendapatkan semua yang ia inginkan." 

    pause 

    "Dan kehilangan satu-satunya hal yang membuatnya berarti." 

    scene black 
    with fade 

    "END — GOLDEN SILENCE" 

    return