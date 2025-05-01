# primitive data types
# INT
age = 1903
print("Your age:", age)

# FLOAT
price = 23.98
print("The price:$", price)

# BOOL
is_running = False
print(f"Engine running: {is_running}")

# STR can only concat str
your_name = "Jurassic"
print("Your name: " + your_name)

a = "app"
n = "le"
print(a + n)
# noneType
result = None

# Not primitives
# LIST
nums = [1, 2, 3, 4, 5]
nums.append(6)
print(nums)

# TUPLE order, immutable/ this prints 20
coordinates = (10, 20, 30)
print(f"COORDS: {coordinates[1]}")

# DICTIONARY or DICT
person = {"name": "Joe", "age": 34}
print(f"Person name: {person['name']}")
print(f"Person age: {person['age']}")
person["age"] = 45
# changes age
print(f"Person age: {person['age']}")

for i in range(len(nums)):
    print(i)
