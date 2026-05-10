## ============================================================
##  MIRROR — Scene 20A (Updated Format)
##  Judul   : Kamar Tanpa Suara
##  Karakter: Raka (monolog)
##  Latar   : APARTEMEN RAKA → flash black → APARTEMEN RAKA
##  Catatan : Conditional berdasarkan flag awareness / ambition
## ============================================================

label scene_20a:

    scene APARTEMEN RAKA with fade

    # Memutar BGM bertema kesunyian dan ruang kosong
    play music "empty_room.ogg" fadein 3.0

    "Malam itu, apartemen Raka terasa lebih berisik dari biasanya."
    "Bukan karena ukurannya berubah. Tapi karena pikirannya tidak lagi punya tempat untuk bersembunyi."

    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Lampu tidak dinyalakan."
    "Kota di luar jendela cukup terang untuk memperlihatkan segalanya, dan cukup dingin untuk tidak memberi kehangatan apa pun."

    raka "(dalam hati) ..."

    "Di tangan kanannya..."

    # Logika kondisional berdasarkan pilihan di Scene 19D
    if awareness >= 2 or ambition >= 2:
        "Elite Drive."
        "Kecil. Diam. Tapi terasa seperti beban yang tidak bisa dijelaskan."
    else:
        "Kosong."
        "Tapi anehnya terasa lebih berat dari biasanya."

    "Di kepalanya... Suara. Bukan satu. Banyak."

    raka "(dalam hati) Lo ngapain sih?"
    raka "(dalam hati) Ini cuma kerjaan. Data ya data."
    raka "(dalam hati) Semua sistem punya cacat."

    pause 1.0

    raka "(dalam hati) Tapi kalau semua orang tahu... kenapa nggak ada yang berhenti?"

    "Pertanyaan itu berbahaya. Karena jawabannya bukan 'tidak tahu', tapi 'tidak mau kehilangan'."

    raka "(dalam hati) Lo juga sama. Lo nggak berhenti."
    raka "(dalam hati) Lo cuma mulai mikir."

    "Dan berpikir... adalah awal dari ketidaknyamanan yang tidak bisa dibatalkan."

    ## ── FLASH MEMORY — AYAH ──

    scene black with dissolve

    # Transisi musik ke tema memori yang rapuh
    play music "memory_fragile.ogg" fadein 2.0

    "Suara palu. Bau kulit. Cahaya sore masuk dari jendela kecil."

    show Casual_Netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    # Menggunakan suara Ayah (pastikan karakter 'ayah' didefinisikan di characters.rpy)
    "Ayah" "Raka."
    "Ayah" "Kalau kamu bikin sesuatu, pastikan kamu berani pakai hasilnya."

    "Raka kecil tertawa. Sepatu kebesaran di kakinya."

    ## ── KEMBALI KE REALITA ──

    scene APARTEMEN RAKA with dissolve

    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "(dalam hati) ..."
    raka "(dalam hati) Gue bahkan nggak pakai apa pun yang gue buat."
    raka "(dalam hati) Gue cuma bikin orang beli."

    ## ── DUA SUARA ──

    "Dua suara mulai berbentuk di dalam benaknya."

    # Menggunakan karakter suara (voice) agar berbeda dari dialog fisik
    adrian_voice "Dunia tidak berubah oleh orang baik. Stabilitas lebih penting dari idealisme."
    adrian_voice "Kau bisa naik lebih tinggi."

    nara_voice "Orang kota ini tidak rusak. Mereka cuma lupa cara berdiri."
    nara_voice "Lo mau jadi apa?"

    "Dua arah. Dua masa depan."
    "Dan satu keputusan yang belum diambil."

    # Menghentikan musik perlahan sebelum masuk ke klimaks
    stop music fadeout 3.0

    jump scene_20b
