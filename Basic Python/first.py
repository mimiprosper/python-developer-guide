# import statement
import  os
import  shutil
import pathlib as path

# import  django as new_django
# from  django import urls
# from  django import  utils

# import module as imported_module
# user =imported_module.GetUser("victor",26,1995,"male")
# print(user.call_user())


# file operation
# import pathlib as path
# all = path.Path("text.text")
# try:
#     # for readLines in fs.read():
#     #     print(readLines)
#     fs = open("text.text")
#     fileWrite = open("text.text", "w")  # to write contents inside the file
#     # print(fileWrite.writable())
#     fileWrite.write("""
# this file was modify
#     """)  # calling the write function to write into the
#     fileRead = open("text.text", "r")  # to read file
#     append = open("text.text", "a")  # appending contents to a file
#
# except SyntaxError:
#     print('invalid')
# finally:
#     fs.close()  # closing file after operation








# new_django.setup(True)
# importing file from directory to a module
# using pathlib library to import all files from the root directory

# import  pathlib as all_files
# store = []
# for filesList in all.glob("*.*"):
#  store.append(filesList)
#
# print(store[5])


# using the "path()" function to get the path of the directory example
# "folder/file.py or folder/suborder/file.py" the default is the parent directory
# get_file = all_files.Path()
# using the "glob()" function to specify the type of file you want to retun or use
# for all in get_file.glob("*.*"):
#     print(all)


# use = path.Path("email")
# for files in use.glob("*.*"):
#     print(files)
import sys
import os
# creating directory
# use.rmdir()


# installing external packages from another source using the terminal
# to install packages go to pypi.org and search for any package name
# copy the command line example "pip install Django"


# shop_list = [62, 38, 90, 67, 89, 37, 28]
# start = 0
#
# higher = shop_list[0]
# for get in shop_list:
#     if higher < get:
#         higher = get
# print(f"the highest number is {higher}")
#
# lower = shop_list[0]
# for get in shop_list:
#     if lower > get:
#         lower = get
# print(f"the lowest number is {lower}")

# list = [5,2,5,2,2]
# for count in list:
#     print("*"*count)

# items = [73,3,84,490,]
# items[0]= 80
# print(items[:])


# _2D_list = (
#     [
#         [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         ["chide", "mark", "josh"],
#         [False, True],
#         (1999, 1998, 1956, 1978),
#         {"name": "jane", "age": 49, "is_married": False}
#     ])
#
# _2D_list.append([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
# for rows in _2D_list:
#     print(rows)
#     for items in rows:
#         print(items)

# greeting = input("> ")
# emoji = {
#     "sad":":(",
#     "happy":":)",
# }
# output = ""
# split_all = greeting.split(" ")
# for words in split_all:
#     output += f"{emoji.get(words,' ')} "
#
# print(greeting+output)
# print(split_all)
#
# number = (input("enter a number" ))
# convert_to_words ={
#     "0":"zero",
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine"
# }
# to_string = ""
# for numbers in number:
#     to_string += convert_to_words.get(numbers) +" "
# print(to_string)

# list_duplicate = [1,3,5,5,3,7,5,7,8,3,1,8,6,9]
# sorted_item = []
#
# for list_sort in list_duplicate:
#     if list_sort not in sorted_item:
#         sorted_item.append(list_sort)
#
# print(sorted_item)

# functions in python
# def first_function(my_name,last_name):
#     private = "my name"
#     print(f"hi {my_name} {last_name}")
#     return private
#
#
# greeting = input("> ")
# def greetings(greet):
#     emoji = {
#         "sad": ":(",
#         "happy": ":)",
#     }
#     output = ""
#     split_all = greet.split(" ")
#     for words in split_all:
#         output += f"{emoji.get(words,' ')} "
#     return  f'{greet} {output}'
#
#
# print(greetings("hey am sad today"))
# print(greetings("hey am so happy today"))
# print(greetings("hey am not happy today"))


# first_function("jane","miller")
# store = first_function("john","williams")


