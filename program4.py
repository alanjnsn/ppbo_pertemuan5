class Mobil:
    def __init__(self, merk, harga):
        self.merk= merk
        self.harga= harga

    def __str__(self):
        return f"merk: {self.merk} \nharga: US${self.harga}"
    
    
lamborghini= Mobil('lamborghini', 6000000)
print(lamborghini)
        