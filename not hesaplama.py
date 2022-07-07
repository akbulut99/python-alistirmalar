def not_hesapla(satır):
    satır =satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    sonuc = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
    if sonuc >=85:
        harf = "AA"
    elif sonuc >= 80:
        harf = "BA"    
    elif sonuc >= 75:
        harf = "BB"    
    elif sonuc >= 70:
        harf = "CB" 
    elif sonuc >= 65:
        harf = "CC"
    elif sonuc >= 60:
        harf = "DC" 
    elif sonuc >= 55:
        harf = "DD"
    else:
        harf = "ff"
    return isim + "------------------------>" + harf + "\n"                                           




with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)     
with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/notlar.txt","w",encoding="utf-8") as file2:
   for i in eklenecekler_listesi:  
     file2.write(i)