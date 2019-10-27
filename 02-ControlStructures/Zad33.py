cyfry = ["0", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
x = input("Podaj liczbę: ") 
temp = [int(i) for i in str(x)]
print(temp)

#print(cyfry[int(j) for j in temp])