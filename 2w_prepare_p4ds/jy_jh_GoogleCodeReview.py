n = int(input())
matrix = [[0]*n for i in range(n)]   #0이 n개인 리스트를 n개 만들어줌 eg)3x3
cnt = 0

for i in range(0, n):
    if i % 2:   #나머지가 0이 아닐때, 순방향으로
        for j in range(0, n):
            cnt += 1
            matrix[i][j] = cnt
    else:      #나머지가 0일때, 역방향으로
        for j in range(n-1, -1, -1):
            cnt += 1
            matrix[i][j] = cnt

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end=' ')  #j와i를 바꿔서 행과 열의 위치를 바꿈
    print()