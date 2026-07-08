# =========================================
# MINI PROJECT DFK50083
# Sistem Pengurusan & Pesanan Kedai Buku
# =========================================

# -----------------------------
# Bahagian 1
# -----------------------------

data_mentah = " b001:mUdaHnya pYtHon:39.90:5 , b002:bElAjAr dAtA sCieNce:49.90:2 , b003:aSaS a.i. uNtUk pEmUlA:55.00:0 "

# Buang ruang kosong
data_mentah = data_mentah.strip()

# Split ikut koma
senarai_buku = data_mentah.split(",")

# Simpan data bersih
data_bersih = []

for buku in senarai_buku:

    buku = buku.strip()

    info = buku.split(":")

    id_buku = info[0].upper()
    tajuk = info[1].title()
    harga = float(info[2])
    stok = int(info[3])

    data_bersih.append((id_buku, tajuk, harga, stok))

print("===== DATA BERSIH =====")
for item in data_bersih:
    print(item)

# -----------------------------
# Bahagian 2
# -----------------------------

inventori = {}

for item in data_bersih:

    inventori[item[0]] = (item[1], item[2], item[3])

print("\n===== INVENTORI =====")
print(inventori)

# Tambah stok B002

tajuk, harga, stok = inventori["B002"]

inventori["B002"] = (tajuk, harga, stok + 10)

print("\nInventori selepas tambah stok B002")
print(inventori)

# -----------------------------
# Bahagian 3
# -----------------------------

genre_haziq = {"Teknologi", "Sains", "Biografi", "Fiksyen"}

genre_siti = {
    "Masakan",
    "Sains",
    "Novel",
    "Teknologi",
    "Kesihatan"
}

sama = genre_haziq.intersection(genre_siti)

beza = genre_haziq.difference(genre_siti)

semua_genre = genre_haziq.union(genre_siti)

print("\n===== ANALISIS SET =====")
print("Genre sama :", sama)
print("Genre Haziq sahaja :", beza)
print("Semua genre :", semua_genre)

# -----------------------------
# Bahagian 4
# -----------------------------

pesanan_pelanggan = ["B001", "B003", "B001", "B999"]

jumlah_bil = 0.0

buku_gagal_dibeli = []

for id_buku in pesanan_pelanggan:

    if id_buku not in inventori:

        print("Ralat: Buku", id_buku, "tidak wujud!")

        buku_gagal_dibeli.append(id_buku)

    else:

        tajuk, harga, stok = inventori[id_buku]

        if stok > 0:

            jumlah_bil += harga

            inventori[id_buku] = (tajuk, harga, stok - 1)

        else:

            print("Maaf, Buku", tajuk, "telah habis stok!")

            buku_gagal_dibeli.append(id_buku)

print("\n==========================")
print("KEPUTUSAN AKHIR")
print("==========================")

print("\nInventori Akhir")
print(inventori)

print("\nJumlah Bil = RM{:.2f}".format(jumlah_bil))

print("\nBuku Gagal Dibeli")
print(buku_gagal_dibeli)

print("\nGenre Sama")
print(sama)

print("\nGenre Haziq Sahaja")
print(beza)

print("\nSemua Genre")
print(semua_genre)