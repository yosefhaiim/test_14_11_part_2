from models.device_info import device_info
from models.location import location
from models.sentence import sentence



# "email": "jeremy37@example.org",
# "username": "jonesalejandra",
# "ip_address": "215.67.111.124",
# "created_at": "2024-10-15T05:29:13.450066",



class email_model(location, sentence, device_info):
    def __init__(self, email, username, ip_address, created_at, latitude, longitude, city, country):
        super().__init__(latitude, longitude, city, country)
        self.email = email
        self.username = username
        self.ip_address = ip_address
        self.created_at = created_at
        self.device_info = device_info
        self.sentence = sentence
        self.location = location