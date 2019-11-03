import re
suma = 0
tab = []
wyrazenie = "\\d"
with open("C:/Users/grzeg/Desktop/pp1/03-FileHandling/land.txt", "r") as file:
    x = re.findall(wyrazenie, file.read())
    for a in x:
        a = int(a)
        suma = suma + a
print(suma)
    

    


    
        


    