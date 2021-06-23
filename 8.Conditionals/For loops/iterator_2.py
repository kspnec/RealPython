# iterators with dict.
>>> a = {'foo': 1, 'bar': 2, 'baz': 3}
# here, iterator will have the key values from the dict.
>>> for k in a:
...     print(k)
...
...
foo
bar
baz
# iterator will have only dict values.
>>> for k in a.values():
...     print(k)
...
...
# returns values of the dict.
1
2
3
# here, iterator will have both key/values from the dict.
>>> for k in a.items():
...     print(k)
...
...
# returns dict key/values as tuples.
('foo', 1)
('bar', 2)
('baz', 3)
>>>
>>> for k in a.items():
...
...     print(k)
...
...
('foo', 1)
('bar', 2)
('baz', 3)
>>>
>>> for k, v in a.items():
...     print(f"k={k} v={v}")
...
...
k=foo v=1
k=bar v=2
k=baz v=3
>>> for k, v in a.items():
...     print(f"k={k}\tv={v}")
...
...
k=foo	v=1
k=bar	v=2
k=baz	v=3
>>>
>>>
>>> for k, v in a.items():
...     print(f"k={k}, v={v}")
...
...
k=foo, v=1
k=bar, v=2
k=baz, v=3
>>>