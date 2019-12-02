class University():
    #konstruktor obiektu __init__
    def __init__(self):
        #pola(zmienne, cechy obiektów)
        self.name = "UEK"
        
        #metody(funkcje w klasie, zachowania obiektu)
        def print_name(self):
            print(self.name)
            
        def set_name(self):
            new_name = input("Podaj nowa nazwe: ")
            self.name = new_name
        
            
p1 = University()
p1.set_name()
print(p1.name)