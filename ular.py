from animal import *

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