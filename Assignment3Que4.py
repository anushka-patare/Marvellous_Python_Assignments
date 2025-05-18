def Display():
    print("Enter size of list:")
    size=int(input())
    
    Data2=list()
    print("Enter elements in list:")
    for i in range(size):
        no=int(input())
        Data2.append(no)

    print("Enter elements to search its frequency:")
    N=int(input())
    count=0
    for i in Data2:
        if i == N:
            count=count+1
    print("The frequency of number is:",count)

if __name__=="__main__":
    Display()