import pandas as pd
import networkx as nx
import os

LATENCY_CSV = os.getenv("LATENCY_CSV", "data/synthetic_latencies.csv")

def build_graph():
    df = pd.read_csv(LATENCY_CSV)
    print("📄 CSV Preview:\n", df.head())

    graph = nx.DiGraph()

    for _, row in df.iterrows():
        source = row["source"]
        target = row["target"]
        latency = row["latency_ms"]
        graph.add_edge(source, target, latency=latency)

    print("🧠 Nodes in graph:", list(graph.nodes()))
    print("🔗 Edges in graph:", list(graph.edges(data=True)))

    return graph


def find_optimal_path(graph, source, target):
    try:
        path = nx.dijkstra_path(graph, source, target, weight='latency_ms')
        latency = nx.dijkstra_path_length(graph, source, target, weight='latency_ms')
        return {
            "path": " → ".join(path),
            "latency_ms": round(latency, 2),
            "hops": len(path) - 1
        }
    except nx.NetworkXNoPath:
        return {
            "path": None,
            "latency_ms": None,
            "hops": None
        }
