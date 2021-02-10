# IP_ADDRESS = '54.209.126.74'
IP_ADDRESS = 'localhost'
USERNAME = 'neo4j'
PASSWORD = 'testing321'
BOLT_PORT = '8002'


url = f'bolt://{USERNAME}:{PASSWORD}@{IP_ADDRESS}:{BOLT_PORT}'

from py2neo import Graph, Node, Relationship
graph = Graph(url)
graph.delete_all()

# Creating Nodes
manas = Node('Person', name='Manas', age='22') 
lakshya = Node('Person', name='Lakshya', age='101 NOT OUT')
divya = Node('Person', name='Divya', age='21')
# graph = Graph()

graph.create(manas)
graph.create(lakshya)
graph.create(divya)

# CREATING UNI-DIRECTIONAL RELATIONSHIPS
graph.create(
    Relationship(lakshya, 'BULLIES😢', manas)
)

# EXECUTING AND VIEWING QUERIES
query = 'match (person:Person) return person'
records = graph.run(query)

for record in records:
    node = record.get('person')
    print(node)


# MATCHING USING 'match' method
results = graph.nodes.match('Person')
for node in results:
    print(node)
