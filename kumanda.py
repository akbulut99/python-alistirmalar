import random
import time
class kumanda():
    def __init__(self,tv_durum = "kapalı", tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if self.tv_durum == "açık":
            print("Televizyon açık...")
        else:
            self.tv_durum = "Açık"
            print("Televizyon açılıyor...")
    def tv_kapat(self):
        if self.tv_durum == "kapalı":
            print("Televizyon kapalı")
        elif self.tv_durum != "kapalı":
            self.tv_durum == "kapalı"
            print("televizyon kapatılıyor...")
    def ses(self):
        while True:
            cevap = input("sesi arttırmak için '>' \nazaltmak için'<' \nçıkış için 'çıkış': ")  
            if cevap == ">":
                if self.tv_ses != 31:
                    print("ses düzeyi arttırılıyor...")
                    self.tv_ses += 1
                    time.sleep(1)
                    print("ses düzeyi: {}".format(self.tv_ses))
                else:
                    print("Ses maksimum düzeyde!!!")          
            elif cevap == "<":
                if self.tv_ses != 0:
                    print("Ses düzeyi azaltılıyor...")
                    self.tv_ses -= 1 
                    time.sleep(1)
                    print("ses düzeyi: {}".format(self.tv_ses))
                else:
                    print("ses zaten kapalı!!!!")
            else:
                print("ses güncellendi.... {}".format(self.tv_ses))
                break                          
    def kanal_ekle(self,kanal_adi):         
        print("kanal ekleniyor")
        self.kanal_listesi.append(kanal_adi)
        time.sleep(1)
        print("Güncel kanal listesi: {}".format(self.kanal_listesi))
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal: {}".format(self.kanal))
    def __str__(self):
        return "Tv durumu: {}\nSes seviyesi: {}\nKanal listesi: {}\nŞu anki kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal) 

    def __len__(self):
        return len(self.kanal_listesi)     

remote1 = kumanda()          
print(""""
 Televizyon Uygulaması
 1. Tv Aç

 2. Tv Kapat

 3. Ses Ayarları

 4. Kanal EKle

 5. Kanal Sayısını Öğrenme

 6. Rastgele Kanal Geçme

 7. Televizyon Bİlgileri

 Çıkmak için q ya Basın.
 """)
while True:
    islem = input("işlem seçin: ")
    if islem == "q":
        print("program sonlandırılıyor...")
        break
    elif islem == "1":
        remote1.tv_ac()
    elif islem == "2":
        remote1.tv_kapat()    
    elif islem =="3":
        remote1.ses()
    elif islem == "4":
        k_adi = input("Kanal adı (',' ayırarak) girin: ")
        kanal_listesi = k_adi.split(",")
        for i in kanal_listesi:
            remote1.kanal_ekle(i)
    elif islem == "5":
        print("kanal sayısı: ", len(remote1.kanal_listesi))
    elif islem == "6":
        remote1.rastgele_kanal()   
    elif islem == "7":
        print(remote1)
    else:
        print("geçersiz işlem!!!") 