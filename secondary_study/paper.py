import pandas as pd
import math

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


  @classmethod
  def papers_from_excel(cls, filename):
    is_row_valid = lambda row: not math.isnan(row[1].values[0])
    excel_file = pd.read_excel(filename)
    authors = set()
    papers = []
    for row in excel_file.iterrows():
      if not is_row_valid(row):
        break
      paper = Paper.from_row(row)
      papers.append(paper)
    return papers
    

  # def to_node(graph):
