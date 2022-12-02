try:
    print(x)
#many exceptions
except NameError:
    print('x is not defined')
except:
    print('something went wrong')

#else
try:
    print('Hello')
except:
    print('something went wrong')
else:
    print('nothing went wrong')

#finaaly
try:
    print(x)
except:
    print('something went wrong')
finally:
    print('executed')

#USER INPUT

username = input('Enter username: ')
print('Username is:', username)

#string formatting
price = 200
print('The price is {:.2f} dollors'.format(price))

#multiple values
name = 'john'
age = 30
print('My name is {} , Iam {} years old'.format(name, age))

#using indexes
print('My name is {0} , Iam {1} years old'.format(name, age))