#데이터의 개수, 질의 개수
n, m = map(int, input().split( )) #split 띄어쓰기로 기준을 잡아줌

#구간합을 구할 배열
sumlist = list(map(int, input().split( )))

perfix_sum = [0]
temp = 0

for i in sumlist: #합을 
    temp += i
    perfix_sum.append(temp)

for j in range(m):
    s, e = map(int, input().split( ))
    print(perfix_sum[e] - perfix_sum[s - 1])
