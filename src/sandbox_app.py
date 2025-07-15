import streamlit as st
from router import find_optimal_path, build_graph
from graph_builder import get_available_nodes
import pandas as pd

st.title("Quantisphere Routing Sandbox")
st.markdown("Select a home node and a destination node to simulate routing-based arbitrage.")

nodes = get_available_nodes()

home = st.selectbox("Home Node", nodes)
destination = st.selectbox("Destination Node", nodes)

# Display full latency matrix from CSV
st.markdown("### All Node-to-Node Latencies")
df = pd.read_csv("data/synthetic_latencies.csv")
st.dataframe(df)

if st.button("Run Path Simulation"):
    if home != destination:
        graph = build_graph()
        result = find_optimal_path(graph, home, destination)
        
        if result["path"] is not None:
            st.success(f"**Path:** {' → '.join(result['path'])}")
            st.info(f"**Total Latency:** {result['latency_ms']} ms")
            st.info(f"**Hops:** {result['hops']}")
        else:
            st.error("No path could be found between the selected nodes.")
    else:
        st.warning("Please choose different nodes.")
