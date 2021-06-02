import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
from connect import data_emas as data
import datetime

time = datetime.datetime.now()

x = data["date"]
X = x.values.reshape(-1, 1)
y = data["price"]

plt.scatter(X, y)

#Linear
lin = LinearRegression()
lin.fit(X, y)
print("Intercept / kemiringan = " + str(lin.coef_))
print("Coefisien / titik potong = " + str(lin.intercept_))

X_future = np.array((time.day)+1)
X_future = X_future.reshape(-1, 1)

lin_predict = lin.predict(X)
lin_predict_future = lin.predict(X_future)

plt.plot(X, lin_predict)
plt.plot(X_future, lin_predict_future)

print("prediksi besoknya adalah : " +  str(lin_predict_future))

plt.show()