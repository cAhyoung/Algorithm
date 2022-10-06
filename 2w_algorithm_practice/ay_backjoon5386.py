test_case = int(input('test case: '))  # 테스트케이스 입력

for i in range(test_case):  # 테스트케이스만큼 반복문 실행
    s, k = map(int, input('s, k: ').split())  # 금화의 갯수와 제곱수 제시
    cnt = 0  # 누가 승리했는지 계산하기 위한 카운트 변수
    while True:  # 반복문 계속해서 진행
        cnt += 1
        s -= k
        k *= k
        if s <= 0:  # 금화의 갯수가 0보다 작거나 같으면 while문에서 탈출
            break

    if cnt % 2 == 0:  # 누가 승리했는지 알아보기 위한 조건문
        print('해적2 승리')
    else:
        print('해적1 승리')
