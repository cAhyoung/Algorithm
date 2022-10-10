def factorial(N):
    if N <=1 :  # N이 1보다 작거나 같아지는 경우 1을 반환하여 팩토리얼 계산을 마무리함
        return 1
    else:
        return factorial(N-1)*N  # 아닌 경우 계속해서 팩토리얼 계산

N = int(input('계산할 팩토리얼을 입력하세요: '))
print(factorial(N))
