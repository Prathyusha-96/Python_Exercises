mylist = ['apple', 'banana', 'cherry']
print(type(mylist))
list1 = ['apple', 'banana', 'cherry']
list2 = [20, 10, 52]
list3 = [True, False]
print(len(list1))
print(list2[1])
print(list3)

#The list() Constructor
l1 = list(('john', 'deo'))
print(l1)

#change list items
my_list = ['apple', 'banana', 'kiwi', 'cherry']

my_list[1] = 'Guva'

my_list[1:3] = ['Guva', 'melon']
print(my_list)
print(my_list[1:3])
print(my_list[:-1])

#using insert method
#to insert a new list item without replacing any of the existing value
my_list.insert(2, 'Mango')
print(my_list)

#list methods
#append
my_list.append('orange')
print(my_list)

#extend
list2 = ['fruits', 'colors', 'veggies']
my_list.extend(list2)
print(my_list)

#remove 
list2.remove('colors')
print(list2)

#pop specified the index
list2.pop(0)
print(list2)

#pop the last item in the list
list2.pop()
print(list2)

#del specified the index
li = [1, 2, 3, 4, 5]
del li[0]
print(li)

#delete the list completely
del li

#clear
# li.clear()
# print(li)

#looping through list
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)

#looping through range and len
my_list1 = [1, 2, 3, 4, 5]
for i in range(len(my_list1)):
    print(my_list[i])

#using while loop
this_list = ['white', 'red', 'yellow']
i = 0
while i < len(this_list):
      print(this_list[i])
      i = i + 1

#Looping Using List Comprehension
thislist1 = ['john', 'deo', 'cris', 'leo']
[print(x) for x in thislist1]

