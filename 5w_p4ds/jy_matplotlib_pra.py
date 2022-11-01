import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1, 2, 3], [2, 4, 9])
# 타이틀 & font 설정
plt.title('Anatomy of a figure', fontsize=20)
# X축 & Y축 Label 설정
plt.xlabel('x Axis label')
plt.ylabel('y Axis label')
# X tick, Y tick 설정
plt.xticks()
plt.yticks()
# legend 설정
plt.legend(['blue signal', 'orange signal'], fontsize=12, loc='upper right')
# x, y limit 설정
plt.xlim()
plt.ylim()
# 스타일 세부 설정 - 마커,라인,컬러
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')
# 그리드 설정
plt.grid()

plt.show()