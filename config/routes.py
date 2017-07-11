from app.controllers import HomeController
from config.application import App

App.add_url_rule('/home/', view_func=HomeController.as_view('home'))
