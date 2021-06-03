from sklearn.linear_model import Lasso
import numpy as np
import matplotlib.pyplot as plt
from connect import data_emas as data
import datetime

time = datetime.datetime.now()

date = data["date"]
date = date.values.reshape(-1, 1)

price = data["price"]

#plt.scatter(date, price)

#Lasso
las = Lasso()
las.fit(date, price)

intercept = las.intercept_
coef = las.coef_

date_predict = np.array((time.day)+1)
date_predict = date_predict.reshape(-1, 1)

las_predict = las.predict(date)
las_predict_future = las.predict(date_predict)

#plt.plot(date, las_predict)
#plt.plot(date_predict, las_predict_future)

#plt.show()