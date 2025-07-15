
import os

# General Config
RANDOM_SEED = 42
NUM_TRADES = 20
LATENCY_THRESHOLD_MS = 300

# File paths
LATENCY_CSV = "data/synthetic_latencies.csv"
LOG_DIR = "logs"

# Neo4j Config (for visual only)
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASS", "password")

# WebSocket config
WS_PORT = 6789
    