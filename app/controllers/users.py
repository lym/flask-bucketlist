from flask import (
    render_template,
    request,
)
from flask.views import View as FlaskController


class UsersController(FlaskController):
    """ Controller for the user resource """
    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('login.html', name='login-template')
        return render_template('register.html', name='user-registration')
