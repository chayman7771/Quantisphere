# Quantisphere Routing Sandbox

A real-time routing-based arbitrage simulator built using NetworkX, Neo4j, and Streamlit. Designed to visually and computationally demonstrate optimal latency paths across synthetic or real financial networks.

---

## Project Overview

The **Quantisphere Routing Sandbox** simulates microsecond-level arbitrage routing by finding the lowest-latency path between nodes on a graph. This project visualizes the shortest path between two nodes using Dijkstra’s algorithm and supports real-time updates via Neo4j.

Live App: [quantisphere-production.up.railway.app](https://quantisphere-production.up.railway.app)

---

## Features

- **Network Graph Construction**: Automatically builds directed graphs from a CSV of latency edges.
- **Optimal Pathfinding**: Uses Dijkstra’s algorithm to compute the shortest-latency path.
- **Live Latency Matrix**: Displays all node-to-node connections and their latencies in milliseconds.
- **Path Simulation Output**:
  - Optimal Path
  - Total Latency (ms)
  - Number of Hops
- **Neo4j Integration**: Graph data is stored and visualized using Neo4j for advanced analytics.

---

## Tech Stack

- `Python`
- `Streamlit`
- `NetworkX`
- `Pandas`
- `Neo4j`
- `Railway` (for cloud hosting)

---

## File Structure

```bash
quantisphere/
├── data/
│   └── synthetic_latencies.csv     # Latency graph data
├── graph_builder.py                # Builds the NetworkX graph from CSV
├── router.py                       # Pathfinding logic using Dijkstra
├── neo4j_push.py                   # Pushes NetworkX graph to Neo4j
├── app.py                          # Streamlit frontend
├── config.py                       # Neo4j connection info (env-driven)
├── requirements.txt                # Python deps
└── README.md
