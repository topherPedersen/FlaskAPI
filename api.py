from flask import Flask
from routes import *

app = Flask(__name__)

@app.route('/')
def index_route():
    return index()