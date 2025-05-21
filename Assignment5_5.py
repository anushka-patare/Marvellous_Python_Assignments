def ChkEvenOdd(no):
    if no%2==0:
        print(no,"number is an even.")
    
    else:
        print(no,"number is an odd.")

def main():
    print("Enter number :")
    value=int(input())

    ChkEvenOdd(value)

if __name__=="__main__":
    main()