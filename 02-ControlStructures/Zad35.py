import math
a = int(input("Podaj współczynnik a funkcji: "))
b = int(input("Podaj współczynnik b funkcji: "))
c = int(input("Podaj współczynnik c funkcji: "))

delta = (b*b) - (4*a*c)

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Miejsca zerowe funkcji to x1 = {x1} oraz x2 = {x2}")
    
elif delta == 0:
    x0 = -b / (2*a)
    print(f"Funkcja posiada jedno miejsce zerowe x0 = {x0}")
    
elif delta < 0:
    print("Ta funkcja nie posiada miejsc zerowych!")
    
