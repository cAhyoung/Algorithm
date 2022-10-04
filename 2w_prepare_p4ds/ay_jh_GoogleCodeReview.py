n = int(input())  # nxn 정방행렬 수 받기
matrix = [[0]*n for i in range(n)]  # 수를 입력하기 위해 영행렬 만들어줌
cnt = 0  # 카운트용 수

for i in range(0, n):
    if i % 2:  # 뭘까...?
        for j in range(0, n):  # 나머지가 0일 때 -> 첫번째부터 시작
            cnt += 1
            matrix[i][j] = cnt
    else:  # 나머지가 1일 때 -> 마지막부터 시작
        for j in range(n-1, -1, -1):
            cnt += 1
            matrix[i][j] = cnt


print(matrix)
