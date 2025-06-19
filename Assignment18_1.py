import os

def main():
    print("Enter file name that you want to check:")
    FileName=input()

    flag=os.path.exists(FileName)
    
    if flag==True:
        print("The file is exists in current directory")

    else:
        print("The file is not exists in current directory")
    
if __name__=="__main__":
    main()