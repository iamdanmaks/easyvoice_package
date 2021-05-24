import base64
import os
import requests

from datetime import datetime

from .member import User
from .voice import Voice
from .query import Query


class EasyVoice:
    __BASE_URL = 'http://34.118.9.73:8080/'
    __voice_fetch_datetime = None
    __query_fetch_datetime = None
    
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get('EASYVOICE_KEY')
        
        self.__api_key = 'Bearer ' + api_key

        organization_info = requests.get(
            self.__BASE_URL + 'api/organization/',
            headers={
                'Authorization': self.__api_key
            }
        ).json()

        self.name = organization_info.get('name')
        self.description = organization_info.get('description')
        self.registration_date = organization_info.get('registration_date')
        self._public_id = organization_info.get('public_id')
        self._demo = organization_info.get('demo')
        self._tokens_left = organization_info.get('tokens_left')
        self._members = []

        for u in organization_info.get('users'):
            self._members.append(User(u))

    def to_base64(file):
        with open(file, 'rb') as f:
            return base64.b64encode(f)
    
    def add_voice(self, name, desciption, file):
        data = requests.post(
            self.__BASE_URL + 'api/voice/',
            data={
                'name': name,
                'description': desciption,
                'file': self.to_base64(file)
            }
        ).json()
        return self.get_voices()

    def timedelta(self, date):
        current_date = datetime.utcnow()
        return (current_date - date).total_seconds() >= 3600

    def get_voices(self):
        if self.__voice_fetch_datetime is None or self.timedelta(self.__voice_fetch_datetime):
            voices_info = requests.get(
                self.__BASE_URL + 'api/voice/',
                headers={
                    'Authorization': self.__api_key
                }
            ).json()
            self.voices = []
            for v in voices_info:
                self.voices.append(Voice(v))
            
            self.voices = list(set(self.voices))
            
            self.__voice_fetch_datetime = datetime.utcnow()
            
        return self.voices

    def get_voicing_queries(self):
        if self.__query_fetch_datetime is None or self.timedelta(self.__query_fetch_datetime):
            queries_info = requests.get(
                self.__BASE_URL + f'api/query/?organization={self.public_id}',
                headers={
                    'Authorization': self.__api_key
                }
            ).json()
            self.queries = []
            for q in queries_info:
                self.queries.append(Query(q))
            
            self.__query_fetch_datetime = datetime.utcnow()
            
        return self.queries

    def voice_text(self, text, voice):
        pass

    def voice_text_file(self, file, voice):
        pass
    
    def download_query_result(self, public_id):
        pass
