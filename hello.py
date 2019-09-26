from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from weather import Weather
from goodnews import GoodNews
from threading import Lock


#from flask import render_template
app = Flask(__name__)
socketio=SocketIO(app)
wt=Weather()
news=GoodNews()

weather_thread = None
thread_lock=Lock()

news_thread = None


def background_weather_thread():
    while True:
        #Make a weather request every hour
        wt.request()
        socketio.emit('weather_event', wt.information)
        socketio.sleep(3000)

def background_news_thread():
    while True:
        #Make a weather request every hour
        news.request()
        socketio.emit('news_event', news.news)
        socketio.sleep(43200)

@app.route('/')
def hello_world():
    return render_template('hello_world.html',name="Andi")

@socketio.on('connect')
def connect():       
    global weather_thread
    with thread_lock:
        if weather_thread is None:
            weather_thread = socketio.start_background_task(background_weather_thread)
            socketio.start_background_task(background_news_thread)


if __name__== '__main__':
    socketio.run(app)

