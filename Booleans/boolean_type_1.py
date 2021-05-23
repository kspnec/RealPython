# boolean is subclass of integers.
print(issubclass(bool, int))

import keyword
print(keyword.kwlist)

# is True an instance of bool ?
y = isinstance(True, bool)
print(y)
# is False an instance of bool ?
print(isinstance(False, bool))

# True evaluates to 1, but it is not an instance of bool.
print(isinstance(1, bool))
# False evaluates to 0, but it is not an instance of bool.
print(isinstance(0, bool))

codes = [264, 118, 534, 705, 1152, 674]
N = 3
m = [c % N ==0 for c in codes]
print(m)
# test.