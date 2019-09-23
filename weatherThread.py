from weather import Weather
from flask_socketio import SocketIO, emit
import threading
import time

#Start a separate thread, collecting the weather data
class WeatherThread(threading.Thread):
    
    def __init__(self):
        self.weather_info=Weather()
        self.reload_time=1800
        #Variable that may stop the thread
        self.thread_stop_event = threading.Event()
        super().__init__()

    def run(self):
        while not self.thread_stop_event.is_set():
            # Request new weather data
            self.weather_info.request()
            # emit socket data to sockets listening on 'weather'
            #emit('weather',self.weather_info.information)
            emit('weather',{"data":"Funktioniert! "})
            # Wait for 30 minutes
            time.sleep(self.reload_time)