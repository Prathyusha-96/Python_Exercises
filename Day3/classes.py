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
#add __str__
    def __str__(self) :
        return(f'{self.name}{self.age}')

s1 = Student('john', 20)
s2 = Student('Deo', 18)
print(s1.name)
print(s2.age)
print(s1)

#create methods (object methods)
class Person:
    def __init__(self,name,proffe):
        self.name = name
        self.proffe = proffe

    #creating method
    def myfunc(self):
        print('hello i am an' + self.proffe)
p1 = Person('Krish', 'Actor')
p1.myfunc()

#inheritence
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def func(self):
        print('{}{}'.format(self.fname, self.lname))
#create child class
class Employee(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    
    def my_self(self):
        print('My name is {} {}, Iam {} years old'.format(self.fname, self.lname, self.age))

p2 = Person('Cris', 'Leo')
p2.func()

e1 = Employee('Charli', 'Chaplin', 25)
e1.my_self()
print(issubclass( Employee,Person))
print(isinstance(e1, Employee))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee('Suhan', 50000)
print(emp.salary)