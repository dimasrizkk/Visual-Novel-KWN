## ============================================================
##  MIRROR — Visual Novel
##  File    : characters.rpy
##  Isi     : Semua definisi karakter & variabel flag global
##  Catatan : File ini dibaca otomatis oleh Ren'Py saat startup
## ============================================================

## ── NARRATOR ─────────────────────────────────────────────────
## Narrator cukup pakai tanda kutip biasa: "teks narasi"
## Tidak perlu define khusus — Ren'Py sudah handle otomatis.

## ── CHARACTER DEFINITIONS ────────────────────────────────────

define raka          = Character("Raka",             color="#a8d8ea")
define nara          = Character("Nara",             color="#f7c59f")
define adrian        = Character("Adrian",           color="#c8a2c8")

define system        = Character("[ SISTEM ]",       color="#00e5ff", what_color="#00e5ff")

define pengrajin1    = Character("Pengrajin",        color="#c8b89a")
define penjahit      = Character("Penjahit",         color="#c8b89a")
define pengrajin_tua = Character("Pak Jaya",         color="#d4b896")
define anak          = Character("Anak Kecil",       color="#ffe4b5")

define adrian_voice  = Character("[ Suara Adrian ]", color="#c8a2c8", what_italic=True)
define nara_voice    = Character("[ Suara Nara ]",   color="#f7c59f", what_italic=True)

## ── FLAG VARIABLES ───────────────────────────────────────────

define worker = Character("Worker")
define ayah = Character("Ayah", what_italic=True) #deklarasi utk suara memori scene5
define worker1 = Character("Worker 1") #deklarasi utk scene 8
define worker2 = Character("Worker 2")
define worker3 = Character("Worker 3")
define penjaga = Character("Penjaga") #deklarasi utk scene 9
define old_woman = Character("Nenek Tua")
define pedagang = Character("Suara Pedagang", what_italic=True)
define anak_kecil = Character("Suara Anak Kecil", what_italic=True)
define kerumunan = Character("Kerumunan") #deklarasi utk scene 10
define ibu = Character("Ibu")
define nara = Character("Nara") #deklarasi utk scene 11
define penyiar = Character("Penyiar Radio", what_italic=True) #deklarasi utk scene 12
define analyst = Character("Senior Analyst") #deklarasi utk scene 17
define guard_core = Character("Penjaga_Core_Mirror")

#default loyalty   = 0
#default awareness = 0
#default ambition  = 0
default rebellion = 0
default doubt     = 0
default betrayal  = 0
#default ruthless  = 0

# Inisialisasi Variabel Poin (Sangat penting agar tidak error saat ditambah)
default ambition = 0
default ruthless = 0
default loyalty = 0
default awareness = 0  
default trust_nara = 0 #variabel scene 16