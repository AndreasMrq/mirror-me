from flask import Flask, render_template
from flask_socketio import SocketIO, emit,send

app = Flask(__name__)
socketio=SocketIO(app)

@app.route('/')
def index():
    return render_template('hello_world.html',name="Andi")

@socketio.on('connect')
def connect():
    emit('WITNESSME',{"data":"INDIVIDUAL"})
    print("CONNECTED!!!")
    #send({"data":"Hallo"})
    pass

if __name__== '__main__':
    socketio.run(app)