import pandas as pd
import numpy as np

'''
데이터 저장 및 불러오기
'''

#여러 데이터를 저장하고 불러올수 있다.
#일단 파일은 csv밖에 없어서 나머지는 주석
# df = pd.read_excel('./pandas/data/scores.xlsx')
# df = pd.read_csv('./pandas/data/scores.txt', sep='\t')
df = pd.read_csv('./pandas/data/scores.csv')

# 저장도 마찬가지.
# df.to_csv('./pandas/data/scores.csv')
# df.to_excel('./pandas/data/scores.xlsx')
# df.to_csv('./pandas/data/scores.txt', sep='\t')

'''
loc 와 iloc의 차이
loc는 '변수명'을 기준으로 DataFrame을 분류하고
iloc는 '인덱스 번호'를 기준으로 DataFrame을 분류한다.
'''

'''
loc와iloc 모두 0으로 지정해줬지만
loc의 0은 따로 인덱스 이름을 지정해 주지않았기때문에
인덱스번호 0 이 아닌 인덱스이름이 0으로 되어있는 상태이다.
'''
df.loc[0]
df.iloc[0]

df.index = 'idx' + df.index.astype('str')

# 위에서 인덱스 이름을 변경했기 때문에 loc[0]으로 다시 불러오면 에러가 발생한다.
# print(df.loc[0])  
df.loc['idx0'] # 인덱스 이름으로 불러와야 한다.
df.iloc[0]

# row 데이터 추출하기

# 리스트형으로 원하는 row의 데이터만 가져올수 있다
df.loc[['idx0', 'idx1', 'idx10']]
df.iloc[[0, 1, 10]]

# 슬라이싱해서 row 데이터 가져오기
# 슬라이싱은 [start : end - 1] 이다
df.loc['idx2' : 'idx10']
df.iloc[2 : 10]

# row 데이터와 column 데이터 추출하기
df.loc['idx0', 'name']
df.iloc[0, 0]

# row와 column모두 리스트, 슬라이싱으로 데이터를 추출할수 있다.
df.iloc[0,[1,2]] # 0번row 1, 2번 column
df.iloc[[1,3,4],1] # 1, 2, 3번 row 1번 column
df.iloc[[1,3,4],[0,2]]
df.iloc[0:4, 1:3]
df.iloc[1:6:2, :3:2]
df.iloc[-1, 1:4:2]

'''
column 추가

df[새로만들 컬럼 이름] = ... (column이 맨 뒤에 추가됨)
이렇게 추가하는 방법과

insert를 사용하는 방법
df.insert(loc, column, value, allow_duplicates=False)
loc = 삽입될 column의 위치
column = 삽입될 column의 이름
value = 삽입될 column의 값
allow_duplicates = column 이름 중복을 허용할지 default값은 False
'''

df['no'] = range(1,len(df)+1) # 맨뒤에 no컬럼을 1~1씩 증가하도록 추가
df.insert(1, 'number', range(1,len(df)+1)) #인덱스 번호 1위치에 number컬럼을 같은 값으로 추가


'''
column 데이터 수정하기

df[컬럼 이름] = ...

replace함수를 사용하는 방법.
df[컬럼 이름].replace({바꾸고 싶은 값:바꿀 값}, inplace)
'''

df['no'] = df['no'] + 99 # no 컬럼 각각의 값에 99를 더해준다
#replace 함수를 사용하면 원하는 값을 골라서 수정해 줄수 있다.
df['eng'].replace({100:90, 90:100}, inplace = True)

'''
column 삭제하기

df.drop([컬럼], axis=1) 
axis = 0이면 row 1이면 column

df.drop(columns=[컬럼], inplace=True)
두가지 방법이 있다.
'''
df.drop(['number'], axis=1, inplace=True) 
df.drop(columns=['no'], inplace=True)


'''
colmn 이름 변경하기

이름 한꺼번에 변경하는 방법
df.columns = [모든 칼럼 이름] 
한개라도 빼먹으면 안된다. inplace 없이 바로 변경됨

특정 column이름만 변경하는 방법
df.rename(columns = {바꾸고싶은컬럼 : 바꿀컬럼})
'''

df.columns = ['이름', '국어','영어', '수학']
df.rename(columns = {'이름':'name', '국어':'korean', 
                    '영어':'english', '수학':'mathematics'}, inplace=True)
df.columns = ['name', 'kor','eng', 'math']

'''
row 데이터 추가 하기

pandas 2.0 버전 이후부터 append함수는 사용하지 않기 때문에
concat 함수를 사용한다.

pd.concat([DataFrame1, DataFrame2], ignore_index)

데이터를 추가하는 다른 방법들은 꾸준히 공부 하면서 알아보자
'''

#dict 형태를 DataFrame으로 변환하기 위해선 Value값이 하나만 있더라도 list로 만들어 줘야 한다.
new_value = {'name':['Python'],'kor':[80.],'eng':[90.],'math':[100.]}
newdf = pd.DataFrame(new_value)
df = pd.concat([df, newdf], ignore_index=False)

'''
row 삭제하기

row를 삭제하는 방식은 column이랑 같다.
df.drop([인덱스이름], axis=0) 
axis = 0이면 row 1이면 column

df.drop(index=[인덱스이름], inplace=True)
두가지 방법이 있다.
'''

# 인덱스번호가 아니고 인덱스이름으로 삭제해야 한다.
df.drop(['idx0'], axis=0, inplace=True)
df.drop(index=['idx1'], inplace=True)

df.reset_index(drop=True, inplace=True)

'''
결측치
결측값(missing value)란 데이터에서 값이 비어있는 경우.
pandas에서는 numpy의 NaN 값으로 결측값을 표시한다.
'''

'''
결측치 제거하기
df.dropna(axis=0, how='any, inplace=True)
axis 0이면 row 제거 1이면 column 제거
how : 'any'결측값이 존재하면 제거, 'all' 모든 값이 결측값이면 제거
'''

df.dropna(axis=0)

'''
결측값 채우기
df.fillna(특정값)

- 결측값 이전행 값으로 채우기
df.fillna(method='ffill') or df.fillna(method='pad')

- 결측값 다음행 값으로 채우기
df.fillna(method='bfill') or df.fillna(method='backfill')

- dict 형태로 원하는 column마다 채울값을 지정해주기
df.fillna({컬럼:값, 컬럼:값})
'''

'''
데이터에 함수 적용하기.
Series.map(함수 이름) - Series 데이터 모든 값에 적용
DataFrame.apply(함수 이름, axis) - DataFrame의 row, column 단위로 적용
DataFrame.applymap(함수 이름) - DataFrame의 모든 값에 일괄 적용
'''

tempdf = pd.DataFrame(np.arange(12).reshape(4, 3), columns=['a', 'b', 'c'])

# plusdf = tempdf.apply(lambda x: x.sum())
# plusdf = tempdf.apply(lambda x: x.sum(), axis=1)
plusdf = tempdf.applymap(lambda x: '%.2f'% x if (x >= 5) else x)

# 에러 발생 코드
# plusdf = tempdf.apply(lambda x: '%.2f'% x) 


print(tempdf)
print(plusdf)
