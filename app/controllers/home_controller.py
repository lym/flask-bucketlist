from flask import render_template
from flask.views import View as FlaskController


class HomeController(FlaskController):
    """ Controller for the home page, the page that non-logged in users see """
    def dispatch_request(self):
        return render_template('home.html', name='')
