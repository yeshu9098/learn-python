# print("Hello World!")

# Variables in python

# name = "Yeeshu"
# age = 24
# float_age = 24.0
# is_adult = True
# print(type(age))

# x, y, z = "Orange", "Banana", "Cherry"

# print(name)
# print(age)
# print(float_age)
# print(is_adult)

# name = input("What is your name : ")
# print("Hello " + name)

# old_age = input("Enter Your Old Age : ")
# new_age = int(old_age) + 2
# print(new_age)

# first = input("Enter First No. : ")
# second = input("Enter Second No. : ")

# sum = int(first) + int(second)

# print(sum)

# name = "Yeeshu Sharma"

# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.find('h'))
# print(name.replace('Yeeshu', 'Yeshu'))
# print(name.replace("Y", "I"))
# print('Y' in name)


# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# Operators

# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print('Output ' + str(5 ** 2))

# i = 5
# i = i + 2
# i += 2
# print(i)

# Conditional Operators
# print(3 > 2)


# Logical Operators

# print(2 > 3 or 3 > 2)
# print(2 > 3 and 3 > 2)
# print(not 4 > 3)


# if-else statement

# age = 18

# if age > 18:
#     print("You can vote")
# elif age == 18:
#     print("Apply for Voter card")
# else:
#     print("You are under age")

# Range

# number = range(5)
# print(number)

# Loops

# i = 1
# while i <= 5:
#     print(i * '*')
#     i = i + 1

# for i in range(5):
#     print(i)

# List

# number = [1,2,2,2,3,4,5]


# print(number[-2])
# print(number[1:4])

# for i in number:
#     print(i)

# number.append('num')
# number.insert(1, 'insert')
# print('insert' in number)
# print(number)
# print(len(number))

# count = number.count(2)
# print(count)

# number.clear()


# number.reverse()
# print(number)

# Break and continue

# students = ['a', 'b', 'c', 'd', 'e']

# for student in students:
#     if student == 'd':
#         break
#     print(student)

# for student in students:
#     if student == 'c':
#         continue
#     print(student)


# Tuple

# a = (1,2,3,2,2,4,5,6)

# print(a.count(2))
# print(a.index(3))

# a = 1,2,3,4
# print(a)

# Set

# set = {1,2,3,4,4,5,5,6,6,6}

# for i in set:
#     print(i)

# Dictionary

# marks = {'english': 68, 'math':78}
# print(marks['english'])

# marks['physics'] = 67
# print(marks)

# marks['physics'] = 78
# print(marks)

# Functions

# 1. in-build function
# 2. Module Functions
# 3. User defined Functions

# import math
# print(dir(math))

# from math import sqrt
# print(sqrt(64))

# def sum(a, b):
#     return a + b

# print(sum(1, 2))

# x = lambda a : a + 10
# print(x(5))

# def my_function(name):
#   print(name + " Sharma")

# my_function("Yeeshu")


# Classes

# class Person:
#     name = 'Yeeshu'
#     age = 24

# p1 = Person()

# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    # def __str__(self):
    #     return f"{self.name} ({self.age})"

    # def myfunc(self):
    #     print("Hello my name is " + self.name, "And my age is " + f"{self.age}" + " and marks is " + f"{self.marks}")

# p1 = Person('Yeeshu', 24)

# print(p1)
# p1.myfunc()

# class Student(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks


# x = Student("Mike", 23, 78)
# x.myfunc()

# print(x.marks)


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 

# try:
#   print(x)
# except:
#   print("An exception occurred")

# Create a file
# f = open("myfile.txt", "x")

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read()) 


# import os
# os.remove("demofile.txt") 