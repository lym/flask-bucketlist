from flask import (
    abort,
    request,
    jsonify,
)
from flask.views import MethodView
from flask_api import status

from app.models import User


class UsersController(MethodView):
    """ Controller for the user resource """
    def post(self):
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        accept_terms = request.form.get('accept_terms')
        email = request.form.get('email')
        password = request.form.get('password')
        # username = request.form.get('username')
        if (len(email.split()) == 0 or
                len(password.split()) == 0 or accept_terms is None):
            abort(status.HTTP_400_BAD_REQUEST)
        # Check if user already exists
        if User.valid_user(email, password):
            print('User already exists!')
            abort(status.HTTP_400_BAD_REQUEST)
        User.create(
            email=email, password=password, first_name=first_name,
            last_name=last_name
        )
        print(request.form)
        res = status.HTTP_201_CREATED
        return jsonify(res)

    def get(self):
        users = jsonify(User.all())
        return users
