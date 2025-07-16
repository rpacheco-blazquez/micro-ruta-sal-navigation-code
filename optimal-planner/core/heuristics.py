
from utils.geo import haversine

def haversine_heuristic(wp1, wp2):
    return haversine(wp1.lat, wp1.lon, wp2.lat, wp2.lon)
