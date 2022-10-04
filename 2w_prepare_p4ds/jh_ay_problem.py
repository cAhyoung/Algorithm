import numpy as np

def solution(numbers):
    answer = np.array(numbers)
    return answer

numbers = list(map(int, input('입력 : ').split()))
a = solution(numbers)
print(a*2)
