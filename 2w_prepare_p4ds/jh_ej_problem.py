import numpy as np


a = np.random.seed(32)
a = np.random.random((3,3,3))
print(a)

b = np.random.random((10,10))
print("최솟값:",np.min(b),"최댓값:",np.max(b))

c = np.random.rand(30)
print('평균:',np.mean(c))
