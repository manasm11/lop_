import React from "react";
import { Node } from "react-vis-network";
import "./GraphNode.css";

function GraphNode(props){
  const node_props = getNodeProps(props);
  return (
      <Node {...node_props} />
  );
}

export default GraphNode;

function getNodeProps({ type, name, id, ...rest }) {
  const p = { label: name, id };
  let bgcolor = undefined;
  let fontcolor = undefined;
  switch(type){
    case 'title':
      bgcolor = '#996DE8';
      p.mass = 3
      break;
      case 'author':
        bgcolor = '#4BA96F'
        break;
      case 'year':
        bgcolor = '#FEC034'
        break;
      case 'keyword':
        bgcolor = '#2D6FF7'
        break;
      case 'conference':
        bgcolor = '#F35A55'
        break;
  }
  p.color = {background: bgcolor}
  p.font = {color: 'white'}
  p.shape = 'circle'
  p.title = rest.detail
  p.widthConstraint = {maximum: 75}
  console.log(p);
  return p;
}
