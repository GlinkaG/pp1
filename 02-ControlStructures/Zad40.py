import random
tab = [0, 0, 0, 0, 0, 0, 0]
nazwy = ["Jedynki: ", "Dwójki: ", "Trójki: ", "Czwórki: ", "Piątki: ", "Szóstki: "]

for i in range (0, 100):
    x = random.randint(1,6)
    tab[x] = tab[x] + 1
    print(x)
    

        
for i in range(6):
    print(f"{nazwy[i]}{tab[i+1]}")
    



        