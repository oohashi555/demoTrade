from flask import Flask
from flask_cors import CORS
from pandas_datareader.famafrench import _URL_PREFIX
from flask_app.api import api
from flask import render_template

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')
app.config.from_object('flask_app.config')
app.register_blueprint(api, url_prefix='/api')
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

#データベース作成
import flask_app.db.init_database as init_db
init_db.create_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
