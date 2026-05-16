label scene29_25:

    scene core_main 
    with fade 
    play music "cold_core.ogg" 
    
    "Ruang inti MIRROR." 
    "Tidak seperti yang dibayangkan." 
    "Tidak megah." 
    "Tidak penuh cahaya." 
    "Hanya dingin." 
    "Rapi." 
    "Efisien." 
    "Data mengalir." 
    "Preferensi." 
    "Kebiasaan." 
    "Ketakutan." 
    "Semua dikumpulkan." 
    "Disusun." 
    "Diarahkan." 
    
    pause 
    
    show adrian kantor netral: 
        xalign 0.5
        yalign 1.1  
        zoom 0.85
    with dissolve

    show raka rebel serius:
        xalign 0.0
        yalign 1.6
        zoom 0.85
    with dissolve

    show nara eksplor serius:
        xalign 1.0
        yalign 1.6
        zoom 0.9
    with dissolve

    adrian "Kalian terlalu lama." 
    
    pause 
    
    "Nara langsung tegang." 
    
    nara "Jadi lo udah nunggu ya." 
    adrian "Tentu." 
    adrian "Kalian pikir kalian tidak terlihat?" 
    adrian "Atau kalian pikir… kalian yang pertama?" 
    
    pause 
    
    "Raka menatap Adrian." 
    
    raka "Kau pahamkan ini semua salah dan merusak?" 
    
    "Adrian tersenyum tipis." 
    
    show adrian kantor senyum:
        xalign 0.5
        yalign 1.1  
        zoom 0.85

    adrian "‘Semua’ itu kata yang terlalu sederhana." 
    
    adrian "Kota ini tidak rusak." 
    adrian "Ia hanya… disederhanakan." 
    nara "Lo sebut ini ‘sederhana’?" 
    adrian "Lebih tepatnya menjadi efisien." 
    adrian "Orang tidak perlu bingung memilih." 
    adrian "Tidak perlu takut salah ataupun gagal." 
    adrian "Tidak perlu berharap pada sesuatu yang tidak bekerja." 
    nara "Yang tidak bekerja… atau yang lu bunuh?" 
    
    pause 
    
    "Adrian tidak langsung jawab." 
    
    adrian "Aku tidak membunuh apa pun." 
    adrian "Aku hanya memilih apa yang pantas untuk bertahan." 
    raka "Dengan membuat orang benci miliknya sendiri?" 
    
    "Adrian menatap Raka lebih dalam." 
    
    adrian "Itu hanya ada dalam narasimu." 
    
    pause 
    
    "Raka diam." 
    
    adrian "Dan kau menulis narasinya dengan sangat baik." 
    
    "Adrian melangkah pelan." 
    
    adrian "Aku lihat perubahanmu Raka." 
    adrian "Kau berjalan pada pilihan dengan ragu." 
    adrian "Kau mulai berpikir atas pilihanmu." 
    adrian "Itu hal yang bagus." 
    
    pause 
    
    adrian "Tapi pada akhirnya kau masih tetap di sini." 
    adrian "Artinya kau tahu…" 
    adrian "Bahwa di luar sana tidak ada yang lebih baik." 
    nara "Itu karena system yang lu buat memastikan untuk tetap begitu!" 
    adrian "Tidak." 
    adrian "Karena manusia tidaklah konsisten." 
    adrian "Mereka membutuhkan arah." 
    adrian "Dan kalau mereka tidak bisa memilih apa yang benar untuknya" 
    adrian "Dan kita hadir untuk memilihkan." 
    
    adrian "Aku tidak akan menghentikan tujuan kalian." 
    
    pause 
    
    nara "Omong kosong!" 
    adrian "Aku serius, dengan pernyataanku" 
    
    show adrian kantor serius:
        xalign 0.5
        yalign 1.1  
        zoom 0.85

    "Adrian menatap Raka." 
    
    adrian "Aku akan memberikan kebebasan untukmu Raka, dan itukan yang kau mau?." 
    adrian "Serahkan dia." 
    
    "Adrian menunjuk Nara." 
    
    adrian "Aku pastikan, kau tidak hanya aman." 
    adrian "Kau akan naik." 
    adrian "Jauh lebih tinggi dari sebelumnya dengan kehidupan yang nyaman." 
    
    pause 
    
    adrian "Atau…" 
    
    "Adrian melihat sekitar." 
    
    adrian "Melanjutkan tujuan kalian." 
    adrian "Menghancurkan semuanya, menghancurkan system ‘kebebasan’ mu itu." 
    adrian "Dan lihat berapa banyak yang ikut jatuh, berapa banyak kekacauan yang akan kau sebabkan." 

    # FINAL DECISION TREE
    if has_gun: 
        menu: 
            "Apa yang dilakukan Raka?"
            
            "Tembak Adrian": 
                jump ending_kill 
            
            "Hancurkan core": 
                jump ending_chaos 
            
            "Turunkan senjata": 
                jump decision_no_gun 
    else:
        jump decision_no_gun 

label decision_no_gun: 
    menu: 
        "Apa pilihan Raka?"            

        "Sebarkan semua data ke publik": 
            jump ending_true 
            
        "Serahkan Nara": 
            jump ending_bad 
            
        "Diam… tidak melakukan apa-apa": 
            jump ending_sad