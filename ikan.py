from animal import *
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