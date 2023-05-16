import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 실습용 샘플 데이터
scores = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

'''
히스토그램

plt.hist(values, bins, cumulative, histtype)

values = 그래프에 표시할 리스트 형태의 값
bins = 히스토그램 x축 구간의 개수
cumulative = 누적히스토그램 사용여부
histtype = 히스토그램의 종류 지정 'bar', 'barstacked', 'step', 'stepfilled'

'''

# 각 파라미터 값의 비교를 위해 같은데이터로 두개의 히스토그램을 그린다.
plt.hist(scores, cumulative = False)
plt.hist(scores, cumulative = True)

plt.show()

