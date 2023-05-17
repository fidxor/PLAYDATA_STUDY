import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 샘플데이터 
flights = sns.load_dataset('flights')


'''
sns.lineplot(data x, y, estimator, errorbar, hue)

data = 그래프를 표시할 데이터 객체
x = x축에 표시할 데이터 column
y = y축에 표시할 데이터 column
estimator = 사용할 통계 함수
hue = y를 그룹핑할 column 
'''

sns.lineplot(data = flights, x = 'month', y = 'passengers', hue = 'year')

plt.show()

