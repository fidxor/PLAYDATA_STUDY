import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

titanic = sns.load_dataset('titanic')

class_names = ['first', 'second', 'third']


plt.figure(figsize = (16, 6))
# sns.boxplot(x = 'fare', y = 'class', orient = 'h', data = titanic)
plt.grid()
# plt.show()

titanic3 = titanic.copy()

# IQR(inter Qunatile Range) 값으로 이상치 제거하기
def get_bound(series):
    quartile_1, quartile_3 = np.percentile(series, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return lower_bound, upper_bound

class_1 = titanic3[titanic.pclass == 1]['fare']
class_2 = titanic3[titanic.pclass == 2]['fare']
class_3 = titanic3[titanic.pclass == 3]['fare']

class_1_lower, class_1_upper = get_bound(class_1)
class_2_lower, class_2_upper = get_bound(class_2)
class_3_lower, class_3_upper = get_bound(class_3)

# class1의 운임이 class_1_fare보다 낮으면 class_1_lower값으로, 높으명 class_1_upper 값으로 바꾼다.
titanic3.loc[(titanic3.pclass == 1) & (titanic3.fare < class_1_lower), 'fare'] = class_1_lower
titanic3.loc[(titanic3.pclass == 1) & (titanic3.fare > class_1_upper), 'fare'] = class_1_upper
titanic3.loc[(titanic3.pclass == 2) & (titanic3.fare < class_2_lower), 'fare'] = class_2_lower
titanic3.loc[(titanic3.pclass == 2) & (titanic3.fare > class_2_upper), 'fare'] = class_2_upper
titanic3.loc[(titanic3.pclass == 3) & (titanic3.fare < class_3_lower), 'fare'] = class_3_lower
titanic3.loc[(titanic3.pclass == 3) & (titanic3.fare > class_3_upper), 'fare'] = class_3_upper

# sns.boxplot(x = 'fare', y = 'class', orient = 'h', data = titanic3)
plt.grid()
# plt.show()

titanic4 = titanic.copy()

# 각 객실 등급별 평균값 구하기
class_1_mean = titanic4[titanic4.pclass == 1]['fare'].mean()
class_2_mean = titanic4[titanic4.pclass == 2]['fare'].mean()
class_3_mean = titanic4[titanic4.pclass == 3]['fare'].mean()

# 표준편차를 이용한 이상치 구하기
titanic4 = titanic4[~((titanic4.pclass == 1) & (np.abs(titanic4.fare - class_1_mean) > 3 * titanic4.fare.std()))]
titanic4 = titanic4[~((titanic4.pclass == 2) & (np.abs(titanic4.fare - class_2_mean) > 3 * titanic4.fare.std()))]
titanic4 = titanic4[~((titanic4.pclass == 3) & (np.abs(titanic4.fare - class_3_mean) > 3 * titanic4.fare.std()))]

sns.boxplot(x = titanic4['fare'], y = titanic4['class'], orient = 'h', data = titanic4)
plt.grid()
plt.show()