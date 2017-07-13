from flask import (
    jsonify,
    request,
)
from flask.views import MethodView


class LoginController(MethodView):
    def post(self):
        email = request.form.get('email')
        passw = request.form.get('password')
        print('Email: {}\nPass: {}'.format(email, passw))
        res = {'email': email, 'status': 'OK'}
        return jsonify(res)
