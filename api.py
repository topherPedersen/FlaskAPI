from flask import Flask
from endpoints import *

app = Flask(__name__)

@app.route('/')
def index_route():
    return index()