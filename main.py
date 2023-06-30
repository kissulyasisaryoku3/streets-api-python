import osmnx as ox
import matplotlib.pyplot as plt

# Define the city
city = "Moscow, Russia"

# Create a street network graph
graph = ox.graph_from_place(city, network_type="drive")

# Visualize the graph
ox.plot_graph(graph)
plt.show()
