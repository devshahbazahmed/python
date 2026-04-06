class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping Chai")
    
    def addSugar(self, amount):
        print("Added the sugar")


my_Chai = Chai(sweetness=3, milk_level=5)

my_Chai.addSugar(5)
my_Chai.sip()