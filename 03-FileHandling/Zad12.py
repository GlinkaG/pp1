wpis = str(" ")
with open('shoppinglist.txt','a') as file:
    while len(wpis) != 0:
        wpis = str(input("Wpisz produkt aby dodać go do listy: "))
        file.write(wpis + "\n")
    else:
        print("test")
    