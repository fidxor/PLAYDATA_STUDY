'''
 여러 그래프를 한번에 그릴수 있다.
'''
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 한글설정 
mpl.rcParams['font.family'] = 'Malgun Gothic'
# 마이너스 기호 깨지는 문제 해결
mpl.rcParams['axes.unicode_minus'] = False

df1 = pd.DataFrame({'월':[1,2,3,4,5],'몸무게':[80,78,75,73,70]})
df2 = pd.DataFrame({'월':[1,2,3,4,5],'몸무게':[60,62,59,55,54]})


'''
범례 표시
plt.plot(x, y, label = '그래프 이름')그래프에 범례이름을 지정한다
plt.legend() 범례를 표시한다.
'''
# 데이터가 다른 두 그래프 그리기
plt.plot(df1['월'], df1['몸무게'], label = 'James')
plt.plot(df2['월'], df2['몸무게'], label = 'Amy')
plt.legend()

# x축 틱 라벨
def fn_xtickLabel(x):
    x = str(x) # x를 문자열로 변환한다
    if x == '0' or x == '13':
        return ''
    else:
        return x + '월' # 0과13을 제외한 나머지에 '월'을 붙인다.
    
xtick_label = pd.Series(range(0, 14, 1))    # 0 ~ 13 까지 리스트
xtick_label = xtick_label.apply(fn_xtickLabel)

# y축 틱 라벨
def fn_ytickLabel(x):
    x = str(x)
    return x + 'kg'

ytick_label = pd.Series(range(30, 95, 5)) # 30 부터 5단위로 90까지 리스트
ytick_label = ytick_label.apply(fn_ytickLabel)

#그래프 제목
plt.title('월별 몸무게 변화', size = 15)

#축 라벨
plt.xlabel('월', fontsize = 12)
plt.ylabel('몸무게', fontsize = 12)

# x축 틱 : 1월, 2월, 3월, ..... 12월
plt.xticks(range(0, 14, 1), labels = xtick_label)

#y축 틱 : 30kg, 35kg, 40kg, ..... 90kg
plt.yticks(range(30, 95, 5), labels = ytick_label)

#그리드
plt.grid(ls = ':')

'''
범례 위치 지정

plt.legend(loc = '') '위치이름', '위치번호'
위치이름은 문자열로 위치번호는 정수로
plt.legend(loc=(x, y)) 좌표로 범례위치 지정. 왼쪽아래 꼭지점 기준

'best'            0
'upper right'     1
'upper left'      2
'lower left'      3
'lower right'     4
'right'           5
'center left'     6
'center right'    7
'lower center'    8
'upper center'    9
'center'          10
'''

'''
범례 속성 지정
열 개수 : plt.legend(ncol=열개수)
폰트 사이즈 : plt.legend(fontsize=폰트사이즈)
테두리 사용유무 : plt.legend(frameon=True/False) 기본값을 True
음영 : plt.legend(shadow=True/False)
바탕색 : plt.legend(facecolor=색상)
테두리색 : plt.legend(edgecolor=색상)
'''

plt.legend(loc = 5,ncol = 2, fontsize = 12, shadow = True, facecolor = 'purple',
           edgecolor = 'k')

plt.show()

