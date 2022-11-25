my_dict = {'name':'john', 'age': 25, 'proffe': 'engineer'}
print(my_dict['name'])
print(len(my_dict))
print(type(my_dict))

#accessing items
print(my_dict.get('age'))

#get keys
print(my_dict.keys())

my_dict['hobby'] = 'playing'

print(my_dict.keys())

#get values
print(my_dict.values())

my_dict['age'] = 30
print(my_dict.values())

#items
print(my_dict.items())

#change items
dict1 = {'Name': 'Cris', 'Subject': 'Maths', 'Hobby': 'Reading', 'Age': 20}
dict1['Proffe'] = 'Artist'
print(dict1)

#update the values
dict1['Subject'] = 'Science'
print(dict1)

dict1.update({'Age': 25})
print(dict1)

#remove items
dict1.pop('Name')
print(dict1)

dict1.popitem()
print(dict1)

del dict1['Age']
print(dict1)

dict1.clear()
print(dict1)

#looping through a dictionary
for x in my_dict:
    print(x) #keys 

for x in my_dict.keys():
    print(x)   

for x in my_dict:
    print(my_dict[x]) #print the values

for x in my_dict.values():
    print(x)


for x, y in my_dict.items():
    print(x,y)
