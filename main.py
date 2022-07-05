liste = [3, 5, 6, 7,-2,-4, 8, 9, 0, 11, 442]
liste_bos = []
toplam = []
istenen = []
for i in liste:
    if i != liste[0]:
        liste_bos += [i]
    for a in liste_bos:
        toplam += [a]
        if a + i == liste[0]:
            istenen += [[a], [i]]

print(istenen)
