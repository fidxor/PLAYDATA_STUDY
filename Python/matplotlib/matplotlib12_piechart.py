import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


#샘플 데이터
blood_type = ['A','B','O','AB']
Personnel = [111901,87066,86804,36495]

'''
파이차트

plt.pie(values, labels, labeldistance, autopct, pctdistance
         startangle, counterclock, explode, shadow, colors, 
         wedgeprops, textprops)

values = 1차원 리스트/배열/시리즈 데이터
labels = 각 데이터의 이름 values 와 같은 개수
labeldistance = 그래프와 레이블의 간격
autopct = 부채꼴에 들어갈 숫자의 형식.
pctdistance = 중심에서 데이터 숫자의 간격
startangle = 부채꼴이 그려지는 시작 각도
counterclock = False 면 시계방향으로 부채꼴영역이 표시
explode = 부채꼴이 차트 중심에서 떨어지는 정도
shadow = 그림자 효과
colors = 색상 지정
radius = 반지름 길이 설정 그래프 원크기에 관련
wedgeprops = 부채꼴 영역의 스타일을 설정
            딕셔너리의 'width', 'edgecolor', 'linewidth' 키를 이용해서
            각각 부채꼴 영역의 너비 (반지름에 대한 비율), 테두리의 색상, 테두리 선의 너비를 설정
textprops = 폰트 스타일 설정
            딕셔너리의 fontsize, color, rotation 키값을 가지고 설정.
    
'''

explode = [0.05, 0, 0, 0]
colors = ['plum', 'gold', 'orangered', 'palegreen']

plt.pie(Personnel, labels = blood_type, autopct = '%.2f%%', explode = explode
        , colors = colors, startangle = 90
        , wedgeprops = {'edgecolor':'k', 'width':0.8})

plt.title('혈액형 분포', size = 17)
plt.legend(loc = 0)
plt.show()