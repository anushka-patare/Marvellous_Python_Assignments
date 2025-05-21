def Sum(no1,no2):
    Ans=0
    Ans=no1+no2
    return Ans

def Difference(no1,no2):
    Ans=0
    Ans=no1-no2
    return Ans

def Product(no1,no2):
    Ans=0
    Ans=no1*no2
    return Ans

def Division(no1,no2):
    Ans=0
    Ans=no1/no2
    return Ans

def main():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())
    
    add=Sum(value1,value2)
    print("The sum is :",add)
    
    sub=Difference(value1,value2)
    print("The difference is:",sub)

    mult=Product(value1,value2)
    print("The product is :",mult)

    div=Division(value1,value2)
    print("The division is :",div)

if __name__=="__main__":
    main()