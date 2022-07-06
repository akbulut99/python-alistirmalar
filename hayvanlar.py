import random
import time

class hayvan():
    def __init__(self,hayvan_cinsi= ["at","köpek","kuş"],hayvan_sayisi = 0,bilgi = "at") :
        self.hayvan_cinsi = hayvan_cinsi
        self.hayvan_sayisi = hayvan_sayisi
        self.bilgi = bilgi
    def hayvan_ekle(self,ekle):
        print("hayvanlar ekleniyor....")
        self.hayvan_sayisi += ekle
        time.sleep(1)
        print("Güncel hayvan sayısı: ",self.hayvan_sayisi)
    def rast_gele(self):
        rastgele_hayvan = random.randint(0, len(self.hayvan_cinsi)-1)
        bilgi = self.hayvan_cinsi[rastgele_hayvan]
        print("seçilen hayvan:", bilgi)
    def __len__(self):
        return len(self.hayvan_cinsi)            
class köpke(hayvan):
  def __init__(self, hayvan_cinsi=["at", "köpek", "kuş"], hayvan_sayisi=0, bilgi="at",köpek_cinsi = ["golden","alman kurdu"]):
     super().__init__(hayvan_cinsi, hayvan_sayisi, bilgi)
     self.köpek_cinsi = köpek_cinsi
  def köpek_ekle(self,köpek_ekle):
    self.köpek_cinsi.append(köpek_ekle)
    print("güncel köpek listesi: {}".format(self.köpek_cinsi))
     
     
  def __str__(self) :
          return "hayvan cinsi: köpek \nhayvan sayısı: {}\nköpeklerin cinsi: {}".format(self.hayvan_sayisi,self.köpek_cinsi)


class kus(hayvan):      
    def __init__(self, hayvan_cinsi, hayvan_adi, hayvan_sayisi,kus_cinsi):
        super().__init__(hayvan_cinsi, hayvan_sayisi)
        self.kus_cinsi = kus_cinsi
        self.hayvan_adi = hayvan_adi
class at(hayvan):
    def __init__(self, hayvan_cinsi= "AT", hayvan_sayisi=10,atın_cinsi=["ingiliz ATI","Arap ATI","Mustang","Moğol ATI"]):
        super().__init__(hayvan_cinsi, hayvan_sayisi=10)  
        self.atın_cinsi = atın_cinsi
        
        self.hayvan_sayisi = hayvan_sayisi       
    
    def __str__(self) :
          return "hayvan cinsi: AT \nhayvan sayısı: {}\n".format(self.hayvan_sayisi)
    def at_ekle(self,at_ekle):
        self.hayvan_sayisi += at_ekle
        print("mevcut at sayısı: ",self.hayvan_sayisi)

print("""
        -----Bilgi Paneli-----
        1.Hayvan ekle
        2.Hayvan bilgilerini görüntüle
        3.Rastgele hayvan seç
        çıkış için 'q' ya basın!!!


""")
at1 = at()
köpek = köpke()
tarcın = hayvan()
while True:
 cevap = input("İşleminiz...: ")
 if cevap =="q":
    print("program sonlandırılıyor...")
    time.sleep(1)
    break   

 elif cevap == "1":
  print("""
         1.köpek
         2.at
         3.kuş
         
    
    """)
  sec = input("Hayvan seçin: ")

  if sec == "1":
    cinsi = input("hayvan cinsi girin: ")
    hayvan_cinsi = cinsi.split(",")
    for i in hayvan_cinsi:
        köpek.köpek_ekle(i)
    print("hayvan cinsi ekleniyor...")
    time.sleep(1)
    print("EKLENDİ")
  elif sec == "2":
    sayısı = int(input("hayvan sayısı girin: "))
    print("hayvan sayısı ekleniyor...")
    at1.at_ekle(sayısı)
    time.sleep(1)
  elif cevap == "2":
    print("""
         1.köpek
         2.at
         3.kuş
         
    
    """)
    secim = input("hayvan seçin...: ")
    if secim == "1":
         print(köpke())
 elif cevap == "3":
    tarcın.rast_gele()
    break