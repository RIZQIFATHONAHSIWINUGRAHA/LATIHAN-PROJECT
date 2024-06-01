def tambah_barang(inventaris, nama_barang):
    # Mengubah nama_barang menjadi huruf kecil untuk pengecekan
    nama_barang_lower = nama_barang.lower()
    # Mengecek apakah nama_barang sudah ada di dalam inventaris (dengan mengabaikan kapitalisasi)
    if any(barang.lower() == nama_barang_lower for barang in inventaris):
        # Jika nama_barang sudah ada, cetak pesan bahwa barang sudah ada
        print(f"Barang '{nama_barang}' sudah ada di dalam inventaris.")
    else:
        # Jika nama_barang belum ada, tambahkan ke inventaris dan cetak pesan sukses
        inventaris.append(nama_barang)
        print(f"Barang '{nama_barang}' berhasil ditambahkan ke dalam inventaris.")

def tampilkan_inventaris(inventaris):
    # Mengecek apakah inventaris kosong
    if len(inventaris) == 0:
        # Jika inventaris kosong, cetak pesan bahwa inventaris kosong
        print("Inventaris kosong.")
    else:
        # Jika inventaris tidak kosong, cetak daftar barang dalam inventaris
        print("Daftar barang dalam inventaris:")
        for barang in inventaris:
            # Cetak setiap barang yang ada di dalam inventaris
            print(f"- {barang}")

def main():
    # Membuat daftar inventaris kosong
    inventaris = []
    while True:
        # Meminta pengguna memasukkan nama barang
        nama_barang = input("Masukkan nama barang (ketik 'selesai' untuk mengakhiri): ")
        # Jika pengguna mengetik 'selesai', keluar dari loop
        if nama_barang.lower() == 'selesai':
            break
        # Memanggil method tambah_barang untuk menambahkan barang ke dalam inventaris
        tambah_barang(inventaris, nama_barang)
    
    # Setelah pengguna selesai menambahkan barang, tampilkan seluruh daftar inventaris
    tampilkan_inventaris(inventaris)

if __name__ == "__main__":
    # Memanggil fungsi main untuk menjalankan program
    main()
