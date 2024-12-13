class animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
        
    def cetak (self):
        print (f"Hewan {self.nama} ini memakan {self.makanan} ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembangbiak}")
        
c1 = animal ("buaya", "daging", "darat dan air", "bertelur")
c1.cetak()
print()
print()
print()
#from animals import *
class burung(animal):
    def __init__ (self, nama, makanan, hidup, berkembangbiak, bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.bulu = bulu
        self.bunyi = bunyi
        
    def cetakburung(self):
        super().cetak()
        print(f"hewan ini berbulu {self.bulu} dan hewan ini berbunyi {self.bunyi}")
        
beo = burung ("burung beo", "biji-bijian", "udara", "bertelur", "biru dan oren", "kamu jelek")

beo.cetakburung()

print ()
print()
print ()
#from animals import *
class ikan (animal):
    def __init__ (self, nama, makanan, hidup, berkembangbiak, warnaikan, jenisikan):
        super().__init__ (nama, makanan, hidup, berkembangbiak)
        self.warna = warnaikan
        self.jenis = jenisikan
    
    def cetakikan(self):
        super().cetak()
        print (f"warna ikan ini adalah warna {self.warna} dan hewan ini jenisnya ikan {self.jenis}")
        
nemo = ikan ("ikan nemo", "plankton", "air", "bertelur", "orange", "air laut")

nemo.cetakikan()
    
print()
print()
print()

class ular (animal):
    def __init__ (self, nama , makanan, hidup, berkembangbiak, warnaular, jenisular):
        super().__init__ (nama, makanan, hidup, berkembangbiak)
        self.warnaular = warnaular
        self.jenisular = jenisular
        
    def cetakular (self):
        super().cetak()
        print (f"warna dari ular ini {self.warnaular} dan ular ini berjenis ular yang {self.jenisular}")
        
python = ular (" python", "daging", "alam liar", "ovovivipar", "hitam", "berbisa dan berbahaya")

venom = ular (" venom ", "daging", "alam liar", "ovivipar", "hijau kehitaman", "berbida dan sangat berbahaya")

python.cetakular()
print()
print()
print()
venom.cetakular()
print()
print()
print()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    