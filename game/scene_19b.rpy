## ============================================================
##  MIRROR — Scene 19B (Updated Format)
##  Judul   : Pertemuan + Konfrontasi Halus
##  Karakter: Raka, Adrian
##  Latar   : minister_room_(adrian)
## ============================================================

label scene_19b:

    scene minister_room_(adrian) with fade

    # Memutar BGM bertema manipulasi/psikologis
    play music "mind_game.ogg" fadein 2.0

    # Menampilkan Raka dan Adrian dengan koordinat presisi
    show Formla_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85
    
    show Jas_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85
    with dissolve

    "Adrian berdiri di depan jendela besar, membelakangi pintu."
    "Kota terhampar di bawahnya seperti papan catur."

    adrian "Kau tahu apa yang paling menarik dari kota ini?"

    raka "Efisiensinya?"

    show Jas_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    "Adrian tersenyum tipis."

    adrian "Prediktabilitasnya."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    "Adrian berbalik perlahan."

    adrian "Semua orang berpikir mereka memilih. Padahal mereka hanya memilih dari opsi yang kita sediakan."

    "Tatapannya langsung menembus. Bukan menilai, tetapi menghitung."

    adrian "Duduk."

    show Formal_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka duduk."

    show Jas_Netral:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Kampanye sepatu impor minggu lalu. Naik signifikan."
    adrian "Narasi 'rasa malu terhadap produk lama' itu efektif."

    raka "Itu tugas saya."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Bukan. Itu kemampuan."

    "Pujian dari Adrian tidak terasa hangat. Terasa seperti label harga."

    adrian "Kau tahu kenapa aku memanggilmu?"

    raka "Evaluasi?"

    adrian "Sebagian."

    "Adrian mengambil tablet, memutar layar ke arah Raka."

    system "Log Aktivitas Internal - Raka Pradana"

    "File distorsi data. Folder tersembunyi. Akses tidak biasa."

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka diam."

    show Jas_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Menarik. Kau mulai melihat sesuatu yang tidak semua orang lihat."

    raka "Itu data internal."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Semua data internal. Pertanyaannya bukan siapa yang boleh melihat."

    "Adrian mendekat sedikit."

    adrian "Pertanyaannya: apa yang kau lakukan setelah melihat."

    show Formal_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Saya hanya... memastikan."

    adrian "Memastikan apa?"

    raka "Bahwa sistem berjalan sesuai tujuan."

    show Jas_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    "Adrian tersenyum."

    adrian "Dan menurutmu?"

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka diam sejenak."

    raka "Sistem berjalan."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Jawaban aman."

    "Adrian berjalan perlahan mengelilingi meja."

    adrian "Kau tahu, Raka... Aku suka orang yang cerdas."
    adrian "Tapi aku lebih suka orang yang tahu kapan berhenti bertanya."

    raka "Kalau tidak ada yang bertanya, kesalahan jadi permanen."

    show Jas_Marah:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Kesalahan?"

    "Adrian berhenti."

    show Jas_Serius:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    adrian "Kau menyebut stabilitas sebagai kesalahan?"

    raka "Saya menyebut ketergantungan sebagai risiko."

    "Sunyi jatuh. Bukan karena mereka kehabisan kata. Karena keduanya mulai memilih kata dengan hati-hati."

    adrian "Kau berubah."

    show Formal_Netral:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    raka "Saya belajar."

    adrian "Dari siapa?"

    show Formal_Serius:
        xalign 0.15
        yalign 1.1
        zoom 0.85

    "Raka tidak menjawab."

    show Jas_Senyum:
        xalign 0.85
        yalign 1.1
        zoom 0.85

    "Adrian tertawa kecil."

    adrian "Bagus. Artinya kau tidak sepenuhnya bodoh."

    # Menghentikan BGM sebelum masuk ke scene berikutnya
    stop music fadeout 2.0

    jump scene_19c
