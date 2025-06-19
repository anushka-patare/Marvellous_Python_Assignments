class Calculator:
    def __init__(self,A,B):
        self.value1=A
        self.value2=B
    
    def Add(self):
        self.Ans=0
        self.Ans=self.value1+self.value2
        print("Addition is:",self.Ans)

    def Subtract(self):
        self.Ans=0
        self.Ans=self.value1-self.value2
        print("Subtraction is:",self.Ans)

    def Multiply(self):
        self.Ans=0
        self.Ans=self.value1 * self.value2
        print("Multiplication is :",self.Ans)
    
    def Divide(self):
        self.Ans=0
        self.Ans=self.value1 / self.value2
        print("Division is :",self.Ans)

def main():
    print("Enter the first number : ")
    no1=int(input())

    print("Enter second number:")
    no2=int(input())

    obj=Calculator(no1,no2)
    
    print("Enter operation:")
    operation=int(input())
    
    if operation==1:
        result= obj.Add()
        
    elif operation==2:
        result = obj.Subtract()
    
    elif operation==3:
        result = obj.Multiply()
    
    elif operation==4:
        result=obj.Divide()
       
    else:
        print("Invalid operation")

if __name__=="__main__":
    main()
