# example: 1
# while & else behavior with break.
m = 5
while m > 0:
    m = m-1
    if m == 2:
        break # if while uses break, then else will not be executed.
    print(m)
else:
    print("Loop is exhausted completely.")


# example: 2
# while & else behavior with continue.
n = 5
while n > 0:
    n = n-1
    if n == 2:
        continue # exhausts the loop completely.
    print(n)
else:
    print("Loop is exhausted completely.")