class Book:
    def __init__(self,price):
        self.__price=price

    def GetPrice(self):
        print("Book price :",self.__price)

    def SetPrice(self,newprice):
        if newprice>=0:
            self.__price=newprice
            print("The new price of book is:",self.__price)
        else:
            print("Price not match.")


def main():
    print("Enter price of book:")
    price1=int(input())

    obj=Book(price1)
    obj.GetPrice()

    print("Enter new price of book:")
    newprice1=int(input())

    obj.SetPrice(newprice1)

if __name__=="__main__":
    main()    
