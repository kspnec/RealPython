>>> x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
>>> x
['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
>>> x[0]
'a'
>>> print(x[0], x[2], x[4])
a g j
>>> x[1]
['bb', ['ccc', 'ddd'], 'ee', 'ff']
>>> x[1][0]
'bb'
>>> x[1][1]
['ccc', 'ddd']
>>> x[1][2]
'ee'
>>> x[1][1][1]
'ddd'
>>> x[3][0]
'hh'
>>> x[-2][-1]
'ii'
>>> x[-4][-3][-2]
'ccc'

>>> x
['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
>>> len(x)
5
>>> 'ddd' in x
False
>>> 'ddd' in x[1]
False
>>> 'ddd' in x[1][1]
True