# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

 DEFINISI KARAKTER UTAMA
define raka = Character("Raka Pradana", color="#00ffff")
define nara = Character("Nara Wisesa", color="#ffaa00")
define adrian = Character("Adrian Wiratma", color="#ffffff")

# karakter sampingan
define system = Character("SISTEM MIRROR", color="#ff00ff", who_suffix=":", what_italic=True)
define narrator = Character(None, what_italic=True)
define worker = Character("Worker", color="#aaaaaa")
define ayah = Character("Ayah", color="#ff0000")

# DEFINISI BACKGROUND
image apartemen_raka:
    "assets/background/APARTEMEN RAKA.jpg"
    size (config.screen_width, config.screen_height)

image community_hub:
    "assets/background/community_hub.png"
    size (config.screen_width, config.screen_height)

image community_hub2:
    "assets/background/community_hub2.png"
    size (config.screen_width, config.screen_height)

image gang_tua_malam:
    "assets/background/GANG TUA MALAM.jpg"
    size (config.screen_width, config.screen_height)

image gang_tua_pagi:
    "assets/background/GANG TUA PAGI.png"
    size (config.screen_width, config.screen_height)

image interogation_room:
    "assets/background/interogation_room.png"
    size (config.screen_width, config.screen_height)

image jaringan_bawah_tanah_1:
    "assets/background/JARINGAN BAWAH TANAH 1.jpg"
    size (config.screen_width, config.screen_height)

image jaringan_bawah_tanah_2:
    "assets/background/JARINGAN BAWAH TANAH 2.jpg"
    size (config.screen_width, config.screen_height)

image kantor_elite_adrian:
    "assets/background/KANTOR ELITE_ RUANG ADRIAN.jpg"
    size (config.screen_width, config.screen_height)

image kantor_mirror_pusat:
    "assets/background/KANTOR MIRROR (PUSAT OPERASI).jpg"
    size (config.screen_width, config.screen_height)

image kota_nawasena:
    "assets/background/KOTA NAWASENA.jpg"
    size (config.screen_width, config.screen_height)

image kota_saat_chaos:
    "assets/background/KOTA SAAT CHAOS.jpg"
    size (config.screen_width, config.screen_height)

image minister_room_adrian:
    "assets/background/minister_room_(adrian).png"
    size (config.screen_width, config.screen_height)

image mirror_pusat_kendali:
    "assets/background/MIRROR PUSAT KENDALI.jpg"
    size (config.screen_width, config.screen_height)

# DEFINISI KARAKTER png
#Raka
image raka formal marah = "assets/character/raka_pradana/kostum_formal/Formal_Marah.png"
image raka formal neutral = "assets/character/raka_pradana/kostum_formal/Formal_Neutral.png"
image raka formal sedih = "assets/character/raka_pradana/kostum_formal/Formal_Sedih.png"
image raka formal senyum = "assets/character/raka_pradana/kostum_formal/Formal_Senyum.png"
image raka formal serius = "assets/character/raka_pradana/kostum_formal/Formal_Serius.png"
image raka formal terkejut = "assets/character/raka_pradana/kostum_formal/Formal_terkejut.png"

image raka casual marah = "assets/character/raka_pradana/kostum_casual/Casual_Marah.png"
image raka casual neutral = "assets/character/raka_pradana/kostum_casual/Casual_Neutral.png"
image raka casual sedih = "assets/character/raka_pradana/kostum_casual/Casual_Sedih.png"
image raka casual senyum = "assets/character/raka_pradana/kostum_casual/Casual_Senyum.png"
image raka casual serius = "assets/character/raka_pradana/kostum_casual/Casual_Serius.png"
image raka casual terkejut = "assets/character/raka_pradana/kostum_casual/Casual_terkejut.png"

image raka rebel marah = "assets/character/raka_pradana/kostum_rebel/Rebel_Marah.png"
image raka rebel neutral = "assets/character/raka_pradana/kostum_rebel/rebel_Neutral.png"
image raka rebel sedih = "assets/character/raka_pradana/kostum_rebel/Rebel_Sedih.png"
image raka rebel senyum = "assets/character/raka_pradana/kostum_rebel/Rebel_Senyum.png"
image raka rebel serius = "assets/character/raka_pradana/kostum_rebel/Rebel_Serius.png"
image raka rebel terkejut = "assets/character/raka_pradana/kostum_rebel/Rebel_terkejut.png"

