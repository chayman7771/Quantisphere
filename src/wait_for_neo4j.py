import time
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASS

def wait_for_neo4j(timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
            with driver.session() as session:
                session.run("RETURN 1")
            print("✅ Connected to Neo4j.")
            return True
        except Exception as e:
            print(f"⏳ Waiting for Neo4j... ({int(time.time() - start)}s)")
            time.sleep(2)
    print("❌ Failed to connect to Neo4j after timeout.")
    return False
