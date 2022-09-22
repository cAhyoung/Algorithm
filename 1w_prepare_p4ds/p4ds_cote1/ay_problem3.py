dir_lst = ['main.h', 'operater.c', 'define.h', 'run.py', 'build.py', 'run.c']

for i in dir_lst:  # dir_lst 안에 있는 요소들을 하나씩 불러옴
    if '.c' in i or '.py' in i:  # 차례대로 불러온 요소들 안에 '.c'나 '.py'라는 문자가 있다면 출력
        print(i)
    else:
        continue
