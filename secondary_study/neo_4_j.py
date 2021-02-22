import py2neo
from config import URL
from paper import Paper

class Graph(py2neo.Graph):

  author_set = set()
  year_set = set()
  conference_set = set()
  keyword_set = set()

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
    year = paper.year
    year_node = self.add_year(year)
    rel2 = py2neo.Relationship(paper_node, 'PUBLISHED_IN', year_node)
    self.create(rel2)
    # print(paper.author)
    for author in paper.author.split(','):
      author = author.strip()
      author_node = self.add_author(author)
      rel = py2neo.Relationship(author_node, 'PUBLISHED', paper_node)
      self.create(rel)

    conference_node = self.add_conference(paper.conference)
    rel3 = py2neo.Relationship(paper_node, 'PRESENTED_IN', conference_node)
    self.create(rel3)

    for keyword in paper.keywords.split(','):
      keyword = keyword.strip()
      keyword_node = self.add_keyword(keyword)
      rel4 = py2neo.Relationship(paper_node, 'USES', keyword_node)
      self.create(rel4)

  def add_conference(self, conference):
    if conference not in self.conference_set:
      conference_node = py2neo.Node('Conference', name=conference)
      self.conference_set.add(conference)
      self.create(conference_node)
    else:  
      conference_node = self.nodes.match('Conference', name=conference).first()
    return conference_node

  def add_keyword(self, keyword):
    if keyword not in self.keyword_set:
      keyword_node = py2neo.Node('Keyword', name=keyword)
      self.keyword_set.add(keyword)
      self.create(keyword_node)
    else:
      keyword_node = self.nodes.match('Keyword', name=keyword).first()
    return keyword_node

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