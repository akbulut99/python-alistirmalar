import time
class calısan():
    def __init__(self,isim,soyisim,maas,departman) :
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman

    def bilgiler(self):
        print("İsim: {} \nSoyisim: {} \nMaas: {} \nDepartman:{} \n".format(self.isim,self.soyisim,self.maas,self.departman))

class yönetici(calısan):
    def __init__(self, isim, soyisim, maas, departman,kisi_sayisi):
     super().__init__(isim, soyisim, maas, departman)
     self.kisi_sayisi = kisi_sayisi
    def bilgiler(self):
        print("İsim: {} \nSoyisim: {} \nMaas: {} \nDepartman:{} \nSorumlu kişi sayısı: {}"
        .format(self.isim,self.soyisim,self.maas,self.departman,self.kisi_sayisi))

    def zam_yap(self,zam_miktarı = 0):
        self.maas += zam_miktarı
        print("yeni maaş: {}".format(self.maas))


yönetici1 = yönetici("Mustafa", "AKBULUT", 3000, "AR-GE", 10)


yönetici1.bilgiler()

i = input("Zam yapmak istiyor musunuz?..: ")
if i == "e":
    tutar = int(input("Artırılacak Tutarı girin: "))
    print("bilgiler güncelleniyor...")
    time.sleep(1)
    yönetici1.zam_yap(tutar)
else:
    print("program sonlandırılıyor....")
    time.sleep(1)

