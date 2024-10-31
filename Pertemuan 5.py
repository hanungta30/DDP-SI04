# 1. Buat Variabel list dengan value : [namaKendaraan] [JenisKendaraan]
#    [ccKendaraan] [warnaKendaraan] [rodaKendaraan]
#    tambahkan dari list tersebut di belakang dengan value :
#    [hargaKendaraan] [tipeKendaraan]
#    tambahkan setelah jenis kendaraan dengan value [merkKendaraan]

dftmtr = ["Nama Kendaraan : Honda Beat Deluxe", "Jenis Kendaraan : Motor", "CC Kendaraan : 109.5 cc",
          "Warna Kendaraan : Hitam Doff", "Roda Kendaraan : Radial, Tubeless"]
print ("Merk: ", dftmtr)

print ("=============================")

dftmtr.append ("Harga Kendaraan : Rp 18,43 Juta") 
dftmtr.append ("Tipe Kendaraan : CBS") 
print (dftmtr)

print ("=============================")

dftmtr.insert (2, "Merk Kendaraan: Honda ") 
print (dftmtr)

print ("=============================")






#   2. buatlah program python dengan match case untuk menghitung luas bangun datar
#   Jika pilih 1, maka menghitung luas persegi
#   Jika pilih 2, maka menghitung luas lingkaran
#   Jika pilih 3, maka menghitung luas segitiga


pilih = int((input("""Selamat Datang Diaplikasi Menghitung
                   1. Untuk Menghitung Luas Persegi
                   2. Untuk Menghitung Luas Lingkaran
                   3. Untuk Menghitung Luas Segitiga 
                   
                   
                   
                   masukan pilihan anda : \n""")))


match  pilih:
    case 1:
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukan sisi persegi : "))
        luaspersegi = sisi * sisi
        print("luas persegi yang sisinya", sisi, "adalah", luaspersegi)
    
    case 2:
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jari_jari = int(input("Masukan jari-jari lingkaran : "))
        luaslingkaran = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran yang jari-jari nya", jari_jari, "adalah", luaslingkaran)
        
    case 3:
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukan alas segitiga : "))
        tinggi = int(input("Masukan tinggi segitiga : "))
        luassegitiga = 0.5 * alas * tinggi
        print("Luas segitiga yang alas nya", alas, "dan tingginya", tinggi, "adalah", luassegitiga)
        
        
    case _:
        print("Input yang anda masukan salah!")
        
        
        
        
        