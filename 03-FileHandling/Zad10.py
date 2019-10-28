suma = 0
with open("C:/Users/s-115-21/Desktop/pp1/03-FileHandling/numbers.txt") as file:
    for line in file:
        line = int(line)
        suma = suma + line
        
print(suma)