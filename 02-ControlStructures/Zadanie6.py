x = 0
y = 2

if (x > 0) & (y > 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się w pierwszej ćwiartce układu współrzędnych")
elif (x < 0) & (y < 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się w trzeciej ćwiartce układu współrzędnych")
elif (x > 0) & (y < 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się w czwartej ćwiartce układu współrzędnych")
elif (x < 0) & (y > 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się w drugiej ćwiartce układu współrzędnych")
elif (x == 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się na osi Y układu współrzędnych")
elif (y == 0):
    print("Punkt P(" + format(x) + ", " + format(y) + ") znajduje się na osi X układu współrzędnych")
