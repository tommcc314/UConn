import math
class Polygon:
    def __init__(self,nbr_sides):
        self.nbr_sides=nbr_sides
    def whoamI(self):
        if self.nbr_sides==3:
            return 'Triangle'
        elif self.nbr_sides==4:
            return 'Rectangle'
    def howmanysides(self):
        return int(self.nbr_sides)
    def area(self):
        return 'No area'
    def perimeter(self):
        return 'No perimeter'
class Rectangle(Polygon):
    def __init__(self,breadth,length):
        self.nbr_sides=4
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)
class Triangle(Polygon):
    def __init__(self,a,b,c):
        self.nbr_sides=3
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        self.s = (self.a + self.b + self.c) / 2
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
if __name__=='__main__':
    t1 = Triangle(3,4,5)
    r1 = Rectangle(3,4)
    print(f"Shape: {t1.whoamI()}, Number of sides: {t1.howmanysides()}, Area: {t1.area()}, Perimeter: {t1.perimeter()}.")
    print(f"Shape: {r1.whoamI()}, Number of sides: {r1.howmanysides()}, Area: {r1.area()}, Perimeter: {r1.perimeter()}.")