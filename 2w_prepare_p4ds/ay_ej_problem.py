import numpy as np

# 1 랜덤 시드값을 32로 초기화:
np.random.seed(32)

# 2 3X3X3 배열을 만들어 출력
array_333 = np.random.random((3, 3, 3))
print(array_333)

# 3 10X10 배열을 만들고 최대, 최솟값을 한줄에 출력
array_1010 = np.random.random((10, 10))
print(np.min(array_1010), np.max(array_1010))

# 4 random 함수를 이용해 30개의 원소를 만들고 평균값을 출력
list_1 = np.random.random(30)
array = np.array(list_1)
print(np.mean(array))
