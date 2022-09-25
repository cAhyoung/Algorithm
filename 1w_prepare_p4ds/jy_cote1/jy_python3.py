dir_1st = ['main.h', 'operate.c', 'define.h', 'run.py', 'build.py', 'run.c']

for i in dir_1st:
    if '.py' in i or '.c' in i:
        print(i)
    else:
        continue  #다시 if로 돌아가/ break쓰면 바로 끝내버리기