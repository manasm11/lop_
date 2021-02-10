# pip install neo4j-driver
from datetime import datetime
from os import system
from neo4j import GraphDatabase, basic_auth
import neo4j
history_file = open("query_history.txt","a")
# history_file.write(f"session started: {datetime.now()}\n")

driver = GraphDatabase.driver(
  "bolt://54.236.24.253:33034",
  auth=basic_auth("neo4j", "elapse-halts-bead"))
session = driver.session()

while True:
    cypher_query = input("Enter Query > ")
    if cypher_query == "clear":
        system("clear")
        continue
    history_file.write(cypher_query+"\n")
    try:
        results = session.run(cypher_query, parameters={})

        for record in results:
            for value in record.values():
                if type(value) == neo4j.graph.Node:
                    print("id=",value.id," ,labels=",list(value.labels)," ,properties=", dict(value.items()), sep="")
                else:
                    print(value)
    except neo4j.exceptions.Neo4jError as e:
        print(e.message)
        continue