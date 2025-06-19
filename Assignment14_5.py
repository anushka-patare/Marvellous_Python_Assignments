class BankAccount:
    def __init__(self,A,B,C):
        self.account_number=A
        self.name=B
        self.balance=C

    def Deposit(self):
        print("Enter amount to deposit:")
        self.deposit=int(input())

        self.deposit=self.deposit + self.balance
        print("The deposited amount is :",self.deposit)

    def Withdraw(self):
        print("Enter amount to withdraw:")
        self.withdraw=int(input())
        if self.withdraw < self.balance:
            self.withdraw=self.balance-self.withdraw
            print("The withdrawn ammount is :",self.withdraw)
        else:
            print("The balance is insufficient")

def main():
    print("Enter account number:")
    acc_num=int(input())

    print("Enter name of account holder:")
    name1=input()

    print("Enter balance:")
    bal=int(input())

    obj=BankAccount(acc_num,name1,bal)
    obj.Deposit()
    obj.Withdraw()

if __name__=="__main__":
    main()
