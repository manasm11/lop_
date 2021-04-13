import React, { useState } from 'react';
import { Multiselect } from 'multiselect-react-dropdown';

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



export const InputField2 = ({ type, state, option, setState, onSelect, onRemove }) => {
    const [title, placeholder] = getInputDetails(type);
    return (
        <div>
            <label>{title}</label>
            <input type="checkbox" value={state.checked} onChange={() => { setState((state) => ({ ...state, checked: !state.checked })) }} />
            <DropdownReturn placeholderValue={placeholder} option={option} setState={setState} onRemove={onRemove} onSelect={onSelect} />
            <br />

        </div>
    );
}

function DropdownReturn({ placeholderValue, option, onSelect, onRemove }) {
    return (
        <Multiselect
            placeholder={placeholderValue}
            options={option} // Options to display in the dropdown
            // selectedValues={selectedValue} // Preselected value to persist in dropdown
            onSelect={onSelect} // Function will trigger on select event
            onRemove={onRemove} // Function will trigger on remove event
            displayValue="name" // Property name to display in the dropdown options
        />
    )
}

