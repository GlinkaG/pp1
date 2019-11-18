import statistics
XYZ = [21600, 4350, 3920, 5590, 3250, 4010]

def srednia(XYZ):
    srednie_zarobki = statistics.mean(XYZ)
    print(srednie_zarobki)
    return srednie_zarobki

def mediana(XYZ):
    XYZ.sort()
    #print(XYZ)
    mediana = statistics.median(XYZ)
    print(mediana)
    return mediana

def odchylenie(XYZ):
    XYZ.sort()
    odchylenie_stand = statistics.pstdev(XYZ)
    print(odchylenie_stand)
    return odchylenie_stand
    


#srednia(XYZ)
mediana(XYZ)
odchylenie(XYZ)