>>> t = ('spam', 'egg', 'bacon', 'tomato')
>>> t
('spam', 'egg', 'bacon', 'tomato')
>>> t[0]
'spam'
>>> t[1]
'egg'

>>> (s1, s2, s3, s4) = t
>>> s1
'spam'
>>> s2
'egg'
>>> s3
'bacon'
>>> s4
'tomato'

>>> (s1, s2, s3) = t
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    (s1, s2, s3) = t
ValueError: too many values to unpack (expected 3)

>>> t
('spam', 'egg', 'bacon', 'tomato')
>>> (s1, s2, s3, s4, s5) = t
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    (s1, s2, s3, s4, s5) = t
ValueError: not enough values to unpack (expected 5, got 4)

>>> (s1, s2, s3, s4) = ('spam', 'egg', 'bacon', 'tomato')
>>> s1
'spam'
>>> s2
'egg'
>>> s3
'bacon'
>>> s4
'tomato'

>>> (s1, s2, s3) = ('spam', 'egg', 'bacon', 'tomato')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    (s1, s2, s3) = t
ValueError: too many values to unpack (expected 3)

>>> t = 1, 2, 3
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>

>>> x1, x2, x3 = t
>>> x1, x2, x3
(1, 2, 3)
>>> x1, x2, x3 = 4, 5, 6
>>> x1, x2, x3
(4, 5, 6)

>>> t = 2,
>>> t
(2,)
>>> type(t)
<class 'tuple'>

>>> a = 'spam'
>>> b = 'egg'
>>> a, b
('spam', 'egg')
>>> # You need to define a temp variable to accomplish the swap.
>>> temp = a
>>> a = b
>>> b = temp
>>> a, b
('egg', 'spam')

>>> a = 'spam'
>>> b = 'egg'
>>> a, b
('spam', 'egg')
>>> # Ready for Magic Time!
>>> a, b = b, a
>>> a, b
('egg', 'spam')

>>> # Fibonacci series
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 30:
...    print(a)
...    a, b = b, a+b
...
0
1
1
2
3
5
8
13
21