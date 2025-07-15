import streamlit as st
from router import find_shortest_path  # or your relevant pathfinding func
from graph_builder import get_available_nodes  # assumes you have this

st.title("Quantisphere Routing Sandbox")

st.markdown("Select a home node and a destination node to simulate routing-based arbitrage.")

nodes = get_available_nodes()

home = st.selectbox("Home Node", nodes)
destination = st.selectbox("Destination Node", nodes)

if st.button("Run Path Simulation"):
    if home != destination:
        path, latency = find_shortest_path(home, destination)
        st.success(f"Path: {' → '.join(path)}")
        st.info(f"Total Latency: {latency} ms")
    else:
        st.warning("Please choose different nodes.")
