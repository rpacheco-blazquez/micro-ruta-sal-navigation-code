import folium

def plot_route(waypoints, path):
    m = folium.Map(location=[waypoints[0].lat, waypoints[0].lon], zoom_start=6)
    for idx in path:
        wp = waypoints[idx]
        folium.Marker([wp.lat, wp.lon], popup=wp.name).add_to(m)
    folium.PolyLine([(waypoints[i].lat, waypoints[i].lon) for i in path], color="blue").add_to(m)
    m.save("route_map.html")

