from flask import Flask, render_template, request
import sqlite3
import base64

app = Flask(__name__)


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


# ==========================================
# HALAMAN IDENTIFIKASI
# ==========================================

@app.route("/identifikasi")
def identifikasi():

    return render_template("identifikasi.html")


# ==========================================
# PROSES UPLOAD FOTO
# ==========================================

@app.route("/upload", methods=["POST"])
def upload():

    foto = request.files.get("foto")

    if foto is None or foto.filename == "":
        return "Tidak ada foto yang dipilih."

    # ==========================================
    # MEMBACA FOTO LANGSUNG KE MEMORY
    # ==========================================

    foto_data = foto.read()

    foto_base64 = base64.b64encode(
        foto_data
    ).decode("utf-8")

    content_type = foto.content_type or "image/jpeg"

    foto_url = f"data:{content_type};base64,{foto_base64}"


    # ==========================================
    # SEMENTARA
    # ID BARANG MASIH MANUAL
    # ==========================================

    id_barang = 1


    # ==========================================
    # MENGAMBIL DATA DATABASE
    # ==========================================

    connection = get_db_connection()

    barang = connection.execute(
        """
        SELECT *
        FROM barang
        WHERE id_barang = ?
        """,
        (id_barang,)
    ).fetchone()

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
        foto_url=foto_url
    )


# ==========================================
# MENJALANKAN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
