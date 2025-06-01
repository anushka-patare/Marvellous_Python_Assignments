from functools import reduce
def Number(no):
    return no%2 ==0

def Square(no):
    return no**2

def Sum(no1,no2):
    return no1+no2

print("Enter size of list:")
size=int(input())

Data = list()
print("Enter elements into list:")
for i in range(size):
    no=int(input())
    Data.append(no)

FData=list(filter(Number,Data))
print("Filter data is:",FData)

MData=list(map(Square,FData))
print("The map data is :",MData)

RData=reduce(Sum,MData)
print("The reduce data is :",RData)