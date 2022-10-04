import numpy as np

def zig_zag_matrix(n_by_n):
    emp_array = np.zeros((n_by_n, n_by_n))
    num = 1
    for i in range(n_by_n):  # 열
        if i % 2 == 1:  # 마지막부터 시작
            for j in range(n_by_n-1, -1, -1):  # 행
                num += 1
        else:  # 처음부터 시작
            for j in range(n_by_n):
                emp_array[j, i] = num
                num += 1

    array_fin = emp_array
    return array_fin

n_by_n = int(input('어느 사이즈의 정방행렬을 원하나요: '))

zig_zag_array = zig_zag_matrix(n_by_n)
print(zig_zag_array)
