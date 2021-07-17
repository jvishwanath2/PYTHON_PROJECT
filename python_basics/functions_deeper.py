# country="india"
# city="banglore"
# def details():
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)

# details()
# country = "india"
# city = "banglore"

# here in this statement the print statement references local variable not the global variable
# def details():
#     city = "hyd"
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)

# details()
# country = "india"
# city = "banglore"


# def details():
#     city = "orissa"
#     city += "chennai"
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)


# details()

# country = "india"
# city = "banglore"


# def details():
#     global city
# # if we want to change and reference globa variable within function then global keyword is used so this also effects global variables declared intially.
#     city += "chennai"
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)


# details()

# def details(country, city):
#     country += "orissa"
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)


# details("india", "bangalore")

# country = "india"
# city = "banglore"


# def details1():
#     country += "orissa"
#     print("my country is"+" "+country)
#     print("my  city is"+" "+city)


# details1()

# help("modules")
# import math
#print(math.pi, math.e, math.ceil(8.1), math.pow(2, 4), math.sqrt(24))
# math.factorial(6)
from os import path
import os
# os.getcwd()
# print(os.environ)
# #  - - dictionary of all environment variables
# print(os.environ['PATH'])
# print(user)
# print(os.listdir())  lists all directories
# print(os.listdir("."))
# os.mkdir("./my_temp_dir")    creates a new directory or folder
# os.rename(t1.t2) renames from t1 to t2
# os.rmdir("any directory name")
# os.mkdir("my_temp_dir2")
# path.isdir(cwd)
# path.isfile(cwd)
# # *

# import random
# print(random.random())
# print(random.randint(100, 110))
# mylist = []
# random.choice(mylist) - - returns any element


# functions are first class citizens in python
# example
import math


# def perimeterofcircle(radius):
#     return 2*math.pi*radius


# def areaofcircle(radius):
#     return math.pi*radius*radius


# def diameterofcircle(radius):
#     return 2*radius


# def calculate(radius, fn):
#     return fn(radius)


# print(calculate(10, diameter))

#   *args is variable length input argument and it is in tuple and when we invoke the function the *args decouples or unpacks the tuple  into individual elements and it is better to use keyword argument instead of positional arguments to avoid confusion while using *args which is variable length argument

# def perimeterofrect(l, h):
#     return 2*(l+b)


# def areaofrect(l, h):
#     return l*h


# def calculate(*args, fn):
#     return fn(*args)


# print(calculate(10, 5, fn=areaofrect))
#  we can also asign  variables to functions like calprac =  calculate(10, 5, fn=areaofrect)  and  call this function using this variable  name and they can also be assigned to key value pairs in dictionary which is amazing


# functions as return values should explore later
# example
# store all operators in dictionary and invoke like shown below
# calc_dictionary[*](100,3)


# ////////// use of lambas
# imp points: - we cannot use control structure like if else, while and for loops in lambda function and u can only have expression and it is returned from lambda

#  we can also specify default specification in function argument when we call the function with no input arguments
# def cube(x): return x*x*x


# print(cube(5))

print((lambda x: x*2)(10))
print((lambda *num: sum(num))(1, 2, 3))
# should explore about **num --  it is variable length keyword arguments

# filter function
