from flask import request, jsonify
from application.userland.controller import mod_userland
from application.core.utils.user_utils import UserUtils


@mod_userland.route('/sign_up', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    password = request.form.get('password')
    response = UserUtils.sign_up_user(email, password)
    return jsonify(response.__dict__)


@mod_userland.route('/sign_in', methods=['POST'])
def sign_in():
    email = request.form.get('email')
    password = request.form.get('password')
    response = UserUtils.sign_in_user(email, password)
    return jsonify(response.__dict__)
