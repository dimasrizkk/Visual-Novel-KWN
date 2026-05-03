label scene3:
    # Memutar efek suara pintu terbuka
    play sound "audio/door_open.mp3"

    scene office_hall with dissolve

    worker "Pak Menteri datang!"

    # Menampilkan sprite karakter Adrian
    show adrian calm at center with dissolve

    # Jika ada BGM yang sedang menyala, ini momen yang bagus untuk menurunkan volumenya 
    # atau mematikan musik agar suasananya terasa canggung/menegang
    # stop music fadeout 1.0

    "Ruangan langsung rapi."
    "Suara langkahnya pelan, tapi cukup untuk membuat orang menahan napas."

    adrian "Lanjutkan pekerjaan kalian."
    adrian "Kota tidak menunggu."

    "Adrian Wiratma."
    "Bagi sebagian orang: penyelamat."
    "Bagi sebagian lain: alasan mereka tak lagi percaya pada pilihan."

    adrian "Raka Pradana."

    show raka neutral at left

    raka "Pak."
    
    adrian "Aku membaca hasil kerjamu."
    adrian "Kau paham manusia lebih baik daripada mereka memahami dirinya sendiri."

    "Itu pujian."
    "Atau peringatan."

    menu:
        "Bagaimana respons Raka?"

        "Terima kasih, Pak.":
            $ ambition += 1
            raka "Saya hanya melakukan tugas saya."
            "Dan menikmati pengakuannya."

        "Diam dan mengamati.":
            $ awareness += 1
            "Raka tidak menjawab."
            "Ia hanya bertanya-tanya mengapa pujian terasa seperti rantai."

        "Saya tidak yakin itu hal baik.":
            $ loyalty += 1
            raka "Memahami orang untuk menggerakkan mereka... belum tentu mulia."
            worker "..."
            "Ruangan menegang."

    show adrian smiles
    
    adrian "Bagus."
    adrian "Orang yang terlalu yakin biasanya tak berguna."
    adrian "Ikut aku."

    return