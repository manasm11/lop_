from py2neo import *
from config import URL
from paper import Paper
import json

class Graph(Graph):

  _author_set = set()
  _year_set = set()
  _conference_set = set()
  _keyword_set = set()

  def __init__(self, *args, **kwargs):
    '''Initializes graph from data from config (if arguments not specified)'''
    if not args and not kwargs:
      super().__init__(URL)
    else:
      super().__init__(*args, **kwargs)

  def get_query_results(self, title={}, author={}, year={}, conference={}, keyword={}):
    # conference = {'value': '', 'checked': True};
    # year = {'value': '', 'checked': False};
    # author = {'value': '', 'checked': False};
    # title = {'value': '', 'checked': False};
    # keyword = {'value': '', 'checked': False};

    query = 'match (conference:Conference),(title:Title),(year:Year),(author:Author),(keyword:Keyword)'

    any_has_value = any([conference['value'], year['value'], author['value'], title['value'], keyword['value']])
    add_and = False
    if any_has_value:
      query += ' where'
    if conference['value']:
      query += ' conference.name="'+conference['value']+'"'
      add_and = True
    if year['value']:
      if add_and:
        query += ' and'
      query += ' year.name='+year['value']
      add_and = True
    if author['value']:
      if add_and:
        query += ' and'
      query += ' author.name="'+author['value']+'"'
      add_and = True
    if title['value']:
      if add_and:
        query += ' and'
      query += ' title.name="'+title['value']+'"'
      add_and = True
    if keyword['value']:
      if add_and:
        query += ' and'
      query += ' keyword.name="'+keyword['value']+'"'
    
    query+= ' return distinct'
    add_comma = False
    if conference['checked']:
      query += ' conference'
      add_comma = True
    if year['checked']:
      if add_comma:
        query += ','
      query += ' year'
      add_comma = True
    if author['checked']:
      if add_comma:
        query += ','
      query += ' author'
      add_comma = True
    if title['checked']:
      if add_comma:
        query += ','
      query += ' title'
      add_comma = True
    if keyword['checked']:
      if add_comma:
        query+=','
      query += ' keyword'
      
    res = self.run(query)
    nodes = set()
    for r in res:
      # values = list(node.items())[0]
      node = r.values()[0]
      print(dir(node))
      # print(node.relationships)
      nodes.add(json.dumps({
        'id': node.identity,
        'type': list(r.keys())[0],
        'name': list(node.values())[0]
      }))
      # print(type)
      # n = {
      #   'type': values[0],
      #   'name': values[1]['name'],
      # }
      # print(dir(values[1]))
      # print(dir(values[1].nodes[0]))
      # print(values[1].nodes[0].identity)
      # print(values[1].keys())
      # print(node.items()[0])
    nodes_final = []
    for node in nodes:
      nodes_final.append(json.loads(node))
    return {'nodes': nodes_final}
    # print(result)


  # def get_titles(self):
  #   nodes = NodeMatcher(self)
  #   year_data = nodes.match('Year').all()
  #   author_data = nodes.match('Author').all()
  #   arr = []
  #   for i in year_data:
  #     arr.append({'labels': i.labels, 'properties': dict(i)})
  #     # print(i.labels)
  #     # print(dict(i))
  #   return arr
 
  # def get_relationship(self):
  #   nodes = RelationshipMatch(self, 'Title', 'Author')
  #   # relationship_data = nodes.

    

  def add_paper(self, paper):
    assert isinstance(paper, Paper)
    
    title_node = Node('Title', name=paper.title)
    self.create(title_node)


    year_node = self.create_year_node(paper.year)
    # print(title_node, year_node)
    self.create(
      Relationship(title_node, 'PUBLISHED_YEAR', year_node)
    )

    for author_node in self._author_nodes(paper.author):
      rel = Relationship(title_node, 'PUBLISHED_BY', author_node)
      self.create(rel)

    conference_node = self.create_conference_node(paper.conference)
    self.create(
      Relationship(title_node, 'PRESENTED_IN', conference_node)
    )

    for keyword_node in self._keyword_nodes(paper.keywords):
      self.create(
        Relationship(title_node, 'USED', keyword_node)
      )

  def create_conference_node(self, conference):
    return self._create_node(self._conference_set, 'Conference', name=conference)

  def create_keyword_node(self, keyword):
    return self._create_node(self._keyword_set, 'Keyword', name=keyword)

  def create_author_node(self, author):
    return self._create_node(self._author_set, 'Author', name=author)

  def create_year_node(self, year):
    print('*********year', year)
    return self._create_node(self._year_set, 'Year', name=year)

  def add_papers(self, papers):
    assert isinstance(papers, list), 'papers is not a list'
    self._author_set = set()
    for paper in papers:
      self.add_paper(paper)

  def print_all_nodes(self):
    res = self.run('match (n) return n')
    for i in res:
      print(i.get('n'))

  def nodes_count(self):
    count = self.run('match (n) return count(n) as c').data()[0]['c']
    return count

  def _create_node(self, set_, label, **properties):
    property_ = list(properties.values())[0]
    if property_ not in set_:
      node = Node(label, **properties)
      set_.add(property_)
      self.create(node)
    else:
      node = self.nodes.match(label, **properties).first()
    return node

  def _author_nodes(self, authors):
    for author in authors.split(','):
      author = author.strip()
      yield self.create_author_node(author)

  def _keyword_nodes(self, keywords):
    for keyword in keywords.split(','):
      keyword = keyword.strip()
      yield self.create_keyword_node(keyword)