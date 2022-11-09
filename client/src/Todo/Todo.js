import axios from 'axios'
import React from 'react'

export default function Todo(props) {
    const deleteTodoHandler = (id) => {
        axios.delete("https://sampletodoappfortesting97.herokuapp.com/api/todo/" + id)
            .then(res => console.log(res))
    }
    return (
        <div style={{ display: "flex", justifyContent: 'center' }}>
            <div style={{ width: "500px" }}>
                <p><span style={{ fontWeight: 'bold' }}>{props.todo.title}:</span> {props.todo.description} <button onClick={() => deleteTodoHandler(props.todo.id)} style={{ color: 'red' }}>Delete</button></p>
            </div>
        </div>
    )
}
