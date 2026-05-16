label scene_22a_sunyi_yang_tidak_normal:

    # Transisi dari scene black di 21F ke fajar yang mengalami glitch
    scene city_dawn_glitch with fade 
    
    # Memutar BGM bernuansa kota mati/kosong dengan transisi halus
    play music "empty_city.ogg" fadein 2.5 

    "Pagi datang seperti biasa." 
    "Lampu jalan masih menyala. Transportasi tetap berjalan. Iklan tetap tersenyum." 
    
    pause 1.0 
    
    "Dan kebiasaan itu justru menjadi hal yang terasa sangat salah." 

    scene billboard_glitch with dissolve 
    
    # Suara iklan mulai berjalan
    ad_voice "Produk luar, pilihan cerdas—" 
    
    # SFX Efek kerusakan audio/digital pada papan iklan
    play sound "glitch.ogg" 
    
    ad_voice "—kenapa kamu membelinya?" 
    
    pause 1.0 
    
    "Sebuah glitch kecil." 
    "Cukup untuk membuat beberapa orang yang lewat berhenti sejenak, namun tidak cukup kuat untuk membuat mereka benar-benar berubah." 

    scene street_people with dissolve 
    
    "Di sudut trotoar, seorang ibu menarik tangan anaknya dengan terburu-buru." 
    
    mother "Jangan yang itu. Cepet rusak." 
    child "Tapi bagus…" 
    mother "Yang ini aja." 
    
    "Di tempat lain, seorang pria paruh baya menatap etalase toko." 
    "Menampilkan deretan produk lokal. Ia ragu sesaat, lalu memilih berbalik pergi." 
    
    "Kota ini tidak runtuh secara instan." 
    "Ia hanya… perlahan-lahan mulai retak."

    # Menghentikan audio secara halus sebelum lanjut ke scene berikutnya
    stop music fadeout 2.0
    stop sound fadeout 1.0

    return
