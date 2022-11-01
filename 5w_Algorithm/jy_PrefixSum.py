N, M = map(int, input().split())   # N, M 입력 받기
numbers = list(map(int, input().split()))  # 숫자 리스트로 입력 받기

i_j_list = []  # 입력받은 i와 j 리스트로 정리
for m in range(M):
    i_j = list(map(int, input().split()))
    i_j_list.append(i_j)

prefix_sum = [0]  # prefix_sum 리스트 만들기
numbers_sum = 0
for number in numbers:
    numbers_sum += number
    prefix_sum.append(numbers_sum)

for i_j in i_j_list:  # prefix_sum 을 사용해서 주어진 구간의 합 구하기
    i, j = i_j[0], i_j[1]
    print(prefix_sum[j] - prefix_sum[i-1])  # 구간 합 출력