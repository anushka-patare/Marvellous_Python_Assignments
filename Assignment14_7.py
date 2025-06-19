class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def Display(self):
        print("Name of person is :",self.name)
        print("The age of person is:",self.age)

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
        
    def Display_Details(self):
        super().Display()
        print("The subject is :",self.subject)
        print("The salary of teacher is:",self.salary)

def main():
    print("Enter name of person:")
    name1=input()

    print("Enter age of person:")
    age1=int(input())

    print("Enter name subject:")
    sub=input()

    print("Enter salary of Teacher:")
    sal=int(input())

    obj=Teacher(name1,age1,sub,sal)
    obj.Display_Details()

if __name__=="__main__":
    main()

