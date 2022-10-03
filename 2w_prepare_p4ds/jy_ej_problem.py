import numpy as np
#1
a = np.random.seed(32)

#2
b = np.random.random((3,3,3))
print(b)

#3
c = np.random.random((10,10))
cmin, cmax = c.min(), c.max()
print(cmin, cmax)

#4
d = np.random.random(30)
ar = np.array(d)
print(np.mean(ar))

