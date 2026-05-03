## ============================================================
##  MIRROR — Scene 18D
##  Judul   : Foreshadowing
##  Karakter: Raka, Nara
##  Latar   : community_hub → nawasa_city_night → black
## ============================================================

label scene_18d:

    show raka casual terkejut at left

    play sound "device_ping.ogg"

    system "Pengingat: rapat evaluasi 20 menit lagi."
    system "Lokasi: Kantor Menteri Adrian Wiratma."

    show nara eksplor serius at right

    nara "Bos besar manggil?"

    show raka casual serius at left

    raka "Iya."

    show nara eksplor netral at right

    nara "Pergi."

    show raka casual netral at left

    raka "Segampang itu?"

    show nara eksplor serius at right

    nara "Belum."

    "Nara mendekat."

    nara "Raka."
    nara "Kalau suatu hari lo harus milih antara nyaman dan benar..."
    nara "Jangan pura-pura itu pilihan kecil."

    show raka casual netral at left

    raka "Lo ngomong kayak kenal gue."

    show nara eksplor serius at right

    nara "Nggak."
    nara "Gue ngomong kayak kenal kota ini."

    hide nara
    hide raka

    scene nawasa_city_night
    with fade

    play music "tension_rise.ogg"

    "Raka kembali ke permukaan."
    "Di atas tanah, layar-layar kembali menyala."
    "Diskon."
    "Prediksi."
    "Kemudahan."
    "Semua masih sama."
    "Masalahnya, sekarang ia tahu ada dunia lain yang sengaja dibuat tak terlihat."
    "Dan seseorang paling berkuasa di kota sedang menunggunya."

    scene black
    with fade

    jump scene_19a
