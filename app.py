from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Folder upload
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ==========================================
# FUNGSI KONEKSI DATABASE
# ==========================================

def get_db_connection():

    connection = sqlite3.connect(
        "database/reuse_smart.db"
    )

    connection.row_factory = sqlite3.Row

    return connection


# ==========================================
# HALAMAN UTAMA
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/identifikasi")
def identifikasi():
    return render_template("identifikasi.html")


# ==========================================
# PROSES UPLOAD
# ==========================================

@app.route("/upload", methods=["POST"])
def upload():

    # Mengambil foto
    foto = request.files.get("foto")

    if foto is None or foto.filename == "":
        return "Tidak ada foto yang dipilih."

    # Menyimpan foto
    lokasi = os.path.join(
        app.config["UPLOAD_FOLDER"],
        foto.filename
    )

    foto.save(lokasi)


    # ==========================================
    # SEMENTARA:
    # ID BARANG MASIH DITENTUKAN MANUAL
    # ==========================================

    id_barang = 1


    # ==========================================
    # MENGAMBIL DATA DARI DATABASE
    # ==========================================

    connection = get_db_connection()


    # Mengambil data barang
    barang = connection.execute(
        """
        SELECT *
        FROM barang
        WHERE id_barang = ?
        """,
        (id_barang,)
    ).fetchone()


    # Mengambil rekomendasi
    rekomendasi = connection.execute(
        """
        SELECT *
        FROM rekomendasi
        WHERE id_barang = ?
        """,
        (id_barang,)
    ).fetchall()


    connection.close()


    # ==========================================
    # MENAMPILKAN HASIL
    # ==========================================

    return render_template(
        "hasil.html",
        barang=barang,
        rekomendasi=rekomendasi,
        foto=foto.filename
    )


# ==========================================
# MENJALANKAN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)