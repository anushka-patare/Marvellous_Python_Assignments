def ChkEligible(age):
    
    if (age>=18):
        print("Eligible to vote.")

    else:
        print("Not eligible.")

def main():
    print("Enter age :")
    no=int(input())

    ChkEligible(no)
    

if __name__=="__main__":
    main()
