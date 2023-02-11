class Student:
    def __init__(self, height=160):
        self.height = height
nick = Student()
kate = Student(height=170)
sheldon = Student(height=190)
print(nick.height)
print(kate.height)
print(sheldon.height)

class Prepod:
    def __init__(self, height=120):
        self.height = height
Vasya = Prepod(height=130)
print(Vasya.height)

