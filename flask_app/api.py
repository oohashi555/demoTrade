from flask import Blueprint, jsonify, request
import flask_app.models.user as user

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
