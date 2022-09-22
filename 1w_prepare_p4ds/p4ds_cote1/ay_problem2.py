cities = {
    'Korea' : 'Busan',
    'Japan' : 'Tokyo',
    'China' : 'Beijing',
    'USA' : 'Washington',
    'London' : 'England'
}

# 1 매칭되지 않은 틀린수도를 찾아 올바른 수도로 변경
cities['Korea'] = 'Seoul'  # Korea에 접근해 직접 값을 변경

# 2 'France'와 이 나라의 수도를 딕셔너리에 추가
cities['France'] = 'Paris'  # 새로운 변수를 만들어 넣어줌

# 딕셔너리 key값이 국가가 아닌 것을 삭제
del cities['London']  # del 메서드를 이용해 국가가 아닌 값을 삭제

print(cities)
