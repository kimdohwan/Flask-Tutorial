from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi Flask'


@app.route('/test1/')
def test1():
    return 'test1'
