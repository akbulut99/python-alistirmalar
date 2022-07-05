def mükemmel(sayı):
    toplam = []
    for i in range(1, sayı):
        if sayı % i == 0:
            toplam.append(i)

    return sum(toplam) == sayı
for i in range(1, 1001):
    if mükemmel(i):
        print("mükemmel sayı: ", i)

"2.yol"
"""""""""  def mukemmel(sayı):

        toplam = 0

        for i in range(1, sayı):

            if (sayı % i == 0):
                toplam += i

        return toplam == sayı


    for i in range(1, 1001):
        if (mukemmel(i)):
            print("Mükemmel Sayı:", i)"""""