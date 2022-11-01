#box plot
# 샘플 데이터 생성
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))


#다중 박스플롯 생성

# 샘플 데이터 생성
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

spread = np.random.rand(50) * 100
center = np.ones(25) * 40

flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100

d2 = np.concatenate((spread, center, flier_high, flier_low))

data.shape = (-1, 1)
d2.shape = (-1, 1)

data = [data, d2, d2[::2,0]]

plt.boxplot(data)
plt.tight_layout()
plt.show()


#7-3, Box Plot 축 바꾸기
plt.boxplot(data, vert = 0)
plt.tight_layout()

plt.show()

#7-4 Outlier 마커 심볼과 컬러 변경
outlier_marker = dict(markerfacecolor='r', marker='D')
plt.show()
plt.title('Changed Outlier Symbols', fontsize=15)
# 코드를 입력해 주세요
plt.tight_layout()
plt.show()

plt.title('Changed Outlier Symbols', fontsize=15)
# 코드를 입력해 주세요
#outlier_marker = dict(markerfacecolor='r', marker='D')
plt.boxplot(data,sym='r')
#plt.tight_layout()
plt.show()



#8. 3D 그래프 그리기 
fig = plt.figure()
# 코드를 입력해 주세요
fig = plt.figure()
fig.set_size_inches(15, 15)
ax = plt.axes(projection='3d')

fig = plt.figure()
fig.set_size_inches(15, 15)
ax = plt.axes(projection='3d')
plt.show()


#8-2. 3d plot 그리기
# project=3d로 설정합니다
ax = plt.axes(projection='3d')

# x, y, z 데이터를 생성합니다
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

ax.plot(x, y, z, 'gray')
plt.show()

# project=3d로 설정합니다
ax = plt.axes(projection='3d')

sample_size = 100
x = np.cumsum(np.random.normal(0, 1, sample_size))
y = np.cumsum(np.random.normal(0, 1, sample_size))
z = np.cumsum(np.random.normal(0, 1, sample_size))

# 코드를 입력해 주세요
ax.plot(x, y, z, alpha=0.6, marker='o') #alpha는 투명도 이걸로 색깔 조정 가능한 듯

plt.title("ax.plot")
plt.show()



#8-3. 3d-scatter 그리기
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sample_size = 500

x = np.cumsum(np.random.normal(0, 5, sample_size))
y = np.cumsum(np.random.normal(0, 5, sample_size))
z = np.cumsum(np.random.normal(0, 5, sample_size))

# 코드를 입력해 주세요
ax.scatter(x, y, z, c = z, s= 20, alpha=0.5, cmap=plt.cm.Greens)

plt.title("ax.scatter")
plt.show()


#8-4 contour3D 그리기 (등ㄱ선)
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection='3d')

ax.contour3D(x, y, z, 20, cmap='Reds')

plt.title("ax.contour3D")
plt.show()

from sklearn.datasets import load_digits

digits = load_digits()
X = digits.images[:10]
X[0]

import matplotlib.cm as cm

fig, axes = plt.subplots(nrows=2, ncols=5, sharex=True, figsize=(12, 6), sharey=True)

for i in range(10):
    axes[i//5][i%5].imshow(X[i], cmap=cm.cividis)# 코드를 입력해 주세요
    axes[i//5][i%5].set_title(str(i), fontsize=20)
    
plt.tight_layout()
plt.show()
