import matplotlib.pyplot as plt
import seaborn as sns

anscombe = sns.load_dataset('anscombe')

print(anscombe.head())

# 4가지 데이터를 각각 DataFrame으로 만들기
df1 = anscombe[anscombe['dataset']=='I']
df2 = anscombe[anscombe['dataset']=='II']
df3 = anscombe[anscombe['dataset']=='III']
df4 = anscombe[anscombe['dataset']=='IV']

#4개의 데이터를 하나의 그래프에 그린다.

# plt.plot(df1['x'], df1['y'], 'o')
# plt.plot(df2['x'], df2['y'], 'o')
# plt.plot(df3['x'], df3['y'], 'o')
# plt.plot(df4['x'], df4['y'], 'o')

#각 데이터 통계 수치를 바인딩한다.
df1 = df1.describe()
df2 = df2.describe()
df3 = df3.describe()
df4 = df4.describe()

'''
subplot()

plt.figure(figsize = (x, y), facecolor = '색') 
figsize : 출력되는 figure 창의 크기를 지정해준다.
facecolor : 색상 지정

plt.subplot(전체행개수 전체열개수 그래프순서)
plt.title('제목이름') 각 그래프의 제목

fig.subtitle('제목이름', size = 10) 전체 figure 의 제목과 폰트 사이즈

예 )
plt.subplot(221)
2개의 열 2개의 행 구조로 되어있는 figure에 1번째 그래프
'''
fig = plt.figure(figsize = (9, 6), facecolor = 'y')

plt.subplot(221)
plt.plot(df1['x'], df1['y'], 'o')
plt.title('ax1')

plt.subplot(222)
plt.plot(df2['x'], df2['y'], '+')
plt.title('ax2')

plt.subplot(223)
plt.plot(df3['x'], df3['y'], '*')
plt.title('ax3')

plt.subplot(224)
plt.plot(df4['x'], df4['y'], 'd')
plt.title('ax4')

fig.suptitle('Amscombe', size = 20)
fig.tight_layout()

plt.show()



