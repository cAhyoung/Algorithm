n=int(input())
number= [[0]*n for i in range(n)]  #0이 n개인 리스트를 n개 만들어줌 eg)3x3
cnt=1

for x in range(n):
    if x % 2:   #나머지가 0이 아닐때, 순방향으로
        for y in range(n):
            number[y][x]=cnt  #행과 열이 바뀜 주의
            cnt+=1

    else:      #나머지가 0일때, 역방향으로
        for y in reversed(range(n)):
            number[y][x]=cnt
            cnt+=1



for y in range(n):
    for x in range(n):
        print(number[y][x],end=" ")
    print()