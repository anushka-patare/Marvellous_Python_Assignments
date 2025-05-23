def Prime(no):
    if no>1:
        for i in range(2,no+1):
           if no%i==0:
               return False
               break
           else:
               return True
    
print("Enter size of list :")
size =int(input())

Data=list()
print("Enter elements:")
for i in range(size):
    no = int(input())
    Data.append(no)

FData=list(filter(Prime,Data))
print("Prime numbers: :",FData)