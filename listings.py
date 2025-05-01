# list
fruit_basket = ["apple", "grapes", "bananas"]
# append adds to the list
fruit_basket.append("pears")
print(f"Added pears {fruit_basket}")

# removes the first occurence of grapes
fruit_basket.remove("grapes")
print(f"Removed grapes {fruit_basket}")

# insert oranges at index 1
fruit_basket.insert(1, "oranges")
print(f"Inserted Oranges at index 1 {fruit_basket}")

# removes the last item from a list and returns it.
lost_items = fruit_basket.pop()
print(f"Removed last item which was {lost_items} from {fruit_basket}")

# reading elements from lists
print("-----Complete list-----")
for fruits in fruit_basket:
    print(fruits)
print("-----------------")

# checking for one element in a list
if "bananas" in fruit_basket:
    print("We got bananas!")





print(len(fruit_basket))

# ['apple', 'oranges', 'bananas']
print(fruit_basket[1:])  # ['oranges', 'bananas'] -> starts at index 1 finishes list
print(fruit_basket[:2])  # ['apple', 'oranges'] -> starts at index 0 and goes up to
# but does not include index 2


# creating lists
empty_lists = []
numbs = [2, 4, 6, 8, 10, 12, 14, 16]

# access elements
# count starts at 0
print(numbs[1])  # = 4
print(numbs[-1])  # the last element = 16
print(numbs[-5])  # the last element = 8











# reversing a list
# numbs = [2, 4, 6, 8, 10, 12, 14, 16]
# reversed: [16, 14, 12, 10, 8, 6, 4, 2]
def reverse_numbs(N):
    left = 0
    right = len(N) - 1
    while left < right:
        N[left], N[right] = N[right], N[left]
        left += 1
        right -= 1
    return N


print(reverse_numbs(numbs))


# modifying lists
numbs[0] = 100
print(numbs)





# lists comprehensions
num_examp = [1, 2, 3, 4, 5]
squares = [x * x for x in range(1, 7)]
print(squares)
# double numbers between 1, up to but not including 12 so 1-11
doubles = [x * 2 for x in range(1, 12)]
print(doubles)

num_examp = [1, 2, 3, 4, 5]

triples = [x * 3 for x in num_examp]
print(triples)
# list comp
evens = [x for x in range(10) if x % 2 == 0]









# reversing strings
s = "hello"
reversed_s = s[::-1]
print(reversed_s)

w = "howdy"
rev_howdy = ""
for char in w:
    rev_howdy = char + rev_howdy
print(rev_howdy)

l = "lowers"
rev_l = "".join(reversed(l))
print(rev_l)









# recursive rev str
# space O(n) time O(n)
def rev_recur(s):
    if len(s) == 0:
        return s
    return rev_recur(s[1:]) + s[0]


# w o r l d   -> orld + w  -> rld + ow  -> ld + row  -> d + lrow -> dlrow
print(rev_recur("world"))


# stack string rev
# .pop is o(1)
# time O(n)  space O(n)
s = "pancakes"
pan_stack = list(s)  # = ['p', 'a', 'n', 'c', 'a', 'k', 'e', 's']
rev_pancakes = ""
while pan_stack:
    rev_pancakes += pan_stack.pop()
print(rev_pancakes)


# converting strings to lists
def rev_words(t):
    t = list(t)
    left = 0
    right = len(t) - 1

    while left < right:
        t[left], t[right] = t[right], t[left]

        left += 1
        right -= 1
    return t


print(rev_words("tacos"))

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = 7
def find_tar(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == target:
                return i, j
    return None

print(find_tar(nums, t)) #(2,0)
