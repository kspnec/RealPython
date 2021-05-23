# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

#%% Lesson 5
print(1 == 1)
print(True == 1)
print(1.0 == 1)
print(1 + 0j == 1)
print(4/2 == 2)
print('1' == 1)

print(2 == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3])
print({1, 2, 3} == {3, 1, 2})

print(0.25 + 0.25 == 0.5)

print(0.2 + 0.1 == 0.3)

x = 0.1

print(f"{x:.50f}")

print(1.0 < 3)

print([4, 0] >= [3, 2000000, 5000000])

print([4, 0] >= [4.1, 2000000, 5000000])

# returns TypeError
#print([1, 2, 3] < {4, 5, 6})

print(1.0 < 3)

a = {"x": 1, "y": 2}
b = {"x": 3, "y": 4}

# returns TypeError
# print(a < b)

print({1, 2, 3} < {4, 5, 6})
print({4, 5, 6} < {1, 2, 3})
print({4, 5, 6} == {1, 2, 3})
print({4, 5, 6} >= {1, 2, 3})
print({4, 5, 6} != {1, 2, 3})

x, y = [1, 2, 3], [1, 2, 3]

print(x == y)

id(x)
id(y)

print(x is y)

z = x

print(x == z)

id(z)
id(x)

print(x is z)
print(z is x)

print(1 in [1, 2, 3])

print("luigi" in {"luigi", "mario", "yoshi"})

print("luigi" in "luigi mario yoshi")

print("bowser" in "luigi mario yoshi")

d = {"a": 1, "b": 3}

print("c" in d)
print("b" in d)
print("b" not in d)
