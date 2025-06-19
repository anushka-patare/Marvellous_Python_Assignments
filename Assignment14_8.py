class Vehicle:
    def Start(self):
        print("This is base class method")

class Car(Vehicle):
    def Start(self):
        print("This is derived class method")

def main():
    vobj=Vehicle()
    cobj=Car()
    
    vobj.Start()
    cobj.Start()
if __name__=="__main__":
    main()
