class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet_students(self):
        print(f"Welcome to class! I am {self.name}, your teacher for {self.course} teaching")
    #
    # def greet_students(self, name):
    #     print(f'welocome to class, I am {name} your teacher ')
    #


# Define your class below this line

class ScienceProfessor(Professor):
    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        Professor.greet_students(self)


science_professor = ScienceProfessor("Lucas", 45, "SCIENCE1001")
science_professor.greet_students()
