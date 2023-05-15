import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 셋팅
anscombe = sns.load_dataset('anscombe')

df1 = anscombe[anscombe['dataset']=='I']
df2 = anscombe[anscombe['dataset']=='II']
df3 = anscombe[anscombe['dataset']=='III']
df4 = anscombe[anscombe['dataset']=='IV']

fig = plt.figure(figsize = (9, 6), facecolor = 'yellow')

# add_subplot() 함수를 사용하여 그래프를 그릴 axes 객체들을 생성.
ax1 = fig.add_subplot(2, 2, 1)
# ax1의 x축 과 y축을 공유한다.
ax2 = fig.add_subplot(2, 2, 2, sharex = ax1, sharey = ax1)
ax3 = fig.add_subplot(2, 2, 3, sharex = ax1, sharey = ax1)
ax4 = fig.add_subplot(2, 2, 4)

# axes 각각의 그래프를 만들어 준다.
ax1.plot(df1['x'], df1['y'], 'o', label = 'ax1')
ax2.plot(df2['x'], df2['y'], '^', label = 'ax2')
ax3.plot(df3['x'], df3['y'], '*', label = 'ax3')
ax4.plot(df4['x'], df4['y'], '+', label = 'ax4')

# 틱 간격 지정해 주기
ax4.set_xticks(range(1, 20, 1))
ax4.set_yticks(range(1, 15, 1))

# 각 그래프의 범례 표시해주기
ax1.legend(loc = 0)
ax2.legend(loc = 0)
ax3.legend(loc = 0)
ax4.legend(loc = 0)

# figuredml 제목 지정하기
fig.suptitle('Anscombe', size = 20)

# 그래프 크기, 간격 최적화 하기
fig.tight_layout()

plt.show()

# 그래프를 이미지로 저장하기.
# 작동 확인후 주석처리 
# fig.savefig('img200.jpg', dpi = 200)




