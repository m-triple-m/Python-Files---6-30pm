class Computer:

    ram = '8 GB'
    hdd = '1 TB'

    def __repr__(self):
        return 'Parent Class Computer'

    def showspecs(self):
        return f""" 
                    RAM : {self.ram}
                    HDD : {self.hdd}"""

class Laptop(Computer):
    screen = '1080 p'

    # method overriding
    def showspecs(self):
        return f""" 
                    RAM : {self.ram}
                    HDD : {self.hdd}
                    Screen Resolution : {self.screen}"""

class GamingLaptop(Laptop):
    ram = '16 GB'
    ssd = '2 TB'
    screen = '4K'

class SuperComputer:
    pass

class GamingDesktop(GamingLaptop, SuperComputer):
    pass

print("laptop module imported...")

if __name__ == "__main__":
    comp1 = Computer()

    print(comp1.showspecs())

    lap1 = Laptop()

    print(lap1.showspecs())

    g1 = GamingLaptop()

    print(g1.showspecs())
    print(g1)