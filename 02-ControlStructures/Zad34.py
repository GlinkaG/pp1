PESEL = str(input("Podaj swój numer PESEL: "))

#obliczamy wiek
rok_urodzenia = int("19" + PESEL[0:2])
data_urodzenia = ("19" + PESEL[0:2] + "-" + PESEL[2:4] + "-" + PESEL[4:6])

wiek = 2018 - rok_urodzenia
print(f"Wiek: {wiek}")

#sprawdzamy płeć
id_plci = int(PESEL[9])
if id_plci == 1 or id_plci == 3 or id_plci == 5 or id_plci == 7 or id_plci == 9:
    print("Płeć: mężczyzna")
elif id_plci == 0 or id_plci == 2 or id_plci == 4 or id_plci == 6 or id_plci == 8:
    print("Płeć: kobieta")
#print(id_plci)
