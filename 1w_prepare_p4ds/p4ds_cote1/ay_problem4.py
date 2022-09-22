'''
def calculator(operation):  # operation을 입력받아 이를 토대로 if문을 돌림

    if operation == '+':            # +인 경우 두 값을 더하는 연산 실시
        calutation_value = 20+10
    elif operation == '-':          # -인 경우 두 값을 빼는 연산 실시
        calutation_value = 20-10
    elif operation == '*':          # *인 경우 두 값을 곱하는 연산 실시
        calutation_value = 20*10
    elif operation == '/':          # /인 경우 두 값을 나누는 연산 실시
        calutation_value = 20/10
    else:                           # 이 모든 것이 아닌 경우 error메세지 출력
        print('error')

    return calutation_value

operation = '-'                     # -연산자를 문자열로 받음
subtraction_value = calculator(operation)
# calculator에 operation을 넣어 연산 실시 후 값을 해당 변수에 넣어줌

print(subtraction_value)
'''

def calculator(num1, num2, operation):  # operation을 입력받아 이를 토대로 if문을 돌림

    if operation == '+':            # +인 경우 두 값을 더하는 연산 실시
        calutation_value = num1 + num2
    elif operation == '-':          # -인 경우 두 값을 빼는 연산 실시
      if num1 >= num2
        calutation_value = num1 - num2
      else:
        calutation_value = num2 - num1
    elif operation == '*':          # *인 경우 두 값을 곱하는 연산 실시
        calutation_value = num1 * num2
    elif operation == '/':          # /인 경우 두 값을 나누는 연산 실시
        calutation_value = num1 / num2
    else:                           # 이 모든 것이 아닌 경우 error메세지 출력
        print('error')

    return calutation_value

num1, num2 = map(int, input('정수 두개를 공백으로 분리해 입력하세요: ').split())  # 계산할 두 정수를 입력받음

operation = input('+, -, *, / 중 하나를 입력하세요: ')                    # 연산자를 문자열로 받음

subtraction_value = calculator(operation)
# calculator에 operation을 넣어 연산 실시 후 값을 해당 변수에 넣어줌

print(subtraction_value)
