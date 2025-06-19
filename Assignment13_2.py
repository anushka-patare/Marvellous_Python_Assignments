class BankAccount:
    ROI=10.5
    def __init__(self,A,B):
        self.Name=A
        self.Amount=B

    def Display(self):
       print("Name of account holder is :",self.Name)
       print("Enter the value of amount:",self.Amount)
    
    def Deposit(self):
        print("Enter the deposited amount:")
        deposit_amt=int(input())
        deposit_amt = deposit_amt + self.Amount
        print("Deposited amount is :",deposit_amt)
        
    def Withdraw(self):
        print("Enter amount to withdraw:")
        withdraw=int(input())
        if withdraw < self.Amount:
            withdraw=self.Amount-withdraw
            print("The withdrawn ammount is :",withdraw)
        else:
            print("The balance is insufficient")
        
    def CalculateInterest(self):
        interest=self.Amount*BankAccount.ROI/100
        print("The interest is:",interest)

def main():
    print("Enter name of account holder:")
    name1=input()
    print("Enter amount:")
    amt=int(input())

    obj=BankAccount(name1,amt)
    obj.Display()
    obj.Deposit()
    obj.Withdraw()
    obj.CalculateInterest()

if __name__=="__main__":
    main()