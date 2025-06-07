import time
from datetime import datetime, timedelta

# ================================
# Bagian 1: Data Sementara (Simulasi Database)
# ================================
users = {}  # Menyimpan akun pengguna, format: {username: {"password": str, "phone": str}}

products = {
    "kopi": {"price": 10000, "stock": 10},
    "teh": {"price": 8000, "stock": 20}
}

# ================================
# Bagian 2: Fitur Akun Pengguna
# ================================

def create_account():
    """Membuat akun baru"""
    username = input("Buat Username: ")
    if username in users:
        print("Username sudah ada.\n")
        return
    password = input("Buat Password: ")
    phone = input("Masukkan Nomor HP: ")
    users[username] = {"password": password, "phone": phone}
    print("Akun berhasil dibuat!\n")

def login():
    """Login pengguna"""
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print("Login berhasil!\n")
        return username
    else:
        print("Login gagal.\n")
        return None

def forgot_password():
    """Reset password jika lupa, dengan verifikasi nomor HP"""
    username = input("Masukkan Username: ")
    if username in users:
        phone = input("Masukkan Nomor HP: ")
        if users[username]["phone"] == phone:
            new_pass = input("Masukkan Password Baru: ")
            users[username]["password"] = new_pass
            print("Password berhasil diubah!\n")
        else:
            print("Nomor HP tidak cocok.\n")
    else:
        print("Username tidak ditemukan.\n")

# ================================
# Bagian 3: Fitur Produk dan Kasir
# ================================

def show_menu():
    """Menampilkan daftar produk yang tersedia"""
    print("\n--- MENU PRODUK ---")
    for item, info in products.items():
        print(f"{item.title()} - Rp{info['price']} - Stok: {info['stock']}")

def buy_item(cart):
    """Menambahkan produk ke keranjang belanja"""
    item = input("Masukkan nama produk: ").lower()
    if item in products:
        qty = int(input("Jumlah: "))
        if qty <= products[item]["stock"]:
            cart[item] = cart.get(item, 0) + qty
            print("Produk ditambahkan ke keranjang.\n")
        else:
            print("Stok tidak cukup.\n")
    else:
        print("Produk tidak ditemukan.\n")

def add_item():
    """Menambahkan produk baru ke sistem"""
    item = input("Nama produk baru: ").lower()
    if item not in products:
        price = int(input("Harga: "))
        stock = int(input("Stok: "))
        products[item] = {"price": price, "stock": stock}
        print("Produk berhasil ditambahkan.\n")
    else:
        print("Produk sudah ada.\n")

def update_item():
    """Mengubah harga dan stok produk"""
    item = input("Nama produk yang akan diupdate: ").lower()
    if item in products:
        price = int(input("Harga baru: "))
        stock = int(input("Stok baru: "))
        products[item]["price"] = price
        products[item]["stock"] = stock
        print("Produk diperbarui.\n")
    else:
        print("Produk tidak ditemukan.\n")

# ================================
# Bagian 4: Flash Sale
# ================================
flash_sale_end = datetime.now() + timedelta(seconds=60)  # 60 detik dari awal program

def apply_flash_sale(item, price):
    """Menerapkan diskon jika flash sale masih aktif"""
    if datetime.now() < flash_sale_end:
        print("⚡ Flash Sale Aktif! Diskon 20%!")
        return int(price * 0.8)
    return price

# ================================
# Bagian 5: Pembayaran
# ================================

def checkout(cart):
    """Menghitung total dan memproses pembayaran"""
    total = 0
    for item, qty in cart.items():
        price = apply_flash_sale(item, products[item]["price"])
        total += price * qty
        products[item]["stock"] -= qty  # Mengurangi stok setelah checkout

    print(f"Total bayar: Rp{total}")
    metode = input("Metode pembayaran (transfer/cod): ").lower()
    if metode in ["transfer", "cod"]:
        print("Pembayaran berhasil. Terima kasih!\n")
    else:
        print("Metode tidak dikenali.\n")

# ================================
# Bagian 6: Menu Utama Program
# ================================

def main():
    """Menu utama program"""
    while True:
        print("\n=== APLIKASI LOGIN & KASIR ===")
        print("1. Login")
        print("2. Daftar Akun")
        print("3. Lupa Password")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            user = login()
            if user:
                cart = {}
                while True:
                    print("\n--- MENU KASIR ---")
                    print("1. Tampilkan Menu")
                    print("2. Beli Produk")
                    print("3. Tambah Produk")
                    print("4. Update Produk")
                    print("5. Bayar")
                    print("6. Logout")
                    aksi = input("Pilih aksi: ")

                    if aksi == "1":
                        show_menu()
                    elif aksi == "2":
                        buy_item(cart)
                    elif aksi == "3":
                        add_item()
                    elif aksi == "4":
                        update_item()
                    elif aksi == "5":
                        checkout(cart)
                        cart = {}  # Reset keranjang
                    elif aksi == "6":
                        print("Logout berhasil.\n")
                        break
                    else:
                        print("Pilihan tidak valid.\n")
        elif pilihan == "2":
            create_account()
        elif pilihan == "3":
            forgot_password()
        elif pilihan == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak tersedia.\n")

# ================================
# Jalankan Program
# ================================
main()