# object oriented programming in Python

class Student:
    """
    This is a class Student to manage student info and activities.
    """

    # class variable
    school_name = "ABC School"
    departments = ["Science", "Arts", "Commerce"]

    # any method defined in a class is called an instance method, and it takes 'self' as the first parameter
    def __init__(self, name, roll): 
        # instance variable
        self.roll = roll  
        self.name = name

    def study(self, num_hours):
        print(self)
        print(f"The student studies for {num_hours} hours.")

    def sports(self, sport_name):
        print(f"The student plays {sport_name}.")

    # creating a class method
    # class methods are methods that are bound to the class and not the instance of the class. They take 'cls' as the first parameter and '@classmethod'
    @classmethod
    def greet(cls):
        print(cls)
        print(f"Welcome to {cls.school_name}!")

    # does not take 'self' or 'cls' as the first parameter, and is defined with '@staticmethod'
    @staticmethod
    def school_rules():
        print("Rules:")
        print("1. Be punctual.")
        print("2. Respect teachers and classmates.")
        print("3. Keep the school clean.")

# creating an object of the Student class
student1 = Student("Alice", 101)    
student1.study(3)
student1.sports("basketball")
Student.greet()  # calling the class method
student1.school_rules()  # calling the static method

# difference between instance method and class method
# instance method is called on an instance of the class and can access instance variables, 
# while class method is called on the class itself and can only access class variables.

class Teacher:

    grade_level = "5th Grade"


    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}.")
        print(self.grade_level) # accessing class variable from instance method is possible, but not recommended

    @classmethod
    def school_info(cls):
        print(f"Teachers are in {cls.grade_level}.")

teacher1 = Teacher("Mr. Smith", "Mathematics")
teacher1.teach()
teacher1.school_info()

# Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # calling the constructor of the parent class
        self.roll = roll

    def study(self):
        print(f"{self.name} is studying.")

student2 = Student("Bob", 102)
student2.introduce()  # inherited method from Person class
student2.study()  # method from Student class

# Multiple Inheritance
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def play(self):
        print(f"Playing {self.sport}.")

class StudentAthlete(Student, Athlete): # multilevel inheritance, Student inherits from Person and StudentAthlete inherits from both Student & Person
    def __init__(self, name, roll, sport): 

        # multiple inheritance
        Student.__init__(self, name, roll)  # calling the constructor of Student class
        Athlete.__init__(self, sport)  # calling the constructor of Athlete class

student_athlete = StudentAthlete("Charlie", 103, "soccer")
student_athlete.introduce()  # inherited from Person class
student_athlete.study()  # inherited from Student class
student_athlete.play()  # inherited from Athlete class





