import sys
input = sys.stdin.readline

n = int(input())  # 수의 개수
s = set()  # 두 수를 더해서 나오는 중복을 없애기 위한 함수
a = list(map(int,input().split(' ')))  # 수 데이터 저장 배열 (*map 안에 int or else 해줘야함)

# a + b + c = d 를 만족하는 d가 몇개인지 구하는 문제임
# a + b = d - c 로 변형시켜서 시각 복잡도를 줄여 풀 것임

result = 0
s.add(a[0] + a[0])

for i in range(1, n):
    for j in range(i):
        if a[i] - a[j] in s:  # d - c 값이 존재하는지 판별
            result += 1
            break

    for j in range(i+1):
        s.add(a[i] + a[j])

print(result)