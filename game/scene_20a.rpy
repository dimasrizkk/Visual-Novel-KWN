## ============================================================
##  MIRROR — Scene 20A
##  Judul   : Kamar Tanpa Suara
##  Karakter: Raka (monolog)
##  Latar   : raka_apartement → flash black → raka_apartement
##  Catatan : Conditional berdasarkan flag awareness / ambition
## ============================================================

label scene_20a:

    scene raka_apartement
    with fade

    play music "empty_room.ogg"

    "Malam itu, apartemen Raka terasa lebih berisik dari biasanya."
    "Bukan karena ukurannya berubah."
    "Tapi karena pikirannya tidak lagi punya tempat untuk bersembunyi."

    show raka casual sedih at center

    "Lampu tidak dinyalakan."
    "Kota di luar jendela cukup terang untuk memperlihatkan segalanya."
    "Dan cukup dingin untuk tidak memberi kehangatan apa pun."

    raka "(dalam hati) ..."

    "Di tangan kanannya.."

    if awareness >= 2 or ambition >= 2:
        "Elite Drive."
        "Kecil. Diam."
        "Tapi terasa seperti beban yang tidak bisa dijelaskan."
    else:
        "Kosong."
        "Tapi anehnya terasa lebih berat dari biasanya."

    "Di kepalanya.."
    "Suara."
    "Bukan satu."
    "Banyak."

    raka "(dalam hati) Lo ngapain sih?"
    raka "(dalam hati) Ini cuma kerjaan."
    raka "(dalam hati) Data ya data."
    raka "(dalam hati) Semua sistem punya cacat."

    pause

    raka "(dalam hati) Tapi kalau semua orang tahu..."
    raka "(dalam hati) kenapa nggak ada yang berhenti?"

    "Pertanyaan itu berbahaya."
    "Karena jawabannya bukan tidak tahu."
    "Tapi tidak mau kehilangan."

    raka "(dalam hati) Lo juga sama."
    raka "(dalam hati) Lo nggak berhenti."
    raka "(dalam hati) Lo cuma mulai mikir."

    "Dan berpikir..."
    "adalah awal dari ketidaknyamanan yang tidak bisa dibatalkan."

    ## ── FLASH MEMORY — AYAH ──

    scene black
    with dissolve

    play music "memory_fragile.ogg"

    "Suara palu. Bau kulit. Cahaya sore masuk dari jendela kecil."

    show raka casual netral at center

    "Ayah" "Raka."
    "Ayah" "Kalau kamu bikin sesuatu"
    "Ayah" "pastikan kamu berani pakai hasilnya."

    "Raka kecil tertawa."
    "Sepatu kebesaran di kakinya."

    scene raka_apartement
    with dissolve

    show raka casual sedih at center

    raka "(dalam hati) ..."
    raka "(dalam hati) Gue bahkan nggak pakai apa pun yang gue buat."
    raka "(dalam hati) Gue cuma bikin orang beli."

    ## ── DUA SUARA ──

    "Dua suara mulai berbentuk."

    adrian_voice "Dunia tidak berubah oleh orang baik."
    adrian_voice "Stabilitas lebih penting dari idealisme."
    adrian_voice "Kau bisa naik lebih tinggi."

    nara_voice "Orang kota ini tidak rusak."
    nara_voice "Mereka cuma lupa cara berdiri."
    nara_voice "Lo mau jadi apa?"

    "Dua arah."
    "Dua masa depan."
    "Dan satu keputusan yang belum diambil."

    jump scene_20b
