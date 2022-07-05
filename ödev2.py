sayi = int(input("bir sayı girin: "))
i = 1
toplam = 0

while i < sayi:
    if sayi % i == 0:
        toplam += i
    i += 1
if toplam == sayi:
    print(sayi, "mükkemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir")