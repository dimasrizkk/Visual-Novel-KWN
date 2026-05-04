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