# ---------FOR LOOPS------
# for letter in [1,2,3,4]:
#     print(letter)
# for letter in 'string':
#     print(letter)
# for letter in 'hi','bye','gn': -- can assume it treats as list
#     print(letter)

# print("\tscore:",score)  check whether \t is for space or tab
# print(4/2),print(4//2) / returns floating point and // returns integer
# ** returns square of the number
# print(3**2)
# we can also use else block along with for Loop 
#  from types import CodeType ---- needs to be checked once again in python documentation


# x=list(range(5,10,2))
# print(x)
# print('I love {} for "{}!"'.format('Geeks', 'Geeks'))


# break statement in for loops
# continue is used to skip executing the remaining part of the body(example in for loop)
# print()  -- this function prints a blank line 
# the pass statement --- used to indicate that nothing needs to be done and just pass on to the next code snippet available

# is.digit(),is.alpha() tells whether they are characters or numbers

# explore about list comprehensions
# like writing a line in short form of Code 
# print([x for  x in range(5)])
# combined=[(i,j) for j in stationery for i in colors]
# combined=[number for number in range(51) if number%2==0 if number%5 ==0 ]


# comprehension including transformations

# num=['even' if i%2==0 else 'odd' for i in range(10)]
numbers=[30,12,18]
z=['small' if number<20 else 'large' for number in numbers if number%2==0 if number%3==0]
print(z)
print(True)
print(True+1)
