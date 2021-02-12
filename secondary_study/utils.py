import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from paper import Paper
from neo_4_j import Graph
from config import URL

def papers_from_excel(filename):
  excel_file = pd.read_excel(filename)
  papers = []
  for row in excel_file.iterrows():
    paper = Paper.from_row(row)
    papers.append(paper)
  return papers

if __name__ == '__main__':
  papers = papers_from_excel('./papers.xlsx')
  graph = Graph()
  graph.delete_all()
  graph.add_papers(papers)
  graph.print_all_nodes()