import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 샘플데이터
age = [13,14,15,16,17]
height = [160,165,170,173,177]
weight = [80,85,83,78,73]

'''
두가지의 정보를 하나의 그래프에 만들수 있다.
'''

fig, ax1 = plt.subplots()

barplt = ax1.bar(age, height, color = 'skyblue', width = 0.5, ec = 'lightgray', label = 'height')

# twinx를 이용하여 ax1 데이터와 x축의 값을 공유하는 ax2를 만들어 준다.
ax2 = ax1.twinx()
lineplt = ax2.plot(age, weight, color = 'darkred', marker = 'o', ls = '-', label = 'weight')

# 각축의 레이블을 설정해준다
ax1.set_xlabel('나이')
ax1.set_ylabel('키(cm)')
ax2.set_ylabel('몸무게(kg)')

# 각 그래프의 y축 범위를 지정해 준다.
ax1.set_ylim(150, 180)
ax2.set_ylim(60, 90)

# 각 y 축의 눈금 간격을 지정해 준다.
ax1.set_yticks(height)
ax2.set_yticks(weight)

ax1.tick_params(axis = 'y', colors = 'skyblue')
ax2.tick_params(axis = 'y', colors = 'darkred')

# 그리드 표시
ax1.grid(axis = 'y', ls = '--', color = 'skyblue')
ax2.grid(axis = 'y', ls = '--', color = 'pink')


# 각각의 범례를 출력해 준다.
ax1.legend(loc = 'upper left')
ax2.legend(loc = 0)

# subplot 으로 return 받은 fig 를 이용해서 범례를 출력하면
# 두개의 그래프 범례를 하나로 통합해서 볼수 있다.
# 그러나 loc로 위치 조정은 안되고 autoposition이다.
fig.legend()

plt.show()
