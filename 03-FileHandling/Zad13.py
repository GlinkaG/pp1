tab = [31,16,5,8,24,7]

with open("Numeryztablicy.txt", "w") as file:
    for i in tab:
        file.write(f"{i}\n")