# python for loop

import numpy as np

i = 0
n = []

for i in range(0, 10):
    print("iterasi ke-%d: %d") % (i, i*i)
    n = np.append(n, i*i)
    i = i+1

np.savetxt('loop.csv', n, fmt='%10.1f')
