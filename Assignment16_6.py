def CopyContent():
   
    FileName1="Source.txt"
    FileName2="Destination.txt"
    fobj=open(FileName1,"r")
    data=fobj.read()
    fobj=open(FileName2,"w")
    fobj.write(data)


def main():
    CopyContent()

if __name__=="__main__":
    main()