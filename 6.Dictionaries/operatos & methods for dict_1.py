# membership operators in dict

# example dict
my_profile = {}
my_profile['fname'] = 'praveenkumar'
my_profile['lname'] = 'kumaravel'
my_profile['city'] = 'salem'
# past_jobs is a list
my_profile['past_jobs'] = ['systems engg', 'cloud support engg', 'service reliability engg']
# Transportation is a dict again.
my_profile['transportation'] = {'skateboard': 'quest', 'bike': 'trek', 'flight': 'vacation'}

print('age' in my_profile) # False
print('age' not in my_profile) # True

# CHECKING THE EXISTANCE OF KEYS IN DICT
# my_profile['age'] # this raises exception "KeyError", to avoid this,
print('age' in my_profile and my_profile['age'])

print(my_profile.get('age'))
print(my_profile.get('fname'))

# this is also useful for iterating items.

>>> for i in list(my_profile.items()):
...     print(i)
...
...
('fname', 'praveen')
('lname', 'kumar')
('city', 'salem')
('past_jobs', ['systems engg', 'cloud support engg', 'service reliability engg'])
('transportation', {'skateboard': 'quest', 'bike': 'trek', 'flight': 'vacation'})

# to get only the values:
>>> for i in list(my_profile.items()):
...     print(i[1])
...
...
praveen
kumar
salem
['systems engg', 'cloud support engg', 'service reliability engg']
{'skateboard': 'quest', 'bike': 'trek', 'flight': 'vacation'}

