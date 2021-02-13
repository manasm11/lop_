import py2neo
from config import URL
from paper import Paper

class Graph(py2neo.Graph):

  author_set = set()
  year_set = set()

  def __init__(self, *args, **kwargs):
    '''Initializes graph from data from config (if arguments not specified)'''
    if not args and not kwargs:
      super().__init__(URL)
    else:
      super().__init__(*args, **kwargs)

  def add_paper(self, paper):
    assert isinstance(paper, Paper)
    paper_dict = paper.to_dict()
    paper_node = py2neo.Node('Paper', title=paper.title)
    self.create(paper_node)
    # print(paper.author)
    for author in paper.author.split(' and '):
      author = author.strip()
      year = paper.year
      author_node = self.add_author(author)
      year_node = self.add_year(year)
      rel = py2neo.Relationship(author_node, 'PUBLISHED', paper_node)
      rel2 = py2neo.Relationship(author_node, 'PUBLISHED_IN', year_node)
      self.create(rel)
      self.create(rel2)



  def add_author(self, author):
    if author not in self.author_set:
        author_node = py2neo.Node('Author', name=author)
        self.author_set.add(author)
        self.create(author_node)
    else:
      author_node = self.nodes.match('Author', name=author).first()
    return author_node

  def add_year(self, year):
    if year not in self.year_set:
      year_node = py2neo.Node('Year', name=year)
      self.year_set.add(year)
      self.create(year_node)
    else:
      year_node = self.nodes.match('Year', name=year).first()
    return year_node

  def add_papers(self, papers):
    assert isinstance(papers, list), 'papers is not a list'
    self.author_set = set()
    for paper in papers:
      self.add_paper(paper)

  def print_all_nodes(self):
    res = self.run('match (n) return n')
    for i in res:
      print(i.get('n'))