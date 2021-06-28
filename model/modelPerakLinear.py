from sklearn.linear_model import LinearRegression
import numpy as np
from ..server import data_perak as data
import datetime
import pandas as pd

besok = datetime.date.today() + datetime.timedelta(days=1)

date = data["date"]
date_predict = np.array([str(str(besok.year)+'-0'+str(besok.month)+'-'+str(besok.day))])
price = data["price"]

def to_datetime(date):
    df = pd.DataFrame({'date': date})
    df.date = pd.to_datetime(df.date)
    return df.date

def to_datetime_pred(date_predict):
    dfe = pd.DataFrame({'prediksi': date_predict})
    dfe.prediksi = pd.to_datetime(dfe.prediksi)
    return dfe.prediksi

x = to_datetime(date).values.astype(float).reshape(-1, 1)
x_predict = to_datetime_pred(date_predict).values.astype(float).reshape(-1, 1)
y = price.values.reshape(-1, 1)

lin = LinearRegression()
lin.fit(x, y)

def coef_intercept(lin):
    coef = lin.coef_
    intercept = lin.intercept_
    return coef, intercept

def prediction(lin):
    lin_predict = lin.predict(x)
    lin_pred_future = lin.predict(x_predict)
    return lin_predict, lin_pred_future

coef, intercept = coef_intercept(lin)
lin_predict, lin_pred_future = prediction(lin)