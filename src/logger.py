import os
import csv
import datetime
from config import LOG_DIR

def save_logs(trades, results):
    timestamp = datetime.datetime.now().strftime("run_%Y_%m_%d_%H%M%S")
    run_dir = os.path.join(LOG_DIR, timestamp)
    os.makedirs(run_dir, exist_ok=True)

    with open(os.path.join(run_dir, "trades.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "target"])
        writer.writeheader()
        writer.writerows(trades)

    with open(os.path.join(run_dir, "results.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "target", "path", "latency_ms", "hops"])
        writer.writeheader()
        writer.writerows(results)

    successful = [r for r in results if r["latency_ms"] is not None]
    avg_latency = round(sum(r["latency_ms"] for r in successful) / len(successful), 2) if successful else None

    with open(os.path.join(run_dir, "summary.txt"), "w") as f:
        f.write(f"Total Trades: {len(trades)}\n")
        f.write(f"Successful Routes: {len(successful)}\n")
        f.write(f"Average Latency: {avg_latency} ms\n")
        f.write(f"Failed Routes: {len(trades) - len(successful)}\n")

    print(f"Logs saved to: {run_dir}")
