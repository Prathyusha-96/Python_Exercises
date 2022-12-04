f = open("demofile.txt", "r")
print(f.read())
print(f.readline())
f.close()

#create a file
# f = open('myfile.txt', 'x')
f = open('myfile.txt', 'a')
f.write('heloo how are you')

import os
os.remove("demofile.txt")

# import os
# if os.path.exists("demofile.txt"):
#    os.remove("demofile.txt")
# else:
#   print("The file does not exist")
