import requests as rq

# Coordinates of Bad Tölz for the URL
lat = 47.761700
lon = 11.564570
#Dark Sky API is in secrets.txt, not to be pushed on Github
fstream=open("secrets.txt",'r')
API=fstream.read()

darksky_url=f"https://api.darksky.net/forecast/{API}/{lat},{lon}"

class Weather():
    def __init__(self):
        self.request()

    def request(self):
        r = rq.get(darksky_url)
        rj=r.json()
        self.information={}
        self.information["today"]={"temp":self.cel(rj["currently"]["temperature"]),"icon":rj["currently"]["icon"]}
        self.information

    #Convert Fahrenheit to Celsius
    def cel(self,temp):
        return (float(temp)-32)*(5./9.)
