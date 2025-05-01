def my_decorator(fun):
    def wrapper():
        print("Progam booting up")
        fun()
        print("Program shutting down")

    return wrapper


@my_decorator
def howdy():
    print("HOWDY")


def bye():
    print("GOODBYE")


howdy()
bye()

# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"⏱️ '{func.__name__}' took {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper

# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Finished processing...")

# slow_function()


# 🧩 *args = Positional Arguments (like a list)
def print_fruit(*args):
    for arg in args:
        print(arg)


food = ["apple", "grapes", "cheese"]

print_fruit(food)

# 🧩 **kwargs = Keyword Arguments (like a dictionary)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Joe", age=34, location="texas")


def use_both(*args, **kwargs):
    print("Positional: ", args)
    print("---------------")
    print("Key/Value: ", kwargs)


positional = ["apple", "banana", "pear"]
key_val = {"name": "Wills", "age": 76, "city": "Moons"}

use_both(*positional, **key_val)



def all_int(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"Argument {arg} is not an integer")
            
        for key,value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"Argument {key} has a non integer {value}")
        return func(*args, **kwargs)
    return wrapper


@all_int
def add_numbers(a,b):
    return a + b

print(add_numbers(5, 10))     # ✅ Works
# print(add_numbers(5, "ten"))   ❌ Raises ValueError

@all_int
def mult_numbs(a,b,c):
    return a * b * c
# print(mult_numbs(5,5,"h")) # ❌ Raises ValueError


print(add_numbers(5, 10))             # ✅ Works
print(add_numbers(5, "ten"))          # ❌ Raises ValueError
print(add_numbers(5, 10, c=15))       # ✅ Works
print(add_numbers(5, 10, c="fifteen")) # ❌ Raises ValueError