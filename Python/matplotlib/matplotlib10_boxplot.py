import matplotlib.pyplot as plt
import pandas as pd

# 그래프에 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프에 마이너스 기호 깨지는 문제 해결
plt.rcParams['axes.unicode_minus'] = False


'''
boxplot(data, showmeans, meanline, vert)

showmeans = 평균치 표시 할지 True, False
mealine = 평군치를 라인으로 표시 할지 True, False
vert = 그래프를 가로, 또는 세로로 표시 할지
'''

# 샘플 데이터
scores = pd.Series([0,10,15,15,15,16,19,20,21,25,25,26,26,29,30,35,36,37,39,40,41,41,44,45,45,45,45,47,
          50,50,50,50,51,51,51,53,54,55,55,56,60,61,62,62,63,64,65,65,65,65,66,66,66,66,66,
          67,68,68,69,70,70,70,70,70,70,70,70,71,71,71,71,71,72,72,72,72,73,74,74,74,75,75,
          76,76,76,77,77,77,77,78,78,78,78,78,79,79,79,79,80,80,80,80,80,80,81,81,81,82,82,
          85,85,85,88,88,89,90,90,90,93,93,95,95,95,97,100])

# 샘플데이터의 이상치 구하기
Q1 = scores.quantile(0.25)
Q3 = scores.quantile(0.75)

#이상치
outlier1 = Q1 - 1.5 * (Q3 - Q1) # 이상치 미만인값
outlier2 = Q3 + 1.5 * (Q3 - Q1) # 이상치 이상인값

# plt.boxplot(scores, showmeans = True, meanline = True)

# 여러개의 데이터 비교하기
import seaborn as sns

iris = sns.load_dataset('iris')

print(iris.head())

plt.boxplot([iris['sepal_length'], iris['sepal_width'], iris['petal_length'], iris['petal_width']],
            labels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], 
            showmeans = True)

plt.grid(axis = 'y')

plt.show()


