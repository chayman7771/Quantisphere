import random

NODES = ["A", "B", "C", "D", "E", "F", "G"]

def generate_trades(n=20):
    trades = []
    for _ in range(n):
        source, target = random.sample(NODES, 2)
        trades.append({
            "source": source,
            "target": target
        })
    return trades
