tab = []
src = "C:/Users/grzeg/Desktop/pp1/03-FileHandling/"
with open("C:/Users/grzeg/Desktop/pp1/03-FileHandling/numbers.txt", "r") as source:
    for line in source:
        line = int(line)
        if line %2 != 0:
            line = str(line)
            tab.append(f"{line}\n")

tab.sort()
with open(f"{src}evennumbers.txt", 'w') as destination:
    for i in tab:
        destination.write(i)
        