from sklearn.linear_model import Ridge
import numpy as np
from ..server import data_dolar as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
price = data["price"]

df = pd.DataFrame({'date': date, 'price': price})
df.date  = pd.to_datetime(df.date)

rid = Ridge(alpha=0.01)
rid.fit(df.date.values.reshape(-1, 1), df['price'].values.reshape(-1, 1))

date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
dfe = pd.DataFrame({'prediksi': date_predict})
dfe.prediksi = pd.to_datetime(dfe.prediksi)

coef = rid.coef_
intercept = rid.intercept_

rid_predict = rid.predict(df.date.values.astype(float).reshape(-1, 1))
rid_pred_future = rid.predict(dfe.prediksi.values.astype(float).reshape(-1, 1))
