from sklearn.linear_model import Ridge
import numpy as np
from ..server import data_perak as data
import datetime
import pandas as pd
from sklearn import metrics
besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
date_predict = np.array([str(str(besok.year)+'-'+str(besok.month)+'-'+str(besok.day))])
price = data["price"]

def to_datetime(date):
    df = pd.DataFrame({'date': date})
    df.date  = pd.to_datetime(df.date)
    return df.date

def to_datetime_pred(date_predict):
    dfe = pd.DataFrame({'prediksi': date_predict})
    dfe.prediksi = pd.to_datetime(dfe.prediksi)
    return dfe.prediksi

x = to_datetime(date).values.astype(float).reshape(-1, 1)
x_predict = to_datetime_pred(date_predict).values.astype(float).reshape(-1, 1)
y = price.values.reshape(-1, 1)

rid = Ridge(alpha=0.01)
rid.fit(x, y)

def coef_intercept(rid):
    coef = rid.coef_
    intercept = rid.intercept_
    return coef, intercept

def prediction(rid):
    rid_predict = rid.predict(x)
    rid_pred_future = rid.predict(x_predict)
    return rid_predict, rid_pred_future

coef, intercept = coef_intercept(rid)
rid_predict, rid_pred_future = prediction(rid)

rmse = np.sqrt(metrics.mean_squared_error(y, rid_predict))