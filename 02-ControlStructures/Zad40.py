import random
tab = [0, 0, 0, 0, 0, 0]
nazwy = ["Jedynki: ", "Dwójki: ", "Trójki: ", "Czwórki: ", "Piątki: ", "Szóstki: "]

for i in range (0, 101):
    x = random.randint(1,6)
    #print(x)
    
    if x == 1:
        tab[0] += 1
                
    elif x == 2:
        tab[1] += 1
            
    elif x == 3:
        tab[2] += 1
            
    elif x == 4:
        tab[3] += 1
                
    elif x == 5:
        tab[4] += 1
                
    elif x == 6:
        tab[5] += 1
        
for i in tab:
    print(f"{nazwy[1]}{i} ")
    



        