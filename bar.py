age = int(input("Enter age: "))

if age >= 21:
    print("Come on in and drink!")
elif age >= 18:
    print("Enter but no drinks")
else:
    print("NO ENTRANCE")
print("-------------------------------------------")
age = int(input("Enter age: "))

match age:
    case age if age >= 21:
        print("Enter and drink")
    case age if age >= 18:
        print("Come on in, but no drinks")
    case _:
        print("NO ENTRANCE")
