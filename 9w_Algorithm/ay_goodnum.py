import sys
input = sys.stdin.readline

tot_count = int(input())  # 수의 총 개수
num_list = list(map(int, input().split()))  # 수의 리스트

num_list.sort()  # 크기순으로 정렬

good_count = 0  # 좋은 수 세기 위한 변수

for k in range(tot_count):  # 수의 총 개수만큼 반복문을 돌림
    start_point = 0
    end_point = len(num_list) - 2

    find = num_list[k]
    num_list.remove(find)

    while start_point < end_point:  # 두 값을 더했을 때 find 값이 나오는지 확인
        if num_list[start_point] + num_list[end_point] > find:
            end_point -= 1
        elif num_list[start_point] + num_list[end_point] < find:
            start_point += 1
        else:
            good_count += 1
            break

    num_list.append(find)
    num_list.sort()
    k += 1


print(good_count)
