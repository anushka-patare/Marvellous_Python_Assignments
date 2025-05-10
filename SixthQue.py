def ChkNum():
    print("Enter number:")
    no=int(input())
    
    if(no>0):
        print("The number is positive")
    
    elif(no<0):
        print("The number is negative")

    else:
        print("The number is zero")

if __name__=="__main__":
    ChkNum()