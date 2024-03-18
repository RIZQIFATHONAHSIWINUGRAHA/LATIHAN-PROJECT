# nama = 'rizqi'
# usia = 23
# mahasiswa = True
# x = 2
# y = x + 3

# print ("Nama = ", nama)
# print ("Usia saya = ", usia)
# print ("Mahasiswa = ", mahasiswa)
# print ("nilai x = ", x)
# print ("nilai y = ", y)

# panjang = input ("Masukkan Nilai Panjang : ")
# lebar = input ("Masukkan Nilai Lebar : ")
# luas = int(panjang) * int(lebar)

# print ("Luas persegi adalah ; ", luas)

# buah_buahan = ["Apel","Jeruk","Leci"]
# print (type(buah_buahan))

# koordinat = (1,2,3)
# print (type(koordinat))

# biodata = {"Rizqi","Fathonah","Tangerang",30}
# print (type(biodata))

# nama = ["Rizqi","Fathonah","Siwi"]
# nama[1] = "budi"
# print(nama[1])

# manipulasi tipe data
# data_int = 9 ;
# print("Data Ini ada lah : ",data_int,"Type Datanya adalah : ",type(data_int))

# data_float = float(data_int)
# print("Data ini adalah : ",type(data_float))

# data = int(input("Masukkan Data"))
# print("Datanya adalah : ",data," Type Data : ",type(data))

# a = 10
# b = 11

# c = int(a + b - a * a / b ** a % b)

# print (c)

# like = 9 

# print("Jumlah Like yang di dapat : ",like,"Tipe Likenya adalah : ",type(like))


print("--------------- Selamat Datang Di Gunshop ---------------")
print("Berikut Price List Harga Senjata Kami")
print("Ak-47 : 4.000.000 ")
print("L115A1 : 8.000.000 ")
print("M4A1 Sil : 6.000.000 ")
print("Benelli M2 : 5.000.000 ")
print("Bayonet : 2.000.000 ")
print("Armor Set : 2.000.000 ")

Ak47 = 4000000 
L115A1 = 8000000
M4A1 = 6000000
Benelli = 5000000
Bayonet = 2000000
Armor = 2000000

nama = input("Masukkan Nama : ")
Team = input("Military Team Name : ")
pilih = input("Silakan Pilih Senjata anda : ")
if pilih == "Ak47":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Ak47)
elif pilih == "ak47":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Ak47)
elif pilih == "L115A1":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",L115A1)
elif pilih == "l115a1":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",L115A1)
elif pilih == "M4A1":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",M4A1)
elif pilih == "m4a1":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",M4A1)
elif pilih == "Benelli":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Benelli)
elif pilih == "benelli":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Benelli)
elif pilih == "Bayonet":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Bayonet)
elif pilih == "bayonet":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Bayonet)
elif pilih == "Armor":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Armor)
elif pilih == "armor":
    print("Selamat Anda Telah Memilih Senjata Dan Harganya Rp.",Armor)
else:
    print("Anda Tidak Memilih")

print ("Berikut Total Pesanan anda Mr ",nama)
print(pilih)