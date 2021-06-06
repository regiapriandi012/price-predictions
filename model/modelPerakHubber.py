from sklearn.linear_model import HuberRegressor
import numpy as np
import matplotlib.pyplot as plt
from ..server import data_perak as data
import datetime

time = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
date = date.values.reshape(-1, 1)

price = data["price"]

#plt.scatter(date, price)

#Hubber
hub = HuberRegressor()
hub.fit(date, price)

intercept = hub.intercept_
coef = hub.coef_

date_predict = np.array(time.day)
date_predict = date_predict.reshape(-1, 1)

hub_predict = hub.predict(date)
hub_predict_future = hub.predict(date_predict)

#plt.plot(date, hub_predict)
#plt.plot(date_predict, hub_predict_future)

#plt.show()