import os
import sys
import filecmp

def main():
    FileName1=sys.argv[1]
    FileName2=sys.argv[2]

    flag = filecmp.cmp(FileName1,FileName2)

    if flag==True:
        print("Success")
    else:
        print("Failure")

if __name__=="__main__":
    main()