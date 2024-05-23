import json

# Fungsi untuk menambahkan data diri
def add_data(data_list):
    print("Masukkan Data Diri : ")
    nama = input("Nama : ")
    age = input("Umur : ")
    gender = input("Jenis Kelamin : ")
    address = input("Alamat : ")

    data = {
        "name" : nama,
        "age" : age,
        "gender" : gender,
        "address" : address
    }

    data_list.append(data)
    print("Data Berhasil di Tambahkan\n")

# Fungsi untuk mencari data diri berdasarkan nama
def search_data(data_list):
    nama_to_search = input("Masukkan Nama yang anda ingin cari : ")
    for data in data_list:
        if data["name"].lower() == nama_to_search.lower():
            print("\nData di Temukan")
            print(f"Nama : {data['name']}")
            print(f"Umur : {data['age']}")
            print(f"Jenis Kelamin : {data['gender']}")
            print(f"Alamat : {data['address']}\n")
            return
    print("Data tidak di temukan\n")

# Fungsi untuk menyimpan data ke file
def save_data(data_list):
    with open("data.json", "w") as file:
        json.dump(data_list, file)
    print("Data Berhasil Disimpan ke File data.json\n")

# Fungsi untuk memuat data dari file
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    data_list = load_data()
    while True:
        print("Pilih Opsi :")
        print("1. Tambah data")
        print("2. Cari data")
        print("3. Keluar")
        choice = input("Masukkan Pilihan (1/2/3): ")

        if choice == "1":
            add_data(data_list)
            save_data(data_list)
        elif choice == "2":
            search_data(data_list)
        elif choice == "3":
            print("Terima Kasih Telah Menggunakan Aplikasi ini! ")
            break
        else:
            print("Pilihan Tidak Valid, Silakan Pilih Kembali.\n")

if __name__ == "__main__":
    main()