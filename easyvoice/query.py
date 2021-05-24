import requests
from dateutil.parser import *


class Query:
    def __init__(self, obj):
        self.text = obj.get('text')
        self.language = obj.get('lang')
        self.date = parse(obj.get('date'))
        self.time_processed = obj.get('time_processed')
        self.voice = obj.get('voice')
        self.url = obj.get('url')

    def download(self, local_filename):
        with requests.get(self.url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
