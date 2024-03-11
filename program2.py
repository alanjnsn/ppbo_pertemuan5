class Pangkat:
    def __init__(self,angka):
        self.angka= angka

    def dipangkatkan(self):
        print(self.angka**1)


class Kuadrat(Pangkat):
    def dipangkatkan(self):
        print(self.angka**2)

class Kubik(Pangkat):
    def dipangkatkan(self):
        print(self.angka**3)
        

perpangkatan= Pangkat(2)
pengkuadratan= Kuadrat(2)
pengkubikan= Kubik(2)

perpangkatan.dipangkatkan()
pengkuadratan.dipangkatkan()
pengkubikan.dipangkatkan()

print()
print()