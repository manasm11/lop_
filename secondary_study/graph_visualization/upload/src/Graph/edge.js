export default function getEdge({ toNode, fromNode, id }) {

    switch (toNode.type) {
        case 'author': return { to: toNode.id, from: fromNode.id, label: "PUBLISHED_BY", id }
        case 'year': return { to: toNode.id, from: fromNode.id, label: "PUBLISHED_YEAR", id }
        case 'keyword': return { to: toNode.id, from: fromNode.id, label: "USED", id }
        case 'conference': return { to: toNode.id, from: fromNode.id, label: "PRESENTED_IN", id }
    }

}