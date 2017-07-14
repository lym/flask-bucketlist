from flask import (
    request,
    jsonify,
)
from flask.views import MethodView
from flask.ext.api import status

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
        if accept_terms is None:
            content = 'You must agree to the terms to use the service'
            status_code = status.HTTP_400_BAD_REQUEST
            res = {'content': content, 'status': status_code}
            return jsonify(res)
        User.create(
            email=email, password=password, first_name=first_name,
            last_name=last_name
        )
        print(request.form)
        res = {'Status': 'OK'}
        return jsonify(res)

    def get(self):
        users = jsonify(User.all())
        return users
