# by default print output at the end defaults to the '\n' new line.
for i in range(100):
    print(i, end=' ')
print()

file = open('sample.txt', 'w')
file.write('Hello World!')
file.close()

file = open('sample.txt', 'r')
# readlines will read all lines in a file as LIST.
print(file.readlines())
file.close()

