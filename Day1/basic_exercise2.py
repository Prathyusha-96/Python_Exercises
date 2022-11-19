#Python Program to Check if a Number is Positive, Negative or Zero

num = -10
if num > 0:
    print('positive number')
elif num < 0:
    print("negative number")
else:
    print('equal to zero')

#Python Program to Check if a Number is Odd or Even
num = 55
if num % 2 == 0:
    print('even number')
else:
    print('odd number')

for i in range(2, 10):
    if i%2 == 0:
        print('even number')
    else:
        print('odd number')

#Python Program to Check Leap Year
year = 1997
if (year%4) == 0:
    print('leap year')
else:
    print('not a leap year')

#Python Program to Check Prime Number
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num%i) == 0:
            print(num, 'is not a prime number')
            break 
    else:
        print(num , 'is a prime number')
# else:
#     print('not a prime number')

#Python Program to Print all Prime Numbers in an Interval

num1 = 10
num2 = 50
for number in range(num1, num2+1):
    if number > 1:
        for i in range(2, number):
            if (number%i) == 0:
                break
        else:
            print(number)

#Python Program to Find the Factorial of a Number
#using built-in function
import math
n = 10
print(math.factorial(n))

n = 5
f = 1
for i in range(1, n+1):
    f = f*i
print(f)

#Python Program to Display the multiplication Table
n = 12
for i in range(1, 11):
    print(n, 'x', i, '=' ,n*i)

#Python Program to Print the Fibonacci sequence
number = 10
n1 = 0
n2 = 1
count = 0
while count< number:
    print(n1)
    n3 = n1+n2
    n1 = n2
    n2 = n3
    count += 1

list1 = [1, 2, 3]
list2 = list1
list1.append(list2)
print(list1)