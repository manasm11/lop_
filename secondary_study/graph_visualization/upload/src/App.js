import React, { useEffect, useState } from 'react';
import Graph from "react-graph-vis";
import getNode from './Graph/node';
import getEdge from './Graph/edge';
import nodes from './data/node.json';
import edges from './data/edge.json';
import InputField from './components/InputField'
import UploadFile from './components/UploadFile'

function App() {

  const [title, setTitle] = useState({});
  const [year, setYear] = useState({});
  const [author, setAuthor] = useState({});
  const [keyword, setKeyword] = useState({});
  const [conference, setConference] = useState({});
  const [path, setPath] = useState("");

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

  return (
    <div>
      <h2>Please upload Excel File</h2>
      <UploadFile setPath={setPath} />
      < h2 > Enter Query Details</h2>
      <div style={{ display: "flex", justifyContent: "space-around", margin: " 0 0 1em 0" }}>
        <InputField type="title" state={title} setState={setTitle} />
        <InputField type="authors" state={author} setState={setAuthor} />
        <InputField type="year" state={year} setState={setYear} />
        <InputField type="keyword" state={keyword} setState={setKeyword} />
        <InputField type="conference" state={conference} setState={setConference} />
        {/* <button style={{ background: "#F05555" }}>Submit</button> */}
      </div>
      <center><button style={{ width: '6em', height: "2.5em", background: "#2D6FF7", color: "white", fontSize: "1em", margin: "0 0 0em 0" }}>Submit</button></center>
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
}

export default App;
