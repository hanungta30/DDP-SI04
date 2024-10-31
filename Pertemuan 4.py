#  1. Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. 
# Program harus menentukan apakah bilangan tersebut genap atau ganjil 
# menggunakan if dan if else.


print ("==================================")

bilangan = int (input("Masukan bilangan :"))

if bilangan % 2 == 0:
    print ("%i adalah bilangan genap" % bilangan)
else:
    print ("%i adalah bilangan ganjil" % bilangan) 


print ("==================================")


# 2. Buatlah program yang meminta pengguna untuk memasukkan nilai ujian. 
# Jika nilai lebih besar atau sama dengan 75,
# cetak "Lulus". Jika tidak, cetak "Tidak Lulus". 
# Gunakan if dan if else.


nilai = int (input("Masuikan Nilai Ujian :"))


if nilai >= 75 and nilai <= 100:
    print ("nilai Lulus")
else:
    print ("nilai Tidak Lulus")

print ("==================================")

# 3. Buatlah program yang meminta pengguna untuk memasukkan usia. 
# Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. 
# Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 
# menggunakan if and.

usia = int(input("Masukan Usia Sekarang:"))

if usia >= 18:
    print ("usia Dewasa")
elif usia >= 13 and usia <= 17:
    print ("Remaja")
else:
    print ("Anak-anak")
    
print ("==================================")
    

# 4. Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). 
# Jika statusnya "gold" atau "silver", 
# cetak "Selamat! Anda mendapatkan diskon". 
# Gunakan if or.

status = (input("Silahkan masukan status keanggotaan anda ~gold,silver,bronze~ pilih sesuai keanggotaan anda:"))

# a = "gold"
# b = "silver"
# c = "bronze"

if  status == "gold" or status == "silver":
    print ("Selamat! Anda mendapatkan diskon")
    
else:
    print ("Silahkan coba lagi")

print ("==================================")


# 5. Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. 
# Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. 
# Cetak total harga setelah diskon jika ada, 
# jika tidak, cetak total harga tanpa diskon.

buat = int(input("Tolong masukan jumlah pembelian anda: "))
hargaitem = 1000

total = buat * hargaitem

if buat > 100:
    diskon = 0.1 * total 
    total -= diskon 
    print("Kamu mendapatkan diskon 10%. Jadi total yang harus kamu bayar adalah:","RP", int(total))
    
else:
    print("Jumlah yang harus dibayar:","RP", int(total))
    
print ("==================================")