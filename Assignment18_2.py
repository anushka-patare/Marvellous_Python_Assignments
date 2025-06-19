import os

def main():
    print("Enter file name:")
    FileName=input()

    fobj=open(FileName,"r")
    data=fobj.read()
    print("The content of file is:",data)

if __name__=="__main__":
    main()