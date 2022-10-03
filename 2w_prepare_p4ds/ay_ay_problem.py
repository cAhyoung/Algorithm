import numpy as np

def solution(numbers):
    array = np.array(numbers)
    array = array * 2
    answer = array
    return answer

numbers = list(map(int, input("숫자를 입력하세요: ").split()))

solution_return = solution(numbers)
print(solution_return)

# 단점: 벡터만 처리가능
