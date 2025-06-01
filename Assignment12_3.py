class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
         print("Enter value1:")
         self.value1=int(input())

         print("Enter value2:")
         self.value2=int(input())

    def Addition(self):
        Ans=0
        Ans=self.value1+self.value2
        return Ans

    def Subtraction(self):
        Ans = 0
        Ans = self.value1-self.value2
        return Ans

    def Multiplication(self):
        Ans=0
        Ans=self.value1*self.value2
        return Ans

    def Division(self):
        Ans=0
        Ans=self.value1/self.value2
        return Ans

def main():
    obj1=Arithmetic()
    obj1.Accept()

    ret1= obj1.Addition()
    print("The addition is:",ret1)

    ret2=obj1.Subtraction()
    print("The subtraction is :",ret2)

    ret3=obj1.Multiplication()
    print("The multiplication is :",ret3)

    ret4=obj1.Division()
    print("The division is :",ret4)
    
if __name__=="__main__":
    main() 



