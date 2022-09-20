def solution(n):
    answer = 0
    for a in range(1, n):
        if n%a == 1: #나머지가 1인 것 
            answer = a #answer에 넣고
            break #가장 처음 넣은걸 그대로 출력하면 되니까 바로 break
    return answer
