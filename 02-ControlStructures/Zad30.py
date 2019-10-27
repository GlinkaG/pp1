import sys
licznik = 0
PIN = "0805"

while licznik < 3:
    x = input("Podaj PIN: ")
    if(x != PIN):
        print("Podałeś nieprawidłowy kod PIN")
        licznik += 1
    else:
        print("Poprawny kod PIN!")
        sys.exit()
else:
    print("Karta płatnicza zostaje zablokowana")
    