def Number():
    print("Enter the number:")
    no=input()
    
    count=0
    for i in range(len(no)):
        count=count+1
    print(count)
         
        
if __name__=="__main__":
    Number()