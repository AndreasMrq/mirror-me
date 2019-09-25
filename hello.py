from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from weather import Weather
from threading import Lock

#from flask import render_template
app = Flask(__name__)
socketio=SocketIO(app)
wt=Weather()

thread = None
thread_lock = Lock()

def weather_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(300)
        wt.request()
        socketio.emit('weather_event', {'content': count})


@app.route('/')
def hello_world():
    return render_template('hello_world.html',name="Andi")

@socketio.on('connect')
def connect():       
    emit('weather_event',wt.information["today"])
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(weather_thread)



if __name__== '__main__':
    socketio.run(app)

