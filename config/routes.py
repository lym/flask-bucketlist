from app.controllers import (
    HomeController,
    UsersController,
)
from config.application import App

App.add_url_rule('/home/', view_func=HomeController.as_view('home'))

App.add_url_rule(
    '/users/',
    view_func=UsersController.as_view('user-login')
)
