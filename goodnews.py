from feedparser import parse

class GoodNews():
    
    def __init__(self):
        self.news={}
        self.request()

    def request(self):
        parsed_feed=parse("https://www.positive.news/feed")
        for i in range(4):
            self.news["title"+str(i)]=parsed_feed["entries"][i]["title"]
