class University():
    
    def __init__(self):
        self.name = "UEK"
        self.fullname = "Uniwersytet Ekonomiczny w Krakowie"
        
    def print_name(self):
        print(self.name)
            
    def set_name(self):
        new_name = input("Podaj nazwe: ")
        self.name = new_name
    
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self):
        new_fullname = input("Podaj pelna nazwe: ")
        self.fullname = new_fullname
            
p1 = University()
p1.set_name()
p1.set_fullname()
p1.print_fullname()
print(p1.name)