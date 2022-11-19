print('Hello World')

#Python program to do arithmetical operations

num1 = input('enter number')
num2 = input('enter number')

add  = int(num1) + int(num2)
print(add)

sub = int(num1) - int(num2)
print(sub)

mul = int(num1) * int(num2)
print(mul)

div = int(num1) / int(num2)
print(div)


num1 = 50
num2 = 60

print(num1 + num2)

print(num1 - num2)

print(num1 * num2)

print(num1 / num2)

#Python program to find the area of a triangle
a = 5
b = 6
c = 7
s = (a+b+c)/2
print(s)
#area of triangle formula
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)

#Python program to swap two variables
#method1
x = 100
y = 200
x, y = y,x 
print(x)
print(y)

#method2
x = 40
y = 50
z = x
x = y
y = z
print(x)
print(y)

#Python program to generate a random number
import random
n = random.random()
print(n)
#Generating a Number within a Given Range

n =  random.randint(0, 12)
print(n)

#Using for loop

li = []
for i in range(0, 10):
    n = random.randint(1, 50)
    li.append(n)
print(li)

#Using random.sample()
#which directly generate a list of random numbers

n = random.sample(range(2,10), 4)
print(n)

#Python program to display calendar
import calendar
yy = 2022
mm = 12
print(calendar.month(yy, mm))
print(calendar.month(2022, 11))