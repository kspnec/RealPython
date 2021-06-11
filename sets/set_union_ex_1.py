
>>> x1 = {'foo', 'baz', 'bar'}
>>> x1
{'bar', 'foo', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}
>>> x2
{'qux', 'quux', 'baz'}

# set union using operator |
>>> x1 | x2
{'bar', 'qux', 'quux', 'foo', 'baz'}

# set union using 'union()' method
>>> x1.union(x2)
{'bar', 'qux', 'quux', 'foo', 'baz'}

>>> x1.union(('qux', 'quux', 'baz'))
{'bar', 'foo', 'qux', 'baz', 'quux'}


>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5 ,6}
>>> d = {4, 5, 6, 7}

>>> a.union(b, c, d)
{1, 2, 3, 4, 5, 6, 7}

>>> a | b | c | d
{1, 2, 3, 4, 5, 6, 7}
