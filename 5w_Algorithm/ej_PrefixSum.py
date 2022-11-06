data_num, run_num = map(int,input().split()) #데이터 개수와 질의 개수 띄어쓰기로 받기
numbers = list(map(int, input().split())) # 구간 합을 구할 대상 배열
 
hap_list = [0] #합 리스트 정의
num = 0

for i in numbers: #합 배열 리스트에 값 넣어주기
    num = num + i
    hap_list.append(num)

for i in range(run_num): #질의 개수만큼 반복
    first, second = map(int, input().split()) #구간 범위 받기
    print(hap_list[second] - hap_list[first-1]) #합 출력하기
