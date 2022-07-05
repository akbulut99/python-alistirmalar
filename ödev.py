"""
sayi1 = int(input("1.sayı girin: "))
sayi2 = int(input("2.sayı girin: "))
sayi3 = int(input("3.sayı girin: "))
if sayi1 > sayi2 and sayi1 > sayi3:
    print(sayi1)
elif sayi2 > sayi1 and sayi2 > sayi3:
    print(sayi2)
elif sayi3 > sayi1 and sayi3 > sayi2:
    print(sayi3)

vize1 = float(input("1.vize notu: "))
vize2 = float(input("2.vize notu: "))
final = float(input("final notu:"))
toplam = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
if  toplam >= 90:
    print("{},Harf Notunuz AA".format(toplam))
elif toplam >= 85:
    print("{},Harf Notunuz BA".format(toplam))
elif toplam >= 80:
    print("{},Harf Notunuz BB".format(toplam))
elif toplam >= 75:
    print("{},Harf Notunuz CB".format(toplam))
elif toplam >= 70:
    print("{},Harf Notunuz CC".format(toplam))
elif toplam >= 65:
    print("{},Harf Notunuz DC".format(toplam))
elif toplam >= 60:
    print("{},Harf Notunuz DD".format(toplam))
elif toplam >= 55:
    print("{},Harf Notunuz FD".format(toplam))
elif toplam < 55:
    print("{}, Harf Notunuz FF".format(toplam))
"""
istek = input("Bulmak istediğiniz geometrik alan: ")
if istek == "dörtgen":
    ab = abs(float(input("AB kenarını girin: ")))
    bc = abs(float(input("BC kenarını girin: ")))
    cd = abs(float(input("CD kenarını girin: ")))
    da = abs(float(input("DA kenarını girin: ")))
    if ab == bc and ab == cd and ab == da and bc == cd and bc == da and cd == da:
        print("bu bir karedir")
    else:
        print("sıradan bir dörtgen")
elif istek == "üçgen":
    u1 = abs(float(input("1.uzun kenarı girin: ")))
    u2 = abs(float(input("2.uzun kenarı girin: ")))
    taban = abs(float(input("tabanı girin: ")))
    if abs(u1-u2) < abs(taban) < abs(u2 + u1) and abs(u1 - taban) < abs(u2) < abs(u1 + taban) and abs(u2 - taban) < abs(u1) < abs(u2 + taban):
       if u1 == u2 and u1 == taban and u2 == taban:
          print("Bu bir eşkenar üçgendir")
       elif u1 == u2 and u1 != taban and u2 != taban or u1 == taban and u1 != u2 and taban != u2 or u2 == taban and u2 != u1:
          print("Bu bir ikiz kenar üçgendir")
    else:
       print("üçgen belirtmez!!!")




