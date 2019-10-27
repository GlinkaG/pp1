x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("Podaj trzecią liczbę: "))

if x > y and x < z or x > z and x < y:
    print(f"Mediana liczb to: {x}")
    
elif z > x and z < y or z < x and z > y:
    print(f"Mediana liczb to: {z}")
    
elif y > x and y < z or y < x and y > z:
    print(f"Mediana liczb to: {y}")