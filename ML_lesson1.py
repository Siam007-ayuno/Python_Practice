
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[12.99], [14.99], [16.99], [10.99],[12.99]])
y = np.array([4.95, 4.51, 4.01, 2.11,4.26])

model = LinearRegression()
model.fit(X, y)   # train

print("Slope:", model.coef_)
print("Start:", model.intercept_)
print(model.predict([[15.99]]))
print("Score:", model.score(X, y))

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[104], [205], [305], [205],[154]])
y = np.array([4.95, 4.51, 4.01, 2.11,4.26])

model = LinearRegression()
model.fit(X, y)   # train

print("Slope:", model.coef_)
print("Start:", model.intercept_)
print(model.predict([[180]]))
print("Score:", model.score(X, y))

