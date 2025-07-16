
class Waypoint:
    def __init__(self, lat, lon, name=""):
        self.lat = lat
        self.lon = lon
        self.name = name

    def __repr__(self):
        return f"{self.name} ({self.lat}, {self.lon})"
