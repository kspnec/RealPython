players = ['joe', 'john', 'randy', 'paul', 'san']

count = 0
for player in players:
    print(count, player)
    count += 1 

# make use of enumarators here.
names = ['joe', 'Bob', 'Mark', 'Ben']

for count, name in enumerate(names):
    print(count, name)