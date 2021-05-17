
""" 
exec()
eval()  -> evaluate a value of a python function. mostly used with calculator.
hash() 
"""

import os
job = input('Tell me a task to do: ')
exec(job)

import os
job = input('give me a math to do: ')
print(eval(job))
# with {} , no name functions will be used. 
print(eval(job, {}))
# to include certain named functions, include them in the dict.
print(eval(job, {'power': pow}))

with open('text.txt', 'r') as file_obj:
    mobi_list = file_obj.readlines()
#print(mobi_list)

# turn mobi_list into a single string using join().
mobi_1 = ''.join(mobi_list)
mobi_2 = ''.join(mobi_list)

print(hash(mobi_1) == hash(mobi_2))

# append a space at the end of mobi_2.
mobi_2 += ' '

# check the length of both files.
print(len(mobi_1))
print(len(mobi_2))

print(hash(mobi_1) == hash(mobi_2))