from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
q = deque()
ans = []
for i in range(n):
    while q and q[-1][0] > arr[i]: 
        q.pop() #삽입하기 전에 덱을 뒤에서부터 보며 삽입하려는 요소보다 큰 값 전부 빼주기
    while q and q[0][1] < i - k + 1:
        q.popleft() #슬라이딩 범위를 벗어난 요소들 제거
    q.append((arr[i],i))
    print(q[0][0], end = ' ')
