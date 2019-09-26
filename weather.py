import requests as rq

# Coordinates of Bad Tölz for the URL
lat = 47.761700
lon = 11.564570
#Dark Sky API is in secrets.txt, not to be pushed on Github
fstream=open("secrets.txt",'r')
API=fstream.read()

darksky_url=f"https://api.darksky.net/forecast/{API}/{lat},{lon}?units=auto"

class Weather():
    def __init__(self):
        self.information={}
        self.request()

    def request(self):
        r = rq.get(darksky_url)
        rj=r.json()
        today=rj["daily"]["data"][0]
        tomorrow=rj["daily"]["data"][1]
        self.information["today"]={"tempMax":today["temperatureHigh"],
                                   "tempMin":today["temperatureLow"],
                                   "icon":today["icon"]}
        self.information["tomorrow"]={"tempMax":tomorrow["temperatureHigh"],
                                      "tempMin":tomorrow["temperatureLow"],
                                      "icon":tomorrow["icon"]}
