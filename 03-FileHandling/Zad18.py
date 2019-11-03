import re
tab = []
with open("C:/Users/grzeg/Desktop/pp1/03-FileHandling/numbers.txt") as file:
    for line in file:
        line = int(line)
        tab.append(line)
        #tab.append(re.findall("[0-9]+", line))
tab.sort()
print(tab)
        