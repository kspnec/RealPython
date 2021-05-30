a = iter([1, 2, 3, 4, 5, 6])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# at 7th time you will get 'StopIteration' Error.
print(next(a))      