# test 1: create a function that take 3 arguments  1. for the name, 2. for the age and 3 for a list of numbers
# test 2: create a function that has a return value and print it out

# def my_function(name, age, some_list_of_numbers):
#     public = [name,age,some_list_of_numbers]
#     print(f'{name} {age} {some_list_of_numbers}')
#     return  public

# list = [1, 2, 3, 4]
# get_function = my_function("emma", 34, list)
# print(get_function)
# my_function("emma", 34, [1, 2, 3, 4])

# def calc_sum(a,b):
#    print(a * b)
#    return a*b

# print(calc_sum(2,4))

# def new_item(_1st,_2nd,_3rd,_4th):
#     sum_total = 0
#     for total in _1st:
#         sum_total += total
#     return sum_total
#
#
#
# print(new_item([6,4,3,6],4,3,6))

# types of function arguments
# def new_item(_1st,_2nd, _3rd, _4th):
#     sum_total = 0
#     for total in _1st:
#         sum_total += total + _2nd + _3rd + _4th
#     return sum_total
#
#
# print(new_item([6, 4, 3, 8],_4th=4,_3rd=5, _2nd=6))


# def set_default(name, day="morning"):
#     message = f"hi {name} {day}"
#     return message
# get = set_default(input("enter your name "))
# print(get)

# def set_default(first_name, last_name, day="morning"):
#     message = f"hi {first_name} {last_name} good {day}"
#     return message
# get = set_default(last_name=input("your last name "),first_name=input("enter your first name "))
# print(get)


# exception in python

# try:
# number = int(input("enter any number"))
#     print(number)
# except ValueError:
#     print("please enter a number")

# obj = {
#     "name": "ven",
#     "last": "miller",
#     "age":23,
#     "is_married":False
# }
# try:
#     print(obj["birth_yr"])
# except KeyError:
#     print("birth_yr is not in this dictionary")
#
#
# obj = {
#     "name": "ven",
#     "last": "miller",
#     "age": 23,
#     "is_married": False
# }
#
#
# def get_data(datList, input_form=input("enter api key ")):
#     status_code = 0
#     try:
#         data = datList[input_form]
#         status_code += 1
#         print({"respond_data": data, "status code": status_code})
#     except KeyError:
#         print(f"invalid Api ker, status code: {status_code}")
#
#
# get_data(obj)

# classes
# class FirstClass:
#
#     def greeting(self,day):
#         print(f"hi good  {day}")
#
#     def get_name(self,Name):
#         print(Name)
#
#
# store = FirstClass()
# store.greeting("morning")
# store.get_name("Jane")

# classes init method
# class FirstClass:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def greeting(self, day):
#         print(f"hi good {self.name}, {day} ")
#
#
# store = FirstClass("john",28)
# print(store.name)
# store.greeting("morning")

# create a class that has two methods one is the name of the person and the other is a greeting message
# hint: like this       -person
#                      -greeting

# class Pastor:
#     def store_name(self, my_name):
#         print(my_name)
#
#
#     def say_greetings(self, good_day):
#             print(f"This is {good_day}")
#
#
# user= Pastor()
# user.store_name("ven")
# user.say_greetings("morning")
#
#

# # inheritance in python
# obj = {
#     "name": "newbie",
#     "age": 20,
#     "gender": "custom"
# }

#
# class Inheritance:
#     def inherit(self, default_name=obj["name"], default_age=obj["age"], default_gender=obj["gender"]):
#         default_name = default_name
#         default_age = default_age
#         default_gender = default_gender
#         return {
#             "name": default_name,
#             "age": default_age,
#             "gender": default_gender
#         }
#
#
# class User(Inheritance):
#     pass
#
#
# class Pastor(Inheritance):
#     pass
#
#
# class Chi(Inheritance):
#     pass
#
#
# chi = Chi()
# pastor = Pastor()
# store = User()
#
# print(store.inherit())
#
#
# def input_form(message):
#     return input(message)
#
#
# print(chi.inherit("chris", 46, "male"))
# print(pastor.inherit(input_form("enter your name"), input_form("enter age "), input_form("gender")))
