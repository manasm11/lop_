from fastapi import FastAPI
import uvicorn
from neo_4_j import Graph
from paper import Paper
import warnings
warnings.filterwarnings("ignore")
# Initialize the app
app = FastAPI()
graph = Graph()
import json
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# GET operation at route '/'
@app.get('/')
async def index(
    year:str='{"value":"", "checked":false}',
    title:str='{"value":"", "checked":false}',
    author:str='{"value":"", "checked":false}',
    keyword:str='{"value":"", "checked":false}',
    conference:str='{"value":"", "checked":true}'
):
    print('######', conference)
    year = json.loads(year)
    title = json.loads(title)
    author = json.loads(author)
    keyword = json.loads(keyword)
    conference = json.loads(conference)
    result = graph.get_query_results(
            title=title,
            author=author,
            year=year,
            conference=conference,
            keyword=keyword,
        )
    print(result)
    return result



if __name__=='__main__':
    filepath = './abcd.xlsx'
    papers = Paper.papers_from_excel(filepath)
    # graph.delete_all()
    graph.add_papers(papers)
    graph.print_all_nodes()
    uvicorn.run("server:app", host='0.0.0.0', port=7000, reload=True, access_log=False)