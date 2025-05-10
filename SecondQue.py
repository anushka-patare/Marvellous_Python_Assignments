def ChkNum():
    print("Enter the number:")
    no=int(input())

    if(no%2==0):
        print("Even number")
    
    else:
        print("Odd number")

if __name__=="__main__":
    ChkNum()