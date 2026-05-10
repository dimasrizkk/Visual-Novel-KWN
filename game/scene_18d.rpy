## ============================================================
##  MIRROR — Scene 18D (Updated Format)
##  Judul   : Foreshadowing
##  Karakter: Raka, Nara
##  Latar   : community_hub → KOTA NAWASENA → black
## ============================================================

label scene_18d:

    scene community_hub with dissolve

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    # SFX Notifikasi perangkat yang memecah suasana
    play sound "device_ping.ogg"

    system "Pengingat: rapat evaluasi 20 menit lagi."
    system "Lokasi: Kantor Menteri Adrian Wiratma."

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Bos besar manggil?"

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Iya."

    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Pergi."

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Segampang itu?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Belum."

    "Nara mendekat. Suasana menjadi lebih intim dan berat."

    nara "Raka."
    nara "Kalau suatu hari lo harus milih antara nyaman dan benar..."
    nara "Jangan pura-pura itu pilihan kecil."

    raka "Lo ngomong kayak kenal gue."

    nara "Nggak. Gue ngomong kayak kenal kota ini."

    # Karakter menghilang sebelum transisi lokasi
    hide nara
    hide raka
    with dissolve

    scene KOTA NAWASENA with fade

    # Mengganti BGM ke tema yang lebih tegang
    play music "tension_rise.ogg" fadein 3.0

    "Raka kembali ke permukaan."
    "Di atas tanah, layar-layar kembali menyala."
    "Diskon. Prediksi. Kemudahan. Semua masih sama."
    "Masalahnya, sekarang ia tahu ada dunia lain yang sengaja dibuat tak terlihat."
    "Dan seseorang paling berkuasa di kota sedang menunggunya."

    # Transisi ke layar hitam untuk mengakhiri bab ini
    scene black with fade
    stop music fadeout 2.0

    jump scene_19a
