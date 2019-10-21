x = int(input("Podaj liczbe: "))

if (x > 0) & (x%2 != 0):
    print("Liczba " + format(x) + " jest dodatnia i nieparzysta")
else:
    print("Liczba " + format(x) + " jest parzysta lub ujemna")