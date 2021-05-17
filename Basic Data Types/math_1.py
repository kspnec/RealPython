# MATH Functions

# absolute value (Removes the sign)
x = abs(456.6)
print(x)

y = abs(-435.76)
print(y)

# modulo % , Gives only the remainder
a = 10 % 3
print(a)
# if you want both divided and remainder values.
b = divmod(10, 3)
print(b)

c = max([1, 2, 3, 4, 5, 6])
print(c)
d = max ([-4, -3, -2, -1])
print(d)

e = min([1, 2, 3, 4, 5, 6])
print(e)
f = min([-4, -3, -2, -1])
print(f)

g = pow(4, 2)
print(g)
# third value in pow is modulo %
h = pow(4, 2, 3)
print(h)

# Note the diff b/w round and int
i = round(6.75)
print(i)
j = round(6.45)
print(j)

k = int(6.75)
print(k)
l = int(6.45)
print(l)

# start value is 0 by default 
m = sum([1, 2, 3, 4, 5])
print(m)
# we can specify the start value at last.
# here the start value is 10.
n = sum([1, 2, 3, 4, 5], 10)
print(n)