def Display():
    print("enter number:")
    n=int(input())

    for i in range(n,0,-1):
        print("*   "*i)

if __name__=="__main__":
    Display()