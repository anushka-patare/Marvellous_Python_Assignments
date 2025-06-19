def AcceptNum():
    FileName="numbers.txt"
    fobj=open(FileName,"w")
    
    print("Enter numbers:")
    for num in range(0,10):
        num=input()
        fobj.write(num +"\n")
     
    fobj.close()



def main():
    AcceptNum()

if __name__=="__main__":
    main()