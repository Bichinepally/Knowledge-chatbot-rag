from neo4j import GraphDatabase

URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def query_graph(keyword):
    with driver.session() as session:
        result = session.run("""
            MATCH (a)-[r]->(b)
            WHERE toLower(a.name) CONTAINS toLower($kw)
               OR toLower(b.name) CONTAINS toLower($kw)
            RETURN a.name AS subject, r.type AS relation, b.name AS object
            LIMIT 5
        """, kw=keyword)
        
        return [f"{r['subject']} {r['relation']} {r['object']}" for r in result]

if __name__ == "__main__":
    print(query_graph("employee"))