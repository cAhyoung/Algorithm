import pandas as pd
import numpy as np

# 1 Series 변환
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

list2series = pd.Series(mylist)
arr2series = pd.Series(myarr)
dict2series = pd.Series(mydict)

# 2 dict2series를 데이터 프레임으로 변환하고, 인덱스를 초기화
series2df = dict2series.to_frame().reset_index()

# 3 list2series, arr2series 데이터프레임으로 합치기
new_df = pd.concat([list2series, arr2series], axis=1)
print(new_df)

# 4 list2series에 이름 붙이기
list2series.name = 'alphabets'
print(list2series)

# 5 ser2에 존재하는 아이템 중 ser1에도 존재하는 아이템을 삭제
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

new_ser1 = ser1[~ser1.isin(ser2)]  # ~ : invert the boolean value
print(new_ser1)

# 6 ser1, ser2 중복제외 후 출력
new_ser2 = ser2[~ser2.isin(ser1)]
new_ser_concat = pd.concat((new_ser1, new_ser2))
print(new_ser_concat)

'''
## 6 모범답안
ser_u = pd.Series(np.union1d(ser1, ser2))  
### union1d: 입력받은 두 데이터의 값들 중 unique 값만 추려 정렬하여 반환

ser_i = pd.Series(np.intersect1d(ser1, ser2))
### intersect1d: 입력받은 두 데이터에 모두 존재하는 값을 추려 정렬하여 반환

ser_u[~ser_u.isin(ser_i)]
'''

# 7 Compute the minimum, 25th percentile, median, 75th, and maximum
info_series = pd.Series(np.random.normal(10, 5, 25))
print(info_series.describe())
