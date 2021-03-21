export function getTitleNode({ id, name }) {
    return { id, label: name, title: name, color: { background: '#996DE8', highlight: { border: '#996DE8', background: '#410287' }, }, font: { color: 'white' } }
}

export function getAuthorNode({ id, name }) {
    return { id, label: name, title: name, color: { background: '#4BA96F' }, font: { color: 'white' } }
}

export function getYearNode({ id, name }) {
    return { id, label: name, title: name, color: { background: '#FEC034' }, font: { color: 'white' } }
}

export function getKeywordNode({ id, name }) {
    return { id, label: name, title: name, color: { background: '#2D6FF7' }, font: { color: 'white' } }
}

export function getConferenceNode({ id, name }) {
    return { id, label: name, title: name, color: { background: '#F35A55' }, font: { color: 'white' } }
}

export default function getNode(node) {
    switch (node.type) {
        case "title": return getTitleNode(node)
        case "author": return getAuthorNode(node)
        case "year": return getYearNode(node)
        case "keyword": return getKeywordNode(node)
        case "conference": return getConferenceNode(node)
    }
}