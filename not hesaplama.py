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
        gecenler_listesi.append(isim + "--->"+ harf +"\n")
    elif sonuc >= 80:
        harf = "BA"
        gecenler_listesi.append(isim + "--->"+ harf +"\n")    
    elif sonuc >= 75:
        harf = "BB"
        gecenler_listesi.append(isim + "--->"+ harf +"\n")    
    elif sonuc >= 70:
        harf = "CB" 
        gecenler_listesi.append(isim + "--->"+ harf +"\n")
    elif sonuc >= 65:
        harf = "CC"
        gecenler_listesi.append(isim + "--->"+ harf +"\n")
    elif sonuc >= 60:
        harf = "DC" 
        gecenler_listesi.append(isim + "--->"+ harf +"\n")
    elif sonuc >= 55:
        harf = "DD"
        kalanlar_listesi.append(isim + "--->"+ harf +"\n")
    else:
        harf = "ff"
        kalanlar_listesi.append(isim +"--->"+ harf + "\n")
    return isim + "------------------------>" + harf + "\n"      
 


with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    gecenler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    print(eklenecekler_listesi)   
      
    print ("kalanlar\n",kalanlar_listesi)
with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/notlar.txt","w",encoding="utf-8") as file2:
   for i in eklenecekler_listesi:  
     file2.write(i)
with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/kalanlar.txt","w",encoding="utf-8") as file3:
    for a in kalanlar_listesi:
        file3.write(a)     
with open("c:/Users/akbul/Desktop/python/nesne tabanlı/not hesaplama/geçenler.txt","w",encoding="utf-8") as file4:
     for b in gecenler_listesi:
        file4.write(b)