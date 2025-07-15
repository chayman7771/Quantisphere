import pandas as pd
import networkx as nx
import os

LATENCY_CSV = os.getenv("LATENCY_CSV", "data/synthetic_latencies.csv")

def build_graph():
    df = pd.read_csv(LATENCY_CSV)
    print("CSV Preview:\n", df.head())

    graph = nx.DiGraph()

    for _, row in df.iterrows():
        source = row["source"]
        target = row["target"]
        latency = row["latency_ms"]
        graph.add_edge(source, target, latency_ms=latency) 

    print("Nodes in graph:", list(graph.nodes()))
    print("Edges in graph:", list(graph.edges(data=True)))

    return graph

def find_optimal_path(graph, source, target):
    try:
        path = nx.shortest_path(graph, source=source, target=target, weight="latency_ms")

        total_latency = sum(
            graph[u][v]["latency_ms"] for u, v in zip(path[:-1], path[1:])
        )

        return {
            "path": path,
            "latency_ms": round(total_latency, 2),
            "hops": len(path) - 1
        }

    except nx.NetworkXNoPath:
        return {
            "path": None,
            "latency_ms": None,
            "hops": None
        }
