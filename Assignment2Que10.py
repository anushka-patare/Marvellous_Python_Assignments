def Sum():
    print("Enter a number:")
    no=input()

    sum=0
    for i in no:
        sum=sum+int(i)
    print(sum)

if __name__=="__main__":
    Sum()