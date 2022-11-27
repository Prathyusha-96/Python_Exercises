fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

list1 = [1 ,2, 3, 5, 8]
for i in list1:
    print(list1)

string = 'prathyusha'
for i in string:
    print(i)
    if i == 'h':
        break

#break
string = 'prathyusha'
for i in string:
    if i == 'h':
        break
    print(i)
    
#continue
list1 = ['red', 'yellow', 'blue']
for x in list1:
    if x == 'red':
        continue
    print(x)

#RANGE FUNCTION
for i in range(6):
    print(i)

for i in range(2, 10, 2):
    print(i)

#nested loop
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
for x in list1:
    for y in list2:
        print(x, y)