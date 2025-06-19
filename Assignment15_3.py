import os
import sys

def main():
    FileName=sys.argv[1]

    fobj=open(FileName,"r")
    data=fobj.read()
    
    FileName2=sys.argv[2]

    fobj=open(FileName2,"w")
    newdata=fobj.write(data)

    fobj.write("The data is successfully copied")

if __name__=="__main__":
    main()
