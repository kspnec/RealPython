# empty dict
# a = {} 
a = dict()

# store some key value pairs
a['name'] = 'praveen'
a['age'] = 27

print(a)

print(a['name'])
# This will introiduce a KeyError
# print(a['country'])

# safer method: using get method to avoid KeyError
print(a.get('name'))
print(a.get('country'))