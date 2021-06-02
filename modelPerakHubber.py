from sklearn.linear_model import HuberRegressor
import numpy as np
import matplotlib.pyplot as plt
from connect import data_perak as data
import datetime

time = datetime.datetime.now()

date = data["date"]
date = date.values.reshape(-1, 1)

price = data["price"]

plt.scatter(date, price)

#Hubber
hub = HuberRegressor()
hub.fit(date, price)

print("Intercept / kemiringan = " + str(hub.coef_))
print("Coefisien / titik potong = " + str(hub.intercept_))

date_predict = np.array((time.day)+1)
date_predict = date_predict.reshape(-1, 1)

hub_predict = hub.predict(date)
hub_predict_future = hub.predict(date_predict)

plt.plot(date, hub_predict)
plt.plot(date_predict, hub_predict_future)

print("prediksi besoknya adalah : " + str(hub_predict_future))
plt.show()