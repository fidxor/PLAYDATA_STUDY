import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

'''
missingno 은 결측데이터들을 파악하는데 직관적인 도움을 주는 패키지이다
'''

titanic = sns.load_dataset("titanic")

# msno.matrix(titanic, color = (0.1, 0.6, 0.6))

msno.bar(titanic, color = (0.1, 0.6, 0.6))

plt.show()

# axis 축을 기준으로 입력된 데이터의 개수가 int(len(titanic)/2) == 445개 미만이면 해당 축을 삭제 해라
# 아래 코드를 적용했을 경우 데이터가 203개 입력된 deck coloumn은 삭제가 된다.
titanic = titanic.dropna(thresh=int(len(titanic)/2), axis=1)

msno.bar(titanic, color = (0.1, 0.6, 0.6))

plt.show()

# age의 빈값들은 age 전체값의 중간값으로 채워준다.
titanic.age.fillna(value = titanic.age.median(), inplace = True)

msno.bar(titanic, color = (0.1, 0.6, 0.6))

plt.show()


