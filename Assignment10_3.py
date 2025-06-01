from functools import reduce

def ChkNum(No):
    return  (70<=No <=90 )

def Increase(No):
    return No + 10

def Product(No1,No2):
    return No1*No2

print("Enter size of list:")
size=int(input())

data=list()
     
print("enter the values:")
for i in range(size):
    no=int(input())
    data.append(no)  

FData=list(filter(ChkNum,data))
print("Filter data is :",FData)

MData=list(map(Increase,FData))
print("Mapped data is:",MData)

RData=reduce(Product,MData)
print("The reduce data is:",RData)