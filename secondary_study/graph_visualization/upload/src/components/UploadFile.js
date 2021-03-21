import React from 'react';
import { useDropzone } from 'react-dropzone';

export default function UploadFile({ setPath }) {
    const styles = {
        flex: 1,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "0px",
        borderWidth: "2px",
        borderRadius: "2px",
        // borderColor: ${ props => getColor(props) },
        borderStyle: "dashed",
        backgroundColor: "#fafafa",
        color: "#bdbdbd",
        outline: "none",
        transition: "border .24s ease -in -out"
    }
    const { acceptedFiles, getRootProps, getInputProps } = useDropzone();

    const files = acceptedFiles.map(file => {
        console.log("file", file);
        return <li key={file.path}>
            {file.path} - {file.size} bytes
        </li>
    });

    return (
        <section style={styles}>
            <div style={{ outline: "none", cursor: "pointer" }} {...getRootProps({ className: 'dropzone' })}>
                <input {...getInputProps()} />
                <p>Drag 'n' drop some files here, or click to select files</p>
            </div>
            <aside>
                <h4>Files</h4>
                <ul>{files}</ul>
            </aside>
        </section>
    );
}

