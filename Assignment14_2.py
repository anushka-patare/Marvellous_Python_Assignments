class Rectangle:
    def __init__(self,A,B):
        self.length=A
        self.width=B
        self.area=0.0
        self.perimeter=0.0

    def Area(self):
        self.area=self.length*self.width
        print("Area :",self.area)

    def Perimeter(self):
        self.perimeter=2*(self.length+self.width)
        print("Perimeter :",self.perimeter)

def main():
    print("Enter length of rectangle :")
    len=int(input())

    print("Enter width of rectangle :")
    wid=int(input())

    obj=Rectangle(len,wid)
    obj.Area()
    obj.Perimeter()

if __name__=="__main__":
    main()