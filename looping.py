print("For loop")
for i in range(5):
    print(i)  # 0 to 4

print("While loop")
x = 0
while x <= 10:
    print(x)
    x += 1

print("Only odds")
# print odds only
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("Only evens")
# print evens
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

print("breaks loop at 6")
# breaks at 6, ends the loop once  i == 6
for i in range(10):
    if i == 6:
        break
    print(i)

print("Placeholder for 13")
for i in range(15):
    # unlucky numb
    if i == 13:
        pass
    print(i)

try:
    print(20 / 0)
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("Complete")
