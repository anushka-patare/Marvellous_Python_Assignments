from functools import reduce

def CheckPrime(no):
    if no>1:
        for i in range(2,no):
            if no%i==0:
                return False
        else:
            return True

def Product(no):
    return no*2

def Maximum(X,Y):
    if X > Y:
        return X
    else:
        return Y


Data=list()
print("Enter size of list:")
size=int(input())

print("Enter elements into list:")
for i in range(size):
    no=int(input())
    Data.append(no)

FData=list(filter(CheckPrime,Data))
print("The filter data is:",FData)

MData=list(map(Product,FData))
print("The mapped data is:",MData)

RData=reduce(Maximum,MData)
print("The reduce data is:",RData)