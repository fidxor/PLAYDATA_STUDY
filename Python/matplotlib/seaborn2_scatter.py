import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 샘플 데이터
tips = sns.load_dataset('tips')


'''
tips_Sun = tips[tips['day']=='Sun']
tips_Sat = tips[tips['day']=='Sat']
tips_Fri = tips[tips['day']=='Fri']
tips_Thur = tips[tips['day']=='Thur']

plt.scatter(tips_Sun['total_bill'], tips_Sun['tip'], label='Sun', s=tips_Sun['size']*30, alpha=0.5)
plt.scatter(tips_Sat['total_bill'], tips_Sat['tip'], label='Sat', s=tips_Sat['size']*30, alpha=0.5)
plt.scatter(tips_Fri['total_bill'], tips_Fri['tip'], label='Fri', s=tips_Fri['size']*30, alpha=0.5)
plt.scatter(tips_Thur['total_bill'], tips_Thur['tip'], label='Thur', s=tips_Thur['size']*30, alpha=0.5)
plt.legend()
plt.xlabel('totla_bill')
plt.ylabel('tip')
'''


'''
sns.scatterplot(data, x, y, hue, size, alpha)

data = 그래프를 표시할 데이터 객체
x = x축에 표시할 데이터 column
y = y축에 표시할 데이터 column
hue = y를 그룹핑할 column
size = 각 마커의 사이즈를 지정
alpha = 각 마커의 투명도
'''

# 위에 코드 처럼 matplotlib으로 복잡하게 만드는 그래프를
# seaborn으로 간단하게 그래프를 만들어 줄수 있다.
sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', hue = 'day', size = 'size', alpha = 0.5)

plt.show()