def Factorial(no):

    fact=1
    for i in range(1,no+1):
        fact=fact*i
    print("Factorial of",no,"is :",fact)
    

def main():
    print("Enter number:")
    num=int(input())
    Factorial(num)

if __name__=="__main__":
    main()