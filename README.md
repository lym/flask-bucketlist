# Bucketlist
This project is an implementation of a bucketlist app. This project is
being developed primarily as a pet project to help me understand how the
Flask Python framework works.

## Features
- User signup
- User session management
- Bucketlist creation
- Bucketlist editing
- Bucketlist deletion
- Bucketlist sharing
- Adding items to bucket lists
- Removing items from bucketlists
- Editing bucke list contents

## Usage
Launch the app server with:

    $ ./run_app.py

and point your web browser to `http://0.0.0.0:5000/`
### Views
- Bucket list create view `http://0.0.0.0:5000/#bucketlist_create`
- Bucketlists index view `http://0.0.0.0:5000/#bucketlists_index`
- Bucket lists show view `http://0.0.0.0:5000/#bucketlist`

## Colaboration
- clone the repository
- Install requirements with `pip install -r requirements.txt`
- Run tests
- Create feature brunch on your developer machine
- Push the branch to this repository and create a pull request

### Running Tests
This project leverages the [pytest](https://docs.pytest.org/en/latest/contents.html)
testing framework so tests can be run with:

    $ cd [project root]
    $ PYTHONPATH=. pytest -r Pf --cov=app


## Coding Style Rules
- [HTML and CSS](http://codeguide.co/)
- [EcmaScript/JavaScript](https://github.com/airbnb/javascript)
- [Python](https://www.python.org/dev/peps/pep-0008/)
