label ending_golden_silence: 

    scene core_main with fade 

    # Memutar BGM kemenangan yang terasa hampa
    play music "empty_victory.ogg" fadein 2.0 

    "Raka mundur." 
    "Satu langkah." 
    "Satu langkah mundur yang cukup untuk mengubah seluruh arah masa depan." 

    pause 1.0 

    # Menampilkan Nara dan Raka berdampingan dalam ketegangan
    show Eksplor_Shocked:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    
    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    "Nara menatap Raka dengan tatapan tidak percaya." 

    nara "…Serius?" 

    pause 1.0 

    show Eksplor_Shocked:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    "Nara tertawa kecil. Terdengar hambar." 

    nara "Gue kira…" 

    pause 1.0 

    nara "Lo beda dari sistem." 

    pause 2.0 

    raka "..." 

    "Nara menatap wajah Raka untuk waktu yang lama, mencari sisa-sisa nurani." 

    nara "Ternyata lo cuma bagian paling lembutnya." 

    scene guard_enter with flash 

    # SFX Dobrakan pintu oleh Unit Penertiban
    play sound "door_break.ogg" 

    guard "Amankan target!" 

    "Nara ditarik paksa oleh unit bersenjata." 
    "Ia tidak melawan, tidak berteriak. Ia hanya terus menatap lurus ke arah Raka." 

    nara "Hebat kamu ya, Raka." 

    pause 1.0 

    nara "Lu selalu berpura-pura." 
    nara "Nikmati pilihan lu, Raka." 

    scene nara_taken with fade 

    "Dan begitu saja…" 
    "Ia hilang ditelan lorong kegelapan kementerian." 

    pause 2.0 

    raka "(dalam hati) Ini pilihanku." 
    raka "(dalam hati) Ini… harusnya bener kan?" 

    ## ── TRANSISI — KOTA MENJADI “SEMPURNA” ──
    scene city_perfect with fade 

    # Mengubah BGM ke tema kedamaian yang terkontrol secara paksa
    play music "controlled_peace.ogg" fadein 3.0 

    "Beberapa waktu kemudian." 
    "Kota menjadi jauh lebih rapi. Lebih tenang. Lebih efisien." 
    "Tidak ada protes. Tidak ada gangguan. Tidak ada… ruang untuk arah lain." 

    pause 1.0 

    "Semuanya berjalan. Persis seperti apa yang telah dirancang oleh algoritma sistem." 

    ## ── RAKA MENJADI ELITE ──
    scene elite_office with dissolve 

    # Raka muncul dengan pakaian formal naik pangkat (Kurator Utama)
    show Formal_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka naik jabatan." 
    "Lebih cepat dari yang pernah ia bayangkan. Lebih tinggi dari yang pernah ia impikan." 

    system "Status: Kurator Utama MIRROR" 
    system "Akses penuh diberikan." 

    pause 1.0 

    # SFX Duduk di kursi kerja besar
    play sound "chair_sit.ogg" 

    "Raka duduk perlahan di kursi kebesaran barunya." 

    raka "(dalam hati) Aman." 

    pause 1.0 

    raka "(dalam hati) Semua… aman." 

    ## ── IRONI — NARASI TETAP BERJALAN ──
    scene billboard with dissolve 

    "Narasi kota tetap berjalan secara berkala." 
    "Lebih halus. Lebih kuat. Lebih tidak terasa memanipulasi." 

    text_on_screen "Produk lokal = tidak relevan" 

    pause 1.0 

    "Raka melihat layar monitornya." 

    raka "(dalam hati) Gue menang…" 

    pause 2.0 

    raka "(dalam hati) ...Iya kan?" 

    ## ── KUNJUNGAN TERAKHIR — RUANG SISA ──
    scene ruang_sisa_demolition with fade 

    # Mengubah BGM ke tema kesepian dan reruntuhan kenangan
    play music "lonely.ogg" fadein 2.5 

    "Beberapa hari kemudian." 
    "Raka datang kembali ke lantai bawah tanah itu. Untuk yang terakhir kalinya." 

    scene ruang_sisa_empty with dissolve 

    "Ruang Sisa… kini sepenuhnya kosong." 
    "Tidak ada lagi suara deru mesin. Tidak ada cahaya hangat. Hanya debu yang beterbangan." 

    pause 1.0 

    "Raka berjalan pelan, setiap hentakan langkah kakinya bergema di dinding yang sepi." 

    raka "(dalam hati) Dulu tempat ini… hidup." 

    ## ── RADIO (SISA TERAKHIR NARA) ──
    scene old_radio with dissolve 

    # SFX Statik radio tua yang mendadak menyala
    play sound "radio_static.ogg" 

    radio "…Kalau lo denger ini…" 

    pause 1.0 

    radio "Gue harap lo milih sesuatu." 

    pause 2.0 

    radio "Bukan nunggu sampai semuanya dipilih-pilihin buat lo." 

    pause 1.0 

    "Raka hanya diam terpaku, tangannya sama sekali tidak bergerak untuk menyentuh radio itu." 

    raka "(dalam hati) Aku udah memilih." 

    pause 1.0 

    raka "(dalam hati) ...Dan sepertinya pilihanku salah ya, Nar?" 

    ## ── PEMBONGKARAN TEMPAT ──
    # SFX Suara alat berat mulai bekerja di luar gedung
    play sound "machine_start.ogg" 

    "Suara bising mesin terdengar keras dari arah luar." 
    "Sebuah proyek pembangunan baru saja dimulai. Zona ini akan segera ‘dimodernisasi’." 

    pause 1.0 

    scene demolition_begin with dissolve 

    "Dinding penopang mulai dihancurkan." 
    "Kenangan di tempat ini tidak dipindahkan, tidak disimpan. Hanya… dihapus secara permanen." 

    pause 1.0 

    "Raka berdiri tegak. Tidak bergerak, tidak melakukan apa pun untuk menghentikannya." 

    raka "(dalam hati) Kalau gue berhenti sekarang…" 

    pause 1.0 

    raka "(dalam hati) ...Apa yang bakal berubah, Nar?" 

    pause 2.0 

    "Raka membalikkan tubuhnya, berjalan melangkah keluar tanpa menoleh ke belakang lagi." 

   ## ── FINAL SHOT ──
    scene city_screens with fade 

    # Mengembalikan BGM hampa utama di akhir layar
    play music "empty_victory.ogg" fadein 2.0 

    "Kota Nawasena bersinar sangat benderang." 
    "Lebih terang dari sebelum-sebelumnya. Lebih sempurna. Dan terasa jauh lebih… kosong." 

    pause 1.0 

    scene raka_reflection with dissolve 

    "Dan di tengah gemerlap kepalsuan itu… ada seseorang yang berhasil mendapatkan semua hal yang ia inginkan." 

    pause 1.0 

    "Sekaligus kehilangan satu-satunya hal yang membuat hidupnya berarti." 

    scene black with fade 

    # Teks judul penutup rute cerita
    "END — GOLDEN SILENCE" 

    # Menghentikan seluruh trek suara saat game ditutup
    stop music fadeout 3.0
    stop sound fadeout 1.0

    return
