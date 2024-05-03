from flask import Blueprint, jsonify, request
import flask_app.models.user as user
import yfinance as yf

api = Blueprint('api', __name__)

@api.route('/user/list')
def user_list():
    data = user.select()
    return jsonify(data)

@api.route('/user/regist', methods=['POST'])
def user_regist():
    form = request.get_json()
    user.regist(form)
    data = user.select()
    return jsonify(data)

@api.route('/user/update', methods=['POST'])
def user_update():
    form = request.get_json()
    user.update(form)
    data = user.select()
    return jsonify(data)

@api.route('/user/delete', methods=['POST'])
def user_delete():
    form = request.get_json()
    user.delete(form)
    data = user.select()
    return jsonify(data)

@api.route('/getchart', methods=['POST'])
def get_chart():
    ticker = '9984.T'
    
    history = yf.download(ticker,period = '1y', interval = '1wk')
    axes = history.axes[0]
    open = history.Open.values
    high = history.High.values
    low = history.Low.values
    close = history.Close.values
    
    data = []
    for i in range(len(axes)):
        data.append({'x':axes[i].timestamp() * 1000, 'o':open[i], 'h':high[i], 'l':low[i], 'c':close[i]})
    
    return jsonify(data)
