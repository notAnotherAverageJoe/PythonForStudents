# Immutable = You cannot change the items after creation.

# Items can be of any type (int, str, list, etc.).



# 🧠 Tuple vs List
# Feature	    Tuple	List
# Mutable	    ❌ No	✅ Yes
# Syntax	    (1, 2)	[1, 2]
# Performance	Faster (immutable)	Slightly slower
# Use case	Fixed structure	Dynamic data
t = (10,20,30)
print(t[0])
print(t[1])
print(t[2])
print(t[-1])
print(len(t))


empty = ()

single = (5,) #must have comma for singles

nested = (1, (2,3), 4)

mixed = ("howdy", 3.14, 42)

print(mixed[0])

t = (1,2,3)
# t[0] = 200 X type error

t = ([1,2], 3)
# this works because the list is mutable
t[0].append(3)
print(t)



# Fixed data structures (e.g., RGB color, x/y coordinates)
rgb = (255, 0, 127)
point = (4.5, 9.2)

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person('Joseph', 28)

print(p.name)  # Joseph
print(p.age)   # 28

# iterating over tuples 
colors = ('red','blue','green')
for color in colors:
    print(color)
    
# destructuring tuples
person = ("James", 68)
name, age = person
print(name, age)






#tuples loops

pairs = [(1,'a'),(2,'b')]
for number, letter in pairs:
    print(number, letter)
    
# use case to return multiple values from a function

def min_max(nums):
    return(min(nums), max(nums))
result = min_max([7,14,2,9])
print(result) #(2,14)

#tuples are hashable, lists are not
cords ={(0,0): "main", (1,1):"Second"}
print(cords[(0,0)]) #main
print(cords[(1,1)]) #second