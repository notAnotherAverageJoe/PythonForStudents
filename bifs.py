# len() – Get the length of an object
len("howdy!") #5 

# type() – Get the type of a variable
type(56) # int

# str() – Convert to string
str(100)

# int() convert to int
int("50") # 50

# convert to float
float("6.43") # 6.43

# convert to bool
bool(0) # false

# range of numbers
for i in range(10): print(i)

#enumerate
for i, v in enumerate(['a','b']): print(i,v) # 0 a, 1 b

#zip
zip(['a','b'], [1,2]) # [('a', 1), ('b', 2)]





#map apply a function to each item
list(map(str.upper, ['a','b'])) # ['A', 'B']

#filter allows you to filter an item based on conditions
list(filter(lambda x: x > 5, [3,6,9])) # [6,9]

#sorted() sorts iterables
sorted([3,5,1,4,2]) # [1,2,3,4,5]

# reversed() reverse an iterable
list(reversed([3,2,1])) # [1,2,3]

# any returns true is any element is true
any([0, False, 10]) #true

#all() returns true if all elements are true
all([1, True, "yes"])

# create a list
list('abc')  # ['a', 'b', 'c']

#create a dictionary
dict(a=3, b=4, c=5) #{'a':3, 'b':4, 'c':5}

#create a set()
set([1,2,3,4,5]) #{1,2,3,4,5}

#immutable tuples
tuple([1,2]) # (1,2)

#id gets memory address
print(id("howdy"))

#isinstance() checks variable types
isinstance(15, int)  #true


print(help(str))
