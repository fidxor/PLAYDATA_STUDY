import matplotlib.pyplot as plt
import pandas as pd


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

scores = pd.Series([0,10,15,15,15,16,19,20,21,25,25,26,26,29,30,35,36,37,39,40,41,41,44,45,45,45,45,47,
          50,50,50,50,51,51,51,53,54,55,55,56,60,61,62,62,63,64,65,65,65,65,66,66,66,66,66,
          67,68,68,69,70,70,70,70,70,70,70,70,71,71,71,71,71,72,72,72,72,73,74,74,74,75,75,
          76,76,76,77,77,77,77,78,78,78,78,78,79,79,79,79,80,80,80,80,80,80,81,81,81,82,82,
          85,85,85,88,88,89,90,90,90,93,93,95,95,95,97,100])

'''
plt.violiplot(Values, showextrema, showmeans, showmedians,
             quantiles)

values = 그래프를 그릴 리스트 형태의 데이터 
showextrema = True, False 최대값, 최소값에 직선 표시 default = True
showmeans = True, False 평균값에 직선 표시 default = False
showmedians = True, False 중간값에 직선표시 default = False
quantiles = [0.25, 0.75]분위수를 지정해 주기
'''

# v1 = plt.violinplot(scores, showextrema = True, showmeans = True, showmedians = True, 
#                quantiles = [0.25, 0.75])

'''
violinplot 스타일 지정하기
'''
# 0번 인덱스의 바이올린그래프
# 여러개의 바이올린 그래프가 있으면 0, 1, 2, ... 인덱스 값을 넣어준다.
# v1['bodies'][0].set_facecolor('r') 
# v1['cmins'].set_edgecolor('g')      # min 표시줄 색상
# v1['cmaxes'].set_edgecolor('g')     # max 표시줄 색상
# v1['cbars'].set_edgecolor('k')      # 가운데 세로 라인 색상
# v1['cmedians'].set_edgecolor('r')   # 가운데 값 표시줄 색상
# v1['cquantiles'].set_edgecolor('w') # 사분위 표시줄 색상
# v1['cmeans'].set_edgecolor('y')     # 평균값 표시줄 색상

#여러개의 바이올린플롯 만들기

# 샘플데이터
import seaborn as sns
iris = sns.load_dataset('iris')

v2 = plt.violinplot([iris['sepal_length'], iris['sepal_width'], iris['petal_length'], iris['petal_width']]
               , showmeans = True, showmedians = True, 
               quantiles = [[0.25, 0.75], [0.25, 0.75], [0.25, 0.75], [0.25, 0.75]])

# x축 틱 설정
plt.xticks(range(1, 5, 1), labels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

v2['bodies'][0].set_facecolor('r')
v2['bodies'][1].set_facecolor('g')
v2['bodies'][2].set_facecolor('b')
v2['bodies'][3].set_facecolor('c')
v2['cmins'].set_edgecolor('r')
v2['cmaxes'].set_edgecolor('r')
v2['cmeans'].set_edgecolor('r')

plt.grid(axis = 'y', ls = ':', alpha = 0.5)

plt.show()