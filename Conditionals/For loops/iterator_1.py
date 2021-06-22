>>> a = ['foo', 'bar', 'baz']
>>> itr = iter(a)
>>> next(itr)
'foo'
>>> next(itr)
'bar'
>>> next(itr)
'baz'
>>> next(itr)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    next(itr)
StopIteration
>>>