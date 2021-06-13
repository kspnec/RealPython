# defining a dict:

bad_guys = {
    "daredevil": 'kingpin',
    'x-men': 'apocalypse',
    'batman': 'bane'
}
print(bad_guys)

# retrive a value from dict by using its key:
>>> bad_guys['batman']
'bane'
>>> bad_guys['daredevil']
'kingpin'

# if the key is not there.
>>> bad_guys['avengers']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    bad_guys['avengers']
KeyError: 'avengers'

# adding an entry to Dict.
>>> bad_guys['deadpool'] = 'evil deadpool'

# update an Dict entry.
>>> bad_guys['x-men'] = 'juggernaut'
>>> bad_guys
{'daredevil': 'kingpin', 'x-men': 'juggernaut', 'batman': 'bane', 'deadpool': 'evil deadpool'}

# delete a Dict entry.
>>> del bad_guys['x-men']
>>> bad_guys
{'daredevil': 'kingpin', 'batman': 'bane', 'deadpool': 'evil deadpool'}

# you can not use index in Dict.
>>> bad_guys[0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    bad_guys[0]
KeyError: 0

# if your dict has integers as key, i.e., 
d = {
    0: 'plane',
    1: "train"
}

# here, this [0] is key not an index.
>>> d[0]
'plane'

