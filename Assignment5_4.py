def LargestNum(x,y,z):
    if (x>y):
        print("largest number is :",x)

    elif (y>z):
        print("Largest number is:",y)

    else:
        print("largest number is :",z)


def main():
    print("Enter  numbers:")
    no1=int(input())
    no2=int(input())
    no3=int(input())

    LargestNum(no1,no2,no3)

if __name__=="__main__":
    main()