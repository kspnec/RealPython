from itertools import product

for x,y in product([True, False], repeat=2):
    print(f"\t{x} or {y} = {x or y}")

def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

print(True or print_and_return(False))
print(True or print_and_return(True))
print(True or print_and_return(1/2))
print(True or print_and_return(1/0))

print(False or print_and_return(True))
print(False or print_and_return(False))
print(False or print_and_return(1/2))

# this returns Exception --> ZeroDivisionError
# print(False or print_and_return(1/0))


# or operator is used to set DEFAULT values.
first_name = ""
first_name = first_name or "Not Given"
print(first_name)

second_name = "Luigi"
second_name = second_name or "Not Given"
print(second_name)