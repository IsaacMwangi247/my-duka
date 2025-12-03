# Create a School system program using Python classes to demnstraate inheritance -
# Create a parent class called Person with: attributes - name , age method : display_info()
# -> Create child classes that inherit the parent class: 
# a)Student class with: -additional attributes - student_id, course -override display_info() to include student_id and course 
# b)Teacher class with: -additional attributes - subject, salary -override display_info() to include subject and salary

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child Class: Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)   # Inherit from Person
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()  # Display name & age from Person
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


# Child Class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Salary: ${self.salary}")


# ---------- Testing the Classes ----------
# Creating objects
student1 = Student("Alice Kamande", 20, "S1001", "Computer Science")
student2 = Student("Peter Gitau", 22, "S1002", "Computer Science")
teacher1 = Teacher("Mr. Allen", 35, "Mathematics", 55000)

# Displaying information
print("=== Student Information ===")
student1.display_info()

print("\n=== Teacher Information ===")
teacher1.display_info()
