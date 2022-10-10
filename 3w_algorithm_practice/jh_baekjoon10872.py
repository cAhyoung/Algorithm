def factorial(n):
    if n == 0:  # n이 0일 때
        return 1
    return n * factorial(n -1)  #n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

print(factorial(0))

#1
a = int(input())
result = 1
for item in range(1, a+1, 1):
    result *= item
    #a= 4이고 result=1일 때, item = 1이 곱해짐 -> 1
    # result = 1일 때, item = 2가 곱해짐 -> 2
    # result = 2일 때, item = 3가 곱해짐 -> 6
    # result = 6일 때, item = 4가 실행되지 않음
    # 6이 반환됨.

print(result)

#2
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    # n이 4일 때, 4 > 1, 4 * factorial(3)
    # 3> 1, factorial(4) = 3 * factorial(2)

    else:
        return 1

b = int(input())
print(factorial(b))
