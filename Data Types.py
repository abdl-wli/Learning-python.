# print("hello world")


# NUMBERS

import random
import math
from traceback import print_tb

# what is numbers datatypes?
# Ansewer > all the number are called Numbers datatypes (all the phone number are called numbers datatypes)

 # I.e:-
# print(random.choice([1,5,4,2,36,7,4,]))
# print(random.randint(0,10))

# print(2 ** 5) 
    # 2*2*2*2*2 => 32

# age = 21
# print(age)

# print(math.pi)
# print(math.e)


# Strings

# any text or number in  double quotation " " or single quotation '' are called strings
# 
# username = 'Abdul Wali'
# print(username)
# print(len(username))
# print(username[5])
# print(username[2])

# course = 'python for everybody'
# print(course)
# print(len(course))
# print(f'Hello my Name is {username} and my course is {course}')
# print(course +" - " + username)

# print(course[9])
# username[1] = "C" string is immutable


# list
# what is list in python?

# Answer-> a list in python are the set of different data types and it begain with [] 

# languages = ['python' , 'javascript','c++','java','C#',]

# print(languages)
# print(type(languages))
#         # must return list []

# print(languages[2])
# print(len(languages))
# print(f"i'm currently learning the language which is {languages[0]}")



# Dictionaries

# Q: what is dictionaries in python?

# Ans->  the dictionaries in nothing but a key value pair and the combination of different datatypes

# I,e->

# user = {
#     'name' : 'abdul wali',
#     'age' : '19',
#     'course' : 'Python',
#     "hobbies" : ['Coding','circket','movies'],
#     'isOnFacebook': True,
    
# }

# print(user['name'])
# print(user['age'])
# print(user['isOnFacebook'])
# print(user['hobbies'][2])
# print(user['hobbies'][0])


# Tuples

# what is tuples?


# my_tupe = (1,2,3)
# print(my_tupe)
# print(my_tupe[0])

# courses = ('python',"javascript",'java','R',"C++")
# print(courses)
# print(courses[2])


mylist = ['kalob','zepher','henry','Toco']
print(mylist)

mylist2  = mylist
print(mylist2)
mylist2[3] = 'dog'
print(mylist2)

print( mylist == mylist2)
print(mylist is  mylist2)
# mylist = [1, 2, 3]
# mylistTwo = mylist

# # mylist[0] = 55
# print(mylistTwo)

# # mylistTwo = [1 , 2 , 3]

# print(mylistTwo == mylist)
# print(mylistTwo is mylist)
