def calculator(a, b, operation):
    if operation == '+':            #+ 연산
        calutation_value = a+b
    elif operation == '-':          #- 연산
        calutation_value = a-b
    elif operation == '/':          #/ 연산
        calutation_value = a/b
    elif operaion == '*':           #* 연산
        calutation_value = a*b
    return calutation_value         #연산결과 반환

operation = '-'   #operation이 뺄셈일 때
subtraction_value = calculator(20, 10, operation) #subtraction_value을 변수로 지정하여 계산

print(subtraction_value)
