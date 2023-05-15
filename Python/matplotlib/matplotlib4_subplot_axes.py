import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 셋팅
anscombe = sns.load_dataset('anscombe')
df1 = anscombe[anscombe['dataset']=='I']
df2 = anscombe[anscombe['dataset']=='II']
df3 = anscombe[anscombe['dataset']=='III']
df4 = anscombe[anscombe['dataset']=='IV']

'''
add_axes([x좌표, y좌표, 가로길이, 세로길이])
'''


fig = plt.figure(figsize = (10, 8))

# figure의 add_axes 함수로 위치와 크기를 지정해준다.
ax1 = fig.add_axes([0.1, 0.55, 0.4, 0.35])
ax2 = fig.add_axes([0.55, 0.55, 0.4, 0.35])
ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.35])
ax4 = fig.add_axes([0.55, 0.1, 0.4, 0.35])

# 생성한 axes에 그래프를 만든다.
ax1.plot(df1['x'], df1['y'], 'o')
ax2.plot(df2['x'], df2['y'], 'r^')
ax3.plot(df1['x'], df3['y'], 'k*')
ax4.plot(df1['x'], df4['y'], 'm+')

# 각 axes 의 제목 추가
ax1.set_title('ax1')
ax2.set_title('ax2')
ax3.set_title('ax3')
ax4.set_title('ax4')

fig.tight_layout()

fig.suptitle('add_axes_Anscombe')

'''
plt.subplots(nrows, ncols, figsize, sharex, sharey)
nrows = 행 개수
ncols = 열 개수
figsize = figure 사이즈
sharex = True = 그래프들끼리 같은x축을 사용, False : 그래프 각각 x축을 사용
sharey = y축을 가지고 공유 하는지 True, False

subplots 로 axes를 배열 형태로 만들어서 
axes[행번호][열번호] 형태로 접근하여 그래프를 그릴수 있다.
'''

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (8, 6), sharex = True, sharey = True)

# axes[행번호][열번호] 형태고 그래프 만들기
ax[0][0].plot(df1['x'], df1['y'], 'o')
ax[0][1].plot(df2['x'], df2['y'], '^')
ax[1][0].plot(df3['x'], df3['y'], '*')
ax[1][1].plot(df4['x'], df4['y'], 'd')

# 각 그래프에 제목 지정
ax[0][0].set_title('ax1')
ax[0][1].set_title('ax2')
ax[1][0].set_title('ax3')
ax[1][1].set_title('ax4')

# 각 그래프에 그리드 지정
ax[0][0].grid(ls=':')
ax[0][1].grid(ls=':', color='pink')
ax[1][0].grid(ls=':', color='skyblue')
ax[1][1].grid(ls=':', color='green', alpha=0.5)

# 그래프 전체의 제목
fig.suptitle('subplots_Anscombe', size = 20)

# 그래프 간격, 크기 최적화
fig.tight_layout()

plt.show()