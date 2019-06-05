import flask as fl
from threading import Thread
from flask import Flask
from flask_socketio import SocketIO, emit
from weatherThread import WeatherThread

#from flask import render_template
app = Flask(__name__)
weather_thread=Thread()
socketio=SocketIO(app)

@app.route('/')
def hello_world():
    return fl.render_template('hello_world.html',name="Andi")

@socketio.on('connect')
def connect():       
    #referenziert die globale Variable weather_thread
    global weather_thread
    #verhindert,dass mehrere weather_threads gleichzeitig gestartet werden
    if not weather_thread.is_alive():
        weather_thread=WeatherThread()
        weather_thread.start()