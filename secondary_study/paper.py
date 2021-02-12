class Paper(object):
  def __init__(self, year, title, author):
    self.year = year
    self.author = author
    self.title = title
    # print(year, author, title)
    
  @classmethod
  def from_row(cls, row):
    row = row[1].values
    year = row[0]
    author = row[1]
    title = row[2]
    return cls(year=year, title=title, author=author)

  def to_dict(self):
        return self.__dict__

  # def to_node(graph):
