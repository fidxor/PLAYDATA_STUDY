import pandas as pd
import numpy as np

'''
groupby()는 데이터를 원하는 그룹별로 분할하여 독립된 그룹에 대하여
별도로 데이터를 처리, 적용 하거나 그룹별로 통계량을 확인할때 사용하는 함수이다.
'''

'''
groupby()에서 사용가능한 통계함수
- coutn() : 누락값을 제외한 데이터 수
- size() : 누락값을 포함한 데이터 수
- sum() : 합계
- mean() : 평균
- std() : 표준편차
- min() : 최소값
- max() : 최대값
- median() : 중앙값
- prod() : 곱
- unique(), nunique() : 고유값, 고유값의 개수
- first(), last() : 첫번째 값, 마지막 값
'''

df = pd.read_csv('./pandas/data/titanic.csv')

#실습을 위해서 몇개의 column만 사용하고 NaN이 있는 row 는 삭제해 준다
#Suvived column의 값에서 0은 사망 , 1은 생존으로 한다.
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]
df = df.dropna()

# Pclass(객실등급) 별 승선자의 수를 구한다.
# Pclass 의 각 1, 2, 3 값의 개수를 구한다. 
df1 = df.groupby('Pclass')['Pclass'].count().to_frame()

# Pclass(객실등급)별 생존자 수를 구한다.
# Survived의 값이 0과 1로 되어있기 때문에 
# 생존값인 1을 이용해 sum()함수로 간단하게 구할수 있다
df2 = df.groupby('Pclass')['Survived'].sum().to_frame()

# 좀더 명확하게 하고 싶어서 Survived 의 값이 1인 데이터만 그룹핑해서 카운트 하고 싶다.
# 만약 데이터가 '사망' , '생존' 이라는 문자열로 되어있을 경우 생존이라는 문자열만 카운트할수도 있기 때문에
df2 = df[(df['Survived'] == 1)]
df2 = df2.groupby('Pclass')['Survived'].count().to_frame()

# Pclass(객실등급) 별 생존율을 구한다.
df3 = df.groupby('Pclass')['Survived'].mean().to_frame()

# 성별 승선자 수를 구한다.
df4 = df.groupby('Sex')['Sex'].count().to_frame()

# 성별 생존자 수를 구한다.
df5 = df[(df['Survived'] == 1)]
df5 = df5.groupby('Sex')['Survived'].count().to_frame()

# 성별 생존률을 구한다.
df6 = df.groupby('Sex')['Survived'].mean().to_frame()

# 성별을 기준으로 객실 등급별 생존율
df7 = df.groupby(['Sex', 'Pclass'])['Survived'].mean()

'''
get_group()

그룹내에서 원하는 데이터의 row만 출력할수 있다.
'''

# Sex(성별) 그룹에서 male에 해당하는 데이터만 추출하기
dfGroup = df.groupby('Sex').get_group('male')

# multiple 그룹으로도 원하는 값으로 데이터를 추출할수 있다.
# Sex 값이 male 이고 Pclass 값이 2인 데이터 추출
dfGroup = df.groupby(['Sex', 'Pclass']).get_group(('male', 2))


# agg함수를 이용해서 평균값구하기
# 사용자정의 함수를 이용해서 평균값을 구할수 있다.
# def my_mean(values):
#     return sum(values)/len(values)

# dfagg = df.groupby(['Sex','Pclass']).Survived.agg(my_mean)


dfagg = df.groupby(['Sex', 'Pclass'])['Survived'].agg(['mean', 'sum'])

print(dfagg)

