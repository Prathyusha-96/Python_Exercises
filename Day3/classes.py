#creating classes
class Myclass:
    x = 5

#create object
p1 = Myclass()
print(p1.x)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student('john', 20)
s2 = Student('Deo', 18)
print(s1.name)
print(s2.age)