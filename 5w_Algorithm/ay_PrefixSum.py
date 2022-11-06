n, q = map(int, input('수 배열의 개수와 합을 구하는 횟수를 입력하시오: ').split())
n_list = list(map(int, input('배열을 입력하시오: ').split()))
sum_list = []  # 각 원소의 누적합을 담을 리스트
n1_n2_sum = 0  # 합을 계산해줄 리스트

for j in n_list:  # 누적합을 담아주는 for문
    n1_n2_sum += j
    sum_list.append(n1_n2_sum)

for i in range(q):  # 구간합을 계산하는 for문
    start, end =map(int, input('첫 인덱스와 마지막 인덱스를 입력하시오: ').split())
    print(sum_list[end] - sum_list[start-1])
