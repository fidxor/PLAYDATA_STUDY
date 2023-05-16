import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic'

mpl.rcParams['axes.unicode_minus'] = False

# 테스트 데이터
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()

'''
scatter - 산점도 그래프

plt.scatter(x, y, 'o'. s, c, cmap)

s : 점의 크기를 공통으로 지정할수도 있고 리스트로 값마다 크기를 지정해 줄수 있다.
c : 색상 값, 리스트를 사용해서 값다가 색상을 다르게 줄수 있다.
cmap : cmap 을 사용하려면 c값에 cmap을 적용시킬 데이터 x 또는 y를 넣어줘야 한다.
컬러맵 : https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html
'''

# 지불 금액에 따른 팁제공 금액
# plt.scatter(tips['total_bill'], tips['tip'], c = tips['total_bill'], cmap = 'cool')


# 데이터에 새로운 column을 추가해서 성별에 따른 점의 색깔을 지정해 줄수 있다.

def set_Color(x):
    if x == 'Male':
        return 'blue'
    elif x == 'Female':
        return 'red'
    
tips['color'] = tips['sex'].apply(set_Color)

plt.scatter(tips['total_bill'], tips['tip'], s = tips['size'] * 50, c = tips['color'], alpha = 0.5)

plt.show()