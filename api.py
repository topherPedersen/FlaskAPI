from flask import Flask
from routes import *

app = Flask(__name__)

@app.route('/')
def index_route():
    return index()

@app.route('/foo')
def foo_route():
    return foo()

@app.route('/bar')
def bar_route():
    return bar()

@app.route('/baz')
def baz_route():
    return baz()