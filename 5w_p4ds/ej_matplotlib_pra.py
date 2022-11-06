import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.rand(50)

np.arange(50)

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 1000

plt.scatter(x, y, s=area, c=colors)
plt.show()

np.random.rand(50)

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(x, y, s=area, cmap='blue', alpha=0.1)
plt.title('alpha=0.1')

plt.subplot(132)
plt.title('alpha=0.5')
plt.scatter(x, y, s=area, cmap='blue', alpha=0.5)

plt.subplot(133)
plt.title('alpha=1.0')
plt.scatter(x, y, s=area, cmap='blue', alpha=1.0)

plt.show()

x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.figure(figsize=(6, 3))
plt.bar(x, y, alpha=0.7, color='red')
plt.xticks(x)
plt.ylabel('Number of Students')
plt.title('Subjects')

plt.show()

x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.barh(x, y, , alpha=0.7, color='green')
plt.yticks(x)
plt.xlabel('Number of Students')
plt.title('Subjects')

plt.show()

x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# 넓이 지정
width = 0.35

# subplots 생성
fig, axes = plt.subplots()

# 넓이 설정
axes.bar(x - width/2, y_1, width, alpha=0.5)
axes.bar(x + width/2, y_2, width, alpha=0.8)

# xtick 설정
plt.xticks(x)
axes.set_xticklabels(x_label)
plt.ylabel('Number of Students')
plt.title('Subjects')

plt.legend(['john', 'peter'])

plt.show()

x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# 넓이 지정
width = 0.35

# subplots 생성
fig, axes = plt.subplots()

# 넓이 설정
axes.barh(x - width/2, y_1, width, alpha=0.5, color='green')
axes.barh(x + width/2, y_2, width, alpha=0.8, color='red')

# xtick 설정
plt.yticks(x)
axes.set_yticklabels(x_label)
plt.xlabel('Number of Students')
plt.title('Subjects')

plt.legend(['john', 'peter'])

plt.show()

x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

plt.plot(x, y)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

plt.grid()

plt.show()

x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.5)
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.5)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.5, marker='o')
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.5, marker='+')

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', linestyle=':')
plt.plot(x, y_2, label='1+cos', color='red', linestyle='-.')

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

