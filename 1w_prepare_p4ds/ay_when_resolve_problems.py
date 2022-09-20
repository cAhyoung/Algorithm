'''
문제를 풀기 위해 들어오는 세 사람의 방문 주기를 입력받았을 때, 세 사람이 첫날 제외 같은 날에 들어온다면 몇일 뒤 인가?
https://codeup.kr/problem.php?id=6091
'''

day_1, day_2, day_3 = map(int, input('방문 주기: ').split())  # map 함수를 이용해 정수형으로 입력을 받은 후 공백을 기준으로 분리

day = 1  # 카운팅할 변수

while day % day_1 != 0 or day % day_2 != 0 or day % day_3 != 0:  # 세 조건 중 하나라도 만족한다면 반복문 실행
    day += 1  # 
    if day % day_1 == 0 | day % day_2 == 0 | day % day_3 == 0:  # day를 방문주기들로 나눴을 때 모두 0이라면 day 출력
        print(day)
    else:  # 아닌 경우 다시 반복문 실행
        continue
