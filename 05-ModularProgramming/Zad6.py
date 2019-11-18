import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    f.readline()   
    for row in reader:
        
        