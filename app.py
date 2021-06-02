from flask import Flask, render_template, request
from modelEmasLinear import lin_predict_future as el
from modelEmasHubber import hub_predict_future as eh
from modelEmasLasso import las_predict_future as ela
from modelDolarLinear import lin_predict_future as dl
from modelDolarHubber import hub_predict_future as dh
from modelDolarLasso import las_predict_future as dla
from modelPerakLinear import lin_predict_future as pl
from modelPerakHubber import hub_predict_future as ph
from modelPerakLasso import las_predict_future as pla

app = Flask(__name__)

@app.route("/")
def indexku():
    return render_template ('index.html')

@app.route("/index")
def index():
    return render_template ('index.html')

@app.route("/model")
def model():
    return render_template('model.html')

@app.route('/', methods=['POST'])
def proses():
    nama = request.form['nama']
    prediksi = request.form['prediksi']
    metode = request.form['metode']

    float = int
    if metode == "linear" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(el),3)))
    elif metode == "linear" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pl),3)))
    elif metode == "linear" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dl),3)))
    elif metode == "hubber" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(int(eh),3)))
    elif metode == "hubber" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ph),3)))
    elif metode == "hubber" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dh),3)))
    elif metode == "lasso" and prediksi == "emas":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(ela),3)))
    elif metode == "lasso" and prediksi == "perak":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(pla),3)))
    elif metode == "lasso" and prediksi == "dollar":
        return render_template('model.html', nama=nama, prediksi=prediksi, metode=metode, hasil='Rp. {}'.format(round(float(dla),3)))

if __name__ == "__main__":
    app.run(debug=True)