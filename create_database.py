import sqlite3
import os

# Membuat folder database jika belum ada
os.makedirs("database", exist_ok=True)

# Membuat / membuka database
connection = sqlite3.connect("database/reuse_smart.db")

cursor = connection.cursor()

# =========================
# TABEL BARANG
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS barang (
    id_barang INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_barang TEXT NOT NULL,
    kategori TEXT NOT NULL,
    deskripsi TEXT
)
""")

# =========================
# TABEL REKOMENDASI
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS rekomendasi (
    id_rekomendasi INTEGER PRIMARY KEY AUTOINCREMENT,
    id_barang INTEGER NOT NULL,
    nama_rekomendasi TEXT NOT NULL,
    deskripsi TEXT,
    tingkat_kesulitan TEXT,
    kategori_pemanfaatan TEXT,
    
    FOREIGN KEY (id_barang)
    REFERENCES barang(id_barang)
)
""")

# =========================
# DATA BARANG
# =========================

barang = [
    ("Botol plastik", "Plastik",
     "Botol berbahan plastik yang sudah tidak digunakan."),

    ("Botol kaca", "Kaca",
     "Botol berbahan kaca yang sudah tidak digunakan."),

    ("Kardus", "Kertas",
     "Kardus bekas yang masih dapat dimanfaatkan kembali."),

    ("Kaleng", "Logam",
     "Kaleng bekas dari makanan atau minuman."),

    ("Koran", "Kertas",
     "Koran bekas yang sudah tidak digunakan."),

    ("Kertas", "Kertas",
     "Kertas bekas yang masih dapat digunakan kembali."),

    ("Plastik kemasan", "Plastik",
     "Kemasan plastik bekas dari berbagai produk."),

    ("Pakaian bekas", "Tekstil",
     "Pakaian yang sudah tidak digunakan tetapi masih dapat dimanfaatkan."),

    ("Ban bekas", "Karet",
     "Ban kendaraan yang sudah tidak digunakan."),

    ("Kayu", "Kayu",
     "Potongan atau sisa kayu yang masih dapat dimanfaatkan.")
]

cursor.executemany("""
INSERT INTO barang
(nama_barang, kategori, deskripsi)
VALUES (?, ?, ?)
""", barang)


# =========================
# DATA REKOMENDASI
# =========================

