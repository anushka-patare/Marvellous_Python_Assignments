import sys

def ReadLine():
    FileName=sys.argv[1]
    fobj=open(FileName,"r")

    lines=fobj.readlines()

    for i in lines:
        word=i.split()
        if len(word) > 5:
            print(i)

def main():
    ReadLine()

if __name__=="__main__":
    main()
    
