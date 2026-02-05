from neo4j import GraphDatabase
import json

# 🔹 Neo4j connection (MATCH YOUR RUNNING INSTANCE)
URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def create_triple(tx, s, p, o):
    query = """
    MERGE (a:Entity {name: $s})
    MERGE (b:Entity {name: $o})
    MERGE (a)-[:RELATION {type: $p}]->(b)
    """
    tx.run(query, s=s, p=p, o=o)

# 🔹 Load triples file (your merged triples)
with open("triples.json", "r", encoding="utf-8") as f:
    triples = json.load(f)

# 🔹 Insert into Neo4j
with driver.session() as session:
    for triple in triples:
        subject = str(triple["subject"])
        predicate = str(triple["predicate"])
        obj = str(triple["object"])
        session.execute_write(create_triple, subject, predicate, obj)

driver.close()
print("✅ Knowledge Graph successfully loaded into Neo4j!")