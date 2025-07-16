import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.Waypoints import Waypoint
from core.Graph import build_graph
from core.routing import a_star_search
from core.heuristics import haversine_heuristic
from utils.plot import plot_route

# Coordenadas de ejemplo
waypoints = [
    Waypoint(38.9089, 1.4321, "Ibiza"),        # 0
    Waypoint(39.35, 1.85, "Waypoint 1"),         # 1
    Waypoint(39.95, 1.6, "Waypoint 2"),         # 2
    Waypoint(40.5, 1.95, "Valencia"),    # 3
    Waypoint(41, 2.1, "Tarragona"),    # 4
    Waypoint(41.3851, 2.1734, "Barcelona"),    # 5
]

# Construir el grafo
graph = build_graph(waypoints)

# Definir la ruta forzada pasando por ciertos puntos intermedios
route_points = [0, 1, 3, 4, 5]  # Orden deseado: Ibiza → Waypoint 1 → Valencia → Tarragona → Barcelona

# Calcular la ruta total concatenando segmentos
full_path = []
for i in range(len(route_points) - 1):
    segment = a_star_search(graph, route_points[i], route_points[i+1], waypoints, haversine_heuristic)
    if segment is None:
        raise ValueError(f"No se pudo encontrar ruta entre {route_points[i]} y {route_points[i+1]}")
    if i > 0:
        segment = segment[1:]  # evitar duplicados
    full_path.extend(segment)

print("Ruta forzada (índices):", full_path)
plot_route(waypoints, full_path)
