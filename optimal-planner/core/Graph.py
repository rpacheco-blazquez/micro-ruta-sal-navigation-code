import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import networkx as nx
from utils.geo import haversine

def build_graph(waypoints):
    G = nx.Graph()
    for i, wp1 in enumerate(waypoints):
        for j, wp2 in enumerate(waypoints):
            if i != j:
                dist = haversine(wp1.lat, wp1.lon, wp2.lat, wp2.lon)
                G.add_edge(i, j, weight=dist)
    return G
