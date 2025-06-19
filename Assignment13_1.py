class BookStore:
    NoOfBooks=0
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print("The name of book is :"+self.Name)
        print("The author name is :"+self.Author)
        print("The number of books are :",BookStore.NoOfBooks)

def main():
    print("Enter name of book:")
    name1=input()
    print("Enter name of author :")
    author1=input()
    
    obj1=BookStore(name1,author1)
    obj1.Display()

    print("Enter name of book:")
    name2=input()
    print("Enter name of author :")
    author2=input()
    
    obj2=BookStore(name2,author2)
    obj2.Display()



if __name__=="__main__":
    main()