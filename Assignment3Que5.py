import MarvellousNum
def ListPrime():
    print("Enter size of list:")
    size=int(input())

    Data=list()
    print("Enter elements into list:")
    for i in range(size):
        num=int(input())
        Data.append(num)
    
    Ans=MarvellousNum.ChkPrime(num)
    sum=0
    for num in Data:
        if MarvellousNum.ChkPrime(num):
               sum = sum + num
    print("the sum is:",sum)   

    
if __name__=="__main__":
    ListPrime()
