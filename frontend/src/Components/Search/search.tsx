import React from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';

import CourseCard from '../CourseCard/CourseCard.js';
import Tooltip from "../ToolTip/ToolTip.tsx";


export function Search() {
  const [items, setItems] = useState<string[]>([])
  const [query, setQuery] = useState<string>("")
  const inputRef = useRef()

  const filteredItems = items.filter(item => {
    return item.toLowerCase().includes(query.toLowerCase())}
  )


  function onSubmit(e) {
    e.preventDefault()

    const value = inputRef.current.value 
    if (value === "") return

    setItems(prev => {
      return [...prev, value]
    })

    inputRef.current.value = ""
  }

  return (
    <div>
      Search 
      <input value={query} onChange={e => setQuery(e.target.value)} type="search" />
      <br />
      <br />
      <form onSubmit={onSubmit}>
        NewItem: <input ref={inputRef} type="text"/>
        <button type="submit">Add</button>
      </form>
      <h3>Items</h3>
      {filteredItems.map(item => (
        <div>{item}</div>
      ))}
    </div>
  );
}

export default Search;
