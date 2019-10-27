from datetime import date
from dateutil import parser
today = date.today()
PESEL = str(input("Podaj swój numer PESEL: "))
print(PESEL[0:6])

#obliczamy wiek
rok_urodzenia = int("19" + PESEL[0:2])
data_urodzenia = ("19" + PESEL[0:2] + "-" + PESEL[2:4] + "-" + PESEL[4:6])
x = parser.parse(data_urodzenia)
print(x)
wiek = today - x
print(today)
print(wiek)