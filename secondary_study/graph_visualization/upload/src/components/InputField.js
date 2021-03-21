import React, { useState } from 'react';

const InputField = ({ type, state, setState }) => {
    const [title, placeholder] = getInputDetails(type);
    return (
        <div>
            <label>{title}</label>
            <input type="checkbox" value={state.checked} onChange={() => { setState((state) => ({ ...state, checked: !state.checked })) }} />
            <br />
            <input type="text" placeholder={placeholder} value={state.value} onChange={(e) => setState((state) => ({ ...state, value: e.target.value }))} />
        </div>
    );
}
export default InputField;

function getInputDetails(type) {
    switch (type) {
        case 'title': return ["Title", "Enter Paper Title"]
        case 'authors': return ["Authors", "Enter Author's Name"]
        case 'year': return ["Year", "Enter Year Published"]
        case 'conference': return ["Conference", "Enter Conference Name"]
        case 'keyword': return ["Keywords", "Mention Keywords Name"]
    }
}
