from flask import Flask
from flask import render_template

app = Flask('bucketlist')


@app.route('/')
def home():
    return render_template('home.html', name='')


@app.route('/greeting/<username>')
def greet_user(username):
    return 'Hullo there, {}'.format(username.upper())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
