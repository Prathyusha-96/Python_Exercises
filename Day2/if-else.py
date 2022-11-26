a = 30
b = 20
if a > b:
    print('a')

#elif
a = 20
b = 25
if a > b:
    print('a')
elif a < b :
    print('b')

#else
a = 100
b = 200
if a>b :
    print('a is greater than b')
elif a == b:
    print('ai is  equal to b')
else:
    print('a is less than b')

#and operator

a = 10
b = 20
c = 15
if a> b and a>c :
    print('both are true')
else:
    print('not true')

#or
a = 18
b = 20
c = 15
if a > b or a > c :
    print('one is true')
else:
    print('not true')

#nested if
x = 20
if x > 10:
    print('above ten')
    if x > 5:
        print('above 30')
    else:
        print('a')

#while loops

# i = 1
# while i < 5:
#     print(i)
#     i += 1

# i = 1
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i +=1

i = 1
while i < 10:
    i +=1
    if i == 5:
        continue
    print(i)
