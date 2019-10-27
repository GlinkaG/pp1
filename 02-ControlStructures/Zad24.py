imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]
x = []

for i in imiona:
    #print(len(i))
    x.append(len(i))
    
print("Najdłuższe imię to: " + imiona[x.index(max(x))])



#ze zmienną
    #temp = x.index(max(x))
    #print(imiona[temp])