rekomendasi = [

    # BOTOL PLASTIK
    (1, "Pot tanaman",
     "Botol plastik dapat dipotong dan digunakan sebagai pot tanaman kecil.",
     "Mudah", "Pertanian"),

    (1, "Tempat pensil",
     "Bagian botol dapat digunakan sebagai tempat menyimpan alat tulis.",
     "Mudah", "Rumah Tangga"),

    (1, "Wadah penyimpanan",
     "Botol dapat digunakan untuk menyimpan benda berukuran kecil.",
     "Mudah", "Rumah Tangga"),

    (1, "Dekorasi",
     "Botol dapat diubah menjadi berbagai macam hiasan.",
     "Sedang", "Kerajinan"),


    # BOTOL KACA
    (2, "Vas bunga",
     "Botol kaca dapat digunakan sebagai wadah bunga.",
     "Mudah", "Dekorasi"),

    (2, "Wadah bumbu",
     "Botol kaca dapat digunakan untuk menyimpan bumbu tertentu.",
     "Mudah", "Rumah Tangga"),

    (2, "Tempat lilin",
     "Botol kaca dapat dimanfaatkan sebagai wadah dekorasi lilin.",
     "Sedang", "Dekorasi"),

    (2, "Dekorasi",
     "Botol kaca dapat dihias dan digunakan sebagai dekorasi ruangan.",
     "Sedang", "Kerajinan"),


    # KARDUS
    (3, "Kotak penyimpanan",
     "Kardus dapat digunakan untuk menyimpan berbagai barang.",
     "Mudah", "Rumah Tangga"),

    (3, "Organizer meja",
     "Kardus dapat dibuat menjadi tempat penyimpanan alat tulis.",
     "Sedang", "Rumah Tangga"),

    (3, "Rak sederhana",
     "Beberapa kardus dapat dirangkai menjadi rak sederhana.",
     "Sedang", "Rumah Tangga"),

    (3, "Bahan kerajinan",
     "Kardus dapat digunakan sebagai bahan membuat berbagai kerajinan.",
     "Mudah", "Kerajinan"),


    # KALENG
    (4, "Pot tanaman",
     "Kaleng dapat dibersihkan dan digunakan sebagai pot.",
     "Mudah", "Pertanian"),

    (4, "Tempat alat tulis",
     "Kaleng dapat digunakan untuk menyimpan alat tulis.",
     "Mudah", "Rumah Tangga"),

    (4, "Wadah penyimpanan",
     "Kaleng dapat digunakan untuk menyimpan benda kecil.",
     "Mudah", "Rumah Tangga"),

    (4, "Tempat lilin",
     "Kaleng dapat dimodifikasi menjadi tempat lilin dekoratif.",
     "Sedang", "Dekorasi"),


    # KORAN
    (5, "Kerajinan kertas",
     "Koran dapat digunakan sebagai bahan berbagai kerajinan.",
     "Sedang", "Kerajinan"),

    (5, "Pembungkus barang",
     "Koran dapat digunakan sebagai bahan pembungkus.",
     "Mudah", "Rumah Tangga"),

    (5, "Bahan anyaman",
     "Koran dapat digulung dan digunakan sebagai bahan anyaman.",
     "Sulit", "Kerajinan"),

    (5, "Bahan kompos",
     "Koran tertentu dapat digunakan sebagai salah satu bahan kompos.",
     "Sedang", "Lingkungan"),


    # KERTAS
    (6, "Kertas daur ulang",
     "Kertas bekas dapat diolah kembali menjadi kertas daur ulang.",
     "Sulit", "Lingkungan"),

    (6, "Kerajinan",
     "Kertas dapat digunakan untuk membuat berbagai kerajinan.",
     "Mudah", "Kerajinan"),

    (6, "Catatan",
     "Sisi kertas yang masih kosong dapat digunakan untuk mencatat.",
     "Mudah", "Pendidikan"),

    (6, "Pembungkus",
     "Kertas dapat dimanfaatkan sebagai bahan pembungkus.",
     "Mudah", "Rumah Tangga"),


    # PLASTIK KEMASAN
    (7, "Ecobrick",
     "Plastik kemasan dapat dikumpulkan dan dimanfaatkan sebagai bahan ecobrick.",
     "Sedang", "Lingkungan"),

    (7, "Kerajinan",
     "Plastik kemasan dapat digunakan sebagai bahan kerajinan.",
     "Sedang", "Kerajinan"),

    (7, "Tempat penyimpanan",
     "Kemasan tertentu dapat digunakan untuk menyimpan benda kecil.",
     "Mudah", "Rumah Tangga"),

    (7, "Dekorasi",
     "Plastik kemasan dapat dimanfaatkan sebagai bahan dekorasi.",
     "Sedang", "Kerajinan"),


    # PAKAIAN BEKAS
    (8, "Lap kain",
     "Pakaian yang sudah tidak layak pakai dapat dipotong menjadi lap.",
     "Mudah", "Rumah Tangga"),

    (8, "Tas sederhana",
     "Pakaian tertentu dapat dijahit kembali menjadi tas.",
     "Sedang", "Kerajinan"),

    (8, "Sarung bantal",
     "Kain pakaian dapat dimanfaatkan sebagai bahan sarung bantal.",
     "Sedang", "Rumah Tangga"),

    (8, "Donasi",
     "Pakaian yang masih layak dapat diberikan kepada pihak yang membutuhkan.",
     "Mudah", "Sosial"),


    # BAN BEKAS
    (9, "Pot tanaman",
     "Ban bekas dapat digunakan sebagai pot tanaman berukuran besar.",
     "Sedang", "Pertanian"),

    (9, "Kursi",
     "Ban dapat digunakan sebagai bahan dasar kursi sederhana.",
     "Sulit", "Furnitur"),

    (9, "Meja kecil",
     "Ban dapat dikombinasikan dengan papan untuk membuat meja.",
     "Sulit", "Furnitur"),

    (9, "Dekorasi taman",
     "Ban dapat dicat dan digunakan sebagai dekorasi taman.",
     "Sedang", "Dekorasi"),


    # KAYU
    (10, "Rak sederhana",
     "Potongan kayu dapat digunakan sebagai bahan rak.",
     "Sedang", "Furnitur"),

    (10, "Papan dekorasi",
     "Kayu dapat digunakan sebagai papan dekorasi.",
     "Mudah", "Dekorasi"),

    (10, "Pot tanaman",
     "Kayu dapat digunakan sebagai bahan pot atau wadah tanaman.",
     "Sedang", "Pertanian"),

    (10, "Furnitur sederhana",
     "Kayu bekas dapat dimanfaatkan sebagai bahan furnitur.",
     "Sulit", "Furnitur")
]

cursor.executemany("""
INSERT INTO rekomendasi
(
    id_barang,
    nama_rekomendasi,
    deskripsi,
    tingkat_kesulitan,
    kategori_pemanfaatan
)
VALUES (?, ?, ?, ?, ?)
""", rekomendasi)


# Menyimpan perubahan
connection.commit()

# Menutup database
connection.close()

print("Database berhasil dibuat!")