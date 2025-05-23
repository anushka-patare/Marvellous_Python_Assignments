
def Display(no):

    for i in range(1,no+1):
        for j in range(i,no+1):
            print("* " *j)
            break

def main():
    print("Enter number :")
    num=int(input())

    Display(num)

if __name__=="__main__":
    main()