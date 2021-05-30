# Real Python
# Python Booleans
# Video Course by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

#%% Lesson 1
issubclass(bool, int)
isinstance(True, bool)
isinstance(False, bool)
isinstance(1, bool)
isinstance(0, bool)

import keyword
print(keyword.kwlist)

int(True)
int(False)

True + True + False + True

codes = [264, 118, 543, 705, 1152, 674]
N = 3

[c % N == 0 for c in codes]

sum([c % N == 0 for c in codes])



