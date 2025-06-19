class Employee:
    def __init__(self,A,B,C):
        self.Name=A
        self.ID=B
        self.Salary=C

    def Display(self):
        print("Name :"+self.Name,"ID:",self.ID,"Salary:",self.Salary)

def main():
    obj=Employee("Rohit",101,50000)
    obj.Display()

if __name__=="__main__":
    main()
    

