from functools import reduce
def Product(no1,no2):
    return no1*no2

print("Enter size of list :")
size =int(input())

Data=list()
print("Enter elements:")
for i in range(size):
    no = int(input())
    Data.append(no)

RData=reduce(Product,Data)
print("Product :",RData)