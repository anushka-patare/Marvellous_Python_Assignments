from Arithmetic import *

def Addition():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    Result=Add(value1,value2)
    print("The addition is:",Result)

if __name__=="__main__":
    Addition()


def Subtraction():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    Result=Sub(value1,value2)
    print("The subtraction is:",Result)

if __name__=="__main__":
    Subtraction()


def Multiplication():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    Result=Mult(value1,value2)
    print("The multiplication is:",Result)

if __name__=="__main__":
    Multiplication()



def Division():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())

    Result=Div(value1,value2)
    print("The division is:",Result)

if __name__=="__main__":
    Division()