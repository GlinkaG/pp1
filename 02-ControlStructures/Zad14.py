wiek = int(input("Podaj wiek psa: "))
wiek_psa = 0
if (wiek > 2):
    wiek_psa = (2*10.5) + (wiek-2)*4
    print(int(wiek_psa))
elif (wiek <= 2):
    wiek_psa = (wiek*10.5)
    print(wiek_psa)