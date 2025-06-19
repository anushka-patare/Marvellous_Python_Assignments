class Student:
    school_name="NEST school"

    def __init__(self,A,B,):
        self.name=A
        self.roll_no=B

    def Student_Details(self):
        print("The name of student is :",self.name)
        print("The roll number of student is :",self.roll_no)
        print("The school name of student is :",Student.school_name)

def main():
    print("Enter name of student:")
    name1=input()

    print("Enter roll number of student:")
    roll_no1=int(input())

    obj1=Student(name1,roll_no1)
    obj1.Student_Details()

    Student.school_name = "Modern school"
    print("The updated school name is :",Student.school_name)


if __name__=="__main__":
    main()