#Soal Nomor 1
def celcius_ke_fahrenheit(celcius):
    print (celcius * 9/5 + 32)
    
celcius_ke_fahrenheit (0)
celcius_ke_fahrenheit (100)

#Soal Nomor 2
def is_genap (genap):
    print(genap % 2 == 0)
    
is_genap(4)
is_genap(7)


print ('\n Keterangan lulus dan tidak lulus')

#Soal Nomor 3
def lulus_tidak_lulus(nilai):
    if nilai >= 80:
        print ("Lulus")
    else:
        print ("Tidak Lulus")
        
lulus_tidak_lulus (80)
lulus_tidak_lulus (40)


#Soal Nomor 4

def ganjil_bil(bilangan):
    for i in range(1, bilangan, 2):
        print(i)


ganjil_bil (20)

