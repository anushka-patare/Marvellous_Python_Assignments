import os
def main():
      FileName="Data.txt"
      fobj=open(FileName,"r")
      data=fobj.read()
      print("The data is in the file is :",data)
      fobj.close()
    
if __name__=="__main__":
    main()
