#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = []
for i in range(1, 100):
    if (i%4  == 0) and (i%3 == 0):
        my_list.append(i)
print(my_list[::-1])


# In[2]:


my_list = []
for i in range(1, 100):
    if (i%4  == 0) and (i%3 == 0):
        my_list.append(i)
print(my_list[::-1])


# In[3]:


my_list = []
for i in range(100, 1, -1):
    if (i%4  == 0) and (i%3 == 0):
        my_list.append(i)
print(len(my_list))


# In[4]:


count = 0
for i in range(100, 1, -1):
    if (i%4  == 0) and (i%3 == 0):
        count += 1
        
print(count)


# In[5]:


for i in range(1, 10, 2):
    print(i)


# In[6]:


for i in range(1, 5):
    print (i*i)


# In[7]:


new_list = ['cat', 'dog', 'rabit']
for letter in new_list:
    for i in letter:
        print(i)


# In[8]:


def my_func(num):
    if num%2 == 0:
        print(num, 'is even number')
    else:
        print(num, 'is odd number')
my_func(27)


# In[9]:


my_list = ['a', 'z', 'l', 'o', 'b', 'e']
my_list.sort()
print(my_list)


# In[23]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
new_list = [x for x in fruits if 'a' in x]
print(new_list)


# In[24]:


new_list = [x for x in fruits if x!= 'apple']
print(new_list)


# In[10]:


my_list1 = []
for i in range(1, 10):
    my_list1.append(i)
print(my_list1)

for i in my_list1:
    if i%2 == 0:
        my_list1.remove(i)
print(my_list1)


# In[11]:


my_list2 = []
for i in range(11, 20):
    my_list2.append(i)
print(my_list2)


# In[12]:


a = [1, 2, 3, 4, 5]
add = 0
for x in a:
    print(x)
    add += x
print(add)


# In[13]:


a = [1, 2, 3, 4, 5]
tot = 1
for x in a:
    tot *= x
print(tot)


# In[14]:


a = [10, 20, 50, 25, 30]
print(max(a))


# In[15]:


list1 = [63, 25, 45]
list1[0],list1[2] = list1[2], list1[0]
tot = 0
for x in list1:
    tot += x
print(tot)
print(list1)


# In[16]:


List = [23, 65, 19, 90]
List[0], List[2] = List[2],List[0]
List


# In[17]:


len(List)


# In[18]:


count = 0
for i in List:
    count += 1
print(count)


# In[19]:


test_list = [1, 6, 3, 5, 3, 4]
i = 7
if i in test_list:
    print('exist')
else:
    print('not exist')


# In[20]:


x = [i for i in range(1, 10)]
print(x)


# In[21]:


#fibonaccie series
num = 10
a = 0
b = 1
print(a, b, end=' ')
for i in range(2, num):
    c = a+b
    a = b
    b = c
    print(c, end=' ')


# In[22]:


list_ = [34, 12, 64, 55, 75, 13, 63]  
  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ) )
  
print(odd_list)  


# In[26]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person('john', 32)
print(p1.name)


# In[34]:


#reverse an integer
n = 123
reverse = 0
while n!= 0:
    reverse = reverse*10 + n%10
    n = (n//10)
print(reverse)


# In[54]:


1%10


# In[52]:


12%10


# In[53]:


12//10


# In[35]:


123%10


# In[36]:


123//10


# In[48]:


n = 12
if n > 1:
    for i in range(2, n):
        if(n%i==0):
            print(n, 'is not a prime number')
            break
    else:
        print(n, 'is prime number')


# In[57]:


n = 11
for i in range(2, n):
    if(n%i==0):
        print(n, 'is not a prime number')
        break
else:
    print(n, 'is prime number')


# In[51]:


num = 10
a = 0
b = 1
print(a, b, end=' ')
for i in range(2, num):
    c = a+b
    a = b
    b = c
    print(c, end=' ')


# In[70]:


#PALINDROME NUMBER
num = 121
reverse = 0
while num!=0:
    reverse = reverse*10 + num%10
    num = (num//10)
# print(reverse)
if reverse==num :
    print('palindrome')
else:
    print('not palindrome')


# In[ ]:




