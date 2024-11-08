import streamlit as st
import plotly.graph_objs as go
import numpy as np

def create_graph(V, E):
    adjacency_list = [[] for _ in range(V)]
    for edge in E:
        adjacency_list[edge[0]].append((edge[1], edge[2]))
        adjacency_list[edge[1]].append((edge[0], edge[2]))
    return adjacency_list

def dijkstra(graph, V, src):
    vis = [0] * V
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        mn = -1
        for j in range(V):
            if not vis[j] and (mn == -1 or dist[j] < dist[mn]):
                mn = j

        vis[mn] = 1
        for edge in graph[mn]:
            if not vis[edge[0]] and dist[edge[0]] > dist[mn] + edge[1]:
                dist[edge[0]] = dist[mn] + edge[1]

    return dist

# Streamlit UI
st.title("Dijkstra's Algorithm Visualizer")

# Input for number of vertices and edges
V = st.number_input("Number of vertices:", min_value=1, value=5)
num_edges = st.number_input("Number of edges:", min_value=0, value=4)

edges = []
for i in range(num_edges):
    from_node = st.number_input(f'From Node {i+1}:', min_value=0, max_value=V-1)
    to_node = st.number_input(f'To Node {i+1}:', min_value=0, max_value=V-1)
    weight = st.number_input(f'Weight {i+1}:', min_value=1, value=1)
    edges.append((from_node, to_node, weight))

# Display graph when button is clicked
if st.button("Visualize Graph"):
    graph = create_graph(V, edges)
    source = st.number_input("Select source vertex for Dijkstra's algorithm:", min_value=0, max_value=V-1)
    distances = dijkstra(graph, V, source)

    # Prepare data for Plotly
    positions = {i: (np.cos(2 * np.pi * i / V), np.sin(2 * np.pi * i / V)) for i in range(V)}
    edge_x = []
    edge_y = []
    for edge in edges:
        x0, y0 = positions[edge[0]]
        x1, y1 = positions[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = [positions[i][0] for i in range(V)]
    node_y = [positions[i][1] for i in range(V)]

    # Create the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=2, color='gray'), hoverinfo='none'))
    fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers+text', 
                             text=[f'Node {i}<br>Distance: {distances[i]}' for i in range(V)],
                             textposition="top center",
                             marker=dict(size=10, color='blue'), 
                             hoverinfo='text'))

    fig.update_layout(title='Graph Visualization', showlegend=False, 
                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      height=600)

    st.plotly_chart(fig)

    st.write("Shortest distances from source vertex:")
    for idx, d in enumerate(distances):
        st.write(f"Vertex {idx}: Distance = {d}")
