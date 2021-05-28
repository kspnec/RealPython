a = ['spam', 'egg', 'lobster', 'egg', 'tomato', 'bacon']
# List indexing
print(a[0])
print(a[5])
print(a[len(a)-1])
print(a[-1])
print(a[-len(a)])


# List slicing -> extract a portion from your list
print(a[1:4]) # upto index 4 but not including 4th index.
print(a[:4]) # slicing starts from frist element.
print(a[1:]) # upto last element in the list.

# returns the copy of the entire list, but 
# not a reference to the same object.
print(a[:])
a == a[:] # --> True
a is a[:] # --> False

# NOTE: if you use string[:], it referes to the same object.
string = 'hello'
string == string[:] # --> True
string is string[:] # --> True
