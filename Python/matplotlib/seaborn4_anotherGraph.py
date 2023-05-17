import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')

iris = sns.load_dataset('iris')

'''
- 카운트 플롯
countplot(data, x, hue)

- 러그 플롯
rugplot(data, x)

- 히스토그램
displot(data, x)

- 상자수염 그래프 : boxplot()
boxplot(data)

- 바이올린 플롯
violinplot(data)

- 스트립 플롯
stripplot(data)

- 스웜 플롯
swarmplot(data)

data = 그래프를 그릴 데이터 객체
x = x축에 적용시킬 데이터 column
hue = 그룹핑 할 데이터 column
'''



# 카운트플롯
sns.countplot(data = titanic, x = 'who', hue = 'alive')

# 러그플롯
# sns.rugplot(data = titanic, x = 'age', hue = 'alive')

#히스토그램
sns.displot(data = iris, x = 'petal_length', bins = 20, rug = True, hue = 'species', kde = True)



plt.figure(figsize = (12, 8))
# 박스플롯
plt.subplot(221)
sns.boxplot(data=iris, x='species', y='petal_length')

# 바이올린플롯
plt.subplot(222)
sns.violinplot(data=iris, x='species', y='petal_length')

# 스트립플롯
plt.subplot(223)
sns.stripplot(data=iris, x='species', y='petal_length')

# 스웜플롯
plt.subplot(224)
sns.swarmplot(data=iris, x='species', y='petal_length',s=2)

plt.tight_layout()

plt.show()