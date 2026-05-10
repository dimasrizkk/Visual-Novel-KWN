label scene21B:

    if active_path >= 1:
        
        scene alley_run 
        with fade 
        play music "urgent_run.ogg" 
        "Langkah Raka cepat." 
        "Kota yang biasanya terasa aman kini terasa seperti labirin pengawasan." 

        sound "drone_pass.ogg" 

            "Drone melintas." 
        "Lebih banyak dari biasanya." 
        "Lebih rendah." 
        "Lebih diam." 

        scene ruang_sisa_outside_dark 
        with dissolve 

        "Lampu Ruang Sisa mati." 
        "Pintu terbuka setengah." 
        "Tidak ada suara." 

        raka "...Nara?" 

        scene ruang_sisa_inside_chaos 
        with dissolve 

        play music "collapse.ogg" 

        "Kacau." 
        "Rak jatuh."

        "Barang berserakan." 
        "Beberapa alat masih panas." 
        "Seolah semua orang pergi terburu-buru." 

        sound "distant_footsteps.ogg" 

        nara (offscreen) "Raka!" 

        scene back_exit 
        with dissolve 

        show nara tense at center 
        
        nara "Lo datang." 
        raka "Apa yang terjadi?" 
        nara "Mereka nggak serbu langsung." 
        nara "Mereka matiin akses dulu." 
        nara "Bekuin transaksi." 
        nara "Ganggu komunikasi." 
        nara "Bikin kita panik." 
        raka "Klasik." 
        nara "Efektif." 

        sound "metal_door_bang.ogg" 
        "Suara keras dari atas." 

        nara "...Mereka di sini." 
        "Bukan tentara." 
        "Bukan polisi biasa." 
        "Unit penertiban sistem." 
        "Lebih cepat." 
        "Lebih diam." 
        "Lebih tidak terlihat."

    return