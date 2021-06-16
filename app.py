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

date = datetime.date.today() + datetime.timedelta(days=1)
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
        from .model.modelEmasLinear import df, dfe, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, lin_predict)
        ax.plot(dfe.prediksi, lin_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(el)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cel, intercept=iel)

    elif metode == "Linear Regression" and prediksi == "Harga Perak":
        from .model.modelPerakLinear import df, dfe, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, lin_predict)
        ax.plot(dfe.prediksi, lin_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Perak")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pl)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cpl, intercept=ipl)

    elif metode == "Linear Regression" and prediksi == "Harga Dollar":
        from .model.modelDolarLinear import df, dfe, lin_predict, lin_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, lin_predict)
        ax.plot(dfe.prediksi, lin_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis linear regression'])
        ax.set_title("Grafik Linear Regression Prediksi Harga Dollar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dl)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdl, intercept=idl)

    elif metode == "Lasso" and prediksi == "Harga Emas":
        from .model.modelEmasLasso import df, dfe, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, las_predict)
        ax.plot(dfe.prediksi, las_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso'])
        ax.set_title("Grafik Lasso Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(ela)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cela, intercept=iela)

    elif metode == "Lasso" and prediksi == "Harga Perak":
        from .model.modelPerakLasso import df, dfe, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, las_predict)
        ax.plot(dfe.prediksi, las_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso'])
        ax.set_title("Grafik Lasso Prediksi Harga Perak")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pla)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cpla, intercept=ipla)

    elif metode == "Lasso" and prediksi == "Harga Dollar":
        from .model.modelDolarLasso import df, dfe, las_predict, las_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, las_predict)
        ax.plot(dfe.prediksi, las_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Lasso'])
        ax.set_title("Grafik Lasso Prediksi Harga Dollar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dla)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdla, intercept=idla)


    elif metode == "Ridge Regression" and prediksi == "Harga Emas":
        from .model.modelEmasRidge import df, dfe, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, rid_predict)
        ax.plot(dfe.prediksi, rid_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")
    
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(er)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cer, intercept=ier)
        
    elif metode == "Ridge Regression" and prediksi == "Harga Perak":
        from .model.modelPerakRidge import df, dfe, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, rid_predict)
        ax.plot(dfe.prediksi, rid_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Perak")
    
        buf = BytesIO()
        fig.savefig(buf, format="png")
    
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(pr)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cpr, intercept=ipr)
        
    elif metode == "Ridge Regression" and prediksi == "Harga Dollar":
        from .model.modelDolarRidge import df, dfe, rid_predict, rid_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, rid_predict)
        ax.plot(dfe.prediksi, rid_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Ridge Regression'])
        ax.set_title("Grafik Ridge Regression Prediksi Harga Dolar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(float(dr)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdr, intercept=idr)


if __name__ == "__main__":
    app.run(debug=True)