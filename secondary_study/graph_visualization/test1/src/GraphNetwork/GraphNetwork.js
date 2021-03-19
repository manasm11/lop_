import React from 'react'
import {Network, Node, Edge} from 'react-vis-network'
import GraphNode from '../GraphNode'
import GraphEdge from '../GraphEdge'
import './GraphNetwork.css'

function GraphNetwork() {

    const options = {
        edges: {
            arrows:{
                to: true
            }
        },
        nodes: {
            shape: 'circle'
        }
    }


    React.useEffect(()=>{
        document.getElementsByTagName('canvas')[0].height=window.innerHeight
    })

    return (
        <div className='network'>
            <h1 className='btn'>Bbjsdifvuj</h1>
            <Network className='network' {...{options}}>
                <Node id={1} label='HELLO' />
                <Node id={2} label='HELLOdskbg' />
                <Edge to={2} from={1} label='ABCD2 '/>
                
                {/* {GraphEdge({to:2, from:1, type: 'PUBLISH_YEAR'})}
                {GraphNode({id:1, name:'2003', type:'year'})}
                {GraphNode({id:2, name:'Super Secret Research', type:'title', detail:'This is node detail !!!'})}
                {GraphNode({id:3, name:'Lakshya', type:'author'})}
                {GraphNode({id:4, name:'Pakistan', type:'conference'})}
                {GraphNode({id:5, name:'Jai Hind', type:'keyword'})} */}
            </Network>
        </div>
    )
}

export default GraphNetwork
