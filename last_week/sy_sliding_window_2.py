from sys import stdin
from collections import deque
stdin = open("input.txt", "r")
# N: 숫자의 개수
# L: 임의의 수 
N, L = map(int, stdin.readline().split())

numbers = list(map(int, stdin.readline().split()))

queue = deque()

for i in range(N):
    # i-L+1 인덱스 이전인 것들을 pop해준다.
    while queue and queue[0][0] <= i-L:
        queue.popleft()

    # 들어갈 숫자보다 큰 것들은 전부 pop해준다.
    while queue and queue[-1][1] >= numbers[i]:
        queue.pop()

    queue.append((i, numbers[i]))
    print(queue[0][1], end=' ')
