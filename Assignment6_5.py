def ChkPrime(no):
    if no>1:
        for i in range(2,no):
            if no%i==0:
                print(no,"is nota prime number.")
                break
        else:
                print(no,"is a prime number.")

def main():
    print("Enter a number :")
    num=int(input())

    ChkPrime(num)

if __name__=="__main__":
    main()