import sys
# ////////functions recursion////////
# print(sys.getrecursionlimit())

#  sys.setrecursionlimit(100)  sets the recursion limit


def increment(num):
    print(num, end=" ")
    increment(num+1)


increment(1)

# explore about series in python how do you declare and use it

# generator function  concept of yield
# next(variable to which generator function is assigned)
# generators and closures


# explore .format function
