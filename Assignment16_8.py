def main():
    print("Enter first file:")
    FileName1=input()
    fobj1=open(FileName1,"r")

    print("Enter second file")
    FileName2=input()
    fobj2=open(FileName2,"x")

    for line in fobj1:
        if line.strip()!=" ":
            fobj2.write(line)
    
if __name__=="__main__":
    main()

