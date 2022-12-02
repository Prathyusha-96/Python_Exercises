#local scope
def myfunc():
    x = 100
    print(x)
myfunc()

#function inside a function
def myfunc():
    x = 200
    def myfunc2():
        x = 500
        print(x)
    myfunc2()
    print(x)
myfunc()

#global scope
x = 400
def myfunc():
    print(x)
myfunc()
print(x)

x = 'hello'
def myfunc():
    x = 'world'
    print(x)
   
myfunc()
print(x)

#global keyword
def myfunc():
    global x
    x = 200
myfunc()
print(x)


import mymodule
mymodule.greeting('prathyusha')

#variables in modules
a = mymodule.person1['age']
print(a)

#renaming a module
import mymodule as mm
a = mm.person1['name']
print(a)

#built-in modules
import platform
x = platform.system()
print(x)

x = dir(platform)
print(x)

#import from module
from mymodule import person1
a = person1['age']
print(a)

#PYTHON MATH MODULE
a = [10, 20, 30, 40]
print(max(a))
print(min(a))

print(abs(7.21))

print(pow(3, 4))

import math
x = math.sqrt(25)
print(x)

x = math.pi
print(x)

x = math.factorial(5)
print(x)
