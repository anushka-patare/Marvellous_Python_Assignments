def Display():
    
    print("Enter number of size:")
    size=int(input())

    Data=list()
    print("Enter elements into list:")
    for i in range(size):
        no=int(input())
        Data.append(no)
    
    sum=0
    for i in Data:
        sum=sum+i
        i=i+1
    print("The addition is:",sum)


if __name__=="__main__":
    Display()
    