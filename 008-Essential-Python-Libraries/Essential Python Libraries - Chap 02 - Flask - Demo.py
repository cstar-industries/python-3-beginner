from flask import Flask, request
from random import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/echo')
def echo():
    msg = request.args.get('msg')
    res = f'<html><body><h1>{msg}</h1></html>'
    return res


@app.route('/echo', methods=['POST'])
def echo_post():
    msg = request.form.get('msg')
    res = f'<html><body><h1>{msg}</h1></html>'
    return res


@app.route('/echo.json', methods=['POST'])
def echo_json():
    msg = request.json.get('msg')
    res = {'echo': msg}
    return res


@app.route('/random_numbers')
def random_numbers():
    try:
        count = int(request.args.get('count'))
    except:
        count = 10
    return {'numbers': [random() for _ in range(count)]}
