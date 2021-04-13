import React, { useEffect, useState } from 'react';
import Graph from "react-graph-vis";
import getNode from './Graph/node';
import getEdge from './Graph/edge';
import nodes from './data/node.json';
import edges from './data/edge.json';
import InputField from './components/InputField'
import UploadFile from './components/UploadFile'
import { InputField2 } from './components/InputField'
// import { Multiselect } from 'multiselect-react-dropdown';

import './App.css'
const axios = require('axios')
const api_url = 'http://143.198.72.178:7000/'

function App() {

  const [title, setTitle] = useState([{ name: 'Software Development', id: 1 }, { name: 'Neo4j database', id: 2 }]);
  const [year, setYear] = useState([{ name: '2012', id: 1 }, { name: '2020', id: 2 }]);
  const [author, setAuthor] = useState([{ name: 'Srigar', id: 1 }, { name: 'Sam', id: 2 }]);
  const [keyword, setKeyword] = useState([{ name: 'Floor planning', id: 1 }, { name: 'K-means clustering', id: 2 }]);
  const [conference, setConference] = useState([{ name: 'IEEE', id: 1 }, { name: 'ACM', id: 2 }]);

  const [isTitle, setIsTitle] = useState({});
  const [isYear, setIsYear] = useState({});
  const [isAuthor, setIsAuthor] = useState({});
  const [isKeyword, setIsKeyword] = useState({});
  const [isConference, setIsConference] = useState({});
  const [path, setPath] = useState("");
  // const [graph, setGraph] = useState({nodes:[], edges:[]})

  const [option, setOption] = useState([{ name: 'Srigar', id: 1 }, { name: 'Sam', id: 2 }]);

  const onSelect = (selectedList, selectedItem) => {
    console.log(selectedList);
  }

  const onRemove = (selectedList, removedItem) => {
    console.log(selectedList);
  }

  const edges_new = edges.map(({ to, from, id }) => {
    const toNode = nodes.find(n => n.id == to)
    const fromNode = nodes.find(n => n.id == from)
    return getEdge({ toNode, fromNode, id })
  })


  const graph = {
    nodes: nodes.map(node => getNode(node)),
    edges: edges_new
  };

  const options = {
    // layout: {
    //   hierarchical: true
    // },
    edges: {
      color: "#000000",
      smooth: {
        enabled: true
      },
      length: 250
    },
    nodes: {
      shape: 'circle',
      widthConstraint: {
        minimum: 70,
        maximum: 145
      }
      // color: 'red'
    },
    height: "600px"
  };

  const events = {
    select: function (event) {
      var { nodes, edges } = event;
      console.log("selected1", nodes)
      console.log("selected2", edges)
    }
  };

  useEffect(() => {

  }, [])

  return (
    <div>
      <h2>Please upload Excel File</h2>
      <UploadFile setPath={setPath} />
      < h2 > Enter Query Details</h2>

      {/* <div className='input-fields'>
        <InputField type="title" state={title} setState={setTitle} />
        <InputField type="authors" state={author} setState={setAuthor} />
        <InputField type="year" state={year} setState={setYear} />
        <InputField type="keyword" state={keyword} setState={setKeyword} />
        <InputField type="conference" state={conference} setState={setConference} />
      </div> */}

      <div style={{ margin: "1em 3em 1em 3em" }}>
        <InputField2 type="title" state={isTitle} option={title} setState={setIsTitle} onSelect={onSelect} onRemove={onRemove} />
        <InputField2 type="authors" state={isAuthor} option={author} setState={setIsAuthor} onSelect={onSelect} onRemove={onRemove} />
        <InputField2 type="year" state={isYear} option={year} setState={setIsYear} onSelect={onSelect} onRemove={onRemove} />
        <InputField2 type="keyword" state={isKeyword} option={keyword} setState={setIsKeyword} onSelect={onSelect} onRemove={onRemove} />
        <InputField2 type="conference" state={isConference} option={conference} setState={setIsConference} onSelect={onSelect} onRemove={onRemove} />
        <center><button className='btn-submit' onClick={handleSubmit}>Submit</button></center>
      </div>
      <hr /> <br />
      <Graph
        graph={graph}
        options={options}
        events={events}
        getNetwork={network => {
          //  if you want access to vis.js network api you can set the state in a parent component using this property
        }}
      />

    </div >
  );
  async function handleSubmit() {
    // const res = await axios.get(api_url, {params: {
    //   year,
    //   author,
    //   conference,
    //   keyword,
    //   title
    // }})
    // console.log(res)
  }
}

export default App;
