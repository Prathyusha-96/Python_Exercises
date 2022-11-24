#list comprehensions
fruits = ['apple', 'banana', 'cherry', 'guva']
new_list = []
for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)

#using list comprehension
res = [x for x in fruits if 'a' in x]
print(res)

newlist = [x for x in fruits if x!='apple']
print(newlist)

#iterable
result = [x for x in range(10)]
print(result)

result = [x for x in range(10) if x < 5]
print(result)

#even no
num = [x  for x in range(10) if x%2 == 0]
print(num)

#sort list
mylist = ['apple', 'banana', 'orange', 'cheery', 'mango']
mylist.sort()
print(mylist)

mylist = ['apple', 'banana', 'orange', 'cheery', 'mango']
mylist.sort(reverse=True)
print(mylist)

list1 = [100, 20, 45, 62, 2, 15]
list1.sort()
print(list1)

#Sort Descending
list1 = [100, 20, 45, 62, 2, 15]
list1.sort(reverse=True)
print(list1)


#CASE sensitive
#by default sort() method is case sensitive

thislist = ['Apple', 'banana', 'Cherry', 'guva','Mango']
thislist.sort()
print(thislist)

thislist = ['Apple', 'banana', 'Cherry', 'guva','Mango']
thislist.sort(key = str.lower)
print(thislist)

#join lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)