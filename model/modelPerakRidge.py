from sklearn.linear_model import Ridge
import numpy as np
from ..server import data_perak as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
price = data["price"]

df = pd.DataFrame({'date': date, 'price': price})
df.date  = pd.to_datetime(df.date)

x = df.date.values.astype(float).reshape(-1, 1)
y = df['price'].values.reshape(-1, 1)

rid = Ridge(alpha=0.01)
rid.fit(x, y)

date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
dfe = pd.DataFrame({'prediksi': date_predict})
dfe.prediksi = pd.to_datetime(dfe.prediksi)

coef = rid.coef_
intercept = rid.intercept_

x_predict = dfe.prediksi.values.astype(float).reshape(-1, 1)

rid_predict = rid.predict(x)
rid_pred_future = rid.predict(x_predict)
