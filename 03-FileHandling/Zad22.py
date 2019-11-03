with open("C:/Users/grzeg/Desktop/pp1/03-FileHandling/students.txt", "r") as file:
    next(file)
    for line in file:
        x = line.split(",")
        if int(x[2]) < 30:
            print(f"{x[0]}\t {x[1]}\t {x[4]}")
    