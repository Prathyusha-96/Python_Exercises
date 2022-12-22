print('Hello world')
x = 'hello world'
print(x)
# x = 5
print(type(x))

x, y, z = 'apple', 'banana', 'cherry'
print(x)

x=y=z = 'orange'
print(y)

#unpack
fruits = ['orange', 'apple','cherry']
x, y, z = fruits
print(z)

#global variables
x = 5
def my_func():
    x =  10
    print(x)
my_func()
print(x)

#strings
x = 'hello world'
print(type(x))
print(len(x))
print(x[1])

#slicing
print(x[:5])
print(x[6::1])
print(x[::-1])

#string methods
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())

y = 'HellO WoRld'
print(y.swapcase())

print(x.isupper())
print(x.strip())

print(x.split(' '))

print(x.replace('h', 'H'))

a = '100'
b = '200'
print(a + " "+ b)

# FORMAT strings
x = 25

print('my name is prathyusha iam {} years old'.format(x))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []

for i in my_list:
    if i%3 == 0:
        print(i)
        # new_list.append(i)
# print(new_list)


for i in range(0, 10):
    if i%2==0:
        print('even no is:', i)

n = 10
i = 1
while i < n:
    if n%2 == 0:
        print(n,'is even')
    else:
        print(n,'is odd')
    i+=1

x = lambda a: a+10
print(x(5))

def my_func(n):
    return lambda a: a*n
x = my_func(3)
print(x(10))

num = 11
if num > 1:
    for i in range(2, num):
        if num%i == 0:
            print(num, 'is not a primenumber')
            break
    else:
        print('prime number')
else:
    print('not a prime number')
