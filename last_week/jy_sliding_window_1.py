from collections import deque

s, p = map(int, input().split())  # s = dna 문자열의 길이, p = 부분 문자열의 길이
string = list(str(input()))  # dna 문자열
A, C, G, T = map(int, input().split())  # 부분 문자열에 포함돼야할 A, C, G, T의 최소 개수

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
left, right = 0, p-1
arr = deque(string[left:right])
for i in arr:
    dic[i] += 1  # 딕셔너리를 사용해서 문자 갯수 세기
cnt = 0

while right < s:

    # 구간 완성
    dic[string[right]] += 1  # 가장 오른쪽 원소 추가

    # 계산
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1

    # 구간이동
    dic[string[left]] -= 1  # 가장 왼쪽 원소 제거
    left += 1
    right += 1

print(cnt)