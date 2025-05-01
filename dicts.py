person = {"name": "Joe", "age": 87, "job": "Developer"}
print(f'Your name is: {person["name"]}')

# adding to dicts
person["city"] = "the moon"
print(person)
# access a key within the dict
print(person.get("age"))  # returns 87 the users age

# remove a key from the dict
del person["job"]  # deletes key and the associated value
print(person.get("job"))  # returns None

# prints keys/values/items
for key, value in person.items():
    print(f"{key}: {value}")
# prints the keys
print(person.keys())
# prints the values
print(person.values())
# prints the items
print(person.items())

menu = {"taco": 2.99, "burger": 5.99, "pizza": 7.99}

print("Choose an item")
print("1. tacos\n2. burgers\n3. pizza\n")
choice = int(input("Enter order number here -> "))
match choice:
    case choice if choice == 1:
        print(menu["taco"])
    case choice if choice == 2:
        print(menu["burger"])
    case choice if choice == 3:
        print(menu["pizza"])
    case _:
        print("Invalid choice")


menu2 = {
    "taco": {"price": 2.99, "ingredients": ["beef", "cheese", "lettuce"]},
    "pizza": {"price": 7.99, "size": "Large"},
}

print(menu2["taco"]["ingredients"])  # ['beef', 'cheese', 'lettuce']
print(menu2["taco"]["price"])  # 2.99
print(menu2["pizza"]["size"]) # Large
print(menu2["pizza"]["price"]) # Large
for key, value in menu2.items():
    print(f"{key}: {value}")

# dictionary comprehensions
squares = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# merge dictionaries
a = {"a": 1}
b = {"b": 2}
c = a | b
print(c)  # {'a': 1, 'b': 2}
# or
print(f"{a.update(b)}")




# reverse a dictionary
rev_dicts = {v: k for k, v in c.items()}
print(f"Reversed dictionary: {rev_dicts}")

def freq_count_sentence(sentence):
    seen = {}
    words = sentence.split()
    print(f"Words after being split {words}")
    
    for word in words:
        if word not in seen:
            seen[word] = 1
        else:
            seen[word] += 1
    return seen

sentence = "this is a test this is only a test"
print(freq_count_sentence(sentence)) # {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
            
    