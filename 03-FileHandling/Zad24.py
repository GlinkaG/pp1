import csv
tab = [ ["Marek", "Zelnik", "zelnik@sed.pl"], ["Ewa", "Maj", "maje@wp.pl"], ["Piotr", "Wyga", "wygap@gop.pl"] ]

with open("C:/Users/grzeg/Desktop/pp1/03-FileHandling/users.csv", "w") as file:
    pola = ["imie","nazwisko","email"]
    konst = csv.DictWriter(file, fieldnames = pola)
    
    konst.writeheader()
    for row in tab:
        konst.writerow({'imie': row[0], 'nazwisko': row[1], 'email': row[2]})
            