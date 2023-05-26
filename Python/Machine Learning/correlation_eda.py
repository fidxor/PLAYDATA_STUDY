import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

import seaborn as sns 
import scipy.stats as stats

plt.rcParams['font.family'] = 'Malgun Gothic'

wine = pd.read_csv('./Machine Learning/example/data/wine.csv')


# duplicated 함수로 중복 데이터 제거
wine = wine[~wine.duplicated(wine.columns, keep = 'last')]

# 컬럼 이름 정의
wine.columns = ['고정산', '휘발산', '구연산', '잔여당', '염화물', '무수아황산', '총이산화황', 
                '밀도', '산성도', '황산염', '알콜도수', '와인품질', '와인종류'] 

 # 히스토그램으로 각 함유 성분 데이터값 확인
# plt.figure(figsize = (12, 12))
# for i in range(0, 11):
#     plt.subplot(3, 4, i + 1)
#     sns.histplot(wine.iloc[:,i])

# plt.tight_layout()
# plt.show()

# countplot으로 와인품질 데이터 확인
# sns.countplot(x = '와인품질', data = wine)
# plt.grid()
# plt.show()

# sns.countplot(x = '와인종류', data = wine)
# plt.grid()
# plt.show()

# # 와인 종류에 따른 와인품질 그래프 확인.
# sns.countplot(x = '와인품질', hue = '와인종류', data = wine)
# plt.show()


wine_corr = wine.corr()

print(wine_corr)

plt.figure(figsize = (15, 15))
mask = np.array(wine_corr)
# 삼각형 마스크를 만든다.
mask[np.tril_indices_from(mask)] = False
sns.heatmap(wine_corr, mask = mask, annot = True, cmap = 'Blues')

plt.show()


