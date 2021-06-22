# simple While loop
n = 5
while n >0:
    n = n-1
    print(n)


# while loops using a List
my_list = ['fizz', 'baz', 'buzz']
while my_list:
    print(my_list.pop(-1))


# BREAK
m = 5
while m > 0:
    m = m-1
    if m == 2:
        break
    print(m)
print("Loop ended.")


# CONTINUE
p = 5
while p:
    p = p-1
    if p == 2:
        continue
    print(p)
print("Loop ended.")