## ============================================================
##  MIRROR — Scene 18B (Updated Format)
##  Judul   : Jaringan Bawah Tanah
##  Karakter: Raka, Nara, Pengrajin1, Penjahit, Pak Jaya, Anak
##  Latar   : community_hub → community_hub2
## ============================================================

label scene_18b:

    # Membersihkan layar dari karakter scene sebelumnya
    hide nara
    hide raka
    with dissolve

    scene community_hub with fade

    "Nara memimpin jalan melewati pintu belakang bengkel."
    "Lorong sempit menurun ke basement bangunan tua."
    "Bau debu berubah jadi bau kayu, logam panas, dan cat."

    # Efek suara lingkungan untuk membangun suasana workshop
    play sound "hammer_echo.ogg" loop
    play sound "machine_manual.ogg" loop

    scene community_hub2 with dissolve

    # Mengganti musik ke tema yang lebih hidup/hangat
    play music "people_alive.ogg" fadein 2.0

    # Menampilkan Raka dan Nara dengan koordinat presisi
    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka berhenti."
    "Ruang besar terbuka di bawah tanah."
    "Bukan markas bersenjata. Bukan sarang kriminal."
    "Workshop."
    "Puluhan orang bekerja. Ada yang menjahit tas, memperbaiki mesin kopi, hingga merakit sepeda."
    "Suara gaduh. Berantakan. Hidup."

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Ini semua masih ada?"

    show Eksplor_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Selama sesuatu berguna, selalu ada yang berusaha menjaganya."

    # Suara latar dari NPC
    pengrajin1 "Nara! Bearing yang lo minta jadi."

    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Taruh meja dua."

    penjahit "Nara, kain lokal batch baru dateng."

    nara "Sip."

    "Mereka bicara padanya bukan seperti bawahan pada pemimpin."
    "Tapi seperti orang pada orang yang dipercaya."

    raka "Mereka semua... sembunyi di sini?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Bertahan."

    raka "Sama aja."

    nara "Nggak."
    nara "Sembunyi itu takut dilihat. Bertahan itu nolak hilang."

    scene community_hub with dissolve

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    anak "Kak Nara! Bunyi!"

    play sound "kresek.ogg"

    "Tawa anak kecil itu terasa asing."
    "Karena di pusat kota, kebanyakan suara bahagia datang dari speaker."

    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    raka "Kalau tempat ini ada, kenapa nggak buka aja resmi?"

    show Eksplor_Sedih:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Pernah. Tiga kali."
    nara "Pertama, izin bahan ditahan. Kedua, inspeksi keamanan mendadak. Ketiga, akun pembayaran dibekukan."

    raka "Kalau kualitas bagus, pasar bakal cari."

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Pasar mana?"

    "Nara mendekat."

    nara "Yang hasil pencariannya dibayar sponsor? Yang review-nya dibentuk bot?"
    nara "Yang ongkirnya dimurahin kalau barang lewat jalur negara?"

    "Raka ingin menyela. Tak ada celah."

    # Munculnya karakter Pak Jaya (Pengrajin Tua)
    # Gunakan placeholder jika belum ada aset gambarnya
    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    pengrajin_tua "Nara."

    nara "Pak Jaya."

    pengrajin_tua "Anak baru?"

    nara "Masih uji coba."

    pengrajin_tua "Duduk sini."

    "Di meja kayu tua, pria sepuh sedang menjahit sepatu kulit. Gerakan jarinya familiar."

    pengrajin_tua "Pernah lihat orang bikin beginian?"

    show Casual_Sedih:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "...Ayahku."

    # Momen emosional: Menambah poin Loyalty karena koneksi masa lalu
    $ loyalty += 1

    pengrajin_tua "Namanya?"

    raka "Arman Pradana."

    pengrajin_tua "Keras kepala itu."

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Bapak kenal?"

    pengrajin_tua "Dia ngajarin gue jahitan silang. Ngamuk kalau ukuran miring setengah senti."

    "Ada sesuatu bergerak di dada Raka. Rasa kehilangan, atau rasa ditemukan."

    pengrajin_tua "Pegang."

    "Pak Jaya menyerahkan sepatu setengah jadi."

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    pengrajin_tua "Berat?"

    raka "Lumayan."

    pengrajin_tua "Karena ada tangan di baliknya. Barang murah enteng dibawa. Barang bernilai, berat ditanggung."

    "Kalimat itu terdengar kuno. Dan justru karena itu terasa penting."

    # Menghentikan SFX loop sebelum pindah scene
    stop sound fadeout 1.0
    stop music fadeout 2.0

    jump scene_18c
