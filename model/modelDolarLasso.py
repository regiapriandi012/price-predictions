from sklearn.linear_model import Lasso
import numpy as np
from ..server import data_dolar as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
price = data["price"]

df = pd.DataFrame({'date': date, 'price': price})
df.date  = pd.to_datetime(df.date)

las = Lasso()
las.fit(df.date.values.reshape(-1, 1), df['price'].values.reshape(-1, 1))

date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
dfe = pd.DataFrame({'prediksi': date_predict})
dfe.prediksi = pd.to_datetime(dfe.prediksi)

coef = las.coef_
intercept = las.intercept_

las_predict = las.predict(df.date.values.astype(float).reshape(-1, 1))
las_pred_future = las.predict(dfe.prediksi.values.astype(float).reshape(-1, 1))
