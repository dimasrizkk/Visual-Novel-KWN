label scene9:
    scene transit_gate_locked with fade
    
    # Memutar BGM perjalanan di kota tua
    play music "old_city_walk.mp3" fadein 2.0

    show raka formal netral:
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Karena perangkatnya mati, gerbang transit menolak membukakan jalan."

    show raka formal sedih : #raka formal tired blom ada
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    show penjaga:
        xalign 0.9
        yalign 1.6
        zoom 0.85
    with dissolve

    penjaga "Identitas?"
    raka "Gangguan sistem."
    penjaga "Kalau sistem bilang tidak, saya juga bilang tidak."

    show raka formal marah: 
        xalign 0.0
        yalign 1.6
        zoom 0.43
    with dissolve

    raka "Aku pegawai Divisi MIRROR."
    
    "Penjaga menatap datar."
    penjaga "Sekarang kau hanya pejalan kaki."
    
    "Raka ingin marah."
    "Namun ia sadar, orang di depannya hanya versi kecil dari seluruh kota."
    "Tak ada yang mengambil keputusan."
    "Semua hanya meneruskan keputusan."

    scene city_walk_bridge with dissolve
    
    "Ia berjalan menyeberangi jembatan lama menuju sektor yang jarang ia lihat."
    "Semakin jauh dari pusat kota, cahaya menjadi lebih jujur."
    "Lampu tak lagi dibuat untuk memikat. Hanya untuk menerangi."

    scene old_market_ruins with dissolve #blom ada bg nya

    show raka formal netral:   
        xalign 0.5
        yalign 1.1
        zoom 0.85
    with dissolve

    "Bangunan pertama yang ia lewati adalah pasar tua."
    "Atau sisa dari sesuatu yang dulu disebut pasar."
    "Papan kayu lapuk. Rolling door berkarat. Lorong kosong tempat tawar-menawar pernah terdengar seperti musik harian."
    
    raka "...Aku pernah ke sini."

    scene black with dissolve #buat flashback nya gt ok ga?
    # Bagian Flashback - Bisa ditambahkan efek suara reverb atau gema
    ayah "Pegang kuat-kuat tangan Bapak."
    pedagang "Sepatu kulit! Jahitan tangan!"
    
    # SFX Anak kecil tertawa
    play sound "audio/child_laugh_echo.mp3"
    anak_kecil "*Tertawa*"
    
    "Kenangan datang tanpa izin."
    "Ia membencinya."

    scene old_market_ruins with dissolve #blom ada bg nya

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve
    
    raka "Tempat seperti ini memang tak bisa bertahan."

    show old_woman at right

    old_woman "Bertahan dari apa?"

    scene old_market_corner with dissolve #blom ada bg

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    show old_woman at right
    
    "Seorang nenek duduk di kursi plastik, menjual dua termos teh dan tiga bungkus kue."
    
    raka "Saya tidak bicara dengan Anda."
    
    old_woman "Tapi kau bicara cukup keras untuk didengar orang tua."
    
    "Raka diam."
    
    old_woman "Dulu di sini ramai."
    old_woman "Sekarang sepi bukan karena orang tak mau datang."
    old_woman "Mereka dipindahkan."
    
    raka "Ke tempat yang lebih efisien."
    
    "Nenek tua itu tertawa kecil."
    
    old_woman "Kata-kata bagus."
    old_woman "Sepi tetap sepi, meski diberi nama modern."
    
    "Raka pergi sebelum percakapan itu sempat tinggal di kepalanya."

    scene factory_apartments with dissolve #blom ada bg

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    "Di blok berikutnya berdiri apartemen mewah."
    "Halaman depannya menampilkan slogan:"
    
    system "LIVE ABOVE THE PAST."
    
    "Di dinding belakang, tulisan cat lama yang nyaris hilang masih terlihat."
    "\"PABRIK TEKSTIL BINA KARYA\""
    
    "Ia menatap cerobong yang kini menjadi dekorasi."
    
    raka "Mereka mengubah pabrik jadi pemandangan."
    "Kota ini pandai menjual luka sebagai desain."

    scene mural_wall with dissolve #blom ada bg nya

    show raka formal netral:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    
    "Ia melewati mural besar."
    "Separuh dinding menggambar Nawasena lama: kios, bengkel, orang tersenyum sambil bekerja."
    "Separuh lain ditutupi cat resmi: gedung kaca, drone, dan slogan negara."
    
    system "MAJU TANPA BEBAN MASA LALU"
    
    raka "... Tanpa beban."
    
    "Ia mulai curiga bahwa di kota ini, masa lalu hanya dihargai jika sudah dibungkam."

    stop music fadeout 3.0
    return
