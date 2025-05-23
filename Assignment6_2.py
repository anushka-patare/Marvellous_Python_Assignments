#Logic 1

def SumofEven():
    sum=0
    for no in range(1,101):
        if no%2==0:
            sum=sum+no
    print("Sum of even numbers between 1 to 100 is :",sum)

if __name__=="__main__":
    SumofEven()  


#Logic 2

def SumofEven():
    sum=0
    for i in range(0,101,2):
        sum=sum+i
    print("Sum of even numbers between 1 to 100 is :",sum)

if __name__=="__main__":
    SumofEven()     

