wzrost = int(input("Podaj swoj wzrost w cm: "))
waga = float(input("Podaj swoja wage w kg: "))
assert type(waga) == float, "Nie pyklo"
assert waga >= 40 and waga <= 150, "Waga spoza przedzialu"
assert wzrost >= 150 and wzrost <= 250
test = (wzrost/100)
BMI = waga/((wzrost/100)**2)
print(BMI)