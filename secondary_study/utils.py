import warnings
warnings.filterwarnings("ignore")
from paper import Paper
from neo_4_j import Graph


if __name__ == '__main__':
  filepath = '/home/laozi/Manas/LIFE/MONEY/Acads/lop_/secondary_study/papers copy.xlsx'
  papers = Paper.papers_from_excel(filepath)
  graph = Graph()
  graph.delete_all()
  graph.add_papers(papers)
  graph.print_all_nodes()