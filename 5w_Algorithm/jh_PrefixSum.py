#코드잇 알고리즘 p43

#import sys  #프롬프트를 자유롭게 변경할 수 있는 기능
#input = sys.stdin.readline    #여러 줄의 입력이 있을 때 한 줄을 읽고 다음 줄을 가리킴.
suNo, quizNo = map(int, input().split())    #sys써도 되고 안써도 되고
numbers = list(map(int, input().split()))
prefix_sum = [0] #비어있는 배열 선언
temp = 0    #초기 변수 선언

for i in numbers:
    temp += i
    prefix_sum.append(temp) #배열에 원소 추가하기

for i in range(quizNo):
    s, e = map(int, input().split())    #e = 최종인덱스, s = 최초인덱스
    print(prefix_sum[e] - prefix_sum[s-1])  #구간 합 출력
