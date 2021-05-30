# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

#%% Lesson 4
from itertools import product
for x, y in product([True, False], repeat=2):
    print(f"\t{x} or {y} = {x or y}")
    
    
def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

True or print_and_return(False)
True or print_and_return(1/0)

False or print_and_return(5)
#False or print_and_return(1/0)

first_name = ""
not first_name

first_name = ""
first_name = first_name or "Not given"
print(first_name)

first_name = "Luigi"
first_name = first_name or "Not given"
print(first_name)

