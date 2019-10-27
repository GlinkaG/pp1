from datetime import date
czas = date.today()
PESEL = str(input("Podaj swój numer PESEL: "))
#print(PESEL[0:6])

temp1 = ((czas.year - 1)*365) + ((czas.month - 1)*30) + czas.day
print(temp1)