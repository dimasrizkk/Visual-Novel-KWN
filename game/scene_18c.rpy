## ============================================================
##  MIRROR — Scene 18C (Updated Format)
##  Judul   : Raka vs Nara (Lanjutan)
##  Karakter: Raka, Nara
##  Latar   : community_hub2 → community_hub
## ============================================================

label scene_18c:

    scene community_hub2 with dissolve

    # Mengatur posisi Raka dan Nara agar sejajar secara visual
    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    nara "Nah. Sekarang bilang lagi soal efisiensi."

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Aku nggak bilang kalian nggak berharga."

    nara "Tapi?"

    raka "Tapi kota sebesar ini butuh skala."

    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Setuju."

    raka "Butuh kecepatan."

    nara "Setuju."

    raka "Butuh sistem."

    nara "Setuju."

    show Casual_Terkejut:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Lah?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Aku nggak lawan sistem."
    nara "Aku lawan sistem yang bikin semua orang cuma boleh jadi pembeli."

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka diam."

    nara "Kenapa orang harus memilih antara modern atau ditinggalkan?"
    nara "Mengapa tidak ada pilihan lain?"

    raka "Karena dunia dibentuk oleh sistem itu."

    nara "Benar."
    nara "Makanya sistem suka orang yang udah nyerah duluan."

    "Kena."

    # Transisi ke balkon basement
    scene community_hub with dissolve

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Eksplor_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Dari balkon kecil basement, Raka melihat seluruh ruangan."
    "Tak ada teknologi canggih. Tak ada AI. Tak ada presentasi menteri."
    "Tapi setiap orang di bawah sana sedang membuat sesuatu. Bukan hanya membeli."

    show Casual_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Kalau pemerintah tahu tempat ini..."

    show Eksplor_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Makanya kami nggak pasang billboard."

    show Casual_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Kalian nyimpen barang. Bikin barang. Lalu apa?"

    show Eksplor_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    nara "Lalu ngajarin."

    raka "Ke siapa?"

    # Point Awareness bertambah karena Raka mulai memahami perspektif baru
    $ awareness += 1

    nara "Ke generasi yang belum keburu percaya kalau satu-satunya masa depan adalah checkout."

    jump scene_18d
