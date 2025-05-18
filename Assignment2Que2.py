def Display():
    print("Enter a number:")
    no=int(input())

    for i in range(1,no):
            print("*  "*no)

if __name__=="__main__":
    Display()