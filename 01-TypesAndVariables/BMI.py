x = int(input("Podaj wzrost (w cm): "))
wzrost = x/100
waga = int(input("Podaj wagę (w kg): "))
BMI = waga/(wzrost*wzrost)
print(round(BMI, 2))

if BMI < 18.5:
    print("Niedowaga")
elif 18.5 <= BMI <= 24.9:
    print("Waga prawidłowa")
elif 25 <= BMI <= 29.9:
    print("Nadwaga")
elif BMI > 30:
    print("Otyłość")
    



