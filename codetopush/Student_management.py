
students = []


# create class
class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Roll number: {self.roll}")
        print(f"Marks: {self.marks}")


    def check_result(self):
        if self.marks >= 50:
            print("Pass")
        else:
            print("Fail")



def add_student():

    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))

    obj = Student(name, roll, marks)

    students.append(obj)



def show_students():

    for student in students:
        student.show_details()
        student.check_result()



def top_student():

    if len(students) == 0:
        print("No students found")
        return

    top = students[0]

    for student in students:
        if student.marks > top.marks:
            top = student

    print("Top student is:")
    top.show_details()


def search_student():

    search_name = input("Enter student name: ")

    for student in students:
        if student.name.lower() == search_name.lower():
            print("Student found:")
            student.show_details()
            return

    print("Student not found")



while True:

    print("\n1 Add Student")
    print("2 Show All Students")
    print("3 Show Top Student")
    print("4 Search Student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        top_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")