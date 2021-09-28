class Weather():
    def __init__(self, data):
        self.humidity = data["weather"]["hu"]
        self.wind_speed = data["weather"]["ws"]
        self.min_temp = data["weather"]["tp"]
    