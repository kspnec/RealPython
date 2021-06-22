Towns = ['Morur', 'Kadathur', 'Rasipuram']
Districs = ['Salem', 'Dharmapuri', 'Namakkal']

# create list with Tuples having town and districs pair.
merged = []
for i in range(len(Towns)):
    merged.append((Districs[i], Towns[i]))
print(merged)

# Use of zip().
merged_2 = list(zip(Districs, Towns))
print(merged_2)


