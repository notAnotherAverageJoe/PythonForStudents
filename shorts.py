def all_int(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg,int):
                raise ValueError(f"Argument {arg} is not an integer")
        for key,value in kwargs.items():
            if not isinstance(value,int):
                raise ValueError(f"Argument {key} has a non integer {value}")
        return func(*args,**kwargs)
    return wrapper
@all_int
def add_numbers(a,b):
    return a + b
print(add_numbers(5,5))
print(add_numbers(5,8))

@all_int
def mult_numbs(a,b,c):
    return a * b * c
print(mult_numbs(5,10,c = 10))
print(mult_numbs(5,10,c = "five"))