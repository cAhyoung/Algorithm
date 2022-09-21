'''
https://codeup.kr/problem.php?id=1083
'''

num = int(input('1~10 중 수를 적으세요: '))  # 1~10의 수 중 입력을 받음

for i in range(1, num+1):  # 1~num까지 반복문을 돌림
    if i%3 == 0:  # 3, 6, 9... 일 때 X를 출력하기 위한 조건문
        print('X', end='')
    else:  # 아닌 경우 숫자 출력
        print(i, end='')
