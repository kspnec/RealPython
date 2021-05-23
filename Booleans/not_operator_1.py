print(not True)
print(not False)

print(not 1)
print(not 0)

# is object "a" an empty string ? no --> False.
a = 'hello'
print(not a)

# is object "b" an empty string ? Yes --> True.
b = ''
print(not b)

# is object "c" an empty List ? no --> False.
c = [1, 2, 3]
print(not c)

# is object "d" an empty List ? Yes --> True.
d = []
print(not d)

# 1. excersice:
first_name = ''
if not first_name:
    print("Not Given")

second_name = 'san'
if not second_name:
    print("Not Given")
else:
    print(second_name)

# above example by using TERNARY Operator:
third_name = ""
third_name = "Not Given" if not third_name else third_name
print(third_name)

fourth_name = "map"
fourth_name = "Not Given" if not fourth_name else fourth_name
print(fourth_name)