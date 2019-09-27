import requests as rq
from helpers import get_api_for

class Routes():
    home='20+Lain+Wackersberg'
    work_andi='15+Lochhamer Straße+Planegg'
    work_lena='47+Böhmerwaldstraße+Geretsried'
    base_url='https://maps.googleapis.com/maps/api/directions/json?'
    
    def __init__(self):
        self.information={}
        self.key=get_api_for("google")
        self.request()

    def request(self):
        url=self.base_url+'origin='+self.home+"$departure_time=now"+'&key='+self.key
        url_lena=url+'&destination='+self.work_lena
        url_andi=url+'&destination='+self.work_andi
        print(url)


new_route=Routes()
