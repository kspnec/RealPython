# Lists are MUTABLE -> means they can be changed.
# Defined using square [] brackets.
a = [1, 2, 3, 4, 5, 6]

print(a[0])
print(a[-1])
print(a[1])

# Last one after : will not be considered.
print(a[1:3])

# # Lists are MUTABLE -> means they can be changed, list elements values can be reassigned.
a[0] = 10
print(a)