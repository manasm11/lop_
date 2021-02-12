import py2neo
from config import URL
from paper import Paper

class Graph(py2neo.Graph):
  def __init__(self, *args, **kwargs):
    '''Initializes graph from data from config (if arguments not specified)'''
    if not args and not kwargs:
      super().__init__(URL)
    else:
      super().__init__(*args, **kwargs)

  def add_paper(self, paper):
    assert isinstance(paper, Paper)
    paper_dict = paper.to_dict()
    paper_node = py2neo.Node('Paper', **paper_dict)
    self.create(paper_node)

  def add_papers(self, papers):
    assert isinstance(papers, list), 'papers is not a list'
    for paper in papers:
      self.add_paper(paper)

  def print_all_nodes(self):
    res = self.run('match (n) return n')
    for i in res:
      print(i.get('n'))