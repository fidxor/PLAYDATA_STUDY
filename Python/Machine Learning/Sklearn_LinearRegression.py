import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rs = np.random.RandomState(10)
x = 10 * rs.rand(100)
y = 3 * x + 2 * rs.rand(100)

# 선형회귀
regr = LinearRegression(fit_intercept = True)

# 훈련을 위하여 x 를 2차원 배열로 바꿔준다
x = x.reshape(-1, 1)

regr.fit(x, y)

print(regr.coef_)
print(regr.intercept_)

x_new = np.linspace(-1, 11, num = 100)
x_new = x_new.reshape(-1, 1)

# x_new 모델로 부터 종속변수를 예측
y_pred = regr.predict(x_new)

plt.plot(x_new, y_pred, c = 'red')
plt.scatter(x, y)

plt.show()