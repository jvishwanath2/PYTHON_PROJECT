# -------dictionaries------ contains key value pairs which are enclosed in curly brackets.
# empty_dic={}
# fruits={'mangoes':100,'bananas':20,'guava':50,'apple':200}
# print(fruits['bananas'])
# keys should be unique
fruits_1={'mangoes':100,'bananas':20,'apple':50,'apple':200}
# print(fruits_1)-- returns {'mangoes': 100, 'bananas': 20, 'apple': 200}  
# print(fruits_1.keys()) -- returns keys
# 'bananas'   in    fruits_1.keys()  -- returns true
# print(fruits_1.values()) -- returns values of dic
# fruits_1.['grapes']=300 -- assigning new key value pair and also update the present key value pairs
# fruits_1.get('grapes')-- returns 300  
#  dic are mutable

empty_dic={}
#  using assignment operator
empty_dic[1]=2
empty_dic[2]=3
# empty_dic[3]=4 --example

# dictionaries inside a dictionary is very much possible

# invoking functions on dictionaries
fruits={'mangoes':100,'bananas':20,'guava':50,'apple':200}
# len(fruits)  ---- 4
# print(sorted(fruits)) -- returns ['apple', 'bananas', 'guava', 'mangoes'] -- sorted list of keys

# print(sorted(fruits),reverse=True) -- list of keys in  reverse order
# print(fruits.items())
# -- returns dict_items([('mangoes', 100), ('bananas', 20), ('guava', 50), ('apple', 200)])
# print(fruits.items())-- returns list of  tuples of key value pairs
# copy_fruits=fruits.copy() --- deep copy
# copy_fruits.pop('mangoes') -- removes the key 'mangoes' and returns the value 100 we can store in another variable if we wish to
# copy_fruits.popitem() -- arbitrarily removes any key value pair from the dic it can be anything
# dict_age={'ram':30}
# new_dict_age={'ram':34,'sam':40}
# dict_age.update(new_dict_age)-- updates ram age to 34 and adds the 'sam' key value pair
# copy_fruits.clear()-- clears
# del copy_fruits -- frees up the memory

# --------SETS-------

# no duplicates and no intrinsic order and enclosed in curly braces
# mixed_set={'hi',1 ,True}
# sets can contain only immutable elements and this is how set ensures that its elements are unique
# so sets cannot contain lists and dictionaries which are mutable

# set1={1,2,3,4}
# print(set1[1])-- error bcz sets do not support indexing since order is not unique and constant
# set1.add(5)-- adds 5 to the set
# set1.discard(1)  ,set1.remove(2)  both removes 1 and 2 elements
# discard does not throw error but remove does if we try to discard already discarded element

# num1={1,2,3,4,5}
# num2={6,7,8,9,10}
# num1.union(num2)  -- performs union
# num1.union(num2,num3,num4..so on....)
# num1.intersection(num2) -- finds common elements

# num1.difference(num2) returns num1-num2 exactly as sets in  high school
# num1.intersection_update(num2) -- num1 gets updated and stores the intersecton of num1 and num2
# num1.difference_update(num2)-- num1 gets updated and stores the difference of num1 and num2
# num1.isdisjoint(num2) --- returns true or False

# num1.issubset(num2)

# num1.issuperset(num2)

# ----LIST CONVERSIONS-----

# my_list=['sam',20,'abhi',25,'ram',28,'ravi',30]

# print(tuple(my_list)) --- returns a list

# my_list_1=[['sam',20],['abhi',25],['ram',28],['ravi',30]]
# print(dict(my_list_1)) -- converts list into dic and takes 'sam' ,'abhi' are keys and 20,25 are values 
# correspondingly
# my_list_2 = dict(my_list_1)
# my_list_3= list(my_list_2) -- the new list my_list_3 contains only all the keys from the dictionary my_list_2

# my_list_4= list(my_list_2.values())






