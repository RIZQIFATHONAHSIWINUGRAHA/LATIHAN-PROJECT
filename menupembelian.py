# Dictionary untuk menyimpan daftar menu beserta harganya
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Goreng": 18000,
    "Es Teh Manis": 5000,
    "Es Jeruk": 6000
}

# Diskon untuk pembelian di atas 50000
diskon = 0.1  # 10%

# Daftar menu yang termasuk dalam bundling
bundling = ["Nasi Goreng", "Es Teh Manis"]

# Inisialisasi variabel total harga
total_harga = 0

# Meminta pengguna untuk memilih menu
while True:
    print("\nDaftar Menu:")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga}")

    pilihan = input("Masukkan menu yang dipilih (ketik 'selesai' untuk selesai): ")

    if pilihan.lower() == "selesai":
        break

    if pilihan in menu:
        total_harga += menu[pilihan]
        print(f"{pilihan} telah ditambahkan ke keranjang.")
    else:
        print("Menu tidak valid, silakan pilih kembali.")

# Memeriksa apakah pembelian memenuhi syarat untuk diskon
if total_harga > 50000:
    total_harga -= total_harga * diskon
    print(f"\nDiskon 10% diterapkan!")

# Memeriksa apakah ada bundling
if all(item in menu for item in bundling):
    print("\nAnda mendapatkan bundling Nasi Goreng + Es Teh Manis dengan harga spesial!")
    total_harga -= menu["Nasi Goreng"] + menu["Es Teh Manis"]

# Menampilkan total harga
print(f"\nTotal harga belanja: Rp {total_harga}")
