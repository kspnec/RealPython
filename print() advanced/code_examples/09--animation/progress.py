#!/usr/bin/env python
from time import sleep

def progress(percent=0, width=30):
    # the number of hashes to show is based on the percent passed in, the
    # number of blanks is whatever space is left after
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)


print('This will take a moment')
for i in range(101):
    progress(i)
    sleep(0.1)

# newline so command prompt isn't on the same line
print()
