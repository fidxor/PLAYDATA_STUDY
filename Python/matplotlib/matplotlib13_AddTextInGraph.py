import pandas as pd 
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

'''
그래프에 텍스트 추가하기

plt.text(x, y, text, ha, va, fontdict, rotation, bbox)

x = x의 좌표값
y = y의 좌표값
text = 추가할 텍스트
ha = 포인트 기준 텍스트를 출력할 x 위치
va = 포인트 기준 텍스트를 출력할 y 위치
fontdict = dict 형태로 폰트 스타일 지정
rotation = 텍스트 회전값
bbox = 텍스트 상자의 스타일 지정

fontdict 예제
fontdict = {'family': 'Malgun Gothic',  
      'color':  'blue',                 
      'weight': 'bold',                 
      'size': 12,
      'alpha': 0.7}

bbox 예제
bbox = {'boxstyle': 'square',
        'ec': (0.3, 1.0, 0.5),
        'fc': (0.8, 1.0, 0.5),
        'linestyle': '-.',
        'linewidth': 2}
'''

plt.plot([1, 2, 3, 4], 'ko')
plt.text(2, 3, '(x:2, y:3)', ha = 'left', va = 'bottom', fontsize = 12, rotation = 45
         , bbox = {'boxstyle':'round', 'fc':'skyblue', 'ec':'b', 'alpha': 0.4})

plt.axhline(3, ls = ':', alpha = 0.4, lw = 0.3)
plt.axvline(2, ls = ':', alpha = 0.4, lw = 0.3)

plt.show()

'''
화살표와 텍스트 추가 하기

plt.annotate(text, xy, xytext, arrowprops)

text = 추가할 텍스트
xy = 화살표가 가르킬 x, y 좌표
xytext = 추가할 텍스트의 x, y 좌표
arrowprops = 화살표의 속성

arrowprops 속성 예시
arrowprops = {'facecolor'='red', ## 내부 색깔
                , 'edgecolor'='black', ## 선 색깔
                , 'fill'=True, ## 내부가 비어짐(fill white와 같은 )
                , 'shrink'=0.15, ## 텍스트로부터 얼마나 떨어진 위치에서 화살표가 시작하는가? 0이 최소 1이 최대  
                , 'headwidth'=80, ## 화살 너비
                , 'headlength'=100, ## 화살 길이
                , 'width'=30, ## 화살표에서 화살이 아닌 부분의 너비
                , 'linewidth'=10, ## polygon의 선
                , 'linestyle'=':', ## 선의 특성
                , 'alpha'=0.8, ## 투명도}
                
'''

plt.plot([1,2,3,4], 'ko')
plt.axhline(2, color='orange', lw=0.5, alpha=0.5, ls='--')
plt.axvline(1, color='orange', lw=0.5, alpha=0.5, ls='--')
plt.plot(1,2,'ro')

plt.annotate('(x:1,y:2)', xy=(1,2), xytext=(1.5,2.5)
             , arrowprops={'width':2, 'headwidth':10, 'headlength':10, 'shrink':0.1, 'fc':'r'}
             , fontsize=12, color='r')
plt.show()
