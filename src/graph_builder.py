import os
import time
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASS

def push_to_neo4j(graph):
    retries = 5
    wait_seconds = 5

    while retries > 0:
        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
            with driver.session() as session:
                print("✅ Connected to Neo4j. Clearing old graph.")
                session.run("MATCH (n) DETACH DELETE n")

                for node in graph.nodes:
                    session.run("MERGE (:Node {name: $name})", name=node)

                for u, v, data in graph.edges(data=True):
                    session.run("""
                        MATCH (a:Node {name: $u}), (b:Node {name: $v})
                        MERGE (a)-[:ROUTE {latency: $latency}]->(b)
                    """, u=u, v=v, latency=data.get("latency_ms", 0))

            driver.close()
            print("📡 Neo4j graph updated successfully.")
            return  # Exit after success
        except Exception as e:
            print(f"⚠️ Neo4j connection failed (attempts left: {retries - 1}): {e}")
            retries -= 1
            time.sleep(wait_seconds)

    print("❌ Failed to connect to Neo4j after multiple attempts.")
