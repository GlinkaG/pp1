class TV():
    
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
        self.channels = []
        
    def on(self):
        self.is_on = 1
        
    def off(self):
        self.is_on = 0
    
    def show_status(self):
        if self.is_on == 0:
            print(f"Odbiornik TV jest włączony, kanał {self.channel_no}")
        else:
            print("Telewizor jest włączony")
        
    def print_name(self):
        print(self.nazwa)
        
    def set_channel(self):
        new_channel = input("Podaj numer kanalu: ")
        self.channel_no = new_channel
        
    def set_channels(self):
        for i in self.channels:
            x = input("Podaj kanal: ")
            if x == "":
                print("test")
            else:
                self.channels.append(x)
        
    def show_channels(self):
            print(self.channels)
        
        
test = TV()
test.show_status()
test.on()
test.show_status()
test.set_channels()
test.show_channels()
test.set_channel()
test.show_status()
test.off()
test.show_status()

