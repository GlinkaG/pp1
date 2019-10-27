tab = [15, 8, 31, 47, 2, 19]
suma = 0
n = len(tab)

for i in tab:
    if i%2 != 0:
        suma += i
    
print(f"Średnia arytmetyczna wynosi: {suma/n}")