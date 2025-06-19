import sys
import os
import filecmp

def main():

    FileName1=sys.argv[1]
    FileName2=sys.argv[2]
    
    fobj=open(FileName1,"r")
    fobj=open(FileName2,"r")
    flag = filecmp.cmp(FileName1,FileName2)

    if flag==True:
            print("Success")

    else:
            print("Failure")

    fobj.close()

if __name__=="__main__":
    main() 
