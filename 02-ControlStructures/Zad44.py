limit = int(input("Podaj limit prędkości (km/h): "))
predkosc = int(input("Podaj prędkość pojazdu (km/h): "))
przekroczenie = predkosc - limit

if przekroczenie <= 10:
    mandat = przekroczenie * 5
    print(f"Mandat (zł): {mandat}")
    
elif przekroczenie >= 10:
    mandat = (10 * 5) + ((przekroczenie - 10) * 15)
    print(f"Mandat (zł): {mandat}")