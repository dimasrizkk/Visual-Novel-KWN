## ============================================================
##  MIRROR — Scene 20F (Updated Format)
##  Judul   : Penutup Batin
##  Karakter: Raka (monolog)
##  Latar   : APARTEMEN RAKA → black
##  Catatan : Conditional berdasarkan flag awareness / ambition
## ============================================================

label scene_20f:

    scene APARTEMEN RAKA with fade

    # Memutar BGM penutup dengan nuansa keruntuhan batin
    play music "inner_collapse.ogg" fadein 3.0

    show Casual_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Sunyi kembali. Tapi bukan sunyi yang sama."
    "Sekarang penuh. Penuh kemungkinan. Penuh risiko. Penuh kehilangan."

    raka "(dalam hati) Kalau gue ikut... gue bisa hancurin semuanya."
    raka "(dalam hati) Kalau gue nggak... gue jadi bagian dari semua ini."

    pause 1.5

    # Logika kondisional untuk Elite Drive
    if awareness >= 2 or ambition >= 2:
        "Tangannya menyentuh Elite Drive."
        "Benda itu terasa dingin. Dingin, seperti keputusan yang belum diambil."
    else:
        "Tangannya meraba saku yang kosong. Hampa."

    "Di luar, kota tetap berjalan dengan segala efisiensinya."
    "Di dalam ruangan ini, sesuatu mulai runtuh."

    hide Casual_Sedih with dissolve

    # Transisi akhir menuju layar hitam (End of Chapter)
    scene black with fade
    stop music fadeout 3.0

    "Babak baru dimulai saat keraguan berakhir."

    return
