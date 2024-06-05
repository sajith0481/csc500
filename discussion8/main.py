class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50

    def play(self):
        print('Playing the guitar')

# class ElectricGuitar:
#     def __init__(self):
#         self.n_strings = 6
#         self.play()
#         self.distortion = True
    
#     def play(self):
#         print('Playing the guitar')

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings = 8)
        self.colour = ("#000000","#FFFFFF")


    def playLouder(self):
        print('Playing the guitar louder')

    def __secret(self):
        print('This guitar actually cost me $', self._Guitar__cost, "only")

class BassGuitar(Guitar):
    pass

my_guitar = ElectricGuitar()
my_guitar._ElectricGuitar__secret()
print("My base guitar has", BassGuitar(4).n_strings, "strings")
print("My electric guitar has", my_guitar.n_strings, "strings")