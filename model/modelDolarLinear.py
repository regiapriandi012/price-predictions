from sklearn.linear_model import LinearRegression
import numpy as np
from ..server import data_dolar as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
price = data["price"]

df = pd.DataFrame({'date': date, 'price': price})
df.date  = pd.to_datetime(df.date)

x = df.date.values.astype(float).reshape(-1, 1)
y = df['price'].values.reshape(-1, 1)

lin = LinearRegression()
lin.fit(x, y)

date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
dfe = pd.DataFrame({'prediksi': date_predict})
dfe.prediksi = pd.to_datetime(dfe.prediksi)

coef = lin.coef_
intercept = lin.intercept_

x_predict = dfe.prediksi.values.astype(float).reshape(-1, 1)

lin_predict = lin.predict(x)
lin_pred_future = lin.predict(x_predict)
