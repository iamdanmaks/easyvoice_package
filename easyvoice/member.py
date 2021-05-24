from dateutil.parser import *


class User:
    def __init__(self, obj):
        self.username = obj.get('username')
        self.email = obj.get('email')
        self.first_name = obj.get('first_name')
        self.last_name = obj.get('last_name')
        self.public_id = obj.get('public_id')
        self.registration_date = parse(obj.get('registration_date'))
        self.admin = obj.get('organization_admin')
