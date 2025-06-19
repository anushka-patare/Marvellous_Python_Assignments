class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __eq__(self,another_price):
        return self.price==another_price
    
def main():
    print("Enter name of product:")
    name1=input()

    print("enter price of product")
    price1=int(input())
    obj1=Product(name1,price1)

    print("Enter name of product:")
    name2=input()

    print("enter price of product")
    price2=int(input())
    obj2=Product(name2,price2)

    print("The prices of both product are equal:",obj1==obj2)
if __name__=="__main__":
    main()

