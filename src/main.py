from wait_for_neo4j import wait_for_neo4j
from router import build_graph, find_optimal_path
from trade_generator import generate_trades
from graph_builder import push_to_neo4j

def main():
    if not wait_for_neo4j():
        return

    graph = build_graph()
    push_to_neo4j(graph)

    trades = generate_trades()
    for trade in trades:
        source = trade["source"]
        target = trade["target"]
        try:
            path = find_optimal_path(graph, source, target)
            print(f"Trade route from {source} to {target}: {path}")
        except Exception as e:
            print(f"Could not find route from {source} to {target}: {e}")

if __name__ == "__main__":
    main()
