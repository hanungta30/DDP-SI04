from animal import *
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
