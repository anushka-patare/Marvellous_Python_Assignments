def Display():
    print("Enter number:")
    n=int(input())

    for i in range(n):
        for j in range(1,n+1):
            print(j,end=" ")
        print()

if __name__=="__main__":
    Display()