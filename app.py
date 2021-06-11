from flask import Flask, render_template, request
from .model.modelEmasLinear import lin_pred_future as el
from .model.modelDolarLinear import lin_pred_future as dl
from .model.modelPerakLinear import lin_pred_future as pl
#from .model.modelEmasHubber import hub_pred_future as eh
#from .model.modelDolarHubber import hub_pred_future as dh
#from .model.modelPerakHubber import hub_pred_future as ph
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
    #from .model.modelEmasHubber import coef as ceh, intercept as ieh
    #from .model.modelDolarHubber import coef as cdh, intercept as idh
    # from .model.modelPerakHubber import coef as cph, intercept as iph
    from .model.modelDolarLasso import coef as cdla, intercept as idla
    from .model.modelEmasLasso import coef as cela, intercept as iela
    from .model.modelPerakLasso import coef as cpla, intercept as ipla

    nama = request.form['nama']
    prediksi = request.form['prediksi']
    metode = request.form['metode']

    if metode == "Linear Regression" and prediksi == "Harga Emas":
        #menampilkan grafik
        from .model.modelEmasLinear import df, dfe, lin_predict, lin_pred_future
        #inisisasi variabel fig untuk mengatur ukuran plot
        fig = Figure(figsize=(10, 8))
        #inisiasi variable ax untuk plot
        ax = fig.subplots()
        #untuk menampilkan harga di plot menggunakan scatter plot
        ax.scatter(df.date, df['price'], color='green')
        #untuk menampikan garis linear
        ax.plot(df.date, lin_predict)
        #untuk menampilkan garis linear prediksi besoknya
        ax.plot(dfe.prediksi, lin_pred_future)
        #untuk memiringkan labels
        ax.tick_params(labelrotation=30)
        #keterangan di harga
        ax.set_ylabel("Dalam Rupiah")
        #keterangan di tanggal
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        #judul plot linear
        ax.legend(['Garis linear regression'])
        #judul grafik
        ax.set_title("Grafik Linear Regression Prediksi Harga Emas")

        #untuk mengsave grafik dalam format png
        buf = BytesIO()
        fig.savefig(buf, format="png")
        #menyimpan grafik dalam variable data untuk dibaca di html
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(el),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cel, intercept=iel)

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
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pl),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cpl, intercept=ipl)

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
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dl),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdl, intercept=idl)

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
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ela),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cela, intercept=iela)

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
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pla),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cpla, intercept=ipla)

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
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dla),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdla, intercept=idla)

    """
    elif metode == "Hubber Regressor" and prediksi == "Harga Emas":
        from .model.modelEmasHubber import df, dfe, hub_predict, hub_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, hub_predict)
        ax.plot(dfe.prediksi, hub_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Huber Regressor'])
        ax.set_title("Grafik Huber Regressor Prediksi Harga Emas")

        buf = BytesIO()
        fig.savefig(buf, format="png")
    
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(int(eh),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=ceh, intercept=ieh)
        
    elif metode == "Hubber Regressor" and prediksi == "Harga Perak":
        from .model.modelPerakHubber import df, dfe, hub_predict, hub_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, hub_predict)
        ax.plot(dfe.prediksi, hub_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Huber Regressor'])
        ax.set_title("Grafik Huber Regressor Prediksi Harga Perak")
    
        buf = BytesIO()
        fig.savefig(buf, format="png")
    
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ph),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cph, intercept=iph)
        
    elif metode == "Hubber Regressor" and prediksi == "Harga Dollar":
        from .model.modelDolarHubber import df, dfe, hub_predict, hub_pred_future
        fig = Figure(figsize=(10, 8))
        ax = fig.subplots()
        ax.scatter(df.date, df['price'], color='green')
        ax.plot(df.date, hub_predict)
        ax.plot(dfe.prediksi, hub_pred_future)
        ax.tick_params(labelrotation=30)
        ax.set_ylabel("Dalam Rupiah")
        ax.set_xlabel("Tanggal (jangka 14 hari)")
        ax.legend(['Garis Huber Regressor'])
        ax.set_title("Grafik Huber Regressor Prediksi Harga Dolar")

        buf = BytesIO()
        fig.savefig(buf, format="png")

        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template('model.html', data=data, nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dh),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year), coef=cdh, intercept=idh)
    """

if __name__ == "__main__":
    app.run(debug=True)