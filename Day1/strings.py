#basic strings
str1 = 'Hello'
str1 = "Hello"
print(str1)

#assign string to avariable
a = 'Hello world'
print(a)

#strings are arrays
print(a[1])

#string length
print(len(a))
#looping through

for x in 'banana':
    print(x)

#check string
txt = "The best things in life are free!"
print('free' in txt)
print('expensive'  not in txt)

if 'free' in txt:
    print('free is present')
if 'expensive' not in txt:
    print('no,expensive not present')

#slicing strings
a = 'hello, world'
print(a[2:5])

print(a[:5])
print(a[1:])

#modify strings
print(a.upper())
print(a.lower())
print(a.strip())
print(a.split(','))
print(a.replace('h', 'H'))


#String Concatenation
a = 'Hello'
b = 'World'
print(a + ' ' + b)

#String Format
age = 25
print('My name is john, Iam {} years old'.format(age))

#ex
item = 'Pizza'
price = 20
print('I want to Buy {} for {} dollors'.format(item, price))

#using index
print('I want to pay {1} dollors for {0}'.format(item, price))

#string methods
str1 =  "hello my name is john"
print(str1.capitalize())
print(str1.count('m'))
print(str1.title())

a = "HeLLo"
print(a.swapcase())
print(a.islower())