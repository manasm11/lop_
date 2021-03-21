import React from "react";
import { Edge } from "react-vis-network";

function GraphEdge(props) {
  const edge_props = getEdgeProps(props);
//   return <Edge {...edge_props} />
  return <Edge to={props.to} from={props.from} label={props.type} />

}

export default GraphEdge;

function getEdgeProps({ type, to, from, ...rest }) {
  const p = {
    label: type,
    to,
    from,
  };
  return p;
}
