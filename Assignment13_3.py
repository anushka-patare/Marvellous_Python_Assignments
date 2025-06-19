class Numbers:
    def __init__(self,A):
        self.value=A

    def ChkPrime(self):
        if self.value>1:
            for i in range(2,self.value+1):
                if self.value%i==0:
                    print("The number is not prime")
                    break
        else:
            print("The number is prime")

    def ChkPerfect(self):
        if self.value==self.SumFactors():
            print("True")
        else:
            print("False")
                
    def Factors(self):
        for i in range(1,self.value):
            if self.value%i==0:
                 print("The factors of value is :",i,)
             
    def SumFactors(self):
        self.sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                self.sum=self.sum+i
        print("The sum of all factors of instance variable is :",self.sum)

def main():
    print("Enter number:")
    no=int(input())
    obj1=Numbers(no)
    obj1.ChkPrime()
    obj1.ChkPerfect()
    obj1.Factors()
    obj1.SumFactors()

if __name__=="__main__":
    main()
