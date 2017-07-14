from flask import render_template
from flask.views import View as FlaskController


class LandingPageController(FlaskController):
    """ Controller for the landing page"""
    def dispatch_request(self):
        return render_template(
            '_home_content.html', name='landingpage-template'
        )
