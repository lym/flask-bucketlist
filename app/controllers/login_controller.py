from flask import (
    abort,
    jsonify,
    request,
)
from flask.views import MethodView

from app.models import User


class LoginController(MethodView):
    def post(self):
        email = request.form.get('email')
        passw = request.form.get('password')
        if User.valid_user(email, passw):
            res = {'email': email, 'status': 'OK'}
            return jsonify(res)

        print('Email: {}\nPass: {}'.format(email, passw))
        abort(401)
