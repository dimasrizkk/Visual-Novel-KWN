## ============================================================
##  MIRROR — Scene 19E
##  Judul   : Penutup Pertemuan
##  Karakter: Raka, Adrian
##  Latar   : minister_room → nawasa_city_night → black
## ============================================================

label scene_19e:

    scene minister_room
    with dissolve

    show raka formal serius at left
    show adrian jas netral at right

    "Adrian kembali menghadap kota."

    show adrian jas serius at right

    adrian "Kau boleh pergi."
    adrian "Dan Raka..."

    show raka formal serius at left

    "Raka berhenti di pintu."

    show adrian jas serius at right

    adrian "Hati-hati dengan orang-orang yang membuatmu merasa bebas."
    adrian "Mereka biasanya yang pertama membuatmu kehilangan segalanya."

    "Nama Nara tidak disebut."
    "Namun terasa jelas."

    hide adrian

    show raka formal sedih at center

    "Raka keluar."

    scene nawasa_city_night
    with fade

    play music "descending_tension.ogg"

    show raka formal sedih at center

    "Lift turun perlahan."
    "Di tangannya, keputusan tadi masih terasa."
    "Di kepalanya, suara Nara dan Adrian mulai bertabrakan."
    "Di dadanya, sesuatu yang dulu stabil mulai retak."
    "Dan untuk pertama kalinya..."
    "Raka sadar.."
    "ia tidak lagi berdiri di dalam sistem."
    "Ia berdiri di antara dua dunia."

    hide raka

    scene black
    with fade

    jump scene_20a
