from flask import Flask, render_template, request
from .model.modelEmasLinear import lin_predict_future as el
from .model.modelEmasHubber import hub_predict_future as eh
from .model.modelEmasLasso import las_predict_future as ela
from .model.modelDolarLinear import lin_predict_future as dl
from .model.modelDolarHubber import hub_predict_future as dh
from .model.modelDolarLasso import las_predict_future as dla
from .model.modelPerakLinear import lin_predict_future as pl
from .model.modelPerakHubber import hub_predict_future as ph
from .model.modelPerakLasso import las_predict_future as pla
import base64
from io import BytesIO
from matplotlib.figure import Figure
import datetime
date = datetime.date.today() + datetime.timedelta(days=1)
app = Flask(__name__)

@app.route("/")
def indexku():
    return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/model")
def model():
    return render_template('model.html')

@app.route('/', methods=['POST'])
def proses():
    nama = request.form['nama']
    prediksi = request.form['prediksi']
    metode = request.form['metode']

    if metode == "linear" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(el),2)), date=str(date.strftime("%A"))+', '+str(date.day)+'/'+str(date.month)+'/'+str(date.year))
    elif metode == "linear" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pl),2)))
    elif metode == "linear" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dl),2)))
    elif metode == "hubber" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(int(eh),2)))
    elif metode == "hubber" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ph),2)))
    elif metode == "hubber" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dh),2)))
    elif metode == "lasso" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ela),2)))
    elif metode == "lasso" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pla),2)))
    elif metode == "lasso" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dla),2)))

@app.route('/lala')
def hello():
    from .model.modelEmasLinear import X, y, lin_predict, X_future, lin_predict_future
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.scatter(X, y)
    ax.plot(X, lin_predict)
    ax.plot(X_future, lin_predict_future)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == "__main__":
    app.run(debug=True)