import random
import time

print("*****************************************")
print("           SAYI TAHMİN OYUNU ")
print("******************************************")

hak = 5
a = random.randint(1, 40)
while True:
    sayı = int(input("bir sayı girin: "))

    if sayı > a:
        print("program çalışıyor...")
        time.sleep(1)
        print("girilen sayı gerçek değerden büyük...")
        hak -= 1

    elif sayı < a:
        print("program çalışıyor...")
        time.sleep(1)
        print("girilen sayı gerçek değerden küçük...")
        hak -= 1
    elif sayı == a:
        print("program çalışıyor...")
        time.sleep(1)
        print("Tebrikler doğru TAHMİN...", sayı)
        print("program sonlandırılıyor...")
        time.sleep(1.5)
        break
    elif hak == 0:
        print("Tahmin hakkınız bitmiştir!!!!")
        print("SONUÇ: ", a)
        print("program sonlandırılıyor....")
        time.sleep(1)
        break