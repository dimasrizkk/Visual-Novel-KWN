label scene3:
    # Memutar efek suara pintu terbuka
    play sound door_open

    scene office_hall with dissolve

    worker "Pak Menteri datang!"

    # Menampilkan sprite karakter Adrian
    show adrian jas senyum:
        xalign 0.5
        yalign 1.1
    with dissolve

    # Jika ada BGM yang sedang menyala, ini momen yang bagus untuk menurunkan volumenya 
    # atau mematikan musik agar suasananya terasa canggung/menegang
    # stop music fadeout 1.0

    "Ruangan langsung rapi."
    "Suara langkahnya pelan, tapi cukup untuk membuat orang menahan napas."
    play sound langkah_kaki
    pause 4.0

    adrian "Lanjutkan pekerjaan kalian."
    adrian "Kota tidak menunggu."

    "Adrian Wiratma."
    "Bagi sebagian orang: penyelamat."
    "Bagi sebagian lain: alasan mereka tak lagi percaya pada pilihan."

    show adrian jas netral:
        xalign 0.9
        yalign 1.6
        zoom 0.9
    with dissolve
    adrian "Raka Pradana."

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve
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

    hide raka with dissolve

    show adrian jas senyum:
        xalign 0.5
        yalign 1.1
    with dissolve
    
    adrian "Bagus."
    adrian "Orang yang terlalu yakin biasanya tak berguna."
    adrian "Ikut aku."

    return
