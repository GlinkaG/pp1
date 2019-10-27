a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbe: "))
tab = []

tab.append(a)
tab.append(b)
tab.append(c)
tab.sort()


print(f"Liczby w kolejności rosnącej: {tab[0]}, {tab[1]}, {tab[2]}")