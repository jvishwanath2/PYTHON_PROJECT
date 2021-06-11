#print("hi")
#list is a complex data type which is a ordered collection of elements and are specified within square brackets
# integer=[1,2,3,4]
# print(integer)
# print(type(integer))
# list can contain elements of any datatype
# from io import StringIO
# from os import error, waitpid


mixed_list=[1,True,'true']

# print(len(mixed_list))
#print(mixed_list[-1])
# in lists if we try to access by giving negative index then it means we are trying  to access backwards
mixed_list[2]='false'

#important

# mixed_list[3]='hi'-- error we cannot add element in a list where index is out of range we need to  use invoke functions like append
mixed_list.append('hi')
#append takes only one argument and adds only one element cannot add two.

#list.insert(index position, element that needs to be added)
# mixed_list.insert(5,'bye')

# mixed_list.insert(4,'how are you')
# print(mixed_list)
# list.extend([]--list that needs to be added)
# string_list=['dxc','cgi','ibm']
#concatenating string_list and mixed_list
# total_list=mixed_list+string_list
# print(total_list)
# to find index
# print(total_list.index('ibm'))
#remove function list.remove(element that needs to be removed)
#total_list+=['apple','visa']-- it adds them to the orginal list += operator is used
#list_name.sort()-- sorts in lexicographical order or ascending
#list_name.reverse()-- reverses the list
#list_name.pop() removes the last element
#list_name.count(element)-- tells the occurence
#set(list_name)-- removes the duplicates and converts into  a set which is enclosed in a curly braces
#list_name.clear() clears the elements
#list2=list1.copy()-- creating a copy of list1 and assigning it to list2 AND it creates a deep copy and changes in original does not effect the newly created one
# del list_name deletes the list and disappears from the memory
# list_1=list_2  this is example of shallow  copy they refer to the same list it means changes in one list affects the other
#list_num which is list contains  numbers
#max(list_num)
# min(list_num)
# len(list_num
# list_num.sort()
# sorted_list_num=sorted(list_num)-- returns sorted list of numbers and we are assigning it to sorted_list_num the orginal list is not effected
# sum(list_num)
# list_num*=2 -- result is we will get 2 sets of same lists since we are multiplying the list *2
# all([0]) ---output is False
# all([1]) -- returns true
# all([])-- an empty list returns True
# any([0,1])-- returns true 
# any([])-- returns false-- should refer  to this later some doubt

# list slicing operations----

list=[1,2,3,4,5,6]
# print(list[0:4]) -- end index is exclusive and it creates a deep copy of list
# list[6:]--- returns a empty list
# list[:3] --- starts with 0 and ends with index 2
# list[3:]--- starts with  index 3 and goes up to very end 
# list[0:-4] -- starts with 0 and ends with 4th to last or 4th from last with 4th element excluded
# list[-4,-1]-- output [3,4,5]
# list[a:b:c]-- c is the step size and it is default 1 for above mentioned
#print([list[1:2:]])
# list[::2] -- step size is two output --- [1,3,5]
# list[::-1]   travels through the reverse order
# list[-4:0:-1]
# funky way of assigning values to a list
# list[6:-1]=[100,1000] 100 occupies 6th index and 1000 occupies -1 i.e... last position in list

# --in command
# list=[1,2,3,4,5,6]
#  4 in list -- returns True
# 4 not in list --- returns false
# list.pop(should mention the index in brackets)


# working with strings as list of characters

# x='world'
# x[0]--w
# x[3]-- l -- it is acting as a list of characters
# x[0]--'B'---error as strings are immutable but u can assign entirely new String
# a,b,c,d,e=x
# print(a)-- output 'w'
# a,b,c,d=x throws an error
# a,b,_,_,_=x -- five placeholders on the left but only characters are assigned to a and b variables only

# input function


# input('how are you?')
# health_condition=input('how are you?')

# slicing operations are availale on strings

# invoking functions on strings

# place='newyork'
# place.startswith('n')-- returns True
# place.endswith('k')-- returns True
# place.count('y')-- returns 1
# place.lower()-- lowercase
# place.upper()-- uppercase
# str1==str2 -- checks whether equal or not   returns boolean
# place.find('c') -- returns index position
# place.index('c')-- returns index position
# split_new=place.split('y')--- returns a list of  strings before and after  letter yield
# split_allwords= place.split('') -- returns list of all the words basically
# split_place=['new','york','city']
# join_char=','
# join_char.join(split_place) -- returns new,york,city
# "|".join(split_place)   --- check the output

# -------TUPLES-------

# tuple is ordered collection of elements enclose in rounded brackets

# my_tuple=1,'hi',2.4
# print(type(my_tuple))

# a,b,c=my_tuple-- a=1,b='hi'
# nested tuples are possible and like mixed_tuple may contain string,list and tuple all the three

# all the in built functions supporting lists supports tuples

# int_tuple=(1,2,3,4)
# list(int_tuple) --- changing tuple into list
# set(int_tuple)--changes into set
# int_tuple[0]=99 -- error tuples are immutable
# del int_tuple[2] -- error cannot update or delete th fields in tuple
# but if there is a list in tuple then we can update or insert in that list 

# del int_tuple -- works Fine 

# tuple_a=(a,b)
# tuple_b=(1,2)
# zipped=zip(tuple_a,tuple_b) -- gives ordered pairs taking from tuple_a and tuple_b
# result=tuple(zipped) --- returns ((a,1),(b,2))
# tuple_x,tuple_y=zip(*result) --- to bring back the original tuples used to zip












