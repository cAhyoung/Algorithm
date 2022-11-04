import numpy as np
import matplotlib.pyplot as plt 

#단일 그래프
## data 생성
data = np.arange(1, 100)

## plot
plt.plot(data)

## 그래프를 보여주는 코드
plt.show()



#다중 그래프
data = np.arange(1, 51)
plt.plot(data)


data2 = np.arange(51, 101)
plt.plot(data2)


plt.show()


#2개의 figure로 나누어서 다중 그래프 그리기
data = np.arange(100, 201)
data2 = np.arange(200, 301)

plt.plot(data)
#figure()는 새로운 그래프 canvas를 생성합니다.
plt.figure()
plt.plot(data2)


plt.show()

##여러개의 그래프 그리는 방법
#그래프마다 설정해줘야함
data = np.arange(100, 201)
plt.subplot(2, 1, 1)
plt.plot(data)


data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

#위의 코드와 동일하나 콤마를 빼도 가능
data = np.arange(100, 201)
plt.subplot(211)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(212)
plt.plot(data2)


plt.show()

#3개의 그래프
data = np.arange(100, 201)
plt.subplot(1, 3, 1)
plt.plot(data)


data2 = np.arange(200, 301)
plt.subplot(1, 3, 2)
plt.plot(data2)


data3 = np.arange(300, 401)
plt.subplot(1, 3, 3)
plt.plot(data3)


plt.show()

#여러개의 plot을 그리는 방법 (subplots) - s가 더 붙습니다.
data = np.arange(1, 51)
# data 생성

# 밑 그림
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(data)
axes[0, 1].plot(data * data)
axes[0, 2].plot(data ** 3)
axes[1, 0].plot(data % 10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data // 20)

plt.tight_layout()
plt.show()




















