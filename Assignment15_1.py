import os

def main():
    print("Enter name of file:")
    FileName=input()
    
    flag=os.path.exists(FileName)
    if flag==True:
        print("The file is exists in current directory.")
    else:
        print("The file is not exists in current diretory")

if __name__=="__main__":
    main()
