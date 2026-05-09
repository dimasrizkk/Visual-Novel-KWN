## ============================================================
##  MIRROR — Scene 19E (Updated Format)
##  Judul   : Penutup Pertemuan
##  Karakter: Raka, Adrian
##  Latar   : minister_room_(adrian) → KOTA NAWASENA → black
## ============================================================

label scene_19e:

    scene minister_room_(adrian) with dissolve

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Jas_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Adrian kembali menghadap kota."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Kau boleh pergi."
    adrian "Dan Raka..."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka berhenti di ambang pintu."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Hati-hati dengan orang-orang yang membuatmu merasa bebas."
    adrian "Mereka biasanya yang pertama membuatmu kehilangan segalanya."

    "Nama Nara tidak disebut, namun kehadirannya terasa jelas di antara kata-kata itu."

    hide Jas_Serius with dissolve

    show Formal_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Raka melangkah keluar."

    scene KOTA NAWASENA with fade

    # Mengganti BGM ke tema yang lebih melankolis dan penuh beban
    play music "descending_tension.ogg" fadein 3.0

    show Formal_Sedih:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Lift turun perlahan menembus gemerlap Nawasena."
    "Di tangannya, keputusan tadi masih terasa berat. Di kepalanya, suara Nara dan Adrian mulai bertabrakan."
    "Di dadanya, sesuatu yang dulu stabil kini mulai retak."
    
    "Dan untuk pertama kalinya, Raka sadar..."
    "Ia tidak lagi berdiri di dalam sistem. Ia berdiri di antara dua dunia."

    hide Formal_Sedih with dissolve

    # Transisi ke layar hitam sebagai penanda akhir scene
    scene black with fade
    stop music fadeout 2.5

    jump scene_20a
