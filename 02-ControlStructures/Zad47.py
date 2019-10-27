kwota = int(input("Podaj kwotę w zł: "))
print(f"Kwota {kwota} zł w monetach: ")
tab = []

tab.append(int(kwota / 5))
reszta = kwota%5
kwota = reszta
tab.append(int(kwota/2))
reszta = kwota%2
if reszta == 1:
    tab.append(1)
else:
    tab.append(0)

print(f"Monety 5 zł: {tab[0]}")
print(f"Monety 2 zł: {tab[1]}")
print(f"Monety 1 zł: {tab[2]}")