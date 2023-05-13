import numpy as np
import pandas as pd
'''
Series

- pandas에서 데이터를 생성하는 가장 기본적인 방법.
- Series 형식의 구조적 데이터(라벨을 갖는 1차원 데이터)를 생성할수 있다.
'''

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# s1 데이터의 인덱스 범위를 보여준다.
print(s1.index)

# numpy와는 다르게 타입이 다른 데이터들도 입력이 가능하다.
s2 = pd.Series(["a", "b", "c", 1, 2, 3])
print(s2)

# 데이터가 없으면 numpy의 nan값을 이용할수 있다.
s3 = pd.Series([np.nan, 10, 30])
print(s3)

#index를 명시적으로 지정해서 사용할수 있다.
index_date = ["2018-10-07", "2018-10-08", "2018-10-09", "2018-10-10"]
s4 = pd.Series([200, 195, np.nan, 205], index = index_date)
print(s4)

#dict를 이용하면 index와 value 값을 함께 사용할수 있다.
#key 값이 index , value 값이 value
s5 = pd.Series({"국어":100, "영어":80, "수학":90})
print(s5)

'''
날짜 자동 생성 : date_range
pd.date_range(start=None, end=None, periods=None , freq="D")
Start - 시작날짜
end - 마지막 날짜
periods - 날짜 데이터 생성기간
freq - 날짜 데이서 생성 주기
'''

createDate = pd.date_range(start = "2019-01-01", end = "2019-01-07")


# 입력하는 날짜 형식이 다르더라도 자동으로 padas 에서 지정된 날짜 형식으로 변환 된다.
createDate = pd.date_range(start = "2019-01-01", end = "2019.01.07")
createDate = pd.date_range(start = "01-01-2019", end = "01/07/2019")
createDate = pd.date_range(start = "2019-01-01", end = "01.07.2019")

#end 를 지정하지 않고 periods 를 사용하여 날짜 생성 기간을 지정해 줄수 있다.

periodsDate = pd.date_range(start = "2019-01-01", periods = 9)


# padas에서는 여러가지 freq 옵션을 제공하고 있다.

# 시작날짜에서 2일씩 증가 하는 함수
freqDate = pd.date_range(start = "2019-01-01", periods = 4, freq = "2D")
print(freqDate)

# date_range를 사용해서 Series의 인덱스로 이용할수도 있다.
index_date = pd.date_range(start = "2019-01-01", periods = 5, freq = "D")
index_series = pd.Series([5, 4, 3, 6, 3], index = index_date)


'''
DataFrame
- 표(Table)와 같은 2차원의 데이터를 처리한다.
- 라벨이 있는 2차원의 데이터를 생성하고 처리할수 있다.
- index 와 column 으로 구성되어있다
'''

# 기본적인 2차원 DataFrame 생성 예제코드
dataFrame = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#numpy의 배열로도 생성이 가능하다.
data_list = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dataFrame = pd.DataFrame(data_list)

# data뿐 아니라 index와 column도 지정해서 생성할 수 있다.
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9], [10, 11, 12]])
index_date = pd.date_range('2019-09-01', periods=4)
columns_list = ['A', 'B', 'C']
pd.DataFrame(data, index = index_date, columns = columns_list)

# 파이썬의 dict를 사용해서 데이터를 만들수 있다.
table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
              '지사': ['한국', '한국', '미국', '한국','미국'],
              '고객 수': [200, 250, 450, 300, 500]}


dataFrame = pd.DataFrame(table_data)

# 컬럼의 순서를 바꿔줄수있다.
df = pd.DataFrame(table_data, columns = ["연도", "지사", "고객 수"])

'''
데이터 연산
- Series()와 DataFrame() 으로 생성한 데이터끼리는 사칙 연산을 할수 있다.
'''

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])

s1 + s2
s1 * s2

# numpy와는 다르게 pandas 의 데이터 끼리는 서로 크기가 달라도 연산을 할수 있다
# 대신 사이즈가 다른 부분은 NaN으로 입력이 된다.
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([10, 20, 30, 40, 50])

s1 + s2

# dataFram()으로 생성한 DataFrame끼리도 사칙연산을 할수 있다
table_data1 = {'A': [1, 2, 3, 4, 5],
              'B': [10, 20, 30, 40, 50],
              'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(table_data1)

table_data2 = {'A': [6, 7, 8],
              'B': [60, 70, 80],
              'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)

# Series 와 마찬가지로 사이즈가 달라 연산할수 없는 항목는 NaN으로 입력된다.
df1 + df2
df1 - df2
df1 * df2
df1 / df2



table_data3 = {'봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list = ['봄', '여름', '가을', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, columns = columns_list, index = index_list)

'''
DataFrame 의 통계 메소드
- sum() - 원소의 합
- mean() - 평균
- std() - 표준편차
- var() : 분산
- min() : 최소값
- max() : 최대값
- cumsum() : 각 원소의 누적 합
- cumprod() : 각 원소의 누적 곱
- describe() : 평균, 표준편차, 최소값, 최대값등을 한번에 보여준다
등등등
'''

df3.mean()
df3.std()

# axis 를 인자값으로 사용해서 value의 연산 방향을 설정할수 있다.
# axis 를 0으로 하면 열별로 연산을 수행하고 1이면 행별로 연산을 수행한다. 기본값은 0
df3.mean(axis = 1)
df3.std(axis = 1)

df3.describe()

'''
원하는 데이터만 출력하기
'''

KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)

#데이터의 원하는 행을 가져오는법

# 인자값이 없으면 맨위에서 5개의 데이터만 가져온다.
df_KTX.head()
# 인자값이 없으면 맨 아래에서 5개의 데이터만 가져온다.
df_KTX.tail()

# 슬라이싱 기능을 사용할수 있다.
df_KTX[1:2]
df_KTX[2:5]

#DataFrame을 생성할때 index를 지정했다면 index 이름으로 행을 선택할수 있다.
df_KTX.loc["2011"]
#마찬가지로 슬라이싱 기능을 사용할 수 있다.
df_KTX.loc["2011":"2015"]

#column의 열 데이터만 가져올수 있다.0
df_KTX["경부선 KTX"]

# 하나의 column에 원하는 index 만 선택해서 출력할수도 있다.
df_KTX['경부선 KTX']['2012':'2014']
df_KTX['경부선 KTX'][2:5]

#행과 열을 바꾸는 전치(transpose)도 사용가능
df_KTX.T

'''
데이터 통합하기
- 두개의 데이터를 세로로 통합, 가로로 통합, 특정 열을 기준으로 통합하는 방법이 있다.
'''

'''
세로로 통합할 때는 append를 사용하라고 하지만. 
pandas 2.0 버전 이후에는 append가 삭제 되었다.
append 대신 concat 으로 대처해서 사용한다.
'''

df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]})

df2 = pd.DataFrame({'Class1': [87, 89],
                    'Class2': [85, 90]})

# append로 사용 할때 에러 발생해서 주석처리
# df1.append(df2)
# df1.append(df2, ignore_index = True)

#concat 사용
pd.concat([df1, df2])
pd.concat([df1, df2], ignore_index=True)


# 가로로 통합을 하려면 join 함수를 사용한다.
df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
df1.join(df4)