class Employee:
    def __init__(self,salary,department,name):
        self.__salary=salary   #private
        self._department=department   #protected
        self.name=name
    
    def Display(self):
        print("The salary of employee is :",self.__salary)
        print("The department of employee is :",self._department)
        print("The name of employee is :",self.name)

def main():
    obj=Employee(10000,"Testing","Pravin")

    obj.Display()

if __name__=="__main__":
    main()