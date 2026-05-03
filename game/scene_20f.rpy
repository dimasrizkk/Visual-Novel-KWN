## ============================================================
##  MIRROR — Scene 20F
##  Judul   : Penutup Batin
##  Karakter: Raka (monolog)
##  Latar   : raka_apartement → black
##  Catatan : Conditional berdasarkan flag awareness / ambition
## ============================================================

label scene_20f:

    scene raka_apartement
    with fade

    play music "inner_collapse.ogg"

    show raka casual sedih at center

    "Sunyi kembali."
    "Tapi bukan sunyi yang sama."
    "Sekarang penuh."
    "Penuh kemungkinan."
    "Penuh risiko."
    "Penuh kehilangan."

    raka "(dalam hati) Kalau gue ikut.."
    raka "(dalam hati) gue bisa hancurin semuanya."
    raka "(dalam hati) Kalau gue nggak.."
    raka "(dalam hati) gue jadi bagian dari semua ini."

    pause

    if awareness >= 2 or ambition >= 2:
        "Tangannya menyentuh Elite Drive."
        "Dingin."
        "Seperti keputusan yang belum diambil."

    "Di luar, kota tetap berjalan."
    "Di dalam, sesuatu mulai runtuh."

    hide raka

    scene black
    with fade

    return
