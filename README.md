[![PyPI - Python](https://img.shields.io/pypi/pyversions/iconsdk?logo=pypi)](https://pypi.org/project/iconsdk)

# Sahabat Ormas
## PricePredictions App
Aplikasi prediksi harga emas, harga perak, dan harga dolar ke rupiah besoknya menggunakan algoritma linear regression, ridge regression, dan lasso berbasis web application menggunakan python flask.

## Installation
```
#Save dataset of price on database in server/conf/database.ini
cd Price-Predictions-Flask
source bin/acticate
flask run
```

## Directory Structure
```text
└── PricePredictions
    ├── model
    │   ├── __init__.py
    │   ├── modelDolarRidge.py
    │   ├── modelDolarLasso.py
    │   ├── modelDolarLinear.py
    │   ├── modelEmasRidge.py
    │   ├── modelEmasLasso.py
    │   ├── modelEmasLinear.py
    │   ├── modelPerakRidge.py
    │   ├── modelPerakLasso.py 
    │   └── modelPerakLinear.py   
    ├── server
    │   ├── __init__.py
    │   ├── conf
    │   │    ├── __init__.py
    │   │    ├── database.ini
    │   │    └── setting.py
    │   ├── __init__.py
    │   └── connect.py
    ├── static
    │   ├── img
    │   │   ├── bagus.jpg
    │   │   ├── emas.jpg
    │   │   ├── fahri.jpg
    │   │   ├── logo.jpg
    │   │   ├── perak.jpg
    │   │   ├── reqi.jpg
    │   │   ├── sine.jpg
    │   │   └── uang.jpg
    │   └── style.css
    ├── templates
    │   ├── index.html
    │   └── model.html
    ├── __init__.py
    ├── app.py
    ├── requirements.txt
    └── README.md
```

## Result Of Prediction
![image](https://user-images.githubusercontent.com/69528812/188315392-de93820a-4dde-485d-9c22-85118d6a3d6f.png)

### Read blog about this App on link below
https://medium.com/data-folks-indonesia/build-machine-learning-models-prediction-with-linear-regression-ridge-regression-and-lasso-and-1e0a5bc4503c


