## ============================================================
##  MIRROR — Scene 18A (Updated Format)
##  Judul   : Kembali ke Ruang Sisa
##  Karakter: Raka, Nara
##  Latar   : alley → ruang_sisa
## ============================================================

label scene_18a:

    scene GANG TUA MALAM with fade

    # Memutar BGM dengan efek fadein agar transisi halus
    play music "hidden_path.ogg" fadein 2.0

    "Sore harinya, langkah Raka kembali menemukan gang sempit itu lebih cepat daripada ingatannya mengakui."
    "Kali ini ia datang bukan karena perangkat rusak."
    "Dan itu lebih berbahaya."

    scene RUANG SISA with dissolve

    # Nara muncul di tengah dengan pengaturan koordinat dan zoom yang presisi
    show Bengkel_Netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Kalau device-mu rusak lagi, aku mulai curiga itu sengaja."

    # Raka muncul di sisi kiri
    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "Aku bawa sesuatu."

    show Bengkel_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Biasanya itu kalimat pembawa masalah."

    # Menyembunyikan Raka saat adegan fokus pada penyerahan tablet
    hide raka with dissolve

    # SFX Suara geseran tablet (jika ada asetnya)
    # play sound "tablet_slide.ogg"

    "Raka menyerahkan tablet. Nara membaca layar."

    show Bengkel_Netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "..."
    nara "Dapet dari mana?"

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    with dissolve

    raka "Kantor."

    show Bengkel_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Kau gila?"

    show Casual_Senyum:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Bisa diperdebatkan."

    show Bengkel_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    "Nara terus membaca."

    nara "Kesepian naik."
    nara "Makna kerja turun."
    nara "Ketergantungan konsumsi naik."

    show Bengkel_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Mereka bahkan ngukur luka yang mereka bikin."

    # Menambahkan variabel Awareness karena Raka mulai membagikan data internal
    $ awareness += 1

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Aku pikir kalian bakal senang lihat bukti."

    show Bengkel_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Aku tidak senang."
    nara "Aku lelah, ternyata perkiraanku benar."

    "Ia mengunci tablet, lalu menatap Raka lebih serius dari biasanya."

    show Bengkel_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Mau lihat sesuatu?"

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Apa?"

    show Bengkel_Serius:
        xalign 0.5
        yalign 1.1
        zoom 0.85

    nara "Versi kota yang nggak masuk dashboard."

    # Menghentikan musik perlahan sebelum transisi ke scene berikutnya
    stop music fadeout 2.0

    jump scene_18b
