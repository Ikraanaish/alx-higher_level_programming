#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print(f'{i:01}, {j:01}', end=', ')
print('')
