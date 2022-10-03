import numpy as np

def solution(num_list):
    num_array = np.array(num_list)
    reversed_array = np.flip(num_array)  # np.flip(array) : 순서를 뒤집어주는 함수
    answer = reversed_array
    return answer

num_list = list(map(int, input('공백을 두고 숫자를 입력하세요: ').split()))

answer = solution(num_list)

print(answer)
