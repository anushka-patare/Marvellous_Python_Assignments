import os
def main():
    print("Enter the filename that you want to create:")
    FileName=input()

    flag=os.path.exists(FileName)
    
    if flag==True:
        fobj=open(FileName,"r")
        data=fobj.read()
        print("The dats from file is :",data)
        
    else:
        print("The file is not present in directory")
    
    fobj.close()

if __name__=="__main__":
    main()