>>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

>>> a[2]
'bacon'
>>> a[2] = 10
>>> a
['spam', 'egg', 10, 'tomato', 'ham', 'lobster']
>>> a[-1] = 20
>>> a
['spam', 'egg', 10, 'tomato', 'ham', 20]

>>> s = 'mybacon'
>>> s[2]
'b'
>>> s[2] = 'f'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    s[2] = 'f'
TypeError: 'str' object does not support item assignment

>>> a
['spam', 'egg', 10, 'tomato', 'ham', 20]
>>> del a[3]
>>> a
['spam', 'egg', 10, 'ham', 20]
>>> len(a)
5
>>> a[2:5] = [1.1, 2.2, 3.3]
>>> a
['spam', 'egg', 1.1, 2.2, 3.3]
>>> a[1:4]
>>> a[1:4] = ['Hello']
>>> a
['spam', 'Hello', 3.3]
>>> a[1:2] = ['a', 'b', 'c', 'd']
>>> a
['spam', 'a', 'b', 'c', 'd', 3.3]
>>> len(a)
6
>>> a[1]
'a'
>>> a[1] = [22, 33, 44]
>>> a
['spam', [22, 33, 44], 'b', 'c', 'd', 3.3]
>>> del a[1]
>>> a
['spam', 'b', 'c', 'd', 3.3]
>>> a[1:1] = [22, 33, 44]
>>> a
['spam', 22, 33, 44, 'b', 'c', 'd', 3.3]
>>> a[1:5]
[22, 33, 44, 'b']
>>> a[1:4] = []
>>> a
['spam', 'b', 'c', 'd', 3.3]

>>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a += ['gravy', 'kiwi']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster', 'gravy', 'kiwi']
>>> a = [10, 20] + a
>>> a
[10, 20 'spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster', 'gravy', 'kiwi']

>>> a += 30
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a += 30
TypeError: 'int' object is not iterable

>>> a += [30]
>>> a
[10, 20 'spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster', 'gravy', 'kiwi', 30]
>>> type([30])
<class 'list'>
>>> type(30)
<class 'int'>

>>> a = ['spam', 'egg', 'bacon']
>>> a
['spam', 'egg', 'bacon']
>>> a += 'tomato'
>>> a
['spam', 'egg', 'bacon', 't', 'o', 'm', 'a',' t', 'o']
>>> a[3:] = []
>>> a
['spam', 'egg', 'bacon']
>>> a += ['tomato']
>>> a
['spam', 'egg', 'bacon', 'tomato']