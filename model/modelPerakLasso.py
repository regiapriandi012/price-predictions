import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import numpy as np
from ..server import data_perak as data
import datetime

time = datetime.datetime.now()

x = data["date"]
X = x.values.reshape(-1, 1)
y = data["price"]

#plt.scatter(X, y)

#Lasso
las = Lasso()
las.fit(X, y)

intercept = las.intercept_
coef = las.coef_

X_future = np.array((time.day)+1)
X_future = X_future.reshape(-1, 1)

las_predict = las.predict(X)
las_predict_future = las.predict(X_future)

#plt.plot(X, las_predict)
#plt.plot(X_future, las_predict_future)

#plt.show()