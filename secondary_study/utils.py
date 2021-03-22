import warnings
warnings.filterwarnings("ignore")
from paper import Paper
from neo_4_j import Graph


if __name__ == '__main__':
  # filepath = './abcd.xlsx'
  # papers = Paper.papers_from_excel(filepath)
  graph = Graph()
  # graph.delete_all()
  # graph.add_papers(papers)
  # graph.print_all_nodes()
  print(graph.get_query_results(
    title={'value': '', 'checked': True},
    author={'value': '', 'checked': True},
    year={'value': '', 'checked': True},
    conference={'value': '', 'checked': True},
    keyword={'value': '', 'checked': True},
  ))
  # print("output", graph.get_titles())
  # print('\n\tTotal nodes:', graph.nodes_count(), '\n')
