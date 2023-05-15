import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

'''
데이터 시각화

https://matplotlib.org
'''

# 한글폰트 사용하기
# 폰트매니저에 있는 맑은 관련 폰트 이름을 보여준다.
print([f.name for f in fm.fontManager.ttflist if 'Malgun' in f.name])

# 한글폰트로 지정해 주기
plt.rcParams['font.family'] = 'Malgun Gothic'

# 한글폰트 사용 시 특수기호 깨지는 문제 해결
plt.rcParams['axes.unicode_minus'] = False

#그래프 그려보기
x = ['봄', '여름', '가을', '겨울']
y = [19, 30, 15, -10]

#그래프 그리기
#show()를 사용하면 그래프가 그려진 figure 창이 실행된다.
# plt.plot(x, y)
#plt.show()

# 그래프 라인의 색상 지정해주기
# 그래프 라인의 색상을 지정해 주는 방법은 여러가지가 있다.
# plt.plot(x, y, color='skyblue') # 색상 이름으로 지정
# plt.plot(x, y, color='r') # 색상 이름 약자로 지정
# plt.plot(x, y, color='#00ff00') # 색상 코드로 지정

'''
마커

Argument
marker : 마커종류
ms : 마커사이즈
mec : 마서 선 색상
mew : 마커선 굵기
mfc : 마커 내부 색상
'''

# plt.plot(x,y,color='#A566FF', marker='D', ms='10', mec='b', mew='3', mfc='y')

# plt.show()

'''
선(Line)

linestyle, ls : 선스타일     
'-'          solid line style    
'--'         dashed line style    
'-.'         dash-dot line style        
':'          dotted line style  

lw : 선 굵기
'''

# plt.plot(x,y,color='#A566FF', marker='D', ms='10', mec='b', mew='3', mfc='y', ls=':', lw=1)

# ':' 이렇게 인자값을 넘길수도 있고 선 스타일 이름을 직접 입력할수도 잇다.        
# plt.plot(x,y,color='#A566FF', marker='D', ms='10', mec='b', mew='3', mfc='y', ls='dotted', lw=5)

# 튜플 형식으로도 지정 가능
# plt.plot(x,y,color='#A566FF', marker='D', ms='10', mec='b', mew='3', mfc='y', ls=(0, (1, 1)), lw=3)

# 선과 마커 동시에 나타내기
# plt.plot(x, y, 'bo--')

'''
그래프의 종류

plot은 다양한 형태의 그래프를 지원한다.
'''

# 100명의 혈액형 분석 데이터
blood_type=['A','B','O','AB']
count=[45,35,15,5]


# plt.plot(blood_type, count)   # 선그래프
# plt.bar(blood_type, count, width=0.5)    # 막대 그래프
# plt.barh(blood_type, count)   #가로막대 그래프
# plt.pie(count, labels=blood_type) # 파이 차트


# 샘플데이터 (1~100사이의 랜덤 정수 1000개)
import numpy as np
data = np.random.randint(1,101,1000)

#히스토그램
# bins 는 해당 막대의 영역을 얼마나 채울지에 대한 인자값이다.
# plt.hist(data, bins=200)

#boxplot
# plt.boxplot(data)

# 샘플데이터(지불 금액에 대한 팁)
import seaborn as sns
tips = sns.load_dataset('tips')[['total_bill','tip']]

#산점도(scatter)
# plt.scatter(tips['total_bill'], tips['tip'])

'''
그래프의 제목 설정하기

plt.title('제목')

Argument
loc : 제목 위치('left','center','right')
pad : 타이틀과 그래프와의 간격
color : 폰트색상
fontsize : 폰트사이즈
fontweight : 폰트굵기('normal','bold','heavy','light','ultrabold','ultralight')
fontfamily : 폰트
'''

'''
x축, y축 레이블

plt.xlabel('레이블')     
plt.ylabel('레이블')

Argument
loc : 위치('left','center','right' / 'bottom', 'center','top')
labelpad : 레이블과 그래프와의 간격
color : 폰트색상
fontsize : 폰트사이즈
fontfamily : 폰트
'''

'''
그리드

plt.grid(True)

Argument
axis : 그리드 방향 'both', 'x', 'y'
ls : 라인스타일
lw : 라인 굵기
color : 라인 색상
alpha : 투명값

등의 속성을 지정할 수 있음
 '''

 # 실습을 위한 데이터 프레임 만들기
import pandas as pd
df = pd.DataFrame({'월':[1,2,3,4,5], '몸무게':[80,78,75,73,70]})

x = df['월']
y = df['몸무게']

# 그래프를 섞어서 사용할 수도 있다
plt.plot(x,y,'ro-', mec='b', mfc='b', lw=3, ms=7)
# plt.bar(x, y,)

# 타이틀 설정해주기
plt.title('월별 몸무게 변화', loc='right', pad=10, color='purple', 
          fontsize='20', fontweight='bold', fontfamily='Malgun Gothic')

# x 축 레이블 설정
# loc = 'center', 'right', 'left
plt.xlabel('월', loc='center', labelpad=5, color='pink', fontsize=16)

# y 축 레이블 설정
# loc = 'center', 'top', 'bottom'
plt.ylabel('몸무게', loc='top', labelpad=5, color='b', fontsize='15')

# 그리드 설정
# axis 기본값은 both 가로세로 x는 가로 y는 세로
plt.grid(axis='both', color='r', alpha=0.7, ls='dotted')

'''
축의 범위 지정하기
plt.xlim(min, max)
plt.ylim(min, max)
'''

'''
틱 지정

틱은 그래프의 축에 간격을 구분하기 위해 표시하는 눈금
plt.xticks([틱 리스트], labels)
plt.yticks([틱 리스트], labels)
labels = 틱 label을 지정해줄 리스트
눈금의 개수와 동일한 개수의 label리스를 지정한다.

틱 스타일 지정
plt.tick_params()
axis : 축지정 'both', 'x', 'y'
direction : 눈금의 위치 'in', 'out', 'inout'
length : 눈금의 길이
width : 눈금의 두께
color : 눈금의 색상
labelcolor : 틱 레이블 색상
colors : 틱 레이블의 색상
pad : 눈금과 레이블 사이의 간격
labelsize : 틱 레이블 사이즈
'''

xticks_lable = ['','1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
yticks_lable = ['0kg','10kg','20kg','30kg','40kg','50kg','60kg','70kg','80kg','90kg','100kg']

# 축의 범위 설정
plt.xlim(1, 12)
plt.ylim(0, 100)

# 틱 지정
# 틱 범위와 label리스트의 개수가 안맞으면 에러 발생
plt.xticks(range(0, 13, 1), labels=xticks_lable)
plt.yticks(range(0, 110, 10), labels=yticks_lable)

#틱 스타일 지정
plt.tick_params(axis='x', direction='inout', length=10, width=2, colors='g', labelsize=12)
plt.tick_params(axis='y', direction='out', length=10, width=2, colors='b', labelsize=12)

plt.show()

