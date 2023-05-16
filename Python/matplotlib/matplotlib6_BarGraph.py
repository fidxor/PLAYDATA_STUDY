import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'Malgun Gothic'

plt.rcParams['axes.unicode_minus'] = False

#샘플 데이터 두매장의 요일별 평균매출액
df1 = pd.DataFrame({'요일':['월','화','수','목','금','토','일'], 
                   '매출액':[10000,9000,11000,8000,13000,15000,14000]})

df2 = pd.DataFrame({'요일':['월','화','수','목','금','토','일'], 
                   '매출액':[9000,9500,13000,7000,12000,14000,11000]})

'''
막대 그래프
plt.bar(x, y, width, color, edgecolor, linewidth, hatch, align) 세로 막대 그래프
plt.barh(x, y, height, color, edgecolor, linewidth, hatch, align) 가로 막대 그래프


width : 세로막대의 폭을 지정해 준다, 0 ~ 1 사이의 실수
height : 가로막대의 폭을 지정해 준다, 0 ~ 1 사이의 실수
color : 막대의 색상을 지정해 준다. 리스트를 사용하면 막대별로 색상을 지정해 줄수 있다.
edgecolor : 막대 테두리의 색깔을 지정해 준다.
linewidth : 막대 테두리의 두께를 지정해 준다.
hatch : 막대의 패턴을 지전해 준다. 패턴 기호 - '/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
align : 막대의 위치를 지정해 준다. 'center', 'edge'
        edge를 사용해서 눈금의 왼쪽에 위치하고 싶으면 width값을 음수로 지정해 주면된다.
'''

# 두개데이터의 막대를 모두 표시해서 값을 비교한다.
# align 값으로 위지 지정을 해주지 않으면 두개의 막대가 겹쳐서 표시되게 된다
plt.bar(df1['요일'], df1['매출액'], width = -0.4, align = 'edge', label='매장1')
plt.bar(df2['요일'], df2['매출액'], width = 0.4, align = 'edge', label = '매장2')

plt.title('두 매장의 요일별 평균 매출', size = 15)
plt.grid(axis = 'y', ls = 'dotted')
# 두개 데이터을 표시하니 범례를 표시해 준다.
#범례 위치를 0으로 하니깐 그래프를 움직일 때마다 최적의 위치로 자동이동
plt.legend(loc = 0)

plt.show()