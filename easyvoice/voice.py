class Voice:
    def __init__(self, obj):
        self.name = obj.get('name')
        self.description = obj.get('description')
        self.public_id = obj.get('public_id')
        self.url = obj.get('url')