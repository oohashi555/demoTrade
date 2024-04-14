from flask import Flask

app = Flask(__name__)

app.config.from_object('flask_app.config')

import flask_app.views.login

import pandas as pd

excel = pd.read_excel('flask_app/data_j.xls')
tickers = excel['コード']
