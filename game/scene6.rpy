label scene6:
    scene apartment_dark with dissolve
    
    # Memutar efek suara notifikasi tugas baru
    play sound "audio/device_ping.mp3"
    
    system "Penugasan baru diterima."
    system "PRIORITAS MERAH"
    system "Program: FINAL LOCAL SENTIMENT REMOVAL"
    system "Tujuan: menurunkan kepercayaan warga pada produk lokal sebesar 72%%"
    system "Kurator utama: Raka Pradana"
    
    show raka shocked at center
    
    raka "...Final?"
    
    system "Kampanye ini akan menjadi fondasi ekonomi fase berikutnya."
    system "Konfirmasi penerimaan tugas."

    # Blok interaktif pilihan batin Raka
    menu:
        "Apa yang dirasakan Raka?"

        "Ini kesempatan terbesar dalam hidupku.":
            $ ambition += 1
            raka "Kalau berhasil... aku tak akan kembali ke bawah lagi."

        "Ada yang salah dengan semua ini.":
            $ loyalty += 1
            raka "...Kenapa terasa seperti menghapus sesuatu, bukan membangun?"

        "Kenapa harus aku?":
            $ awareness += 1
            raka "Apa yang sebenarnya mereka lihat dariku?"

    system "Menunggu konfirmasi..."
    
    "Raka menatap layar lama."
    
    scene split_screen with dissolve
    
    "Di satu sisi: layar modern yang menawarkan masa depan."
    "Di sisi lain: sepatu tua yang menolak dilupakan."
    "Raka berdiri di antara keduanya."
    
    raka "...Aku terima."
    
    system "Penugasan dikonfirmasi."

    return