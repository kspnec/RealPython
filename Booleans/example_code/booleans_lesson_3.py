# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

#%% Lesson 3
from itertools import product
for x, y in product([True, False], repeat=2):
    print(f"\t{x} and {y} = {x and y}")
    
def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

True and print_and_return(False)
True and print_and_return(True)

True and print_and_return(2/3)
#True and print_and_return(1/0)

False and print_and_return(True)
False and print_and_return(1/0)
