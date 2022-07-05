print("""""""""
      ****************************
      ATM MAKİNESİ
      1. PARA ÇEKME
      2.PARA YATIRMA
      3.BAKİYE SORGULAMA
      
      ****************************""""")
giris = input("yapmak istediğini işlem: ")
bakiye = 50
while True:
    if giris == "1":
        tutar = float(input("çekmek istediğiniz tutar: "))
        bakiye = bakiye - tutar
        print("mevcut bakiyeniz: {}".format(bakiye))
        giris = input("yeni işlem yapmak istiyor musunuz? :")
        if giris == "e" or "E":
            giris = input("yapmak istediğiniz işlem: ")

        elif giris == "h" or "H":
            print("iyi günler dileriz...")
            break
    elif giris == "2":
        tutar = float(input("yatırılacak tutar: "))
        bakiye = bakiye + tutar
        print("mevcut bakiyeniz: {}".format(bakiye))
        giris = input("yeni işlem yapmak istiyor musunuz? :")
        if giris == "e" or "E":
            giris = input("yapmak istediğiniz işlem: ")
            continue
        elif giris == "h" or "H":
            print("iyi günler dileriz...")
            break
    elif giris == "3":
        print("bakiyeniz: {}".format(bakiye))
        giris = input("yeni işlem yapmak istiyor musunuz? :")
        if giris == "e" or "E":
            giris = input("yapmak istediğiniz işlem: ")
            continue
        elif giris == "h" or "H":
            print("iyi günler dileriz...")
            break
    elif giris == "q":
        print("iyi günler dileriz...")
        break