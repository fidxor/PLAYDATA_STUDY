import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

tips = sns.load_dataset('tips')


'''
sns.parplot(data, x, y, ci, estimator, hue, palette)
data = 그래프를 표시할 데이터 객체
x = x축에 표시할 데이터 column
y = y축에 표시할 데이터 column
ci = 신뢰구간(Confidence Interval)을 함께 표시할지
estimator = 사용할 통계 함수.
hue = y를 그룹핑할 column
palette = hue 의 색상 변경 {'Yes':'gray', 'No':'skyblue'}
 '''

sns.barplot(data = tips, x = 'day', y = 'tip', ci = None, estimator = sum
            , hue = 'smoker', palette = {'Yes':'gray', 'No':'skyblue'})
plt.title('흡연자에 따른 요일별 팁 합계', size = 15)

plt.show()
