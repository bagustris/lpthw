# python for loop

import numpy as np

i = 0
n = []

while i<=10:
    print("iterasi ke-%d: %d") % (i, i*i)
    n = np.append(n, i*i)
    i = i+1

np.savetxt('while.csv', n, fmt='%10.1f')
