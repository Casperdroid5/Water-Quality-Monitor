class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age=17):
        self.color = name
        self.age = age

    def greet(self):
        _greetings = [
            "Hi i'm {}",
            "hello my name is {}",
            "hi oh, my name is {}"
        ]

        greeting = choice(_greetings)

        return greeting.format(self.name)

def class_create(student_names):
    return[Student(name) for name in student_names]

name = ["Alice", "Bryan", "Clayton", "Deirdre", "Elon", "Faye"]

for student in class_create(name):
    print(student.greet())

s1 = Student
s1.name = "john"
s1.age = 19


