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

## Project Structure

```
.
├── data/
│   └── synthetic_latencies.csv          # Edge list with latency in ms
├── logs/
│   └── run_YYYY_MM_DD_HHMMSS/           # Execution logs
├── src/
│   ├── config.py                        # Neo4j URI / creds
│   ├── graph_builder.py                 # Graph construction from CSV
│   ├── logger.py                        # Timestamped logging
│   ├── main.py                          # Entrypoint if needed
│   ├── router.py                        # Dijkstra's logic
│   ├── sandbox_app.py                   # Streamlit app
│   ├── trade_generator.py               # Placeholder for future path-based trade logic
│   ├── wait_for_neo4j.py                # Health check before boot
│   └── websocket_server.py              # Real-time communication server (future extension)
├── .env                                 # Secrets and configs
├── Dockerfile                           # Container spec
├── docker-compose.yml                   # Multi-service orchestration
├── Quantisphere.png                     # App logo or network diagram
├── README.md                            # You are here.
└── requirements.txt                     # Python deps
```

---

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/<your-username>/quantisphere.git
cd quantisphere
python -m venv env && source env/bin/activate
pip install -r requirements.txt
```

### 2. Run Locally

```bash
streamlit run src/sandbox_app.py
```

### 3. Run with Docker (Recommended)

```bash
docker-compose up --build
```

---

## Latency CSV Format

```csv
source,target,latency_ms
A,B,3
B,C,4
C,D,7
...
```

You can update `data/synthetic_latencies.csv` to match your custom infrastructure topology, or plug in your own database!

---

## Stack

- **Python 3.11+**
- **Streamlit**
- **NetworkX**
- **Neo4j (Optional)**
- **Docker + Railway**

---

## Author

**Cameron Hayman**  
Quant Dev | Systematic Trading Architect | Infra + Execution Strategy  
[LinkedIn](https://www.linkedin.com/in/cameron-hayman-27a7a6155)

> *"I don't just simulate routes — I optimize execution."*

---

## Open to Collaborate

Have a project in routing, execution, or latency-sensitive infrastructure?  
Open to freelance, interviews, or building a fund.
