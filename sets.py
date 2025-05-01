# 🧺 What is a set?
# A set is an unordered, mutable collection of unique elements.
# Think of it like a bag that automatically removes duplicates and doesn’t care about order.

nums = set([1, 2, 3, 4, 5])
print(nums)

num2 = set([3, 4, 5, 6, 7, 8, 9, 10])
# merge sets
print(nums | num2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# intersection elements
print(nums & num2)  # {3, 4, 5} what they have in common

# difference
print(nums - num2)  # {1,2} what nums has that num2 does not
print(num2 - nums)  # {6, 7, 8, 9, 10} whats num2 has that numes does not

# symmetric difference
print(nums ^ num2)  # {1, 2, 6, 7, 8, 9, 10} in one but not both

lang = set()
lang.add("Python")  # adds one element
print(lang)  # {'Python'}
lang.update(["Java", "JavaScript", "Go"])
print(lang)  # {'Java', 'JavaScript', 'Python', 'Go'}
lang.remove("Java")  # removes on element if it finds it if not found it sends a error
print(lang)  # {'Python', 'JavaScript'}
lang.discard("Go") # removes it and no error, either way
lang.clear()

# 🧠 Use cases:
# Removing duplicates from a list

# Membership testing (in)

# Comparing datasets

# Tag systems, recommendations, etc.