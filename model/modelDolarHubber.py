from sklearn.linear_model import HuberRegressor
import numpy as np
from ..server import data_dolar as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
price = data["price"]

df = pd.DataFrame({'date': date, 'price': price})
df.date  = pd.to_datetime(df.date)

hub = HuberRegressor()
hub.fit(df.date.values.reshape(-1, 1), df['price'].values.reshape(-1, 1))

date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
dfe = pd.DataFrame({'prediksi': date_predict})
dfe.prediksi = pd.to_datetime(dfe.prediksi)

coef = hub.coef_
intercept = hub.intercept_

hub_predict = hub.predict(df.date.values.astype(float).reshape(-1, 1))
hub_pred_future = hub.predict(dfe.prediksi.values.astype(float).reshape(-1, 1))
