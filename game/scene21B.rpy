label scene21b:

    if active_path >= 1:
        
        scene alley_run with fade 
        
        # Memutar BGM bertema pengejaran/terburu-buru
        play music "urgent_run.ogg" fadein 1.0
        
        "Langkah Raka cepat." 
        "Kota yang biasanya terasa aman kini terasa seperti labirin pengawasan." 

        # SFX Drone pengawas melintas di atas kepala
        play sound "drone_pass.ogg" 

        "Drone melintas. Lebih banyak dari biasanya. Lebih rendah. Lebih diam." 

        scene ruang_sisa_outside_dark with dissolve 

        "Lampu Ruang Sisa mati. Pintu terbuka setengah." 
        "Tidak ada suara." 

        raka "...Nara?" 

        scene ruang_sisa_inside_chaos with dissolve 

        # Mengganti BGM untuk membangun suasana kehancuran
        play music "collapse.ogg" fadein 2.0

        "Kacau. Rak jatuh." 
        "Barang berserakan. Beberapa alat masih panas, seolah semua orang pergi terburu-buru." 

        # SFX Langkah kaki misterius dari kejauhan
        play sound "distant_footsteps.ogg" 

        # Menggunakan narasi offscreen sebelum karakter muncul secara visual
        nara "(offscreen) Raka!" 

        scene back_exit with dissolve 

        # Nara muncul dalam kondisi tegang/panik di posisi tengah
        show Eksplor_Tense:
            xalign 0.5
            yalign 1.1
            zoom 0.85
        with dissolve
        
        nara "Lo datang." 
        
        raka "Apa yang terjadi?" 
        
        nara "Mereka nggak serbu langsung. Mereka matiin akses dulu. Bekuin transaksi. Ganggu komunikasi." 
        nara "Bikin kita panik." 
        
        raka "Klasik." 
        
        nara "Efektif." 

        # SFX Pintu besi digedor keras dari lantai atas
        play sound "metal_door_bang.ogg" 
        
        "Suara keras dari atas." 

        show Eksplor_Tense:
            xalign 0.5
            yalign 1.1
            zoom 0.85

        nara "...Mereka di sini." 
        
        "Bukan tentara. Bukan polisi biasa." 
        "Unit penertiban sistem. Lebih cepat. Lebih diam. Lebih tidak terlihat."

    # Menghentikan audio secara dramatis sebelum pindah ke scene berikutnya
    stop music fadeout 2.0
    stop sound fadeout 1.0

    return
