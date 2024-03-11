class Pangkat:
    def __init__(self, x,y):
        self.x= x
        self.y= y

    def hasil(self):
        print(self.x**self.y)


class Kali:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def hasil(self):
        print(self.x*self.y)

perpangkatan= Pangkat(2,3)
perkalian= Kali(2,3)

perpangkatan.hasil()
perkalian.hasil()
        
print()
print()
print()

