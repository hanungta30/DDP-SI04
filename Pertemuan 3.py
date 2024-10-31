# 1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)

nama = "Hanung Tri Atmojo"
nim = "0110124084"
rombel = "SI04"
notlp = "085775603396"
almt = """Jalan Pisang Batu No 4
RT/RW 7/10
Mangga Dua Selatan 10730"""

print ("Nama Saya", nama)
print ("Nim", nim)
print ("Rombel", rombel)
print ("Nomor Telepon", notlp)
print ("Alamat Rumah", almt)

print ("=====================================")
print ("=====================================")


# 2. buat seperti no 1 tapi 1 nama teman kalian 

nama = "Ananda Dafa Zaky"
nim = "0110223184"
rombel = "TI06"
notlp = "08211484600"
almt = """Parung Kulon, Kelurahan Duren Mekar, Kecamatan Bojong Sari Depok"""

print ("Nama Teman Saya", nama)
print ("Nim Teman Saya", nim)
print ("Rombel Teman Saya", rombel)
print ("Nomor Telepon Teman Saya", notlp)
print ("Alamat Teman Saya", almt)

print ("=====================================")
print ("=====================================")


# 3. buat program python untuk mencari nilai berat badan ideal 

tb = int (input ("Berapa Tinggi Badan Sekarang:"))
data_bb = (tb - 100) - (tb - 100) * 0.1

print  ("berat badan ideal kamu adalah", data_bb)

print ("=====================================")
print ("=====================================")


# 4. buat program python untuk mencari nilai konversi dari celcius ke fahreinheit 

ckef = int (input("Masukan Berapa Celcius Yang Mau Di Konversi?"))

fahr = (9/5 * ckef) + 32

print (ckef , "Derajat Celcius = ", fahr, "Derajat Fahrenheit")

print ("=====================================")
print ("=====================================")


# 5. buat program python untuk mencari luas dan keliling tabung

phi = 22/7
r = int (input ("Masukan Jari Jari Yang Diketahui :"))
t = int (input ("Masukan Tinggi Yang Diketahui :"))
k = ( 2 * phi * r)
lpt = 2 * phi * r * (r + t)

print ("Luas Tabung : %.2f"%lpt) 
print ("Keliling Tabung : %.2f"%k)

print ("=====================================")
print ("=====================================")