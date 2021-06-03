# membersip operator --> in 
a = ['spam', 'egg', 'lobster', 'egg', 'tomato', 'bacon']
print('spam' in a)
print('less' in a)
print('less' not in a)

# concatenation operator
print(a + ['sample', 'add', 'items'])
print(a)
# replication operator
print(a * 2)
print(3 * a)

# build-in functions for lists.
b = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(b))
print(min(b))
print(max(b))

c = ['apple', 'bacon', 'Asparagus', 'Zebra']
print(len(c)) 
print(min(c)) # caculates based on the ASCII values for corresponding characters.
print(max(c)) 
# Capital alphabets has lower ASCII values.

print(ord('a'))
print(ord('A'))
print(ord('b'))
print(ord('Z'))

# NOTE: if a list has mixed data-types then 
# comparision (min, max) functions will return TYPE ERROR.
# i.e., because you can't compare int & str. 