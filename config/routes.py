from app.controllers import (
    HomeController,
    UsersController,
    LoginController,
    BucketlistsController,
    LandingPageController,
    ItemsController,
)
from config.application import App

App.add_url_rule('/', view_func=LandingPageController.as_view('landing_page'))
App.add_url_rule('/bucketlist/', view_func=HomeController.as_view('home'))

App.add_url_rule(
    '/users/',
    view_func=UsersController.as_view('user-login')
)

App.add_url_rule('/login/', view_func=LoginController.as_view('login'))
App.add_url_rule(
    '/bucketlists/',
    view_func=BucketlistsController.as_view('bucketlists')
)
App.add_url_rule(
    '/items/',
    view_func=ItemsController.as_view('items')
)
