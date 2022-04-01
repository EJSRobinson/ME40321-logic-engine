
import solvers.mT as test
import numpy as np


def f(var1, var2):
    return (var1**2 - var2**2)/(var1 + var2)


max1 = 10
min1 = 1

max2 = 45
min1 = -5

var1 = np.arange(min1, max1, 0.01)
var2 = np.arange(min1, max1, 0.01)

results = np.zeros((len(var1), len(var2)))

for i in range(len(var1)):
    for j in range(len(var2)):
        results[i][j] = f(var1[i], var2[j])

ind = np.unravel_index(np.argmax(results), results.shape)
print(results[ind[0]][ind[1]])
