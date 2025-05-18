def Factorial():
    print("Enter number: ")
    n=int(input())
    i=1
    fact=1
    while(i<=n):
        fact=fact*i
        i=i+1
    print("The factorial is:",fact)

if __name__=="__main__":
    Factorial()