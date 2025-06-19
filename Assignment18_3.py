import os
import sys

def main():
    FileName1=sys.argv[1]

    fobj=open(FileName1,"r")
    data=fobj.read()

    FileName2=sys.argv[2]   #Demo.txt
    fobj=open(FileName2,"w")

    fobj.write(data)


if __name__=="__main__":
    main()
        
        
    
