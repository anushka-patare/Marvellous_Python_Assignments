def Increase(no):
    return no*2

print("Enter size of list :")
size =int(input())

Data=list()
print("Enter elements:")
for i in range(size):
    no = int(input())
    Data.append(no)

MapData=list(map(Increase,Data))
print("Doubled list:",MapData)