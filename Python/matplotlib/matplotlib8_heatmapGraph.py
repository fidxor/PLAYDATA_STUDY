import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 히트맵 실습을 위한 테스트 데이터
import seaborn as sns
titanic = sns.load_dataset('titanic')
# 결측치 처리
titanic = titanic.drop(columns = ['deck'])
titanic = titanic.dropna()

# 연령대 column 생성
# 연령대 표현을 위해 뒤에 한자리수를 버린다. 예 ) 25살 이면 20대
titanic['agerange'] = (titanic['age'] / 10).astype('int') * 10

# 연령대 - 객실 등급별 승선자수 데이터를 가지고 pivot_table을 만든다

titanic_pivot = titanic.pivot_table(index = 'class', columns = 'agerange', values = 'survived', aggfunc = 'count')

'''
히트맵 그래프

plt.pcolor(data)
'''

plt.pcolor(titanic_pivot)
plt.colorbar()

plt.xticks(np.arange(0.5, len(titanic_pivot.columns), 1), labels = titanic_pivot.columns)
plt.yticks(np.arange(0.5, len(titanic_pivot.index), 1), labels = titanic_pivot.index)


'''
seaborn으로 히트맵 그리기

sns.heatmap(data, cmap, annot, fmt)
data = 2차원 데이터객체
cmap = 컬러맵 지정. 컬러맵 : https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html
annot = 수치표시 여부
fmt = 'd' 수치를 정수로 표시
'''

sns.heatmap(titanic_pivot, cmap='Blues', annot=True, fmt='d')









