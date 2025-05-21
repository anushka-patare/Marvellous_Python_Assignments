def Area(length,width):
    area=length*width
    return area
    
def Perimeter(length,width):
    perimeter=2*(length+width)
    return perimeter

def main():
    print("Enter length :")
    len=int(input())

    print("Enter width :")
    wid=int(input())

    Ans1=Area(len,wid)
    print("Area of rectangle is :",Ans1)

    Ans2=Perimeter(len,wid)
    print("The perimeter of rectangle is :",Ans2)

if __name__=="__main__":
    main()