#creating a function
def my_func():
    print('hello')

#calling a function
def my_func():
    print('hello')
my_func()

#arguments
#information can be passed into functions as arguments

def my_func(name, age):
    print(name, age)

my_func('prathyusha', 25)

#arbitary arguments(*args)
def my_func(*names):
    print('My name is '+ names[1])
my_func('john', 'deo', 'cris')

#keyword arguments
def my_func(fruit1, fruit2, fruit3):
    print('richest fruit is ' + fruit1)
my_func(fruit1='mango', fruit2='apple', fruit3='banana')

#arbitary keyword arguments(**kwargs)
def my_func(**fruits):
    print('richest fruit is ' + fruits['fruit1'])
my_func(fruit1='mango', fruit2='apple', fruit3='banana')

#default parameter value
def my_func(country = 'India'):
    print('Iam from ' + country)
my_func('usa')
my_func('london')
my_func()

#return values
def my_func(x):
    return 10 *x
print(my_func(10))