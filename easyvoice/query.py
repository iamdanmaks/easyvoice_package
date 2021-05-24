from dateutil.parser import *


class Query:
    def __init__(self, obj):
        self.text = obj.get('text')
        self.language = obj.get('lang')
        self.date = parse(obj.get('date'))

    def download(self):
        pass
