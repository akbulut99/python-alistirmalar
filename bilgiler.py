
from bdb import Breakpoint
import time


class coder():
    def __init__(self,isim = " ",soyisim= " ",maasii = 0,diller= " ") :
        self.isim = isim
        self.soyisim = soyisim
        self.maasii = maasii
        self.diller = diller
    def bilgileri_göster(self):
        print("""
        -----------BİLGİLER-----------
        İsim: {}
        Soy İsim: {}
        Maaş = {}
        Yazılım Dilleri = {}
        
        """.format(self.isim,self.soyisim,self.maasii,self.diller)
        )
    def maas_arttir(self,maas2):
        self.maasii += maas2
    def dil_ekle(self,dill):
        self.diller += dill


yazilimci = coder()
isim1 = input("isim girin: ")
yazilimci.isim = isim1
soy2 = input("Soy isim girin: ")
yazilimci.soyisim = soy2
maas = int(input("Maaş bilgisi girin: "))
yazilimci.maasii = maas
dil = input("Bilinen yazılım dili girin: ")
yazilimci.diller = dil
print("bilgiler ekleniyor...")
time.sleep(1)
print(yazilimci.bilgileri_göster())
i = input("maaş arttırmak ister misiniz?:")
if i == "e":
    yeni_maas= int(input("Arttırılacak fiyat: : "))
    yazilimci.maas_arttir(yeni_maas)
    print("Çalışanın yeni maaşı: {}".format(yazilimci.maasii))
else:
 a = input("yeni bir dil eklemek ister misiniz? ")
 if a == "e":
    y_dil = input("yeni dili girin:") 
    yazilimci.dil_ekle(y_dil)
    print("Yazılımcının bildiği diller: {} ".format(yazilimci.diller)) 