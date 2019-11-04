tab = [15, 38, 7, 23, 14]
liczba = int(23)

def sprawdz(tab, liczba):
    print(f"Liczba: {liczba}")
    print(f"Tablica: {tab}")
    for i in tab:
        i = int(i)
        if liczba == i:
            x = "Liczba jest w tablicy!"
    print(f"Rezultat: {x}")


