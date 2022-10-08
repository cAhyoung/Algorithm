n = int(input('총 설탕 kg 수: '))

cnt_5 = 0  # 5키로 봉투가 몇개 필요한지 카운트할 변수
cnt_3 = 0  # 3키로 봉투가 몇개 필요한지 카운트할 변수

while True:  # 무한루프로 반복문 돌리기
    if n >= 5:  # n이 5보다 클 때 = 5키로 봉투를 계속해서 카운트 할 수 있도록 함
        n -= 5
        cnt_5 += 1
    elif n < 5:  # n이 5보다 작아지면 3키로 봉투로 카운트
        if n >= 3:
            n -= 3
            cnt_3 += 1
        elif n == 0:  # 3과 5로 계산 했을 때 완전히 나눠떨어질 때 총 봉투 수를 출력
            print('5kg %d, 3kg %d' %(cnt_5, cnt_3))
            break
        else:  # 완전히 나눠떨어지는 경우가 아니라면 -1 출력
            print(-1)
            break
