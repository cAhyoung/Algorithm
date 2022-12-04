#p69
#0이 4개인 리스트를 생성.
#조건에 해당하는 원소들의 합 리스트
checkList = [0]*4

#원래 베열에 있는 원소들의 합 리스트
myList = [0]*4

#유효한 비밀번호인지 판단
checkSecret = 0

#함수 정의
def myadd(c):
#c는 새로 들어온 변수
    global checkSecret
    if c == 'A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret += 1

    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1

    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1

    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

#제거되는 문자를 처리하는 함수

def myremove(c):
    global checkSecret
    if c == 'A':
        myList[0] -= 1
        if myList[0] == checkList[0]:
            checkSecret -= 1

    elif c == 'C':
        myList[1] -= 1
        if myList[1] == checkList[1]:
            checkSecret -= 1

    if c == 'G':
        myList[2] -= 1
        if myList[2] == checkList[2]:
            checkSecret -= 1

    if c == 'T':
        myList[3] -= 1
        if myList[3] == checkList[3]:
            checkSecret -= 1

S, P = map(int, input().split())
# S : 문자열 크기
# P : 부분 문자열 크기
result = 0
A = list(input())
checkList = list(map(int, input().split()))

#반복문을 돌릴 때 checkList의 자릿수를 맞추어야 하기 때문이다.
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result += 19


print(result)
