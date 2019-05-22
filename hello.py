import flask as fl
from flask import Flask
#from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return fl.render_template('hello_world.html',name="Andi")