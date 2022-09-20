a, b= map(int,input().split()) #공백을 기준으로 분리, 입력값을 정수형태로 변환

for i in range(1, a+1): #i값이 1부터 순서대로 바뀌는 동안에
    for j in range(1, b+1): #j값이 바뀌며 오름차순으로 정렬됨
        print(i, j)