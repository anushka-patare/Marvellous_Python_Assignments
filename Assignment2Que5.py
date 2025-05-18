def Prime():
    print("Enter number:")
    no=int(input())

    if no>1:
        for i in range(2,no):
            if no%i==0:
                print("The number is not prime")
                break

        else:
             print("The number is prime. ")
                


if __name__=="__main__":
    Prime()