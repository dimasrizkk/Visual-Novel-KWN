label scene21d:

    if passive_path >= 1:

        # Menampilkan latar belakang Raka yang sedang memantau monitor apartemen
        scene bg raka_apartment_monitor with fade

        # Memutar BGM bernuansa dingin, digital, dan berjarak
        play music "cold_watch.ogg" fadein 2.0

        "Raka tidak bergerak dari tempat duduknya."
        "Ia membuka dashboard internal kementerian, memilih untuk melihat operasi yang sedang berjalan secara real-time."

        system "Zona anomali terdeteksi."
        system "Distribusi tidak sah diintervensi."
        system "Subjek tidak terdaftar diamankan."

        "Di atas layar digital, titik-titik merah penanda aktivitas Ruang Sisa mulai bermunculan."
        "Lalu, satu per satu titik itu padam secara sistematis."

        "Efisien. Bersih. Sunyi."

        # Menampilkan Raka dalam kondisi tertekan/sedih di depan monitor
        show Casual_Sedih:
            xalign 0.5
            yalign 1.1
            zoom 0.85
        with dissolve

        raka "...Ini salah."

        "Namun, ia tetap memilih untuk diam dan melihat."
        "Dan di dalam kota seperti Nawasena, diam juga merupakan sebuah pilihan yang memiliki konsekuensi."

    # Menghentikan BGM perlahan sebelum menutup jalur ini
    stop music fadeout 2.0

    return
