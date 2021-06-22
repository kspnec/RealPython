# empty dict
my_profile = {}

my_profile['fname'] = 'praveenkumar'
my_profile['lname'] = 'kumaravel'
my_profile['city'] = 'salem'

# past_jobs is a list
my_profile['past_jobs'] = ['systems engg', 'cloud support engg', 'service reliability engg']

# Transportation is a dict again.
my_profile['transportation'] = {'skateboard': 'quest', 'bike': 'trek', 'flight': 'vacation'}

print(my_profile)
current_job = my_profile['past_jobs'][2]
print(current_job)

bike_used_for = my_profile['transportation']['bike']
print(bike_used_for)