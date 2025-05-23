def Even(no):
    return no%2==0

print("Enter size of list :")
size =int(input())

Data=list()
print("Enter elements:")
for i in range(size):
    no = int(input())
    Data.append(no)

FData=list(filter(Even,Data))
print("Even numbers :",FData)