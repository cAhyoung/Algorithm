n = int(input('휴지통 양: '))

if n >= 10:  # 10의 자리 수 인 경우
    a = n // 10  # 10의 자리수와 1의 자리수 분리
    b = n % 10
    new_num = (b*10 + a) * 2
    if new_num >= 100:  # 압축된 수가 100이 넘은 경우
        new_num = new_num - ((new_num // 100) * 100)  # 100의 자리 수를 무시하도록 설정

if new_num <= 50:
    print(new_num, 'Good')
else:
    print(new_num, 'Oh my god')
