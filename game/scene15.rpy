label scene15:
    # SFX suara perangkat elektronik melakukan reboot/restart
    play sound "audio/device_reboot.mp3"
    
    nara "Selesai."
    
    "Nara menyerahkan device."
    
    system "Sinkronisasi dipulihkan."
    system "Selamat datang kembali, Raka Pradana."
    system "Anda melewatkan 37 promosi."
    
    raka "...Aku tidak merindukannya."
    
    nara "Hati-hati. Ketergantungan dan kenyamanan tidak jauh berbeda."
    
    raka "Berapa biayanya?"
    
    nara "Dua pilihan."
    
    raka "Apa?"
    
    nara "Bayar uang."
    nara "Atau jawab jujur satu pertanyaan."

    # Blok interaktif pilihan respons Raka
    menu:
        "Apa yang dipilih Raka?"

        "Bayar uang.":
            $ ambition += 1
            raka "Aku pilih transaksi normal."
            "Nara menerima."
            nara "Setidaknya kau konsisten."
            "Jarak tetap aman."

        "Jawab pertanyaan.":
            $ loyalty += 1
            raka "Tanya."
            nara "Kapan terakhir kali kau membuat sesuatu dengan tanganmu sendiri?"
            "Raka terdiam."
            "Ia tidak punya jawaban cepat."
            nara "Gratis."

        "Kenapa harus memilih?":
            $ awareness += 1
            raka "Kau suka menguji orang?"
            nara "Tidak. Aku suka melihat orang yang mempunyai kebebasan memilih."
            "Ia tetap memberi uang, tapi pertanyaannya ikut pulang."

    return