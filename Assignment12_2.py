class Circle:
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.Area=0.0
        self.circumference=0.0

    def Accept(self):
        print("Enter radius of circle :")
        self.radius=float(input())

    def CalculateArea(self):
        self.Area=Circle.PI * self.radius *self.radius
        return self.Area
    
    def CalculateCircumference(self):
        self.circumference=2 *Circle.PI * self.radius
        return self.circumference
    
    def Display(self):
        print("The value of radius is:",self.radius)
        print("The value of area is :",self.Area)
        print("The value of circumference is :",self.circumference)


def main():
    obj1=Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__=="__main__":
    main()