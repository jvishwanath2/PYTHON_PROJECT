# def hidxc():
#     print("hi")
# hidxc()

# def 123python():
#     print('hi')     --- this is wrong syntax  function name cannot start with number or digit.
# def documented_func():
# *** this func does something that  is well documented ***
# print("hello")


# documented_func()
# documented_func,documented_func.__doc__   need to check those  able to run in jupiter notebook but not in vscode
# functions as objects  -- needs to be checked
# documented_func()
# return None
# we can return two or more variables in a function and the result will be stored in tuple format

# def add_sub(x, y):
#     return x+y, x-y


# a, b = (add_sub(3, 4))
# print(a, b)
# # a,_=(add_sub(3, 4)) --  ignoring the subtracted value _ is used to ignore the returned value

# positional and keyword arguments are possible in function definition
# default arguments are also possible
# all the arguments that have default values should be specified at the  end otherwise it results in error.


# def print_fn(*args) - --*args represents that we can give any number of arguments and it takes inputs in


# form of tuples

# positional arguments cannot follow keyword arguments it gives error in python in function definition


# def print_fn(*args):
#     args_type = type(args)
#     print(args_type)
#     print(args)


# print_fn('bob')
# print_fn('dxc', 'skf', 'snow')
# names_list = [1, 2, 3, 4, 5]
# print_fn(*names_list) - - *names_list unpacks the elements in the list and makes as individual elements in the tuple
# def print_fn(*arg):
#     args_type = type(arg)
#     print(args_type)
#  print(arg)  ---- doubt needs to verify with others


# print_fn('bob')

# **kwargs takes only variable number of  keyword arguments and returns output in the form of dictionaries.
def stu_det(**kwargs):
    print(type(kwargs))
    print(kwargs)


stu_det(name='ram')
dic = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
print(dic)
stu_det(**dic)
