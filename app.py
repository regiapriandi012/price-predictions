from flask import Flask, render_template, request
from .model.modelEmasLinear import lin_pred_future as el
from .model.modelDolarLinear import lin_pred_future as dl
from .model.modelPerakLinear import lin_pred_future as pl
from .model.modelEmasRidge import rid_pred_future as er
from .model.modelDolarRidge import rid_pred_future as dr
from .model.modelPerakRidge import rid_pred_future as pr
from .model.modelDolarLasso import las_pred_future as dla
from .model.modelPerakLasso import las_pred_future as pla
from .model.modelEmasLasso import las_pred_future as ela
import base64
from io import BytesIO
from matplotlib.figure import Figure
import datetime

besok = datetime.date.today() + datetime.timedelta(days=1)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def indexx():
    return render_template('index.html')

@app.route("/model")
def model():
    return render_template('model.html')

@app.route('/', methods=['POST'])
def modelll():
    from .model.modelEmasLinear import coef as cel, intercept as iel
    from .model.modelPerakLinear import coef as cpl, intercept as ipl
    from .model.modelDolarLinear import coef as cdl, intercept as idl
    from .model.modelEmasRidge import coef as cer, intercept as ier
    from .model.modelDolarRidge import coef as cdr, intercept as idr
    from .model.modelPerakRidge import coef as cpr, intercept as ipr
    from .model.modelDolarLasso import coef as cdla, intercept as idla
    from .model.modelEmasLasso import coef as cela, intercept as iela
    from .model.modelPerakLasso import coef as cpla, intercept as ipla

    prediksi = request.form['prediksi']
    metode = request.form['metode']

    if metode == "Linear Regression" and prediksi == "Harga Emas":
        from .model.modelEmasLinear import date, date_predict, y, to_datetime, to_datetime_pred, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), lin_predict)
        ax.scatter(to_datetime_pred(date_predict), lin_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(el)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cel), intercept=float(iel))

    elif metode == "Linear Regression" and prediksi == "Harga Perak":
        from .model.modelPerakLinear import date, date_predict, y, to_datetime, to_datetime_pred, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), lin_predict)
        ax.scatter(to_datetime_pred(date_predict), lin_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Perak")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pl)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cpl), intercept=float(ipl))

    elif metode == "Linear Regression" and prediksi == "Harga Dollar":
        from .model.modelDolarLinear import date, date_predict, y, to_datetime, to_datetime_pred, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), lin_predict)
        ax.scatter(to_datetime_pred(date_predict), lin_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Dollar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dl)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cdl), intercept=float(idl))

    elif metode == "Lasso" and prediksi == "Harga Emas":
        from .model.modelEmasLasso import date, date_predict, y, to_datetime, to_datetime_pred, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), las_predict)
        ax.scatter(to_datetime_pred(date_predict), las_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Lasso Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(ela)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cela), intercept=float(iela))

    elif metode == "Lasso" and prediksi == "Harga Perak":
        from .model.modelPerakLasso import date, date_predict, y, to_datetime, to_datetime_pred, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), las_predict)
        ax.scatter(to_datetime_pred(date_predict), las_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Lasso Prediksi Harga Perak")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pla)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cpla), intercept=float(ipla))

    elif metode == "Lasso" and prediksi == "Harga Dollar":
        from .model.modelDolarLasso import date, date_predict, y, to_datetime, to_datetime_pred, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), las_predict)
        ax.scatter(to_datetime_pred(date_predict), las_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Lasso Prediksi Harga Dollar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dla)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cdla), intercept=float(idla))


    elif metode == "Ridge Regression" and prediksi == "Harga Emas":
        from .model.modelEmasRidge import date, date_predict, y, to_datetime, to_datetime_pred, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), rid_predict)
        ax.scatter(to_datetime_pred(date_predict), rid_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(er)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cer), intercept=float(ier))

    elif metode == "Ridge Regression" and prediksi == "Harga Perak":
        from .model.modelPerakRidge import date, date_predict, y, to_datetime, to_datetime_pred, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), rid_predict)
        ax.scatter(to_datetime_pred(date_predict), rid_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Perak")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pr)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cpr), intercept=float(ipr))

    elif metode == "Ridge Regression" and prediksi == "Harga Dollar":
        from .model.modelDolarRidge import date, date_predict, y, to_datetime, to_datetime_pred, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(to_datetime(date), y, color='green')
        ax.plot(to_datetime(date), rid_predict)
        ax.scatter(to_datetime_pred(date_predict), rid_pred_future, color="blue")
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression', 'Harga', 'Prediksi'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Dolar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dr)), date=str(besok.strftime("%A"))+', '+str(besok.day)+'/'+str(besok.month)+'/'+str(besok.year), coef=float(cdr), intercept=float(idr))

if __name__ == "__main__":
    app.run(debug=True)