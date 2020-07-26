class Circle:
    def __init__(self,radios,pi):
        self.radios=radios
        self.pi=pi

    def area(self):
        return self.pi*(self.radios*self.radios)
    def circumference(self):
        return 2*self.pi*self.radios


circle1=Circle(5,3.14)
print(circle1.area())
print(circle1.circumference())

