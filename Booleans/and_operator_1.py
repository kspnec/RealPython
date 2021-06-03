# example: 1
from itertools import product

for x,y in product([True, False], repeat=2):
    print(f"\t{x} and {y} = {x and y}")

# example: 2
def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

print(True and print_and_return(True))
print(True and print_and_return(False))

# short-circuit happens and the second value doesn't evaluated, saved computation.
print(False and print_and_return(True))
print(False and print_and_return(False))

print(True and print_and_return(1/2))
print(False and print_and_return(1/2))

print(True and print_and_return(1/0))
print(False and print_and_return(1/0))