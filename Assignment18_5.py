import os
def main():

    print("Enter the file name:")
    FileName=input()
    
    flag=os.path.exists(FileName)
    if flag == True:
        print("Enter a string:")
        string=input()

        fobj=open(FileName,"r")
        data=fobj.read()

        count1=data.count(string)
        print(count1)
    
    else:
        print("The file is not present in current directory")
if __name__=="__main__":
    main()

