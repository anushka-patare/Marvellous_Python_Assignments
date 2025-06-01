class Demo:
    Value=0
    def __init__(self,A,B):
        self.no1 =A  #instance variable
        self.no2 =B  #instance variable

    def Fun(self):
        print("Inside Fun method")
        print("The value of no1 is :",self.no1)
        print("The value of no2 is ",self.no2)

    def Gun(self):
        print("Inside Gun method")
        print("The value of no1 is :",self.no1)
        print("The value of no2 is :",self.no2)

def main():
    
    obj1=Demo(11,21)
    obj2=Demo(51,101)
    obj1.Fun()
    obj2.Fun()
    obj2.Fun()
    obj2.Gun()


if __name__=="__main__":
    main()

