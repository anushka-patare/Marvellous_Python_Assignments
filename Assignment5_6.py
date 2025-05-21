def Temperature(C):
    F=(C*9/5)+32
    return F

def main():
    print("Enter temperature in celsius :")
    cel=float(input())

    Ans=Temperature(cel)
    print("The temperature in fahrenheit :",Ans)

if __name__=="__main__":
    main()