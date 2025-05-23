def Multiplication(no):
    mult=1
    for i in range(1,11):
        mult=no*i
        print(mult)

def main():
    print("Enter number:")
    value=int(input())
     
    Multiplication(value)
     

if __name__=="__main__":
     main()