#Adrian
image adrian jas marah = "assets/character/adrian_wiratma/kostum_jas/Jas_Marah.png"
image adrian jas neutral = "assets/character/adrian_wiratma/kostum_jas/Jas_Neutral.png"
image adrian jas sedih = "assets/character/adrian_wiratma/kostum_jas/Jas_Sedih.png"
image adrian jas senyum = "assets/character/adrian_wiratma/kostum_jas/Jas_Senyum.png"
image adrian jas serius = "assets/character/adrian_wiratma/kostum_jas/Jas_Serius.png"
image adrian jas terkejut = "assets/character/adrian_wiratma/kostum_jas/Jas_terkejut.png"

image adrian kantor marah = "assets/character/adrian_wiratma/kostum_kantor/Kantor_Marah.png"
image adrian kantor neutral = "assets/character/adrian_wiratma/kostum_kantor/Kantor_Neutral.png"
image adrian kantor sedih = "assets/character/adrian_wiratma/kostum_kantor/Kantor_Sedih.png"
image adrian kantor senyum = "assets/character/adrian_wiratma/kostum_kantor/Kantor_Senyum.png"
image adrian kantor serius = "assets/character/adrian_wiratma/kostum_kantor/Kantor_Serius.png"
image adrian kantor terkejut = "assets/character/adrian_wiratma/kostum_kantor/Kantor_terkejut.png"

image adrian santai marah = "assets/character/adrian_wiratma/kostum_santai/Santai_Marah.png"
image adrian santai neutral = "assets/character/adrian_wiratma/kostum_santai/Santai_Neutral.png"
image adrian santai sedih = "assets/character/adrian_wiratma/kostum_santai/Santai_Sedih.png"
image adrian santai senyum = "assets/character/adrian_wiratma/kostum_santai/Santai_Senyum.png"
image adrian santai serius = "assets/character/adrian_wiratma/kostum_santai/Santai_Serius.png"
image adrian santai terkejut = "assets/character/adrian_wiratma/kostum_santai/Santai_terkejut.png"

#Nara
image nara retro marah = "assets/character/nara_wisesa/kostum_retro/Retro_Marah.png"
image nara retro neutral = "assets/character/nara_wisesa/kostum_retro/Retro_Neutral.png"
image nara retro sedih = "assets/character/nara_wisesa/kostum_retro/Retro_Sedih.png"
image nara retro senyum = "assets/character/nara_wisesa/kostum_retro/Retro_Senyum.png"
image nara retro serius = "assets/character/nara_wisesa/kostum_retro/Retro_Serius.png"
image nara retro terkejut = "assets/character/nara_wisesa/kostum_retro/Retro_terkejut.png"

image nara eksplor marah = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_Marah.png"
image nara eksplor neutral = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_Neutral.png"
image nara eksplor sedih = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_Sedih.png"
image nara eksplor senyum = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_Senyum.png"
image nara eksplor serius = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_Serius.png"
image nara eksplor terkejut = "assets/character/nara_wisesa/kostum_eksplor/Eksplor_terkejut.png"

image nara bengkel marah = "assets/character/nara_wisesa/kostum_bengkel/Bengkel_Marah.png"
image nara bengkel neutral = "assets/character/nara_wisesa/kostum_bengkel/Bengkel_Neutral.png"
image nara bengkel sedih = "assets/character/nara_wisesa/kost_bengkel/Bengkel_Sedih.png"
image nara bengkel senyum = "assets/character/nara_wisesa/kostum_bengkel/Bengkel_Senyum.png"
image nara bengkel serius = "assets/character/nara_wisesa/kostum_bengkel/Bengkel_Serius.png"
image nara bengkel terkejut = "assets/character/nara_wisesa/kostum_bengkel/Bengkel_terkejut.png"

# The game starts here.
label start:

    #
    # SCENE !
    #
    call scene1
    call scene2
    call scene3
    call scene4
    call scene5
    call scene6
    call scene7
    call scene8 
    call scene9
    call scene10
    call scene11
    call scene12
    call scene13
    call scene14
    call scene15
    call scene16
    call scene17


    show eileen happy

    # These display lines of dialogue.

    e "tes tes tis tes"

    e "jakang sf terbagus"

    # This ends the game.

    return
